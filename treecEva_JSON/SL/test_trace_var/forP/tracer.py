"""
Python代码执行追踪器
基于sys.settrace实现变量追踪
"""

import sys
import linecache
import os


class PythonTracer:
    """Python代码执行追踪器"""
    
    def __init__(self, target_file):
        self.target_file = os.path.abspath(target_file)
        self.trace_active = False
        self.has_main_function = False
        self.module_started = False
        self.pending_trace = None
        self.output_lines = []
        
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
        
        # 只追踪目标文件
        if not self.should_trace_file(filename):
            return self.trace_handler
        
        func_name = frame.f_code.co_name
        
        # 检测main函数的调用
        if event == 'call' and func_name == 'main':
            self.has_main_function = True
            self.trace_active = True
            return self.trace_handler
        
        # 如果没有main函数，追踪模块级代码
        if not self.has_main_function and func_name == '<module>':
            if not self.module_started:
                self.module_started = True
            self.trace_active = True
        
        # 如果有main函数但还没进入main，不追踪
        if self.has_main_function and not self.trace_active:
            return self.trace_handler
        
        if event == 'line' and self.trace_active:
            lineno = frame.f_lineno
            source_line = linecache.getline(filename, lineno).rstrip()
            local_vars = frame.f_locals.copy()
            
            # 输出之前待输出的行
            if self.pending_trace:
                self.output_pending_trace(local_vars)
            
            # 保存当前行信息，等待下次输出
            self.pending_trace = {
                'lineno': lineno,
                'source': source_line
            }
        
        elif event == 'return':
            # 函数返回时，输出最后一行
            if self.pending_trace and self.trace_active:
                self.output_pending_trace(frame.f_locals.copy())
                self.pending_trace = None
            
            # 如果是main函数返回，停止追踪
            if func_name == 'main':
                self.trace_active = False
            # 如果是模块级代码返回，停止追踪
            elif func_name == '<module>' and self.module_started:
                self.trace_active = False
        
        return self.trace_handler
    
    def output_pending_trace(self, current_vars):
        """输出待输出的追踪行"""
        lineno = self.pending_trace['lineno']
        source = self.pending_trace['source']
        
        # 过滤变量
        filtered_vars = self.filter_variables(current_vars)
        
        # 格式化输出
        self.output_lines.append(f"{lineno} {source}")
        
        if filtered_vars:
            var_names = list(filtered_vars.keys())
            var_values = [self.format_value(filtered_vars[k]) for k in var_names]
            self.output_lines.append(f"{lineno} {var_names} {var_values}")
        else:
            self.output_lines.append(f"{lineno} [] []")
    
    def filter_variables(self, local_vars):
        """过滤变量，只保留数据变量"""
        filtered = {}
        for name, value in local_vars.items():
            # 跳过内置变量
            if name.startswith('__'):
                continue
            # 跳过函数、类、模块等
            if callable(value) and not isinstance(value, type):
                continue
            if isinstance(value, type):
                continue
            if str(type(value)).startswith("<class 'module"):
                continue
            # 跳过namedtuple类型本身（但保留实例）
            if hasattr(value, '__bases__') and tuple in getattr(value, '__bases__', []):
                continue
            
            filtered[name] = value
        return filtered
    
    def format_value(self, value, depth=0):
        """格式化变量值"""
        if depth > 3:  # 防止无限递归
            return "..."
        
        try:
            if isinstance(value, str):
                return f"'{value}'"
            elif isinstance(value, (int, float, bool)):
                return str(value)
            elif isinstance(value, list):
                if not value:
                    return "[]"
                items = [self.format_value(v, depth+1) for v in value]
                return f"[{', '.join(items)}]"
            elif isinstance(value, tuple):
                if hasattr(value, '_fields'):  # namedtuple
                    field_strs = [f"{k}={self.format_value(getattr(value, k), depth+1)}" 
                                 for k in value._fields]
                    return f"{type(value).__name__}({', '.join(field_strs)})"
                else:
                    if not value:
                        return "()"
                    items = [self.format_value(v, depth+1) for v in value]
                    return f"({', '.join(items)})"
            elif isinstance(value, dict):
                if not value:
                    return "{}"
                items = [f"{self.format_value(k, depth+1)}: {self.format_value(v, depth+1)}" 
                        for k, v in value.items()]
                return f"{{{', '.join(items)}}}"
            elif isinstance(value, set):
                if not value:
                    return "set()"
                items = [self.format_value(v, depth+1) for v in value]
                return f"{{{', '.join(items)}}}"
            elif hasattr(value, '__dict__'):  # 自定义对象
                return f"<{type(value).__name__} object>"
            else:
                return str(value)
        except:
            return "<error>"
    
    def save_output(self, output_file):
        """保存输出到文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.output_lines))
    
    @staticmethod
    def trace_file(script_file, output_file='trace_output.txt'):
        """追踪Python文件的执行"""
        tracer = PythonTracer(script_file)
        tracer.has_main_function = tracer.check_for_main(script_file)
        
        # 设置追踪
        sys.settrace(tracer.trace_handler)
        
        # 执行目标脚本
        with open(script_file, 'r', encoding='utf-8') as f:
            code = compile(f.read(), script_file, 'exec')
            exec(code, {'__name__': '__main__'})
        
        # 停止追踪
        sys.settrace(None)
        
        # 保存输出
        tracer.save_output(output_file)
        
        return output_file