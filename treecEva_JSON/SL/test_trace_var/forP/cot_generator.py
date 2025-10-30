"""
基于模板的COT生成器
"""

import ast
import re
from config import COT_TEMPLATES, STEP_CONFIG, STATE_CONFIG


class CodeClassifier:
    """代码行分类器"""
    
    def __init__(self):
        self.loop_counters = {}  # 追踪循环迭代次数
        self.last_lineno = None
        self.in_loop_header = {}  # 记录是否在循环头部
    
    def classify(self, line, prev_line=None, next_line=None):
        """分类代码行"""
        code = line.code.strip()
        lineno = line.lineno
        
        # Print语句
        if code.startswith('print('):
            return 'print_statement'
        
        # For循环特殊处理
        if code.startswith('for '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                self.in_loop_header[lineno] = True
                return 'for_start'
            else:
                self.loop_counters[lineno] += 1
                # 检查是否是最后一次迭代
                if next_line and next_line.lineno != lineno:
                    return 'for_end'
                else:
                    return 'for_continue'
        
        # While循环
        if code.startswith('while '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                return 'while_start'
            else:
                self.loop_counters[lineno] += 1
                if next_line and next_line.lineno != lineno:
                    return 'while_end'
                else:
                    return 'while_continue'
        
        # If语句
        if code.startswith('if '):
            return 'if_true'  # 假设执行到就是True
        
        if code.startswith('elif '):
            return 'elif_true'
        
        if code.startswith('else:'):
            return 'else'
        
        # Return语句
        if code.startswith('return'):
            return 'return'
        
        # 函数定义
        if code.startswith('def '):
            return 'function_def'
        
        # 赋值语句
        if '=' in code:
            # 增强赋值
            if re.search(r'\w+\s*[+\-*/]=', code):
                return 'aug_assign'
            
            # 判断是常量还是表达式
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        # 检查右值
                        if isinstance(node.value, (ast.Constant, ast.Num, ast.Str)):
                            return 'assign_constant'
                        else:
                            return 'assign_expr'
            except:
                # 简单判断
                if re.match(r'^\s*\w+\s*=\s*[\d\'"]+\s*$', code):
                    return 'assign_constant'
                else:
                    return 'assign_expr'
        
        return 'unknown'


class ParameterExtractor:
    """参数提取器"""
    
    def extract(self, line, line_type, classifier):
        """提取模板参数"""
        params = {
            'line': line.lineno,
            'code': line.code.strip(),
        }
        
        var_dict = line.get_var_dict()
        
        # Print语句
        if line_type == 'print_statement':
            # 提取print的内容
            match = re.search(r'print\((.*)\)', line.code)
            if match:
                print_arg = match.group(1).strip()
                # 尝试从变量字典获取值
                if print_arg in var_dict:
                    params['print_content'] = f"{print_arg} = {var_dict[print_arg]}"
                else:
                    # 可能是表达式或常量
                    params['print_content'] = print_arg
        
        # 提取变量名
        if line_type in ['assign_constant', 'assign_expr', 'aug_assign']:
            lvalues = self._extract_lvalue(line.code)
            if lvalues:
                params['var'] = lvalues[0]
                params['value'] = var_dict.get(lvalues[0], '?')
                params['result'] = params['value']
        
        # 表达式展开
        if line_type == 'assign_expr':
            params['expr_detail'] = self._expand_expression(line.code, var_dict)
        
        # 增强赋值
        if line_type == 'aug_assign':
            var = params['var']
            # 提取操作符
            match = re.search(r'([+\-*/])=', line.code)
            if match:
                params['op'] = match.group(1)
            
            # 提取操作数
            parts = line.code.split('=', 1)
            if len(parts) > 1:
                operand = parts[1].strip()
                params['operand'] = operand
            
            # 需要从前一个状态获取old_val
            params['old_val'] = '?'  # 这个需要从前一行获取
        
        # For循环
        if line_type.startswith('for'):
            # 提取循环变量
            match = re.match(r'for\s+(\w+)\s+in', line.code)
            if match:
                iter_var = match.group(1)
                params['iter_var'] = iter_var
                params['iter_val'] = var_dict.get(iter_var, '?')
                params['iter_count'] = classifier.loop_counters.get(line.lineno, 1)
        
        # While循环
        if line_type.startswith('while'):
            params['condition'] = line.code.replace('while', '').replace(':', '').strip()
        
        # Return语句
        if line_type == 'return':
            return_val = line.code.replace('return', '').strip()
            params['value'] = return_val
        
        # 函数定义
        if line_type == 'function_def':
            match = re.match(r'def\s+(\w+)', line.code)
            if match:
                params['func_name'] = match.group(1)
        
        return params
    
    def _extract_lvalue(self, code):
        """提取左值"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    targets = []
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            targets.append(target.id)
                    return targets
                elif isinstance(node, ast.AugAssign):
                    if isinstance(node.target, ast.Name):
                        return [node.target.id]
        except:
            match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[=+\-*/]=', code)
            if match:
                return [match.group(1)]
        return []
    
    def _expand_expression(self, code, var_dict):
        """展开表达式，用实际值替换变量"""
        # 提取右值
        parts = code.split('=', 1)
        if len(parts) < 2:
            return code
        
        expr = parts[1].strip()
        
        # 简单替换变量
        expanded = expr
        for var, val in var_dict.items():
            expanded = re.sub(r'\b' + var + r'\b', str(val), expanded)
        
        # 尝试计算
        try:
            result = eval(expanded)
            return f"{expr} = {expanded} = {result}"
        except:
            return f"{expr} = {expanded}"


class COTGenerator:
    """COT生成器"""
    
    def __init__(self, pruned_file):
        self.pruned_file = pruned_file
        self.target_line = None
        self.target_var = None
        self.lines = []
    
    def load_pruned_trace(self):
        """加载剪枝后的追踪文件"""
        with open(self.pruned_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        # 解析头部
        self.target_line = int(content[0].strip())
        self.target_var = content[1].strip()
        
        # 解析追踪行
        from pruner import TraceLine
        i = 3  # 跳过前三行（目标行、目标变量、---）
        while i < len(content):
            line = content[i].strip()
            if not line:
                i += 1
                continue
            
            parts = line.split(' ', 1)
            if len(parts) < 2:
                i += 1
                continue
            
            lineno = int(parts[0])
            code = parts[1]
            
            # 检查下一行是否是变量列表
            var_names = []
            var_values = []
            if i + 1 < len(content):
                next_line = content[i + 1].strip()
                if next_line.startswith(str(lineno) + ' ['):
                    try:
                        parts = next_line.split(' ', 1)
                        if len(parts) > 1:
                            var_data = parts[1]
                            var_names, var_values = self._parse_var_lists(var_data)
                        i += 1
                    except:
                        pass
            
            trace_line = TraceLine(lineno, code, var_names, var_values)
            self.lines.append(trace_line)
            i += 1
    
    def _parse_var_lists(self, var_data):
        """解析变量列表"""
        try:
            parts = var_data.split('] [')
            if len(parts) == 2:
                names_str = parts[0] + ']'
                values_str = '[' + parts[1]
                names = eval(names_str)
                values = eval(values_str)
                return names, values
        except:
            pass
        return [], []
    
    def generate(self):
        """生成COT"""
        classifier = CodeClassifier()
        extractor = ParameterExtractor()
        
        output_lines = []
        output_lines.append(f"目标: 求第{self.target_line}行执行后变量{self.target_var}的值\n")
        
        # 分类并生成
        current_step = 1
        step_lines = []
        prev_var_dict = {}
        
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            
            # 分类
            line_type = classifier.classify(line, None, next_line)
            
            if line_type == 'unknown':
                continue
            
            # 提取参数
            params = extractor.extract(line, line_type, classifier)
            
            # 补充old_val（用于aug_assign）
            if line_type == 'aug_assign' and 'var' in params:
                var = params['var']
                params['old_val'] = prev_var_dict.get(var, '?')
            
            # 获取模板
            template_info = COT_TEMPLATES.get(line_type)
            if not template_info:
                continue
            
            template = template_info['template']
            cot_text = template.format(**params)
            step_lines.append(cot_text)
            
            # 添加状态
            if template_info.get('with_state') and STATE_CONFIG['show_state']:
                state_text = self._format_state(line.get_var_dict())
                step_lines.append(state_text)
            
            # 记录当前变量状态
            prev_var_dict = line.get_var_dict()
            
            # 步骤划分
            if len(step_lines) >= STEP_CONFIG['lines_per_step']:
                step_title = f"步骤{current_step}: {self._generate_step_title(step_lines)}"
                output_lines.append(step_title)
                output_lines.extend(step_lines)
                output_lines.append("")
                step_lines = []
                current_step += 1
        
        # 剩余行
        if step_lines:
            step_title = f"步骤{current_step}: 最终计算"
            output_lines.append(step_title)
            output_lines.extend(step_lines)
            output_lines.append("")
        
        # 最终答案
        final_value = self.lines[-1].get_var_dict().get(self.target_var, '?')
        output_lines.append(f"最终答案: {final_value}")
        
        return '\n'.join(output_lines)
    
    def _format_state(self, var_dict):
        """格式化状态"""
        if not var_dict:
            return ""
        
        items = [f"{k}={v}" for k, v in var_dict.items()]
        return f"→ 当前状态: {', '.join(items)}"
    
    def _generate_step_title(self, step_lines):
        """生成步骤标题"""
        # 简单版本：根据内容判断
        text = '\n'.join(step_lines)
        if '循环' in text:
            return "循环执行"
        elif '初始化' in text or '赋值' in text:
            return "初始化变量"
        elif '打印' in text:
            return "输出结果"
        else:
            return "计算过程"
    
    def save_cot(self, output_file):
        """保存COT"""
        cot_text = self.generate()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cot_text)
        return output_file
    
    @staticmethod
    def generate_cot(pruned_file, output_file):
        """静态方法：生成COT"""
        generator = COTGenerator(pruned_file)
        generator.load_pruned_trace()
        return generator.save_cot(output_file)