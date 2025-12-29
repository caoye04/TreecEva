"""
Python代码执行追踪器 - 支持函数调用追踪（增强版）
增加函数调用参数映射追踪
"""

import sys
import linecache
import os
import ast
import re


class PythonTracer:
    """Python代码执行追踪器"""
    
    def __init__(self, target_file):
        self.target_file = os.path.abspath(target_file)
        self.trace_active = False
        self.has_main_function = False
        self.module_started = False
        self.pending_trace = None
        self.output_lines = []
        self.call_stack = []
        self.user_functions = set()
        self.in_user_function = 0
        self.function_signatures = {}  # 存储函数签名
        
    def analyze_function_signatures(self, filename):
        """分析文件中的函数签名"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())
                
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    params = [arg.arg for arg in node.args.args]
                    self.function_signatures[node.name] = params
        except:
            pass
    
    def extract_call_arguments(self, source_line):
        """从调用语句中提取实参名称"""
        try:
            # 匹配 var = func(arg1, arg2, ...)
            match = re.match(r'\s*\w+\s*=\s*(\w+)\((.*)\)', source_line)
            if match:
                args_str = match.group(2).strip()
                if not args_str:
                    return []
                args = [arg.strip() for arg in args_str.split(',')]
                return args
        except:
            pass
        return []
    
    def check_for_main(self, filename):
        """检查文件中是否定义了main函数"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                return 'def main(' in content or 'def main():' in content
        except:
            return False
    
    def should_trace_file(self, filename):
        """判断是否应该追踪该文件"""
        if not filename:
            return False
        abs_filename = os.path.abspath(filename)
        return abs_filename == self.target_file
    
    def trace_handler(self, frame, event, arg):
        """追踪处理函数"""
        filename = frame.f_code.co_filename
        
        if not self.should_trace_file(filename):
            return self.trace_handler
        
        func_name = frame.f_code.co_name
        
        special_names = ['<module>', 'main', '<listcomp>', '<dictcomp>', '<setcomp>', '<genexpr>']
        is_special = func_name in special_names
        
        # 处理call事件
        if event == 'call':
            if func_name == 'main':
                self.has_main_function = True
                self.trace_active = True
                self.call_stack.append(('main', frame.f_lineno))
                return self.trace_handler
            elif not is_special:
                self.user_functions.add(func_name)
                if self.trace_active:
                    # 输出挂起的调用行（主流程）
                    if self.pending_trace:
                        caller_frame = frame.f_back
                        if caller_frame:
                            caller_vars = caller_frame.f_locals.copy()
                            self.output_pending_trace(caller_vars)
                            
                            # 提取调用行的实参
                            call_line = self.pending_trace['source']
                            actual_args = self.extract_call_arguments(call_line)
                            
                            # 输出参数映射信息
                            if actual_args and func_name in self.function_signatures:
                                formal_params = self.function_signatures[func_name]
                                param_mapping = {}
                                for i, (formal, actual) in enumerate(zip(formal_params, actual_args)):
                                    param_mapping[formal] = {
                                        'actual_var': actual,
                                        'value': caller_vars.get(actual, actual)
                                    }
                                
                                # 添加映射信息到输出
                                self.output_lines.append(f"PARAM_MAPPING {func_name} {param_mapping}")
                            
                            self.pending_trace = None
                    
                    # 进入函数
                    self.in_user_function += 1
                    self.call_stack.append((func_name, frame.f_back.f_lineno if frame.f_back else 0))
                    
                    # 输出函数进入信息
                    lineno = frame.f_lineno
                    source_line = linecache.getline(filename, lineno).rstrip()
                    
                    self.output_lines.append(f"FUNCTION_ENTER {lineno} {func_name} {source_line}")
                    
                    # 输出函数参数
                    local_vars = frame.f_locals.copy()
                    filtered_vars = self.filter_variables(local_vars)
                    if filtered_vars:
                        var_names = list(filtered_vars.keys())
                        var_values = [self.serialize_value(filtered_vars[name]) for name in var_names]
                        self.output_lines.append(f"{lineno} {var_names} {var_values}")
                    
                return self.trace_handler
        
        # 模块级别代码
        if not self.has_main_function and func_name == '<module>':
            if not self.module_started:
                self.module_started = True
                self.call_stack.append(('<module>', 0))
            self.trace_active = True
        
        if self.has_main_function and not self.trace_active:
            return self.trace_handler
        
        # 处理line事件
        if event == 'line' and self.trace_active:
            lineno = frame.f_lineno
            source_line = linecache.getline(filename, lineno).rstrip()
            
            if source_line.strip().startswith(('class ', 'def ')) and not source_line.strip().startswith('def main'):
                return self.trace_handler
            
            local_vars = frame.f_locals.copy()
            
            if self.pending_trace:
                self.output_pending_trace(local_vars)
            
            depth = self.in_user_function + 1
            self.pending_trace = {
                'lineno': lineno,
                'source': source_line,
                'depth': depth
            }
        
        # 处理return事件
        elif event == 'return':
            if self.trace_active:
                if self.pending_trace:
                    self.output_pending_trace(frame.f_locals.copy())
                    self.pending_trace = None
                
                if func_name in self.user_functions:
                    lineno = frame.f_lineno
                    return_value = arg
                    
                    self.output_lines.append(f"FUNCTION_RETURN {lineno} {func_name} {self.serialize_value(return_value)}")
                    
                    if self.call_stack and self.call_stack[-1][0] == func_name:
                        self.call_stack.pop()
                    
                    self.in_user_function = max(0, self.in_user_function - 1)
                
                if func_name == 'main':
                    self.trace_active = False
                    if self.call_stack and self.call_stack[-1][0] == 'main':
                        self.call_stack.pop()
                elif func_name == '<module>' and self.module_started:
                    self.trace_active = False
                    if self.call_stack and self.call_stack[-1][0] == '<module>':
                        self.call_stack.pop()
        
        return self.trace_handler
    
    def output_pending_trace(self, current_vars, is_function_enter=False):
        """输出待输出的追踪行"""
        lineno = self.pending_trace['lineno']
        source = self.pending_trace['source']
        depth = self.pending_trace.get('depth', 0)
        
        filtered_vars = self.filter_variables(current_vars)
        
        prefix = f"DEPTH_{depth} " if depth > 1 else ""
        self.output_lines.append(f"{prefix}{lineno} {source}")
        
        if filtered_vars:
            var_names = list(filtered_vars.keys())
            var_values = [self.serialize_value(filtered_vars[name]) for name in var_names]
            self.output_lines.append(f"{lineno} {var_names} {var_values}")
        else:
            self.output_lines.append(f"{lineno} [] []")
    
    def filter_variables(self, local_vars):
        """过滤变量，只保留数据变量"""
        filtered = {}
        for name, value in local_vars.items():
            if name.startswith('__'):
                continue
            if callable(value) and not isinstance(value, type):
                continue
            if isinstance(value, type):
                continue
            if str(type(value)).startswith("<class 'module"):
                continue
            if hasattr(value, '__bases__') and tuple in getattr(value, '__bases__', []):
                continue
            
            filtered[name] = value
        return filtered
    
    def serialize_value(self, value, depth=0):
        """序列化值为结构化数据"""
        if depth > 3:
            return "..."
        
        try:
            if isinstance(value, str):
                return {'_type': 'str', '_value': value}
            elif isinstance(value, bool):
                return {'_type': 'bool', '_value': value}
            elif isinstance(value, int):
                return {'_type': 'int', '_value': value}
            elif isinstance(value, float):
                return {'_type': 'float', '_value': value}
            elif value is None:
                return {'_type': 'None'}
            elif isinstance(value, list):
                items = [self.serialize_value(v, depth+1) for v in value[:10]]
                return {'_type': 'list', '_items': items, '_len': len(value)}
            elif isinstance(value, tuple):
                if hasattr(value, '_fields'):
                    attrs = {}
                    for k in value._fields:
                        attrs[k] = self.serialize_value(getattr(value, k), depth+1)
                    return {
                        '_type': 'namedtuple',
                        '_class': type(value).__name__,
                        '_attrs': attrs
                    }
                else:
                    items = [self.serialize_value(v, depth+1) for v in value[:10]]
                    return {'_type': 'tuple', '_items': items, '_len': len(value)}
            elif isinstance(value, dict):
                items = {}
                for i, (k, v) in enumerate(value.items()):
                    if i >= 5:
                        break
                    items[str(k)] = self.serialize_value(v, depth+1)
                return {'_type': 'dict', '_items': items, '_len': len(value)}
            elif isinstance(value, set):
                items = [self.serialize_value(v, depth+1) for v in list(value)[:10]]
                return {'_type': 'set', '_items': items, '_len': len(value)}
            elif hasattr(value, '__dict__'):
                attrs = {}
                for k, v in value.__dict__.items():
                    if not k.startswith('_'):
                        attrs[k] = self.serialize_value(v, depth+1)
                return {
                    '_type': 'object',
                    '_class': type(value).__name__,
                    '_attrs': attrs
                }
            else:
                return {'_type': 'unknown', '_repr': str(value)}
        except Exception as e:
            return {'_type': 'error', '_msg': str(e)}
    
    def save_output(self, output_file):
        """保存输出到文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.output_lines))
    
    @staticmethod
    def trace_file(script_file, output_file='trace_output.txt'):
        """追踪Python文件的执行"""
        tracer = PythonTracer(script_file)
        tracer.has_main_function = tracer.check_for_main(script_file)
        tracer.analyze_function_signatures(script_file)
        
        sys.settrace(tracer.trace_handler)
        
        try:
            with open(script_file, 'r', encoding='utf-8') as f:
                code = compile(f.read(), script_file, 'exec')
                exec(code, {'__name__': '__main__'})
        except SystemExit:
            pass
        
        sys.settrace(None)
        
        tracer.save_output(output_file)
        
        return output_file