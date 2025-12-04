"""
属性访问分析器
用于识别代码中的属性访问模式，并指导对象的精简显示
"""

import ast
from typing import Set, Dict, List
import textwrap


class AttributePathCollector(ast.NodeVisitor):
    """收集代码中所有的属性访问路径"""
    
    def __init__(self):
        self.paths = set()  # 完整的属性路径，如 'student.score.math'
    
    def visit_Attribute(self, node):
        path = self._build_path(node)
        if path:
            self.paths.add(path)
            # 同时添加所有父路径
            parts = path.split('.')
            for i in range(1, len(parts)):
                parent_path = '.'.join(parts[:i])
                self.paths.add(parent_path)
        self.generic_visit(node)
    
    def _build_path(self, node):
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


def analyze_file_for_attribute_usage(filename):
    """分析整个文件，返回每个变量的属性使用映射
    
    Returns:
        {变量名: {使用的属性路径集合}}
        例如: {'student': {'student.score', 'student.score.math'}}
    """
    var_attr_map = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        
        tree = ast.parse(code)
        collector = AttributePathCollector()
        collector.visit(tree)
        
        # 组织成按变量分组的映射
        for path in collector.paths:
            root_var = path.split('.')[0]
            if root_var not in var_attr_map:
                var_attr_map[root_var] = set()
            var_attr_map[root_var].add(path)
        
    except Exception as e:
        print(f"[属性分析警告] 分析文件时出错: {e}")
    
    return var_attr_map


def analyze_lines_for_attribute_usage(filename, start_line, end_line=None):
    """分析指定行范围内的属性使用情况
    
    Args:
        filename: 源文件名
        start_line: 起始行号（包含）
        end_line: 结束行号（包含），None表示到文件末尾
    
    Returns:
        {变量名: {使用的属性路径集合}}
    """
    var_attr_map = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 提取指定范围的代码
        if end_line is None:
            end_line = len(lines)
        
        # 注意：行号从1开始，列表索引从0开始
        relevant_lines = lines[start_line - 1:end_line]
        code_segment = ''.join(relevant_lines)
        
        if not code_segment.strip():
            return var_attr_map
        
        # 去除缩进，使代码可以被解析
        code_segment = textwrap.dedent(code_segment)
        
        # 解析代码段
        tree = ast.parse(code_segment)
        collector = AttributePathCollector()
        collector.visit(tree)
        
        # 组织成按变量分组的映射
        for path in collector.paths:
            root_var = path.split('.')[0]
            if root_var not in var_attr_map:
                var_attr_map[root_var] = set()
            var_attr_map[root_var].add(path)
        
    except Exception as e:
        # 静默失败，不影响主流程
        pass
    
    return var_attr_map


def get_required_attributes_for_var(var_name, attr_paths):
    """提取变量需要显示的属性
    
    Args:
        var_name: 变量名
        attr_paths: 该变量相关的所有属性路径
    
    Returns:
        需要显示的直接属性集合，例如 {'age', 'company'}
    """
    required = set()
    
    for path in attr_paths:
        parts = path.split('.')
        if parts[0] != var_name:
            continue
        
        if len(parts) > 1:
            # 第一级属性
            required.add(parts[1])
    
    return required


class SmartObjectFormatter:
    """智能对象格式化器 - 只显示用到的属性"""
    
    def __init__(self, var_name, used_paths, depth_limit=3):
        """
        Args:
            var_name: 变量名
            used_paths: 该变量的属性使用路径集合
            depth_limit: 深度限制
        """
        self.var_name = var_name
        self.used_paths = used_paths or set()
        self.depth_limit = depth_limit
        
        # 解析出需要显示的属性结构
        self.required_attrs = self._parse_required_attrs()
    
    def _parse_required_attrs(self):
        """解析需要显示的属性结构
        
        Returns:
            {属性名: 子属性字典}
        """
        attrs = {}
        
        for path in self.used_paths:
            parts = path.split('.')
            if parts[0] != self.var_name:
                continue
            
            if len(parts) == 1:
                # 只是变量本身，不是属性访问
                continue
            
            # 构建树结构
            current = attrs
            for part in parts[1:]:
                if part not in current:
                    current[part] = {}
                current = current[part]
        
        return attrs
    
    def format(self, obj, depth=0):
        """格式化对象"""
        if depth > self.depth_limit:
            return "..."
        
        # 基础类型直接返回
        if isinstance(obj, str):
            return f"'{obj}'"
        elif isinstance(obj, (int, float, bool)):
            return str(obj)
        elif obj is None:
            return "None"
        elif isinstance(obj, (list, tuple)):
            return self._format_sequence(obj, depth)
        elif isinstance(obj, dict):
            return self._format_dict(obj, depth)
        elif hasattr(obj, '__dict__'):
            # 自定义对象
            return self._format_custom_object(obj, depth)
        else:
            return str(obj)
    
    def _format_custom_object(self, obj, depth):
        """格式化自定义对象"""
        class_name = type(obj).__name__
        
        if not self.required_attrs:
            # 没有属性被使用，显示简化形式
            return f"{class_name}(...)"
        
        # 只显示需要的属性
        parts = []
        for attr_name in sorted(self.required_attrs.keys()):  # 排序以保证稳定输出
            if hasattr(obj, attr_name):
                attr_value = getattr(obj, attr_name)
                
                # 递归格式化属性值
                sub_required = self.required_attrs[attr_name]
                if sub_required and hasattr(attr_value, '__dict__'):
                    # 子对象也需要精简
                    sub_formatter = SmartObjectFormatter(
                        attr_name, 
                        self._get_sub_paths(attr_name),
                        self.depth_limit
                    )
                    formatted_value = sub_formatter.format(attr_value, depth + 1)
                else:
                    formatted_value = self._basic_format(attr_value, depth + 1)
                
                parts.append(f"{attr_name}={formatted_value}")
        
        if not parts:
            return f"{class_name}(...)"
        
        return f"{class_name}({', '.join(parts)})"
    
    def _get_sub_paths(self, attr_name):
        """获取子属性的路径集合"""
        sub_paths = set()
        prefix = f"{self.var_name}.{attr_name}."
        
        for path in self.used_paths:
            if path.startswith(prefix):
                # 转换为相对路径
                sub_path = attr_name + path[len(self.var_name + '.' + attr_name):]
                sub_paths.add(sub_path)
        
        return sub_paths
    
    def _basic_format(self, value, depth):
        """基础格式化"""
        if depth > self.depth_limit:
            return "..."
        
        if isinstance(value, str):
            return f"'{value}'"
        elif isinstance(value, (int, float, bool)):
            return str(value)
        elif isinstance(value, list):
            if not value or depth >= self.depth_limit - 1:
                return f"[...{len(value)} items]" if value else "[]"
            items = [self._basic_format(v, depth + 1) for v in value[:3]]
            suffix = ", ..." if len(value) > 3 else ""
            return f"[{', '.join(items)}{suffix}]"
        elif isinstance(value, dict):
            if not value or depth >= self.depth_limit - 1:
                return f"{{...{len(value)} items}}" if value else "{}"
            return "{...}"
        elif hasattr(value, '__dict__'):
            return f"{type(value).__name__}(...)"
        else:
            return str(value)
    
    def _format_sequence(self, seq, depth):
        """格式化序列"""
        if not seq:
            return "[]" if isinstance(seq, list) else "()"
        
        if depth >= self.depth_limit - 1:
            bracket = ("[", "]") if isinstance(seq, list) else ("(", ")")
            return f"{bracket[0]}...{len(seq)} items{bracket[1]}"
        
        items = [self._basic_format(item, depth + 1) for item in seq[:5]]
        if len(seq) > 5:
            items.append("...")
        
        if isinstance(seq, list):
            return f"[{', '.join(items)}]"
        else:
            return f"({', '.join(items)})"
    
    def _format_dict(self, d, depth):
        """格式化字典"""
        if not d:
            return "{}"
        
        if depth >= self.depth_limit - 1:
            return f"{{...{len(d)} items}}"
        
        items = []
        for i, (k, v) in enumerate(d.items()):
            if i >= 3:
                items.append("...")
                break
            items.append(f"{self._basic_format(k, depth+1)}: {self._basic_format(v, depth+1)}")
        
        return f"{{{', '.join(items)}}}"