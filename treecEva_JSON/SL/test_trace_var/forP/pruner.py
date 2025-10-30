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
        """提取代码行的变量依赖"""
        deps = set()
        
        try:
            tree = ast.parse(code)
            
            for node in ast.walk(tree):
                # 赋值语句右值
                if isinstance(node, ast.Assign):
                    deps.update(self._extract_names_from_expr(node.value))
                elif isinstance(node, ast.AugAssign):
                    deps.update(self._extract_names_from_expr(node.value))
                    deps.update(self._extract_names(node.target))  # a += 1 需要a
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
            # 匹配所有可能的变量名
            vars_in_code = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code)
            # 过滤掉Python关键字
            keywords = {'if', 'else', 'elif', 'for', 'while', 'in', 'range', 
                       'def', 'class', 'return', 'True', 'False', 'None', 'print'}
            deps = set(v for v in vars_in_code if v not in keywords)
        
        return deps
    
    def _extract_names_from_expr(self, expr_node):
        """从表达式节点提取所有变量名"""
        names = set()
        for node in ast.walk(expr_node):
            if isinstance(node, ast.Name):
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
        
        # 第一遍：回溯确定关注变量和保留行
        focused_vars = {target_var}
        keep_lines = set()
        var_enter_line = {}  # 记录变量何时进入关注集合
        
        # 从目标行向上回溯
        for line in reversed(self.lines):
            if line.lineno > target_line:
                continue
            
            # 如果是目标行，必须保留
            if line.lineno == target_line:
                keep_lines.add(line.lineno)
                # 如果是print语句，提取其中的变量依赖
                if self.analyzer.is_print_statement(line.code):
                    deps = self.analyzer.extract_dependencies(line.code)
                    for dep in deps:
                        if dep not in focused_vars:
                            focused_vars.add(dep)
                            var_enter_line[dep] = line.lineno
                continue
            
            # 控制流语句总是保留
            if self.analyzer.is_control_flow(line.code):
                keep_lines.add(line.lineno)
                # 提取控制流中的依赖
                deps = self.analyzer.extract_dependencies(line.code)
                for dep in deps:
                    if dep not in focused_vars:
                        focused_vars.add(dep)
                        var_enter_line[dep] = line.lineno
                continue
            
            # print语句：如果包含关注变量，则保留
            if self.analyzer.is_print_statement(line.code):
                deps = self.analyzer.extract_dependencies(line.code)
                if any(dep in focused_vars for dep in deps):
                    keep_lines.add(line.lineno)
                continue
            
            # 检查赋值语句
            lvalues = self.analyzer.extract_lvalue(line.code)
            
            # 如果左值在关注集合中，保留此行
            if any(lv in focused_vars for lv in lvalues):
                keep_lines.add(line.lineno)
                
                # 提取右值依赖
                deps = self.analyzer.extract_dependencies(line.code)
                for dep in deps:
                    if dep not in focused_vars:
                        focused_vars.add(dep)
                        var_enter_line[dep] = line.lineno
        
        # 第二遍：正向遍历，为每行分配正确的变量列表
        active_vars = set()
        pruned_lines = []
        
        for line in self.lines:
            if line.lineno not in keep_lines:
                continue
            
            # 检查是否有新变量在此行进入关注集合
            for var, enter_line in var_enter_line.items():
                if enter_line == line.lineno:
                    active_vars.add(var)
            
            # 检查此行是否定义了新变量
            lvalues = self.analyzer.extract_lvalue(line.code)
            for lv in lvalues:
                if lv in focused_vars:
                    active_vars.add(lv)
            
            # 对于print语句，也要包含其使用的变量
            if self.analyzer.is_print_statement(line.code):
                deps = self.analyzer.extract_dependencies(line.code)
                active_vars.update(deps)
            
            # 过滤变量列表
            filtered_names = []
            filtered_values = []
            for name, value in zip(line.var_names, line.var_values):
                if name in active_vars:
                    filtered_names.append(name)
                    filtered_values.append(value)
            
            pruned_line = TraceLine(line.lineno, line.code, 
                                   filtered_names, filtered_values)
            pruned_lines.append(pruned_line)
        
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