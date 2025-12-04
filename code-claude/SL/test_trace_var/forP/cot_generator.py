"""
基于行内注释的COT生成器 - 最终修复版
- 支持中英双语
- 支持长循环总结
- 支持 [line n] + [explain] 双行格式
"""

import ast
import re
from config import TEMPLATES


class CodeClassifier:
    """代码行分类器"""
    
    def __init__(self):
        self.loop_counters = {}
        self.loop_body_lines = {}  # 记录每个循环的循环体行号集合
    
    def classify(self, line, prev_line=None, next_line=None):
        """分类代码行"""
        code = line.code.strip()
        lineno = line.lineno
        
        if code.startswith('print('):
            return 'print_statement'
        
        # For循环处理 - 修复版
        if code.startswith('for '):
            if lineno not in self.loop_counters:
                # 第一次遇到
                self.loop_counters[lineno] = 1
                self.loop_body_lines[lineno] = set()
                # 记录下一行作为循环体的一部分
                if next_line and next_line.lineno > lineno:
                    self.loop_body_lines[lineno].add(next_line.lineno)
                return 'for_start'
            else:
                # 再次遇到
                self.loop_counters[lineno] += 1
                
                if next_line:
                    next_lineno = next_line.lineno
                    # 判断下一行是否是循环体的一部分
                    if next_lineno in self.loop_body_lines.get(lineno, set()):
                        # 下一行在循环体中，继续循环
                        return 'for_continue'
                    else:
                        # 下一行不在循环体中，循环结束
                        return 'for_end'
                else:
                    return 'for_end'
        
        # 如果当前行的前一行是for循环，记录当前行为循环体
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
            # 先检查真正的增强赋值 +=, -=, *=, /=
            if re.search(r'\w+\s*\+=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*-=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*\*=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*/=\s*', code):
                return 'aug_assign'
            
            # 对于 d = d + 1 这种形式，只有当操作数是数字字面量时才视为增强赋值
            # d = d + a 应该被识别为普通表达式赋值
            match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(\d+(?:\.\d+)?)\s*$', code)
            if match:
                # 只有 d = d + 1 这种形式（操作数是数字）视为增强赋值
                return 'aug_assign'
            
            # 普通赋值
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


class VariableTracker:
    """变量来源追踪器 (支持多语言)"""
    
    def __init__(self, lang='en'):
        self.var_definitions = {}
        self.var_history = {}
        self.lang = lang
        self.templates = TEMPLATES[lang]
    
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
            # 格式化: "[line n]" 或 "[第n行]"
            # **注意**: 这里的格式是用于 *注释内部* 的, 不是行首的
            return self.templates['var_source'].format(def_line=def_line)
        return self.templates['var_unknown']


class ParameterExtractor:
    """参数提取器 (支持多语言)"""
    
    def __init__(self, var_tracker, lang='en'):
        self.var_tracker = var_tracker
        self.lang = lang
    
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
                    params['print_content'] = f"{print_arg}={var_dict[print_arg]} (from {source})"
                else:
                    params['print_content'] = print_arg
        
        # 提取变量名
        if line_type in ['assign_constant', 'assign_expr', 'aug_assign']:
            lvalues = self._extract_lvalue(line.code)
            if lvalues:
                params['var'] = lvalues[0]
                params['value'] = var_dict.get(lvalues[0], '?')
                params['result'] = params['value']
        
        # 表达式展开 - 对于普通赋值
        if line_type == 'assign_expr':
            params['expr_detail'] = self._expand_expression_with_source(
                line.code, var_dict, prev_var_dict
            )
            # 如果左值的值是 '?'，尝试从右边表达式推导
            if 'var' in params and params['value'] == '?':
                parts = line.code.split('=', 1)
                if len(parts) == 2:
                    expr = parts[1].strip()
                    # 如果右边是单个变量名（如 result = sum_val）
                    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', expr):
                        # 从当前行或上一行的变量字典获取值
                        if expr in var_dict:
                            params['value'] = var_dict[expr]
                            params['result'] = params['value']
                        elif prev_var_dict and expr in prev_var_dict:
                            params['value'] = prev_var_dict[expr]
                            params['result'] = params['value']
            # 更新变量追踪
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 常量赋值
        if line_type == 'assign_constant':
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 增强赋值
        if line_type == 'aug_assign':
            var = params.get('var')
            
            # 检查具体形式
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
                # d = d + 1 形式（操作数是数字）
                match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(.+)$', line.code)
                if match:
                    params['op'] = match.group(2)
                    operand_expr = match.group(3).strip()
                else:
                    params['op'] = '?'
                    operand_expr = '?'
            
            params['operand'] = operand_expr
            
            # 获取旧值和定义行
            if var and prev_var_dict:
                params['old_val'] = prev_var_dict.get(var, '?')
                # 格式化: "[line n]" 或 "[第n行]"
                def_line_num = self.var_tracker.get_def_line(var)
                params['def_line'] = self.var_tracker.get_var_source_info(var) if def_line_num else '?'
                
                # 兼容中文模板，它只需要行号
                if self.lang == 'zh':
                     params['def_line'] = self.var_tracker.get_var_source_info(var)

            else:
                params['old_val'] = '?'
                params['def_line'] = '?'
            
            # 更新变量追踪
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

                # **新增：更新变量追踪 - 记录循环变量的定义**
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
                params['value'] = f"{return_val}={var_dict[return_val]} (from {source})"
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
        
        # Fallback
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
        
        # 提取左值
        lvalues = self._extract_lvalue(code)
        lvalue_set = set(lvalues)
        
        # 查找表达式中的所有变量
        var_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        variables = re.findall(var_pattern, expr)
        
        # 构建详细说明
        var_details = []
        unique_vars = set() # 确保每个变量只解释一次
        
        for var in variables:
            # 检查是否是Python关键字或内置函数
            if var in ['range', 'len', 'sum', 'max', 'min', 'int', 'str', 'list', 'dict', 'True', 'False', 'None'] or var in unique_vars:
                continue
            unique_vars.add(var)
            
            # 如果变量是左值（在赋值语句左边，如 d = d + 1），使用 prev_var_dict（修改前的值）
            # 如果变量是右值（只在表达式中读取），使用当前行的 var_dict（已经过属性精简）
            if var in lvalue_set:
                # 左值：使用前一次的值（修改前的值）
                if prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(from {source})")
            else:
                # 右值：优先使用当前行的精简值（已根据当前行属性访问精简）
                if var in var_dict:
                    val = var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(from {source})")
                elif prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(from {source})")
        
        if var_details:
            detail_str = f", where {', '.join(var_details)}" if self.lang == 'en' else f", 其中 {', '.join(var_details)}"
            return f"{expr}{detail_str}"
        else:
            return expr


class COTGenerator:
    """行内注释式COT生成器"""
    
    def __init__(self, pruned_file, lang='en'):
        self.pruned_file = pruned_file
        self.lang = lang
        self.templates = TEMPLATES[lang]
        self.target_line = None
        self.target_var = None
        self.lines = []
        self.var_tracker = VariableTracker(lang=self.lang)
    
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
        """生成行内注释式COT（支持长循环总结）"""
        
        # --- 步骤 1: 预计算循环总数 (Dry Run) ---
        total_counts = {}
        dry_classifier = CodeClassifier()
        prev_line = None
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            dry_classifier.classify(line, prev_line, next_line)
            prev_line = line
        total_counts = dry_classifier.loop_counters

        # --- 步骤 2: 实际生成 ---
        classifier = CodeClassifier() # 使用新的分类器进行实际生成
        extractor = ParameterExtractor(self.var_tracker, lang=self.lang)
        
        output_lines = []
        header_template = self.templates['header']
        footer_template = self.templates['footer']
        inline_templates = self.templates['inline']
        
        output_lines.append(header_template.format(
            target_line=self.target_line, 
            target_var=self.target_var
        ))
        
        prev_var_dict = {}
        prev_line_obj = None
        
        current_loop_header = None
        loop_skip_state = {} # 存储循环头的行号: True (正在跳过) / False (正在打印)

        LOOP_SUMMARY_THRESHOLD = 5 # 迭代次数 > 5 才触发总结
        SKIP_AFTER_ITER = 2      # 显示前 2 次
        RESUME_BEFORE_ITER = 2     # 显示后 2 次
        
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            
            # 分类
            line_type = classifier.classify(line, prev_line_obj, next_line)
            
            # --- 循环总结逻辑 ---
            if line_type in ('for_start', 'while_start'):
                current_loop_header = line.lineno
                loop_skip_state[current_loop_header] = False # 默认开始打印
            
            if current_loop_header:
                total_iter = total_counts.get(current_loop_header, 0)
                current_iter = classifier.loop_counters.get(current_loop_header, 0)
                
                # 计算开始跳过和恢复打印的迭代次数
                START_SKIP_ITER = SKIP_AFTER_ITER + 1
                RESUME_ITER = total_iter - RESUME_BEFORE_ITER + 1

                is_summarizable = total_iter > LOOP_SUMMARY_THRESHOLD
                
                if is_summarizable:
                    if current_iter == START_SKIP_ITER:
                        # 这是第3次迭代，打印总结行并开始跳过
                        num_skipped = total_iter - SKIP_AFTER_ITER - RESUME_BEFORE_ITER
                        summary_template = {
                            'en': f"\n... [Line {current_loop_header}] repeats {num_skipped} more times ...\n",
                            'zh': f"\n... [第{current_loop_header}行] 额外循环了 {num_skipped} 次 ...\n"
                        }
                        output_lines.append(summary_template[self.lang].strip()) 
                    
                    elif current_iter == RESUME_ITER:
                        # 这是倒数第2次迭代，停止跳过
                        loop_skip_state[current_loop_header] = False
                        
                # 检查是否应跳过当前行
                if loop_skip_state.get(current_loop_header, False):
                    # 必须更新状态，即使不打印
                    prev_var_dict = line.get_var_dict()
                    prev_line_obj = line
                    if line_type in ('for_end', 'while_end'):
                        current_loop_header = None # 退出循环
                    continue # 跳过本行
            # --- 结束循环总结逻辑 ---

            if line_type == 'unknown':
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            # 提取参数
            params = extractor.extract(line, line_type, classifier, prev_var_dict)
            
            # 获取模板
            template_info = inline_templates.get(line_type)
            if not template_info:
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            

            # -------------------------------------------------
            # 目标格式:
            # [line 1]  a = 1
            # [explain] Assign: a = 1
            # -------------------------------------------------
            
            # 1. 获取注释文本 (不带 '#')
            comment_text = ""
            try:
                # 模板格式为: "  # Assign: {var} = {value}"
                comment_with_prefix = template_info['template'].format(**params)
                # 移除前导空格、'#'号和之后的空格
                comment_text = comment_with_prefix.lstrip().lstrip('#').lstrip()
            except KeyError as e:
                comment_text = f"(Missing param: {e})"

            # 2. 格式化代码行和解释行
            if self.lang == 'zh':
                # 中文版
                code_line = f"[第{line.lineno}行]  {line.code}"
                explain_line = f"[解释] {comment_text}"
            else:
                # 英文版
                code_line = f"[line {line.lineno}]  {line.code}"
                explain_line = f"[explain] {comment_text}"
            
            # 3. 添加两行到输出 (并确保解释非空)
            output_lines.append(code_line)
            if comment_text:
                output_lines.append(explain_line)
            # -------------------------------------------------
            
            # 更新prev_var_dict和prev_line_obj
            prev_var_dict = line.get_var_dict()
            prev_line_obj = line
            
            if line_type in ('for_end', 'while_end'):
                current_loop_header = None # 退出循环
        
        # 最终答案
        final_value = self.lines[-1].get_var_dict().get(self.target_var, '?')
        source_info = self.var_tracker.get_var_source_info(self.target_var)
        
        output_lines.append(footer_template.format(
            target_var=self.target_var,
            final_value=final_value,
            source_info=source_info
        ))
        
        return '\n'.join(output_lines)
    
    def save_cot(self, output_file):
        """保存COT"""
        cot_text = self.generate()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cot_text)
        return output_file
    
    @staticmethod
    def generate_cot(pruned_file, output_file, lang='en'):
        """静态方法：生成COT"""
        generator = COTGenerator(pruned_file, lang=lang)
        generator.load_pruned_trace()
        return generator.save_cot(output_file)