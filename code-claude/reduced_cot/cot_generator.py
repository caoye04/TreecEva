"""
基于行内注释的COT生成器 - 修复生成器表达式重复问题
"""

import ast
import re
from config import TEMPLATES


class CodeClassifier:
    """代码行分类器"""
    
    def __init__(self):
        self.loop_counters = {}
        self.loop_body_lines = {}
        self.seen_generator_lines = {}  # 记录已处理的生成器表达式行
    
    def classify(self, line, prev_line=None, next_line=None):
        """分类代码行"""
        if line.is_function_enter:
            return 'function_enter'
        if line.is_function_return:
            return 'function_return'
        
        code = line.code.strip()
        lineno = line.lineno
        
        # **新增：检测生成器表达式**
        if self._is_generator_expression(code):
            # 如果这一行已经处理过生成器表达式，跳过后续重复
            if lineno in self.seen_generator_lines:
                self.seen_generator_lines[lineno] += 1
                if self.seen_generator_lines[lineno] > 1:
                    return 'generator_iteration'  # 标记为生成器迭代，后续可以跳过
            else:
                self.seen_generator_lines[lineno] = 1
        
        if code.startswith('print('):
            return 'print_statement'
        
        if code.startswith('for '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                self.loop_body_lines[lineno] = set()
                if next_line and not next_line.is_function_enter and not next_line.is_function_return and next_line.lineno > lineno:
                    self.loop_body_lines[lineno].add(next_line.lineno)
                return 'for_start'
            else:
                self.loop_counters[lineno] += 1
                
                if next_line and not next_line.is_function_enter and not next_line.is_function_return:
                    next_lineno = next_line.lineno
                    if next_lineno in self.loop_body_lines.get(lineno, set()):
                        return 'for_continue'
                    else:
                        return 'for_end'
                else:
                    return 'for_end'
        
        if prev_line and not prev_line.is_function_enter and not prev_line.is_function_return and prev_line.code.strip().startswith('for '):
            prev_lineno = prev_line.lineno
            if prev_lineno in self.loop_body_lines and lineno > prev_lineno:
                self.loop_body_lines[prev_lineno].add(lineno)
        
        if code.startswith('while '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                return 'while_start'
            else:
                self.loop_counters[lineno] += 1
                if next_line and not next_line.is_function_enter and not next_line.is_function_return and next_line.lineno > lineno:
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
                        if isinstance(node.value, ast.Call):
                            return 'function_call'
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
    
    def _is_generator_expression(self, code):
        """检测是否包含生成器表达式或列表推导式"""
        # 匹配 sum(...for...), list(...for...), [... for ...], 等模式
        patterns = [
            r'\bsum\s*\([^)]*\bfor\b',  # sum(... for ...)
            r'\blist\s*\([^)]*\bfor\b', # list(... for ...)
            r'\bset\s*\([^)]*\bfor\b',  # set(... for ...)
            r'\bdict\s*\([^)]*\bfor\b', # dict(... for ...)
            r'\bmax\s*\([^)]*\bfor\b',  # max(... for ...)
            r'\bmin\s*\([^)]*\bfor\b',  # min(... for ...)
            r'\bany\s*\([^)]*\bfor\b',  # any(... for ...)
            r'\ball\s*\([^)]*\bfor\b',  # all(... for ...)
            r'\[[^\]]*\bfor\b',         # [... for ...]
            r'\{[^\}]*\bfor\b',         # {... for ...}
        ]
        
        for pattern in patterns:
            if re.search(pattern, code):
                return True
        return False


class VariableTracker:
    """变量来源追踪器 - 支持函数上下文"""
    
    def __init__(self, lang='en'):
        self.var_definitions = {}
        self.var_history = {}
        self.lang = lang
        self.templates = TEMPLATES[lang]
        self.function_contexts = []
        self.param_sources = {}
    
    def enter_function(self, func_name, param_mapping):
        """进入函数，建立参数映射"""
        context = {
            'func_name': func_name,
            'param_mapping': param_mapping.copy(),
            'local_vars': {}
        }
        self.function_contexts.append(context)
        
        for param, info in param_mapping.items():
            actual_var = info.get('actual_var', param)
            def_line = self.var_definitions.get(actual_var)
            self.param_sources[param] = {
                'actual_var': actual_var,
                'def_line': def_line
            }
    
    def exit_function(self):
        """退出函数"""
        if self.function_contexts:
            self.function_contexts.pop()
        
        self.param_sources = {}
        if self.function_contexts:
            current_context = self.function_contexts[-1]
            for param, info in current_context.get('param_mapping', {}).items():
                actual_var = info.get('actual_var', param)
                def_line = self.var_definitions.get(actual_var)
                self.param_sources[param] = {
                    'actual_var': actual_var,
                    'def_line': def_line
                }
    
    def update_var(self, var_name, lineno, value):
        """更新变量定义"""
        self.var_definitions[var_name] = lineno
        if var_name not in self.var_history:
            self.var_history[var_name] = []
        self.var_history[var_name].append((lineno, value))
        
        if self.function_contexts:
            self.function_contexts[-1]['local_vars'][var_name] = lineno
    
    def get_def_line(self, var_name):
        """获取变量最后定义的行号"""
        return self.var_definitions.get(var_name)
    
    def get_var_source_info(self, var_name):
        """获取变量来源信息"""
        if var_name in self.param_sources:
            param_info = self.param_sources[var_name]
            actual_var = param_info.get('actual_var', var_name)
            def_line = param_info.get('def_line')
            
            if def_line:
                if self.lang == 'en':
                    return f"parameter {var_name} defined at [line {def_line}]"
                else:
                    return f"参数 {var_name} 定义于 [第{def_line}行]"
            else:
                if self.lang == 'en':
                    return f"parameter {var_name}"
                else:
                    return f"参数 {var_name}"
        
        def_line = self.var_definitions.get(var_name)
        if def_line:
            return self.templates['var_source'].format(def_line=def_line)
        return self.templates['var_unknown']


class ParameterExtractor:
    """参数提取器"""
    
    def __init__(self, var_tracker, lang='en'):
        self.var_tracker = var_tracker
        self.lang = lang
    
    def extract(self, line, line_type, classifier, prev_var_dict=None, call_line_info=None):
        """提取模板参数"""
        params = {
            'line': line.lineno,
            'code': line.code.strip() if not line.is_function_enter and not line.is_function_return else '',
        }
        
        var_dict = line.get_var_dict()
        
        # 函数进入
        if line_type == 'function_enter':
            params['func_name'] = line.func_name
            param_strs = []
            
            if line.param_mapping:
                for param_name in line.var_names:
                    idx = line.var_names.index(param_name)
                    if idx < len(line.var_values):
                        param_value_raw = line.var_values[idx]
                        from pruner import ValueFormatter
                        param_value = ValueFormatter.format(param_value_raw)
                    else:
                        param_value = '?'
                    
                    if param_name in line.param_mapping:
                        mapping_info = line.param_mapping[param_name]
                        actual_var = mapping_info.get('actual_var', param_name)
                        
                        def_line = self.var_tracker.get_def_line(actual_var)
                        if def_line:
                            if self.lang == 'en':
                                source_info = f"defined at [line {def_line}]"
                                param_strs.append(f"{param_name}={param_value} ({actual_var} {source_info})")
                            else:
                                source_info = f"[第{def_line}行]"
                                param_strs.append(f"{param_name}={param_value} (来自{actual_var}在{source_info})")
                        else:
                            param_strs.append(f"{param_name}={param_value}")
                    else:
                        param_strs.append(f"{param_name}={param_value}")
            else:
                for name in line.var_names:
                    idx = line.var_names.index(name)
                    if idx < len(line.var_values):
                        from pruner import ValueFormatter
                        value = ValueFormatter.format(line.var_values[idx])
                    else:
                        value = '?'
                    param_strs.append(f"{name}={value}")
            
            params['params'] = ', '.join(param_strs) if param_strs else 'no parameters'
            return params
        
        # 函数返回
        if line_type == 'function_return':
            params['func_name'] = line.func_name
            from pruner import ValueFormatter
            params['value'] = ValueFormatter.format(line.return_value)
            return params
        
        # Print语句
        if line_type == 'print_statement':
            match = re.search(r'print\((.*)\)', line.code)
            if match:
                print_arg = match.group(1).strip()
                if print_arg in var_dict:
                    source = self.var_tracker.get_var_source_info(print_arg)
                    params['print_content'] = f"{print_arg}={var_dict[print_arg]} ({source})"
                else:
                    params['print_content'] = print_arg
        
        # 提取变量名
        if line_type in ['assign_constant', 'assign_expr', 'aug_assign', 'function_call']:
            lvalues = self._extract_lvalue(line.code)
            if lvalues:
                params['var'] = lvalues[0]
                params['value'] = var_dict.get(lvalues[0], '?')
                params['result'] = params['value']
        
        # 函数调用赋值
        if line_type == 'function_call':
            match = re.match(r'\s*(\w+)\s*=\s*(\w+)\((.*)\)', line.code)
            if match:
                var_name = match.group(1)
                func_name = match.group(2)
                args_str = match.group(3)
                
                params['var'] = var_name
                params['func_name'] = func_name
                params['value'] = var_dict.get(var_name, '?')
                params['result'] = params['value']
                
                # 解析参数
                arg_details = []
                if args_str:
                    # **修复：检测是否是生成器表达式**
                    if 'for' in args_str:
                        # 生成器表达式，直接显示整个表达式
                        arg_details.append(args_str)
                    else:
                        args = [a.strip() for a in args_str.split(',')]
                        for arg in args:
                            if arg in var_dict or (prev_var_dict and arg in prev_var_dict):
                                val = var_dict.get(arg) or prev_var_dict.get(arg)
                                source = self.var_tracker.get_var_source_info(arg)
                                arg_details.append(f"{arg}={val} ({source})")
                            else:
                                arg_details.append(arg)
                
                params['params'] = ', '.join(arg_details) if arg_details else ''
                
                self.var_tracker.update_var(var_name, line.lineno, params['value'])
        
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
                params['def_line'] = self.var_tracker.get_var_source_info(var)
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
                params['value'] = f"{return_val}={var_dict[return_val]} ({source})"
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
        unique_vars = set()
        
        for var in variables:
            if var in ['range', 'len', 'sum', 'max', 'min', 'int', 'str', 'list', 'dict', 'True', 'False', 'None'] or var in unique_vars:
                continue
            unique_vars.add(var)
            
            if var in lvalue_set:
                if prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val} ({source})")
            else:
                if var in var_dict:
                    val = var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val} ({source})")
                elif prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val} ({source})")
        
        if var_details:
            detail_str = f", where {', '.join(var_details)}" if self.lang == 'en' else f", 其中 {', '.join(var_details)}"
            return f"{expr}{detail_str}"
        else:
            return expr


class COTGenerator:
    """行内注释式COT生成器 - 修复生成器重复问题"""
    
    def __init__(self, pruned_file, lang='en'):
        self.pruned_file = pruned_file
        self.lang = lang
        self.templates = TEMPLATES[lang]
        self.target_line = None
        self.target_var = None
        self.lines = []
        self.var_tracker = VariableTracker(lang=self.lang)
        self.return_values = {}
    
    def load_pruned_trace(self):
        """加载剪枝后的追踪文件"""
        with open(self.pruned_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        self.target_line = int(content[0].strip())
        self.target_var = content[1].strip()
        
        from pruner import TraceLine
        i = 3
        param_mapping = {}
        current_call_line = None
        
        while i < len(content):
            line = content[i].strip()
            if not line:
                i += 1
                continue
            
            if line.startswith('PARAM_MAPPING'):
                parts = line.split(' ', 1)
                if len(parts) >= 2:
                    try:
                        param_mapping = eval(parts[1])
                    except:
                        param_mapping = {}
                i += 1
                continue
            
            if line.startswith('FUNCTION_ENTER'):
                parts = line.split(' ', 3)
                if len(parts) >= 4:
                    lineno = int(parts[1])
                    func_name = parts[2]
                    code = parts[3]
                    
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
                    
                    trace_line = TraceLine(lineno, code, var_names, var_values,
                                         is_function_enter=True, func_name=func_name,
                                         param_mapping=param_mapping.copy())
                    self.lines.append(trace_line)
                    param_mapping = {}
                    i += 1
                    continue
            
            if line.startswith('FUNCTION_RETURN'):
                parts = line.split(' ', 3)
                if len(parts) >= 4:
                    lineno = int(parts[1])
                    func_name = parts[2]
                    return_value_str = parts[3]
                    try:
                        return_value = eval(return_value_str)
                    except:
                        return_value = return_value_str
                    
                    if current_call_line:
                        from pruner import ValueFormatter
                        self.return_values[current_call_line] = ValueFormatter.format(return_value)
                        current_call_line = None
                    
                    trace_line = TraceLine(lineno, '', [], [],
                                         is_function_return=True,
                                         func_name=func_name,
                                         return_value=return_value)
                    self.lines.append(trace_line)
                    i += 1
                    continue
            
            parts = line.split(' ', 1)
            if len(parts) < 2:
                i += 1
                continue
            
            lineno = int(parts[0])
            code = parts[1]
            
            if '=' in code and '(' in code:
                try:
                    tree = ast.parse(code)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
                            current_call_line = lineno
                            break
                except:
                    pass
            
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
        """生成行内注释式COT（修复生成器重复）"""
        
        # 预计算循环总数
        total_counts = {}
        dry_classifier = CodeClassifier()
        prev_line = None
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            dry_classifier.classify(line, prev_line, next_line)
            prev_line = line
        total_counts = dry_classifier.loop_counters

        # 实际生成
        classifier = CodeClassifier()
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
        loop_skip_state = {}
        function_depth = 0

        LOOP_SUMMARY_THRESHOLD = 5
        SKIP_AFTER_ITER = 2
        RESUME_BEFORE_ITER = 2
        
        # **新增：记录已处理的行号**
        processed_lines = set()
        
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            
            line_type = classifier.classify(line, prev_line_obj, next_line)
            
            # **新增：跳过重复的生成器迭代**
            if line_type == 'generator_iteration':
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            # **新增：同一行号只处理一次（针对生成器表达式）**
            if not line.is_function_enter and not line.is_function_return:
                if line.lineno in processed_lines:
                    # 如果是生成器表达式的后续迭代，跳过
                    if classifier._is_generator_expression(line.code):
                        prev_var_dict = line.get_var_dict()
                        prev_line_obj = line
                        continue
                processed_lines.add(line.lineno)
            
            # 处理函数进入
            if line_type == 'function_enter':
                function_depth += 1
                indent = "  " * (function_depth - 1)
                
                self.var_tracker.enter_function(line.func_name, line.param_mapping)
                
                params = extractor.extract(line, line_type, classifier, prev_var_dict)
                template_info = inline_templates.get(line_type)
                
                if template_info:
                    comment_text = template_info['template'].format(**params)
                    comment_text = comment_text.lstrip().lstrip('#').lstrip()
                    
                    if self.lang == 'zh':
                        code_line = f"{indent}[第{line.lineno}行]  {line.code}"
                        explain_line = f"{indent}{comment_text}"
                    else:
                        code_line = f"{indent}[line {line.lineno}]  {line.code}"
                        explain_line = f"{indent}{comment_text}"

                    output_lines.append(code_line)
                    if comment_text:
                        output_lines.append(explain_line)
                
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            # 处理函数返回
            if line_type == 'function_return':
                indent = "  " * (function_depth - 1)
                
                params = extractor.extract(line, line_type, classifier, prev_var_dict)
                template_info = inline_templates.get(line_type)
                
                if template_info:
                    comment_text = template_info['template'].format(**params)
                    comment_text = comment_text.lstrip().lstrip('#').lstrip()
                    
                    if self.lang == 'zh':
                        explain_line = f"{indent}{comment_text}"
                    else:
                        explain_line = f"{indent}{comment_text}"
                    
                    output_lines.append(explain_line)
                
                self.var_tracker.exit_function()
                
                function_depth = max(0, function_depth - 1)
                prev_line_obj = line
                continue
            
            # 循环总结逻辑
            if line_type in ('for_start', 'while_start'):
                current_loop_header = line.lineno
                loop_skip_state[current_loop_header] = False
            
            if current_loop_header:
                total_iter = total_counts.get(current_loop_header, 0)
                current_iter = classifier.loop_counters.get(current_loop_header, 0)
                
                START_SKIP_ITER = SKIP_AFTER_ITER + 1
                RESUME_ITER = total_iter - RESUME_BEFORE_ITER + 1

                is_summarizable = total_iter > LOOP_SUMMARY_THRESHOLD
                
                if is_summarizable:
                    if current_iter == START_SKIP_ITER:
                        num_skipped = total_iter - SKIP_AFTER_ITER - RESUME_BEFORE_ITER
                        summary_template = {
                            'en': f"\n... [Line {current_loop_header}] repeats {num_skipped} more times ...\n",
                            'zh': f"\n... [第{current_loop_header}行] 额外循环了 {num_skipped} 次 ...\n"
                        }
                        output_lines.append(summary_template[self.lang].strip()) 
                        loop_skip_state[current_loop_header] = True
                    
                    elif current_iter == RESUME_ITER:
                        loop_skip_state[current_loop_header] = False
                
                if loop_skip_state.get(current_loop_header, False):
                    prev_var_dict = line.get_var_dict()
                    prev_line_obj = line
                    if line_type in ('for_end', 'while_end'):
                        current_loop_header = None
                    continue

            if line_type == 'unknown':
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            params = extractor.extract(line, line_type, classifier, prev_var_dict)
            
            template_info = inline_templates.get(line_type)
            if not template_info:
                if line_type in ['assign_constant', 'assign_expr', 'aug_assign']:
                    lvalues = extractor._extract_lvalue(line.code)
                    if lvalues:
                        var_name = lvalues[0]
                        var_value = line.get_var_dict().get(var_name, '?')
                        self.var_tracker.update_var(var_name, line.lineno, var_value)
                
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            indent = "  " * function_depth
            
            comment_text = ""
            try:
                comment_with_prefix = template_info['template'].format(**params)
                comment_text = comment_with_prefix.lstrip().lstrip('#').lstrip()
            except KeyError as e:
                comment_text = f"(Missing param: {e})"

            if self.lang == 'zh':
                code_line = f"{indent}[第{line.lineno}行]  {line.code}"
                explain_line = f"{indent}{comment_text}"
            else:
                code_line = f"{indent}[line {line.lineno}]  {line.code}"
                explain_line = f"{indent}{comment_text}"        
            
            output_lines.append(code_line)
            if comment_text:
                output_lines.append(explain_line)
            
            prev_var_dict = line.get_var_dict()
            prev_line_obj = line
            
            if line_type in ('for_end', 'while_end'):
                current_loop_header = None
        
        # 最终答案
        final_value = '?'
        
        if self.target_line in self.return_values:
            final_value = self.return_values[self.target_line]
        else:
            for line in reversed(self.lines):
                if not line.is_function_enter and not line.is_function_return:
                    var_dict = line.get_var_dict()
                    if self.target_var in var_dict:
                        final_value = var_dict[self.target_var]
                        break
        
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