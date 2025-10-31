"""
依赖分析和智能剪枝模块
从目标行回溯，构建依赖图并剪除无关代码
"""

import ast
import re
from typing import Set, Dict, List, Tuple


class TraceLine:
    """表示追踪文件中的一行"""
    def __init__(self, lineno, code, var_names=None, var_values=None):
        self.lineno = lineno
        self.code = code.strip()
        self.var_names = var_names or []
        self.var_values = var_values or []
    
    def get_var_dict(self):
        """获取变量字典"""
        return dict(zip(self.var_names, self.var_values))
    
    def __repr__(self):
        return f"TraceLine({self.lineno}, {self.code[:30]}...)"


class DependencyAnalyzer:
    """依赖分析器"""
    
    def __init__(self):
        self.focused_vars = set()
        self.var_first_use = {}  # 变量首次使用的行号
    
    def extract_lvalue(self, code):
        """提取赋值语句左值"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    targets = []
                    for target in node.targets:
                        targets.extend(self._extract_names(target))
                    return targets
                elif isinstance(node, ast.AugAssign):
                    return self._extract_names(node.target)
        except:
            # 回退到正则匹配
            match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[=+\-*/]=', code)
            if match:
                return [match.group(1)]
        return []
    
    def _extract_names(self, node):
        """从AST节点提取变量名"""
        if isinstance(node, ast.Name):
            return [node.id]
        elif isinstance(node, ast.Tuple) or isinstance(node, ast.List):
            names = []
            for elt in node.elts:
                names.extend(self._extract_names(elt))
            return names
        elif isinstance(node, ast.Subscript):
            return self._extract_names(node.value)
        elif isinstance(node, ast.Attribute):
            return self._extract_names(node.value)
        return []
    
    def extract_dependencies(self, code):
        """提取代码行的变量依赖（右值使用的变量）"""
        deps = set()
        
        try:
            tree = ast.parse(code)
            
            for node in ast.walk(tree):
                # 赋值语句：只分析右值
                if isinstance(node, ast.Assign):
                    deps.update(self._extract_names_from_expr(node.value))
                elif isinstance(node, ast.AugAssign):
                    # 增强赋值：a += b 需要读取 a 和 b
                    deps.update(self._extract_names_from_expr(node.value))
                    deps.update(self._extract_names(node.target))
                # 控制流条件
                elif isinstance(node, (ast.If, ast.While)):
                    deps.update(self._extract_names_from_expr(node.test))
                # for循环
                elif isinstance(node, ast.For):
                    deps.update(self._extract_names_from_expr(node.iter))
                # return语句
                elif isinstance(node, ast.Return):
                    if node.value:
                        deps.update(self._extract_names_from_expr(node.value))
                # print语句
                elif isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id == 'print':
                        for arg in node.args:
                            deps.update(self._extract_names_from_expr(arg))
        except:
            # 回退到简单的正则匹配
            # 如果是赋值语句，只分析右侧
            if '=' in code:
                # 处理增强赋值
                for op in ['+=', '-=', '*=', '/=', '//=', '%=', '&=', '|=', '^=', '>>=', '<<=']:
                    if op in code:
                        parts = code.split(op, 1)
                        if len(parts) == 2:
                            left_var = parts[0].strip()
                            right_expr = parts[1].strip()
                            # 左侧变量也会被读取
                            deps.add(left_var)
                            # 分析右侧
                            vars_in_right = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', right_expr)
                            deps.update(vars_in_right)
                        break
                else:
                    # 普通赋值，只分析右侧
                    parts = code.split('=', 1)
                    if len(parts) == 2:
                        right_expr = parts[1]
                        vars_in_right = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', right_expr)
                        deps.update(vars_in_right)
            else:
                # 不是赋值，分析整行
                vars_in_code = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code)
                deps.update(vars_in_code)
            
            # 过滤掉Python关键字
            keywords = {'if', 'else', 'elif', 'for', 'while', 'in', 'range', 
                       'def', 'class', 'return', 'True', 'False', 'None', 'print',
                       'and', 'or', 'not', 'is', 'with', 'as', 'try', 'except',
                       'finally', 'raise', 'break', 'continue', 'pass', 'lambda',
                       'yield', 'import', 'from', 'global', 'nonlocal'}
            deps = deps - keywords
        
        return deps
    
    def _extract_names_from_expr(self, expr_node):
        """从表达式节点提取所有变量名（只提取Load上下文）"""
        names = set()
        for node in ast.walk(expr_node):
            if isinstance(node, ast.Name):
                # 只提取被读取的变量（Load上下文）
                if isinstance(node.ctx, ast.Load):
                    names.add(node.id)
        return names
    
    def is_control_flow(self, code):
        """判断是否为控制流语句"""
        code_stripped = code.strip()
        control_keywords = ['if ', 'elif ', 'else:', 'for ', 'while ', 
                           'def ', 'class ', 'try:', 'except:', 'finally:', 
                           'with ', 'return', 'break', 'continue']
        return any(code_stripped.startswith(kw) for kw in control_keywords)
    
    def is_print_statement(self, code):
        """判断是否为print语句"""
        code_stripped = code.strip()
        return code_stripped.startswith('print(')


class TracePruner:
    """追踪记录剪枝器"""
    
    def __init__(self, trace_file):
        self.trace_file = trace_file
        self.lines = []
        self.analyzer = DependencyAnalyzer()
        self.target_line = None
    
    def load_trace(self):
        """加载追踪文件"""
        with open(self.trace_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        i = 0
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
                    # 解析变量列表
                    try:
                        parts = next_line.split(' ', 1)
                        if len(parts) > 1:
                            var_data = parts[1]
                            var_names, var_values = self._parse_var_lists(var_data)
                        i += 1  # 跳过变量行
                    except:
                        pass
            
            trace_line = TraceLine(lineno, code, var_names, var_values)
            self.lines.append(trace_line)
            i += 1
    
    def _parse_var_lists(self, var_data):
        """解析变量列表字符串"""
        # 格式: ['a', 'b'] ['1', '2']
        try:
            # 找到两个列表
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
    
    def prune(self, target_line, target_var):
        """执行剪枝"""
        self.target_line = target_line
        
        print(f"\n===== 剪枝分析 =====")
        print(f"目标行: {target_line}, 目标变量: {target_var}")
        
        # ========== 第一遍：回溯确定关注变量和保留行 ==========
        focused_vars = {target_var}
        keep_lines = set()
        var_enter_line = {}  # 记录变量何时进入关注集合
        
        # 找到目标行，分析其依赖
        target_line_obj = None
        for line in self.lines:
            if line.lineno == target_line:
                target_line_obj = line
        
        if target_line_obj:
            # 分析目标行使用的所有变量
            deps = self.analyzer.extract_dependencies(target_line_obj.code)
            print(f"\n目标行代码: {target_line_obj.code}")
            print(f"目标行依赖: {deps}")
            focused_vars.update(deps)
            for dep in deps:
                var_enter_line[dep] = target_line
        
        print(f"初始关注变量集合: {focused_vars}\n")
        
        # 从目标行向上回溯
        for line in reversed(self.lines):
            if line.lineno > target_line:
                continue
            
            # 如果是目标行，必须保留
            if line.lineno == target_line:
                keep_lines.add(line.lineno)
                continue
            
            # 控制流语句总是保留
            if self.analyzer.is_control_flow(line.code):
                keep_lines.add(line.lineno)
                # 提取控制流中的依赖
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - focused_vars
                if new_deps:
                    print(f"第{line.lineno}行(控制流): {line.code.strip()}")
                    print(f"  新增依赖: {new_deps}")
                    focused_vars.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
                continue
            
            # print语句：如果包含关注变量，则保留
            if self.analyzer.is_print_statement(line.code):
                deps = self.analyzer.extract_dependencies(line.code)
                if any(dep in focused_vars for dep in deps):
                    keep_lines.add(line.lineno)
                    print(f"第{line.lineno}行(print): {line.code.strip()}")
                    print(f"  使用了关注变量: {deps & focused_vars}")
                continue
            
            # 检查赋值语句
            lvalues = self.analyzer.extract_lvalue(line.code)
            
            # 如果左值在关注集合中，保留此行
            if any(lv in focused_vars for lv in lvalues):
                keep_lines.add(line.lineno)
                
                print(f"第{line.lineno}行(赋值): {line.code.strip()}")
                print(f"  定义了关注变量: {set(lvalues) & focused_vars}")
                
                # 提取右值依赖
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - focused_vars
                
                if new_deps:
                    print(f"  新增依赖: {new_deps}")
                    focused_vars.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
        
        print(f"\n最终关注变量集合: {focused_vars}")
        print(f"保留的行号: {sorted(keep_lines)}\n")
        
        # ========== 第二遍：为每行计算真正需要的变量 ==========
        # 只保留那些"已经定义 且 后续会使用"的变量
        
        kept_lines = [line for line in self.lines if line.lineno in keep_lines]
        
        print("===== 变量精简分析 =====")
        
        # 为每个保留的行计算需要保留的变量
        pruned_lines = []
        
        for i, line in enumerate(kept_lines):
            # 收集从下一行到最后，哪些变量会被使用
            future_uses = set()
            
            for j in range(i + 1, len(kept_lines)):
                future_line = kept_lines[j]
                
                # 提取这一行使用的变量
                uses = self.analyzer.extract_dependencies(future_line.code)
                future_uses.update(uses & focused_vars)
            
            # 当前行定义的变量
            current_defines = set(self.analyzer.extract_lvalue(line.code))
            
            # 当前行使用的变量
            current_uses = self.analyzer.extract_dependencies(line.code)
            
            # 需要保留的变量 = 
            # 1. 当前行使用的关注变量（右侧需要）
            # 2. 当前行定义的关注变量（左侧）
            # 3. 后续行会使用的关注变量（传播给后续）
            vars_to_keep = (current_uses & focused_vars) | \
                          (current_defines & focused_vars) | \
                          (future_uses & focused_vars)
            
            print(f"第{line.lineno}行: {line.code.strip()}")
            print(f"  当前使用: {current_uses & focused_vars}")
            print(f"  当前定义: {current_defines & focused_vars}")
            print(f"  后续需要: {future_uses & focused_vars}")
            print(f"  保留变量: {vars_to_keep}")
            
            # 过滤变量列表
            filtered_names = []
            filtered_values = []
            for name, value in zip(line.var_names, line.var_values):
                if name in vars_to_keep:
                    filtered_names.append(name)
                    filtered_values.append(value)
            
            pruned_line = TraceLine(line.lineno, line.code, 
                                   filtered_names, filtered_values)
            pruned_lines.append(pruned_line)
        
        print()
        return pruned_lines, focused_vars
    
    def save_pruned(self, pruned_lines, target_line, target_var, output_file):
        """保存剪枝结果"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"{target_line}\n")
            f.write(f"{target_var}\n")
            f.write("---\n")
            
            for line in pruned_lines:
                f.write(f"{line.lineno} {line.code}\n")
                f.write(f"{line.lineno} {line.var_names} {line.var_values}\n")
    
    @staticmethod
    def prune_trace(trace_file, target_line, target_var, output_file):
        """静态方法：执行剪枝"""
        pruner = TracePruner(trace_file)
        pruner.load_trace()
        pruned_lines, focused_vars = pruner.prune(target_line, target_var)
        pruner.save_pruned(pruned_lines, target_line, target_var, output_file)
        return output_file, pruned_lines