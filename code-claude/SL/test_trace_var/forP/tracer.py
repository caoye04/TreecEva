"""
Python代码执行追踪器
保存对象的结构化信息，延迟格式化
"""

import sys
import linecache
import os
import json


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
        
        if not self.should_trace_file(filename):
            return self.trace_handler
        
        func_name = frame.f_code.co_name
        
        if func_name not in ['<module>', 'main', '<listcomp>', '<dictcomp>', '<setcomp>']:
            if func_name not in ['main']:
                return self.trace_handler
        
        if event == 'call' and func_name == 'main':
            self.has_main_function = True
            self.trace_active = True
            return self.trace_handler
        
        if not self.has_main_function and func_name == '<module>':
            if not self.module_started:
                self.module_started = True
            self.trace_active = True
        
        if self.has_main_function and not self.trace_active:
            return self.trace_handler
        
        if event == 'line' and self.trace_active:
            lineno = frame.f_lineno
            source_line = linecache.getline(filename, lineno).rstrip()
            
            if source_line.strip().startswith(('class ', 'def ')) and not source_line.strip().startswith('def main'):
                return self.trace_handler
            
            local_vars = frame.f_locals.copy()
            
            if self.pending_trace:
                self.output_pending_trace(local_vars)
            
            self.pending_trace = {
                'lineno': lineno,
                'source': source_line
            }
        
        elif event == 'return':
            if self.pending_trace and self.trace_active:
                self.output_pending_trace(frame.f_locals.copy())
                self.pending_trace = None
            
            if func_name == 'main':
                self.trace_active = False
            elif func_name == '<module>' and self.module_started:
                self.trace_active = False
        
        return self.trace_handler
    
    def output_pending_trace(self, current_vars):
        """输出待输出的追踪行"""
        lineno = self.pending_trace['lineno']
        source = self.pending_trace['source']
        
        filtered_vars = self.filter_variables(current_vars)
        
        self.output_lines.append(f"{lineno} {source}")
        
        if filtered_vars:
            var_names = list(filtered_vars.keys())
            # 保存结构化数据而非格式化字符串
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
        """序列化值为结构化数据（延迟格式化）"""
        if depth > 3:
            return "..."
        
        try:
            # 基础类型
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
            
            # 列表
            elif isinstance(value, list):
                items = [self.serialize_value(v, depth+1) for v in value[:10]]
                return {'_type': 'list', '_items': items, '_len': len(value)}
            
            # 元组（包括namedtuple）
            elif isinstance(value, tuple):
                if hasattr(value, '_fields'):  # namedtuple
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
            
            # 字典
            elif isinstance(value, dict):
                items = {}
                for i, (k, v) in enumerate(value.items()):
                    if i >= 5:
                        break
                    items[str(k)] = self.serialize_value(v, depth+1)
                return {'_type': 'dict', '_items': items, '_len': len(value)}
            
            # 集合
            elif isinstance(value, set):
                items = [self.serialize_value(v, depth+1) for v in list(value)[:10]]
                return {'_type': 'set', '_items': items, '_len': len(value)}
            
            # 自定义对象 - 保存所有属性
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