"""
倒序COT生成器 - 独立组件
从目标往回推导的思维链生成
"""

import ast
import re
from config import REVERSE_COT_TEMPLATES


class ReverseCodeClassifier:
    """倒序代码行分类器"""
    
    def __init__(self):
        self.loop_counters = {}
        self.loop_body_lines = {}
    
    def classify(self, line, prev_line=None, next_line=None):
        """分类代码行"""
        code = line.code.strip()
        lineno = line.lineno
        
        if code.startswith('print('):
            return 'print_statement'
        
        # For循环处理
        if code.startswith('for '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                self.loop_body_lines[lineno] = set()
                if next_line and next_line.lineno > lineno:
                    self.loop_body_lines[lineno].add(next_line.lineno)
                return 'for_start'
            else:
                self.loop_counters[lineno] += 1
                
                if next_line:
                    next_lineno = next_line.lineno
                    if next_lineno in self.loop_body_lines.get(lineno, set()):
                        return 'for_continue'
                    else:
                        return 'for_end'
                else:
                    return 'for_end'
        
        if prev_line and prev_line.code.strip().startswith('for '):
            prev_lineno = prev_line.lineno
            if prev_lineno in self.loop_body_lines and lineno > prev_lineno:
                self.loop_body_lines[prev_lineno].add(lineno)
        
        if code.startswith('while '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                return 'while_start'
            else:
                self.loop_counters[lineno] += 1
                if next_line and next_line.lineno > lineno:
                    return 'while_continue'
                else:
                    return 'while_end'
        
        if code.startswith('if '):
            return 'if_true'
        
        if code.startswith('elif '):
            return 'elif_true'
        
        if code.startswith('else:'):
            return 'else'
        
        if code.startswith('return'):
            return 'return'
        
        if code.startswith('def '):
            return 'function_def'
        
        # 赋值语句
        if '=' in code and not code.startswith('='):
            if re.search(r'\w+\s*\+=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*-=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*\*=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*/=\s*', code):
                return 'aug_assign'
            
            match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(\d+(?:\.\d+)?)\s*$', code)
            if match:
                return 'aug_assign'
            
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        if isinstance(node.value, (ast.Constant, ast.Num, ast.Str)):
                            return 'assign_constant'
                        else:
                            return 'assign_expr'
            except:
                if re.match(r'^\s*\w+\s*=\s*[\d\'"]+\s*$', code):
                    return 'assign_constant'
                else:
                    return 'assign_expr'
        
        return 'unknown'


class ReverseVariableTracker:
    """倒序变量来源追踪器"""
    
    def __init__(self):
        self.var_definitions = {}
        self.var_history = {}
    
    def update_var(self, var_name, lineno, value):
        """更新变量定义"""
        self.var_definitions[var_name] = lineno
        if var_name not in self.var_history:
            self.var_history[var_name] = []
        self.var_history[var_name].append((lineno, value))
    
    def get_def_line(self, var_name):
        """获取变量最后定义的行号"""
        return self.var_definitions.get(var_name)
    
    def get_var_source_info(self, var_name):
        """获取变量来源信息"""
        def_line = self.var_definitions.get(var_name)
        if def_line:
            return f"第{def_line}行"
        return "未知"


class ReverseParameterExtractor:
    """倒序参数提取器"""
    
    def __init__(self, var_tracker):
        self.var_tracker = var_tracker
    
    def extract(self, line, line_type, classifier, prev_var_dict=None):
        """提取模板参数"""
        params = {
            'line': line.lineno,
            'code': line.code.strip(),
        }
        
        var_dict = line.get_var_dict()
        
        # Print语句
        if line_type == 'print_statement':
            match = re.search(r'print\((.*)\)', line.code)
            if match:
                print_arg = match.group(1).strip()
                if print_arg in var_dict:
                    source = self.var_tracker.get_var_source_info(print_arg)
                    params['print_content'] = f"{print_arg}={var_dict[print_arg]} (来自{source})"
                else:
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
            params['expr_detail'] = self._expand_expression_with_source(
                line.code, var_dict, prev_var_dict
            )
            if 'var' in params and params['value'] == '?':
                parts = line.code.split('=', 1)
                if len(parts) == 2:
                    expr = parts[1].strip()
                    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', expr):
                        if expr in var_dict:
                            params['value'] = var_dict[expr]
                            params['result'] = params['value']
                        elif prev_var_dict and expr in prev_var_dict:
                            params['value'] = prev_var_dict[expr]
                            params['result'] = params['value']
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 常量赋值
        if line_type == 'assign_constant':
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 增强赋值
        if line_type == 'aug_assign':
            var = params.get('var')
            
            if '+=' in line.code:
                params['op'] = '+'
                parts = line.code.split('+=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            elif '-=' in line.code:
                params['op'] = '-'
                parts = line.code.split('-=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            elif '*=' in line.code:
                params['op'] = '*'
                parts = line.code.split('*=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            elif '/=' in line.code:
                params['op'] = '/'
                parts = line.code.split('/=', 1)
                operand_expr = parts[1].strip() if len(parts) > 1 else '?'
            else:
                match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(.+)$', line.code)
                if match:
                    params['op'] = match.group(2)
                    operand_expr = match.group(3).strip()
                else:
                    params['op'] = '?'
                    operand_expr = '?'
            
            params['operand'] = operand_expr
            
            if var and prev_var_dict:
                params['old_val'] = prev_var_dict.get(var, '?')
                params['def_line'] = self.var_tracker.get_def_line(var) or '?'
            else:
                params['old_val'] = '?'
                params['def_line'] = '?'
            
            if var:
                self.var_tracker.update_var(var, line.lineno, params['value'])
        
        # For循环
        if line_type.startswith('for'):
            match = re.match(r'for\s+(\w+)\s+in\s+(.+):', line.code)
            if match:
                iter_var = match.group(1)
                iter_source = match.group(2).strip()
                params['iter_var'] = iter_var
                params['iter_val'] = var_dict.get(iter_var, '?')
                params['iter_count'] = classifier.loop_counters.get(line.lineno, 1)
                params['iter_source'] = iter_source
                
                if iter_var in var_dict:
                    self.var_tracker.update_var(iter_var, line.lineno, var_dict[iter_var])
        
        # While循环
        if line_type.startswith('while'):
            params['condition'] = line.code.replace('while', '').replace(':', '').strip()
        
        # Return语句
        if line_type == 'return':
            return_val = line.code.replace('return', '').strip()
            if return_val in var_dict:
                source = self.var_tracker.get_var_source_info(return_val)
                params['value'] = f"{return_val}={var_dict[return_val]} (来自{source})"
            else:
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
            pass
        
        match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[=+\-*/]=', code)
        if match:
            return [match.group(1)]
        
        return []
    
    def _expand_expression_with_source(self, code, var_dict, prev_var_dict=None):
        """展开表达式，显示每个变量的值和来源"""
        parts = code.split('=', 1)
        if len(parts) < 2:
            return code
        
        left_part = parts[0].strip()
        expr = parts[1].strip()
        
        lvalues = self._extract_lvalue(code)
        lvalue_set = set(lvalues)
        
        var_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        variables = re.findall(var_pattern, expr)
        
        var_details = []
        for var in variables:
            if var in ['range', 'len', 'sum', 'max', 'min', 'int', 'str', 'list', 'dict', 'True', 'False', 'None']:
                continue
            
            if var in lvalue_set:
                if prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(来自{source})")
            else:
                if var in var_dict:
                    val = var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(来自{source})")
                elif prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(来自{source})")
        
        if var_details:
            return f"{expr}, 其中 {', '.join(var_details)}"
        else:
            return expr


class ReverseCOTGenerator:
    """倒序COT生成器 - 独立组件"""
    
    def __init__(self, pruned_file):
        self.pruned_file = pruned_file
        self.target_line = None
        self.target_var = None
        self.lines = []
        self.var_tracker = ReverseVariableTracker()
    
    def load_pruned_trace(self):
        """加载剪枝后的追踪文件"""
        with open(self.pruned_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        self.target_line = int(content[0].strip())
        self.target_var = content[1].strip()
        
        from pruner import TraceLine
        i = 3
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
        """生成倒序COT"""
        # 第一步：正向遍历建立完整的参数缓存
        classifier = ReverseCodeClassifier()
        extractor = ReverseParameterExtractor(self.var_tracker)
        
        params_cache = []
        prev_var_dict = {}
        prev_line_obj = None
        
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            
            line_type = classifier.classify(line, prev_line_obj, next_line)
            
            if line_type == 'unknown':
                params_cache.append((line, 'unknown', {}))
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            params = extractor.extract(line, line_type, classifier, prev_var_dict)
            params_cache.append((line, line_type, params))
            
            prev_var_dict = line.get_var_dict()
            prev_line_obj = line
        
        # 第二步：生成倒序输出
        output_lines = []
        
        # 获取最终答案
        final_value = self.lines[-1].get_var_dict().get(self.target_var, '?')
        source_info = self.var_tracker.get_var_source_info(self.target_var)
        
        output_lines.append(f"目标: 求第{self.target_line}行执行后变量 {self.target_var} 的值")
        output_lines.append(f"答案: {self.target_var} = {final_value}\n")
        output_lines.append("倒推过程（从结果往回推导）:\n")
        
        # 倒序输出
        for i in range(len(params_cache) - 1, -1, -1):
            line, line_type, params = params_cache[i]
            
            if line_type == 'unknown':
                continue
            
            template_info = REVERSE_COT_TEMPLATES.get(line_type)
            if not template_info:
                continue
            
            code_line = f"{line.lineno:3d}  {line.code}"
            
            try:
                comment = template_info['template'].format(**params)
            except KeyError as e:
                comment = f"  # ← (缺少参数: {e})"
            
            output_lines.append(code_line + comment)
        
        return '\n'.join(output_lines)
    
    def save_cot(self, output_file):
        """保存倒序COT"""
        cot_text = self.generate()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cot_text)
        return output_file
    
    @staticmethod
    def generate_reverse_cot(pruned_file, output_file):
        """静态方法：生成倒序COT"""
        generator = ReverseCOTGenerator(pruned_file)
        generator.load_pruned_trace()
        return generator.save_cot(output_file)