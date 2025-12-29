"""
依赖分析和智能剪枝模块 - 增强函数调用支持（支持函数内部剪枝）
"""

import ast
import re
import json
from typing import Set, Dict, List, Tuple, Optional
from attribute_analyzer import (
    analyze_file_for_attribute_usage, 
    analyze_lines_for_attribute_usage,
    SmartObjectFormatter
)


class TraceLine:
    """表示追踪文件中的一行"""
    def __init__(self, lineno, code, var_names=None, var_values=None, depth=0, 
                 is_function_enter=False, is_function_return=False, func_name=None, 
                 return_value=None, param_mapping=None):
        self.lineno = lineno
        self.code = code.strip()
        self.var_names = var_names or []
        self.var_values = var_values or []
        self.depth = depth
        self.is_function_enter = is_function_enter
        self.is_function_return = is_function_return
        self.func_name = func_name
        self.return_value = return_value
        self.param_mapping = param_mapping or {}
    
    def get_var_dict(self):
        """获取变量字典"""
        return dict(zip(self.var_names, self.var_values))
    
    def __repr__(self):
        if self.is_function_enter:
            return f"TraceLine(ENTER {self.func_name} at {self.lineno})"
        elif self.is_function_return:
            return f"TraceLine(RETURN {self.func_name} at {self.lineno})"
        return f"TraceLine({self.lineno}, {self.code[:30]}..., depth={self.depth})"


class ValueFormatter:
    """值格式化器"""
    
    @staticmethod
    def format(value_struct, var_name='', required_attrs=None, depth=0):
        """格式化结构化值"""
        if depth > 3:
            return "..."
        
        if not isinstance(value_struct, dict) or '_type' not in value_struct:
            return str(value_struct)
        
        vtype = value_struct['_type']
        
        if vtype == 'str':
            return f"'{value_struct['_value']}'"
        elif vtype in ['int', 'float', 'bool']:
            return str(value_struct['_value'])
        elif vtype == 'None':
            return 'None'
        elif vtype == 'list':
            items = value_struct.get('_items', [])
            total = value_struct.get('_len', len(items))
            if not items:
                return '[]'
            if depth >= 2:
                return f'[...{total} items]'
            formatted = [ValueFormatter.format(item, '', None, depth+1) for item in items[:5]]
            if total > len(formatted):
                formatted.append('...')
            return f"[{', '.join(formatted)}]"
        elif vtype == 'tuple':
            items = value_struct.get('_items', [])
            total = value_struct.get('_len', len(items))
            if not items:
                return '()'
            if depth >= 2:
                return f'(...{total} items)'
            formatted = [ValueFormatter.format(item, '', None, depth+1) for item in items[:5]]
            if total > len(formatted):
                formatted.append('...')
            return f"({', '.join(formatted)})"
        elif vtype == 'namedtuple':
            class_name = value_struct.get('_class', 'namedtuple')
            attrs = value_struct.get('_attrs', {})
            if not attrs or depth >= 2:
                return f"{class_name}(...)"
            parts = []
            for k, v in list(attrs.items())[:5]:
                formatted = ValueFormatter.format(v, f"{var_name}.{k}", None, depth+1)
                parts.append(f"{k}={formatted}")
            return f"{class_name}({', '.join(parts)})"
        elif vtype == 'dict':
            items = value_struct.get('_items', {})
            total = value_struct.get('_len', len(items))
            if not items:
                return '{}'
            if depth >= 2:
                return f'{{...{total} items}}'
            parts = []
            for k, v in list(items.items())[:3]:
                formatted_v = ValueFormatter.format(v, '', None, depth+1)
                parts.append(f"{k}: {formatted_v}")
            if total > len(parts):
                parts.append('...')
            return f"{{{', '.join(parts)}}}"
        elif vtype == 'set':
            items = value_struct.get('_items', [])
            total = value_struct.get('_len', len(items))
            if not items:
                return 'set()'
            if depth >= 2:
                return f'{{...{total} items}}'
            formatted = [ValueFormatter.format(item, '', None, depth+1) for item in items[:5]]
            if total > len(formatted):
                formatted.append('...')
            return f"{{{', '.join(formatted)}}}"
        elif vtype == 'object':
            class_name = value_struct.get('_class', 'object')
            all_attrs = value_struct.get('_attrs', {})
            
            if not all_attrs:
                return f"{class_name}(...)"
            
            if required_attrs:
                parts = []
                for attr in sorted(required_attrs):
                    if attr in all_attrs:
                        attr_value = all_attrs[attr]
                        sub_required = {a.split('.', 1)[1] for a in required_attrs 
                                      if a.startswith(attr + '.') and '.' in a.split(attr + '.', 1)[1]}
                        formatted = ValueFormatter.format(
                            attr_value, 
                            f"{var_name}.{attr}",
                            sub_required if sub_required else None,
                            depth + 1
                        )
                        parts.append(f"{attr}={formatted}")
                
                if not parts:
                    return f"{class_name}(...)"
                return f"{class_name}({', '.join(parts)})"
            else:
                if depth >= 2:
                    return f"{class_name}(...)"
                parts = []
                for k, v in list(all_attrs.items())[:5]:
                    formatted = ValueFormatter.format(v, f"{var_name}.{k}", None, depth+1)
                    parts.append(f"{k}={formatted}")
                if len(all_attrs) > 5:
                    parts.append('...')
                return f"{class_name}({', '.join(parts)})"
        else:
            return value_struct.get('_repr', str(value_struct))


class AttributeAccessAnalyzer:
    """属性访问分析器"""
    
    @staticmethod
    def analyze_code(code):
        """分析代码中的属性访问"""
        attr_paths = set()
        simple_vars = set()
        
        try:
            tree = ast.parse(code)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Attribute):
                    path = AttributeAccessAnalyzer._build_path(node)
                    if path:
                        attr_paths.add(path)
                        root = path.split('.')[0]
                        simple_vars.add(root)
                elif isinstance(node, ast.Name):
                    simple_vars.add(node.id)
        except:
            pass
        
        return attr_paths, simple_vars
    
    @staticmethod
    def _build_path(node):
        """构建属性访问路径"""
        parts = []
        current = node
        
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        
        if isinstance(current, ast.Name):
            parts.append(current.id)
            return '.'.join(reversed(parts))
        
        return None


class DependencyAnalyzer:
    """依赖分析器"""
    
    def __init__(self):
        self.focused_vars = set()
        self.var_first_use = {}
    
    def extract_lvalue(self, code):
        """提取赋值语句左值"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    targets = []
                    for target in node.targets:
                        targets.extend(self._extract_names(target, include_attrs=True))
                    return targets
                elif isinstance(node, ast.AugAssign):
                    return self._extract_names(node.target, include_attrs=True)
        except:
            match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_.]*)\s*[=+\-*/]=', code)
            if match:
                return [match.group(1)]
        return []
    
    def _extract_names(self, node, include_attrs=False):
        """从AST节点提取变量名"""
        if isinstance(node, ast.Name):
            return [node.id]
        elif isinstance(node, ast.Attribute):
            if include_attrs:
                path = self._build_attr_path(node)
                return [path] if path else []
            else:
                return self._extract_names(node.value, include_attrs)
        elif isinstance(node, ast.Tuple) or isinstance(node, ast.List):
            names = []
            for elt in node.elts:
                names.extend(self._extract_names(elt, include_attrs))
            return names
        elif isinstance(node, ast.Subscript):
            return self._extract_names(node.value, include_attrs)
        return []
    
    def _build_attr_path(self, node):
        """构建属性访问路径"""
        parts = []
        current = node
        
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        
        if isinstance(current, ast.Name):
            parts.append(current.id)
            return '.'.join(reversed(parts))
        
        return None
    
    def extract_dependencies(self, code):
        """提取代码行的变量依赖"""
        deps = set()
        
        try:
            attr_accesses, simple_vars = AttributeAccessAnalyzer.analyze_code(code)
            deps.update(attr_accesses)
            
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    right_attrs, right_simple = AttributeAccessAnalyzer.analyze_code(
                        ast.unparse(node.value) if hasattr(ast, 'unparse') else ''
                    )
                    deps.update(right_attrs)
                    deps.update(right_simple)
                    return deps
                elif isinstance(node, ast.AugAssign):
                    left_name = self._extract_names(node.target, include_attrs=True)
                    deps.update(left_name)
                    
                    right_attrs, right_simple = AttributeAccessAnalyzer.analyze_code(
                        ast.unparse(node.value) if hasattr(ast, 'unparse') else ''
                    )
                    deps.update(right_attrs)
                    deps.update(right_simple)
                    return deps
            
            deps.update(simple_vars)
            
        except:
            if '=' in code:
                for op in ['+=', '-=', '*=', '/=', '//=', '%=', '&=', '|=', '^=', '>>=', '<<=']:
                    if op in code:
                        parts = code.split(op, 1)
                        if len(parts) == 2:
                            left_var = parts[0].strip()
                            right_expr = parts[1].strip()
                            deps.add(left_var)
                            vars_in_right = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\b', right_expr)
                            deps.update(vars_in_right)
                        break
                else:
                    parts = code.split('=', 1)
                    if len(parts) == 2:
                        right_expr = parts[1]
                        vars_in_right = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\b', right_expr)
                        deps.update(vars_in_right)
            else:
                vars_in_code = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\b', code)
                deps.update(vars_in_code)
            
            keywords = {'if', 'else', 'elif', 'for', 'while', 'in', 'range', 
                       'def', 'class', 'return', 'True', 'False', 'None', 'print',
                       'and', 'or', 'not', 'is', 'with', 'as', 'try', 'except',
                       'finally', 'raise', 'break', 'continue', 'pass', 'lambda',
                       'yield', 'import', 'from', 'global', 'nonlocal'}
            deps = deps - keywords
        
        return deps
    
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
    
    def is_function_call(self, code):
        """判断是否为函数调用"""
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    return True
        except:
            pass
        return False
    
    def get_root_var(self, var_name):
        """获取属性路径的根变量"""
        return var_name.split('.')[0]
    
    def is_related_var(self, var1, var2):
        """判断两个变量是否相关"""
        if var1 == var2:
            return True
        if var1.startswith(var2 + '.') or var2.startswith(var1 + '.'):
            return True
        return False


class FunctionCallContext:
    """函数调用上下文"""
    def __init__(self, func_name, enter_idx, call_line_idx=None):
        self.func_name = func_name
        self.enter_idx = enter_idx  # 函数ENTER的索引
        self.return_idx = None      # 函数RETURN的索引
        self.call_line_idx = call_line_idx  # 调用该函数的行索引
        self.function_lines = []    # 函数内部的所有行索引
        self.kept_lines = set()     # 函数内部需要保留的行索引


class TracePruner:
    """追踪记录剪枝器 - 支持函数内部剪枝"""
    
    def __init__(self, trace_file, source_file=None):
        self.trace_file = trace_file
        self.source_file = source_file
        self.lines = []
        self.analyzer = DependencyAnalyzer()
        self.target_line = None
        self.function_contexts = {}  # {func_name: [FunctionCallContext, ...]}
    
    def load_trace(self):
        """加载追踪文件"""
        with open(self.trace_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        i = 0
        param_mapping = {}
        
        while i < len(content):
            line = content[i].strip()
            if not line:
                i += 1
                continue
            
            if line.startswith('PARAM_MAPPING'):
                parts = line.split(' ', 2)
                if len(parts) >= 3:
                    func_name = parts[1]
                    mapping_str = parts[2]
                    try:
                        param_mapping = eval(mapping_str)
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
                    
                    trace_line = TraceLine(lineno, '', [], [], 
                                         is_function_return=True, 
                                         func_name=func_name,
                                         return_value=return_value)
                    self.lines.append(trace_line)
                    i += 1
                    continue
            
            depth = 0
            if line.startswith('DEPTH_'):
                match = re.match(r'DEPTH_(\d+)\s+(.+)', line)
                if match:
                    depth = int(match.group(1))
                    line = match.group(2)
            
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
            
            trace_line = TraceLine(lineno, code, var_names, var_values, depth=depth)
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
        except Exception as e:
            print(f"解析变量列表失败: {e}")
        return [], []
    
    def _build_function_contexts(self):
        """构建函数调用上下文"""
        self.function_contexts = {}
        context_stack = []  # 栈来追踪嵌套的函数调用
        
        for idx, line in enumerate(self.lines):
            if line.is_function_enter:
                # 创建新的函数上下文
                context = FunctionCallContext(line.func_name, idx)
                
                if line.func_name not in self.function_contexts:
                    self.function_contexts[line.func_name] = []
                self.function_contexts[line.func_name].append(context)
                
                context_stack.append(context)
                
            elif line.is_function_return:
                # 结束当前函数上下文
                if context_stack:
                    context = context_stack.pop()
                    if context.func_name == line.func_name:
                        context.return_idx = idx
                        
            elif context_stack:
                # 函数内部的普通行
                context_stack[-1].function_lines.append(idx)
    
    def _prune_function(self, context: FunctionCallContext, focused_vars: Set[str]):
        """
        对单个函数进行剪枝
        
        Args:
            context: 函数调用上下文
            focused_vars: 从调用处传入的关注变量（参数）
        
        Returns:
            函数内部需要保留的行索引集合
        """
        print(f"\n  === 剪枝函数 {context.func_name} ===")
        
        if context.return_idx is None:
            print(f"  警告: 函数 {context.func_name} 没有return")
            return set()
        
        # 获取返回值相关的变量
        return_line = self.lines[context.return_idx]
        
        # 如果有明确的return语句,提取返回的变量
        return_vars = set()
        for idx in reversed(context.function_lines):
            line = self.lines[idx]
            if 'return' in line.code:
                # 提取return后的变量
                match = re.search(r'return\s+(.+)', line.code)
                if match:
                    return_expr = match.group(1).strip()
                    return_vars.update(self.analyzer.extract_dependencies(f"_ = {return_expr}"))
                break
        
        # 如果没找到明确的return变量,使用focused_vars
        if not return_vars:
            return_vars = focused_vars.copy()
        
        print(f"  返回值相关变量: {return_vars}")
        print(f"  参数传入的关注变量: {focused_vars}")
        
        # 合并关注变量
        func_focused = return_vars | focused_vars
        
        keep_lines = set()
        var_enter_line = {}
        
        # 从函数末尾向前回溯
        for idx in reversed(context.function_lines):
            line = self.lines[idx]
            
            # 控制流必须保留
            if self.analyzer.is_control_flow(line.code):
                keep_lines.add(idx)
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - func_focused
                if new_deps:
                    print(f"  第{line.lineno}行(控制流): {line.code.strip()}")
                    print(f"    新增依赖: {new_deps}")
                    func_focused.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
                continue
            
            # print语句
            if self.analyzer.is_print_statement(line.code):
                deps = self.analyzer.extract_dependencies(line.code)
                if any(self.analyzer.is_related_var(dep, fv) for dep in deps for fv in func_focused):
                    keep_lines.add(idx)
                    print(f"  第{line.lineno}行(print): {line.code.strip()}")
                continue
            
            # 赋值语句
            lvalues = self.analyzer.extract_lvalue(line.code)
            
            if any(self.analyzer.is_related_var(lv, fv) for lv in lvalues for fv in func_focused):
                keep_lines.add(idx)
                
                print(f"  第{line.lineno}行(赋值): {line.code.strip()}")
                print(f"    定义了关注变量: {set(lvalues)}")
                
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - func_focused
                
                if new_deps:
                    print(f"    新增依赖: {new_deps}")
                    func_focused.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
        
        print(f"  函数 {context.func_name} 保留 {len(keep_lines)} 行")
        
        # 同时保留函数的ENTER和RETURN
        keep_lines.add(context.enter_idx)
        if context.return_idx:
            keep_lines.add(context.return_idx)
        
        context.kept_lines = keep_lines
        return keep_lines
    
    def prune(self, target_line, target_var):
        """执行剪枝（支持函数内部剪枝）"""
        self.target_line = target_line
        
        print(f"\n===== 剪枝分析（支持函数内部剪枝） =====")
        print(f"目标行: {target_line}, 目标变量: {target_var}")
        
        # 第一步：构建函数调用上下文
        self._build_function_contexts()
        
        print(f"\n发现 {sum(len(v) for v in self.function_contexts.values())} 个函数调用")
        for func_name, contexts in self.function_contexts.items():
            print(f"  - {func_name}: {len(contexts)} 次调用")
        
        # 第二步：主流程剪枝
        focused_vars = {target_var}
        keep_lines = set()
        var_enter_line = {}
        
        target_line_obj = None
        for idx, line in enumerate(self.lines):
            if line.lineno == target_line and not line.is_function_enter and not line.is_function_return:
                target_line_obj = line
                target_idx = idx
        
        if target_line_obj:
            deps = self.analyzer.extract_dependencies(target_line_obj.code)
            print(f"\n目标行代码: {target_line_obj.code}")
            print(f"目标行依赖: {deps}")
            focused_vars.update(deps)
            for dep in deps:
                var_enter_line[dep] = target_line
        
        print(f"初始关注变量集合: {focused_vars}\n")
        
        # 记录需要剪枝的函数调用
        functions_to_prune = {}  # {context: 传入的关注变量}
        
        # 从目标行向上回溯
        for idx in range(len(self.lines) - 1, -1, -1):
            line = self.lines[idx]
            
            if not line.is_function_enter and not line.is_function_return and line.lineno > target_line:
                continue
            
            # 函数返回 - 标记为保留（稍后可能会被函数剪枝移除）
            if line.is_function_return:
                # 先暂时保留,后面函数剪枝时会决定是否真的保留
                pass
            
            # 函数进入 - 检查是否需要剪枝
            elif line.is_function_enter:
                # 查找对应的函数上下文
                for context in self.function_contexts.get(line.func_name, []):
                    if context.enter_idx == idx:
                        # 提取函数参数对应的实参变量
                        param_focused = set()
                        for param_name in line.var_names:
                            if param_name in line.param_mapping:
                                actual_var = line.param_mapping[param_name].get('actual_var', param_name)
                                # 检查实参是否在关注集合中
                                if any(self.analyzer.is_related_var(actual_var, fv) for fv in focused_vars):
                                    param_focused.add(param_name)
                        
                        if param_focused:
                            print(f"\n需要剪枝函数 {line.func_name}, 关注参数: {param_focused}")
                            functions_to_prune[context] = param_focused
                        
                        break
            
            elif line.lineno == target_line:
                keep_lines.add(idx)
                continue
            
            elif self.analyzer.is_control_flow(line.code):
                keep_lines.add(idx)
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - focused_vars
                if new_deps:
                    print(f"第{line.lineno}行(控制流): {line.code.strip()}")
                    print(f"  新增依赖: {new_deps}")
                    focused_vars.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
                continue
            
            elif self.analyzer.is_print_statement(line.code):
                deps = self.analyzer.extract_dependencies(line.code)
                if any(self.analyzer.is_related_var(dep, fv) for dep in deps for fv in focused_vars):
                    keep_lines.add(idx)
                    print(f"第{line.lineno}行(print): {line.code.strip()}")
                continue
            
            else:
                lvalues = self.analyzer.extract_lvalue(line.code)
                
                if any(self.analyzer.is_related_var(lv, fv) for lv in lvalues for fv in focused_vars):
                    keep_lines.add(idx)
                    
                    print(f"第{line.lineno}行(赋值): {line.code.strip()}")
                    print(f"  定义了关注变量: {set(lvalues)}")
                    
                    deps = self.analyzer.extract_dependencies(line.code)
                    new_deps = deps - focused_vars
                    
                    if new_deps:
                        print(f"  新增依赖: {new_deps}")
                        focused_vars.update(new_deps)
                        for dep in new_deps:
                            var_enter_line[dep] = line.lineno
        
        # 第三步：对识别出的函数进行剪枝
        print(f"\n===== 开始函数内部剪枝 =====")
        for context, param_vars in functions_to_prune.items():
            func_kept = self._prune_function(context, param_vars)
            keep_lines.update(func_kept)
        
        print(f"\n最终关注变量集合: {focused_vars}")
        print(f"主流程保留的行: {len(keep_lines - set().union(*[c.kept_lines for c in functions_to_prune.keys()]))}")
        print(f"函数内保留的行: {len(set().union(*[c.kept_lines for c in functions_to_prune.keys()]))}")
        print(f"总共保留的行: {len(keep_lines)}\n")
        
        # 格式化保留的行
        kept_lines = [self.lines[idx] for idx in sorted(keep_lines)]
        
        print("===== 格式化输出 =====")
        
        pruned_lines = []
        
        for i, line in enumerate(kept_lines):
            if line.is_function_enter or line.is_function_return:
                pruned_lines.append(line)
                continue
            
            current_attr_usage = {}
            if self.source_file:
                current_attr_usage = analyze_lines_for_attribute_usage(
                    self.source_file, 
                    line.lineno,
                    line.lineno
                )
            
            future_uses = set()
            for j in range(i + 1, len(kept_lines)):
                future_line = kept_lines[j]
                if not future_line.is_function_enter and not future_line.is_function_return:
                    uses = self.analyzer.extract_dependencies(future_line.code)
                    future_uses.update(uses & focused_vars)
            
            current_defines = set(self.analyzer.extract_lvalue(line.code))
            current_uses = self.analyzer.extract_dependencies(line.code)
            
            vars_to_keep = (current_uses & focused_vars) | \
                          (current_defines & focused_vars) | \
                          (future_uses & focused_vars)
            
            print(f"第{line.lineno}行: {line.code.strip()}")
            
            filtered_names = []
            filtered_values = []
            
            for name, value_struct in zip(line.var_names, line.var_values):
                root_var = self.analyzer.get_root_var(name)
                
                if any(self.analyzer.is_related_var(name, vk) for vk in vars_to_keep):
                    if root_var in current_attr_usage:
                        paths = current_attr_usage[root_var]
                        required = set()
                        for path in paths:
                            parts = path.split('.')
                            if parts[0] == root_var and len(parts) > 1:
                                required.add(parts[1])
                        
                        formatted = ValueFormatter.format(
                            value_struct, 
                            root_var,
                            required if required else None
                        )
                    else:
                        if root_var in current_defines:
                            formatted = ValueFormatter.format(value_struct, root_var, None)
                        else:
                            if isinstance(value_struct, dict) and value_struct.get('_type') == 'object':
                                class_name = value_struct.get('_class', 'object')
                                formatted = f"{class_name}(...)"
                            else:
                                formatted = ValueFormatter.format(value_struct, root_var, None)
                    
                    filtered_names.append(name)
                    filtered_values.append(formatted)
            
            pruned_line = TraceLine(line.lineno, line.code, 
                                   filtered_names, filtered_values, 
                                   depth=line.depth)
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
                if line.is_function_enter:
                    if line.param_mapping:
                        f.write(f"PARAM_MAPPING {line.param_mapping}\n")
                    f.write(f"FUNCTION_ENTER {line.lineno} {line.func_name} {line.code}\n")
                    f.write(f"{line.lineno} {line.var_names} {line.var_values}\n")
                elif line.is_function_return:
                    f.write(f"FUNCTION_RETURN {line.lineno} {line.func_name} {line.return_value}\n")
                else:
                    f.write(f"{line.lineno} {line.code}\n")
                    f.write(f"{line.lineno} {line.var_names} {line.var_values}\n")
    
    @staticmethod
    def prune_trace(trace_file, target_line, target_var, output_file, source_file=None):
        """静态方法：执行剪枝"""
        pruner = TracePruner(trace_file, source_file)
        pruner.load_trace()
        pruned_lines, focused_vars = pruner.prune(target_line, target_var)
        pruner.save_pruned(pruned_lines, target_line, target_var, output_file)
        return output_file, pruned_lines