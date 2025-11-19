"""
依赖分析和智能剪枝模块
从目标行回溯,构建依赖图并剪除无关代码
支持基于未来需求的属性路径精简
"""

import ast
import re
import json
from typing import Set, Dict, List, Tuple
from attribute_analyzer import (
    analyze_file_for_attribute_usage, 
    analyze_lines_for_attribute_usage,
    SmartObjectFormatter
)


class TraceLine:
    """表示追踪文件中的一行"""
    def __init__(self, lineno, code, var_names=None, var_values=None):
        self.lineno = lineno
        self.code = code.strip()
        self.var_names = var_names or []
        self.var_values = var_values or []  # 结构化数据
    
    def get_var_dict(self):
        """获取变量字典"""
        return dict(zip(self.var_names, self.var_values))
    
    def __repr__(self):
        return f"TraceLine({self.lineno}, {self.code[:30]}...)"


class ValueFormatter:
    """值格式化器 - 根据需求格式化结构化数据"""
    
    @staticmethod
    def format(value_struct, var_name='', required_attrs=None, depth=0):
        """
        格式化结构化值
        
        Args:
            value_struct: 序列化的值结构
            var_name: 变量名
            required_attrs: 需要显示的属性集合（只针对对象）
            depth: 当前深度
        """
        if depth > 3:
            return "..."
        
        if not isinstance(value_struct, dict) or '_type' not in value_struct:
            return str(value_struct)
        
        vtype = value_struct['_type']
        
        # 基础类型
        if vtype == 'str':
            return f"'{value_struct['_value']}'"
        elif vtype in ['int', 'float', 'bool']:
            return str(value_struct['_value'])
        elif vtype == 'None':
            return 'None'
        
        # 列表
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
        
        # 元组
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
        
        # namedtuple
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
        
        # 字典
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
        
        # 集合
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
        
        # 自定义对象 - 根据需求选择性显示属性
        elif vtype == 'object':
            class_name = value_struct.get('_class', 'object')
            all_attrs = value_struct.get('_attrs', {})
            
            if not all_attrs:
                return f"{class_name}(...)"
            
            # 如果指定了需要的属性，只显示这些
            if required_attrs:
                parts = []
                for attr in sorted(required_attrs):
                    if attr in all_attrs:
                        attr_value = all_attrs[attr]
                        # 递归检查子属性需求
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
                # 没有指定需求，显示所有属性（用于向后兼容）
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
            # 回退逻辑
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


class TracePruner:
    """追踪记录剪枝器"""
    
    def __init__(self, trace_file, source_file=None):
        self.trace_file = trace_file
        self.source_file = source_file
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
                # values 是结构化数据的列表
                values = eval(values_str)
                return names, values
        except Exception as e:
            print(f"解析变量列表失败: {e}")
        return [], []
    
    def prune(self, target_line, target_var):
        """执行剪枝"""
        self.target_line = target_line
        
        print(f"\n===== 剪枝分析（基于当前行属性访问的精简） =====")
        print(f"目标行: {target_line}, 目标变量: {target_var}")
        
        # 第一遍：回溯确定关注变量和保留行
        focused_vars = {target_var}
        keep_lines = set()
        var_enter_line = {}
        
        target_line_obj = None
        for line in self.lines:
            if line.lineno == target_line:
                target_line_obj = line
        
        if target_line_obj:
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
            
            if line.lineno == target_line:
                keep_lines.add(line.lineno)
                continue
            
            if self.analyzer.is_control_flow(line.code):
                keep_lines.add(line.lineno)
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - focused_vars
                if new_deps:
                    print(f"第{line.lineno}行(控制流): {line.code.strip()}")
                    print(f"  新增依赖: {new_deps}")
                    focused_vars.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
                continue
            
            if self.analyzer.is_print_statement(line.code):
                deps = self.analyzer.extract_dependencies(line.code)
                if any(self.analyzer.is_related_var(dep, fv) for dep in deps for fv in focused_vars):
                    keep_lines.add(line.lineno)
                    print(f"第{line.lineno}行(print): {line.code.strip()}")
                continue
            
            lvalues = self.analyzer.extract_lvalue(line.code)
            
            if any(self.analyzer.is_related_var(lv, fv) for lv in lvalues for fv in focused_vars):
                keep_lines.add(line.lineno)
                
                print(f"第{line.lineno}行(赋值): {line.code.strip()}")
                print(f"  定义了关注变量: {set(lvalues)}")
                
                deps = self.analyzer.extract_dependencies(line.code)
                new_deps = deps - focused_vars
                
                if new_deps:
                    print(f"  新增依赖: {new_deps}")
                    focused_vars.update(new_deps)
                    for dep in new_deps:
                        var_enter_line[dep] = line.lineno
        
        print(f"\n最终关注变量集合: {focused_vars}")
        print(f"保留的行号: {sorted(keep_lines)}\n")
        
        # 第二遍：基于当前行的属性访问来格式化
        kept_lines = [line for line in self.lines if line.lineno in keep_lines]
        
        print("===== 基于当前行属性访问的精简 =====")
        
        pruned_lines = []
        
        for i, line in enumerate(kept_lines):
            # 分析当前行代码中的属性访问
            current_attr_usage = {}
            if self.source_file:
                # 只分析当前这一行
                current_attr_usage = analyze_lines_for_attribute_usage(
                    self.source_file, 
                    line.lineno,
                    line.lineno  # 起止行都是当前行
                )
            
            # 收集后续使用的变量（用于决定是否保留变量）
            future_uses = set()
            for j in range(i + 1, len(kept_lines)):
                future_line = kept_lines[j]
                uses = self.analyzer.extract_dependencies(future_line.code)
                future_uses.update(uses & focused_vars)
            
            current_defines = set(self.analyzer.extract_lvalue(line.code))
            current_uses = self.analyzer.extract_dependencies(line.code)
            
            vars_to_keep = (current_uses & focused_vars) | \
                          (current_defines & focused_vars) | \
                          (future_uses & focused_vars)
            
            print(f"第{line.lineno}行: {line.code.strip()}")
            print(f"  当前行属性访问: {current_attr_usage}")
            
            # 过滤和格式化变量
            filtered_names = []
            filtered_values = []
            
            for name, value_struct in zip(line.var_names, line.var_values):
                root_var = self.analyzer.get_root_var(name)
                
                if any(self.analyzer.is_related_var(name, vk) for vk in vars_to_keep):
                    # 获取该变量在当前行被访问的属性
                    if root_var in current_attr_usage:
                        paths = current_attr_usage[root_var]
                        required = set()
                        for path in paths:
                            parts = path.split('.')
                            if parts[0] == root_var and len(parts) > 1:
                                # 提取所有级别的属性路径
                                # 例如 student.address.city -> 需要 address, address.city
                                for j in range(1, len(parts)):
                                    attr_path = '.'.join(parts[1:j+1])
                                    required.add(parts[1])  # 只记录第一级属性
                        
                        print(f"    {name}: 当前行访问属性 {required}")
                        formatted = ValueFormatter.format(
                            value_struct, 
                            root_var,
                            required if required else None
                        )
                    else:
                        # 当前行没有访问这个变量的属性
                        # 如果是刚定义的变量，显示完整；否则显示省略
                        if root_var in current_defines:
                            formatted = ValueFormatter.format(value_struct, root_var, None)
                        else:
                            # 未访问属性，显示省略形式
                            if isinstance(value_struct, dict) and value_struct.get('_type') == 'object':
                                class_name = value_struct.get('_class', 'object')
                                formatted = f"{class_name}(...)"
                            else:
                                formatted = ValueFormatter.format(value_struct, root_var, None)
                    
                    filtered_names.append(name)
                    filtered_values.append(formatted)
            
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
    def prune_trace(trace_file, target_line, target_var, output_file, source_file=None):
        """静态方法：执行剪枝"""
        pruner = TracePruner(trace_file, source_file)
        pruner.load_trace()
        pruned_lines, focused_vars = pruner.prune(target_line, target_var)
        pruner.save_pruned(pruned_lines, target_line, target_var, output_file)
        return output_file, pruned_lines