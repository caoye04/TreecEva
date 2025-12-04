# gdb_trace.py
import gdb
import sys

print("=== GDB Python 脚本已加载 ===", file=sys.stderr)

class SimpleVariableTracer:
    def __init__(self):
        self.step_count = 0
        print("=== 追踪器初始化 ===", file=sys.stderr)
        
    def is_user_code(self):
        """检查是否是用户代码"""
        try:
            frame = gdb.selected_frame()
            sal = frame.find_sal()
            if sal.symtab:
                filename = sal.symtab.filename.lower()
                print(f"=== 检查文件: {filename} ===", file=sys.stderr)
                exclude_patterns = ['mingw', 'msvcrt', 'stdio', '/usr/', 
                                   'c:\\windows', 'cygwin', 'include', 
                                   'bits/', 'sys/', 'libc']
                is_user = not any(pattern in filename for pattern in exclude_patterns)
                print(f"=== 是用户代码: {is_user} ===", file=sys.stderr)
                return is_user
        except Exception as e:
            print(f"=== is_user_code 异常: {e} ===", file=sys.stderr)
        return False
    
    def get_all_variables(self):
        """获取所有可见变量"""
        result = {}
        try:
            frame = gdb.selected_frame()
            block = frame.block()
            
            while block:
                for symbol in block:
                    if symbol.is_argument or symbol.is_variable:
                        try:
                            var_name = symbol.name
                            value = frame.read_var(var_name)
                            
                            if value.type.code == gdb.TYPE_CODE_INT:
                                result[var_name] = int(value)
                            elif value.type.code == gdb.TYPE_CODE_FLT:
                                result[var_name] = float(value)
                            else:
                                result[var_name] = str(value)
                        except Exception as e:
                            pass
                
                if block.function:
                    break
                block = block.superblock
        except Exception as e:
            print(f"=== get_all_variables 异常: {e} ===", file=sys.stderr)
        
        return result
    
    def record_step(self):
        """记录当前步骤并输出"""
        if not self.is_user_code():
            return False
            
        try:
            frame = gdb.selected_frame()
            sal = frame.find_sal()
            line_num = sal.line
            
            variables = self.get_all_variables()
            
            # 排序变量名
            sorted_vars = sorted(variables.keys())
            
            if sorted_vars:
                var_names = ','.join(sorted_vars)
                var_values = ','.join([str(variables[v]) for v in sorted_vars])
                output = f"{line_num} [{var_names}] [{var_values}]"
            else:
                output = f"{line_num} [] []"
            
            print(output)
            sys.stdout.flush()
            
            self.step_count += 1
            return True
            
        except Exception as e:
            print(f"=== record_step 异常: {e} ===", file=sys.stderr)
            return False

class TraceVarsCommand(gdb.Command):
    """自动追踪变量的命令"""
    
    def __init__(self):
        super(TraceVarsCommand, self).__init__("trace-vars", gdb.COMMAND_USER)
        print("=== trace-vars 命令已注册 ===", file=sys.stderr)
        
    def invoke(self, arg, from_tty):
        print("=== trace-vars 开始执行 ===", file=sys.stderr)
        tracer = SimpleVariableTracer()
        
        try:
            while True:
                tracer.record_step()
                gdb.execute("next", to_string=True)
        except gdb.error as e:
            print(f"=== GDB 错误: {e} ===", file=sys.stderr)
        except KeyboardInterrupt:
            print("=== 被中断 ===", file=sys.stderr)
        
        print(f"=== 追踪完成,共 {tracer.step_count} 步 ===", file=sys.stderr)

# 注册命令
TraceVarsCommand()
print("=== 脚本加载完成 ===", file=sys.stderr)