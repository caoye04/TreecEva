# 代码训练集COT生成框架

[toc]

## 背景

正构建一系列Python代码训练集,用于提升大模型的代码推理能力。每个数据样本包含以下四个部分:

- **代码**: 完整的Python代码片段
- **提问**: 询问某一行执行后某个变量的值
- **答案**: 该变量的正确值
- **COT (Chain of Thought)**: 推理过程的详细思维链

本框架专注于自动化生成高质量的COT推理链,帮助模型理解代码执行的因果关系和逻辑流程。

## 生成流程

---

### 步骤1: 代码执行追踪

**输入**: Python代码文件名(如 `test.py`)

**处理**: 使用 `auto_trace` 工具对代码进行插桩和执行追踪

**输出**: `trace_原文件名.txt`,格式为:

```json
{行号} {代码内容}
{行号} [{变量名列表}] [{变量值列表}]
```

每行代码执行后都会记录当前所有变量的状态,包括循环展开后的每次迭代。

---

### 步骤2: 智能回溯与剪枝

**核心算法**: 从目标行号开始向上回溯,构建依赖图并剪除无关代码

**核心原则**: 每一行的变量列表必须包含**下一行计算所需的所有变量**,确保推理链的连续性和可计算性。

**剪枝规则**:

1. **依赖追踪与传播**:
   - 维护一个"关注变量集合",初始只包含目标变量
   - 遇到赋值语句 `a = b + c`,如果 `a` 在关注集合中,则将 `b` 和 `c` 加入集合
   - **关键**: 变量一旦进入关注集合,就要在所有后续行中保留其值,直到该变量被重新赋值或最终不再需要
   - 不在关注集合中的赋值语句直接删除

2. **控制流保留**:
   - 所有 `if`、`elif`、`else`、`for`、`while` 等控制流语句必须保留
   - 保留 `break`、`continue`、`return` 等流程控制语句
   - 保留函数定义和类定义(如果目标变量涉及)

3. **变量列表精简**:
   - 每行的变量列表只保留"当前关注变量集合"中的变量及其值
   - 保持变量名和值的对应关系
   - 确保下一行所需的所有变量都在当前行的变量列表中

4. **特殊情况处理**:
   - 函数调用: 如 `result = func(a, b)`,需追踪 `func` 和参数 `a, b`
   - 对象属性: 如 `obj.attr = value`,需追踪 `obj` 和 `value`
   - 列表/字典操作: 如 `lst[i] = x`,需追踪 `lst`、`i` 和 `x`
   - 多重赋值: 如 `a, b = 1, 2`,正确拆分依赖关系
   - 增强赋值: 如 `a += b`,等价于 `a = a + b`
   - 切片操作: 如 `lst[1:3]`,需追踪 `lst`
   - 推导式: 如 `[x*2 for x in lst]`,需追踪 `lst`

5. **边缘信息精简规则**

   **问题**：原框架记录完整对象结构，导致 token 浪费且可能丢失关键信息

   **技术方案**：延迟格式化 + 基于当前行需求的精简显示

   **效果对比**：

   原先：Student(name='Alice', age=18, score=Score(math=95, english=88)) 全量显示

   现在：Student(score=Score(math=95)) 仅显示被访问的 score.math

**输出**: `trimed_trace_原文件名.txt`,格式为:

```asciidoc
{目标行号}
{目标变量名}
---
{精简后的追踪记录}
```

---

### 步骤3: 模板化COT生成

**输入**: `trimed_trace_原文件名.txt`

**处理**: 基于代码AST类型和变量值,使用预定义模板生成COT注释

**核心方法**: 模板匹配与参数填充(无需AI调用)

---

## 完整示例流程

### 原始代码 [test.py]

```python
a = 1
b = 2
c = a + b
d = 1
for i in range(2):
    d = d + 1
d = d + a
```

### 步骤1输出: [trace_test.txt]

```basic
1 a = 1
1 ['a'] [{'_type': 'int', '_value': 1}]
2 b = 2
2 ['a', 'b'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}]
3 c = a + b
3 ['a', 'b', 'c'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}]
4 d = 1
4 ['a', 'b', 'c', 'd'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 1}]
5 for i in range(2):
5 ['a', 'b', 'c', 'd', 'i'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 0}]
6     d = d + 1
6 ['a', 'b', 'c', 'd', 'i'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 0}]
5 for i in range(2):
5 ['a', 'b', 'c', 'd', 'i'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 1}]
6     d = d + 1
6 ['a', 'b', 'c', 'd', 'i'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 1}]
5 for i in range(2):
5 ['a', 'b', 'c', 'd', 'i'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 1}]
7 d = d + a
7 ['a', 'b', 'c', 'd', 'i'] [{'_type': 'int', '_value': 1}, {'_type': 'int', '_value': 2}, {'_type': 'int', '_value': 3}, {'_type': 'int', '_value': 4}, {'_type': 'int', '_value': 1}]
```

### 步骤2输出: [trimed_trace_test.txt]

```basic
7
d
---
1 a = 1
1 ['a'] ['1']
4 d = 1
4 ['a', 'd'] ['1', '1']
5 for i in range(2):
5 ['a', 'd', 'i'] ['1', '1', '0']
6 d = d + 1
6 ['a', 'd', 'i'] ['1', '2', '0']
5 for i in range(2):
5 ['a', 'd', 'i'] ['1', '2', '1']
6 d = d + 1
6 ['a', 'd', 'i'] ['1', '3', '1']
5 for i in range(2):
5 ['a', 'd', 'i'] ['1', '3', '1']
7 d = d + a
7 ['a', 'd'] ['1', '4']

```

### 步骤4输出: [final_cot_test.txt]

```apache
Target: Find the value of variable d after [line 7] executes

[line 1]  a = 1
[explain] Assign: a = 1
[line 4]  d = 1
[explain] Assign: d = 1
[line 5]  for i in range(2):
[explain] Loop Start: i takes its first value 0
[line 6]  d = d + 1
[explain] Update: d changed from 1 (from [line 4]) to 1+1 = 2
[line 5]  for i in range(2):
[explain] Loop Iteration: i is now 1 (iteration 2)
[line 6]  d = d + 1
[explain] Update: d changed from 2 (from [line 6]) to 2+1 = 3
[line 5]  for i in range(2):
[explain] Loop End: Iteration finished
[line 7]  d = d + a
[explain] Compute: d + a, where d=3(from [line 6]), a=1(from [line 1]) = 4

Answer: d = 4 (last updated on [line 7])
```

## 目前代码框架

### 项目结构

```
项目目录/ 
├── attribute_analyzer.py      # 边缘信息精简规则实现
├── config.py           	   # 配置和模板
├── tracer.py          		   # 代码追踪
├── pruner.py                  # 依赖分析和剪枝
├── cot_generator.py           # COT生成
├── main.py                    # 主流程
├── test.py                    # 测试代码
└── data_test/                 # 测试代码对应数据目录（自动创建）
    ├── trace_test.txt         # 完整追踪
    ├── trimmed_trace_test.txt # 剪枝后的追踪
    └── final_cot_test.txt     # 最终COT
```

### 运行流程

```
准备一个python文件，假设为test_10.py
确定要预测的行号n和目标变量target_variable
在命令行中输入 python main.py test_10.py n target_variable即可
```

> 值得一提的是，如果目标行是循环中的行，我们默认是从最后一次迭代往回走，保留所有迭代记录。

### 代码细节

#### attribute_analyzer.py

```py
"""
属性访问分析器
用于识别代码中的属性访问模式，并指导对象的精简显示
"""

import ast
from typing import Set, Dict, List


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
        print(f"[属性分析警告] 分析行{start_line}-{end_line}时出错: {e}")
    
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
```

#### config.py

```py
"""
配置文件和COT模板定义 - 增强版行内注释 (中英双语)
"""

# -----------------------------------------------------------------
# 英文COT模板 (EN)
# -----------------------------------------------------------------

HEADER_TEMPLATES_EN = "Target: Find the value of variable {target_var} after [line {target_line}] executes\n"
FOOTER_TEMPLATES_EN = "\nAnswer: {target_var} = {final_value} (last updated on {source_info})"
VAR_SOURCE_TEMPLATES_EN = "[line {def_line}]"
VAR_SOURCE_UNKNOWN_EN = "an unknown source"

INLINE_COT_TEMPLATES_EN = {
    'assign_constant': {
        'template': "  # Assign: {var} = {value}",
    },
    'assign_expr': {
        'template': "  # Compute: {expr_detail} = {result}",
    },
    'aug_assign': {
        'template': "  # Update: {var} changed from {old_val} (from {def_line}) to {old_val}{op}{operand} = {result}",
    },
    'for_start': {
        'template': "  # Loop Start: {iter_var} takes its first value {iter_val}",
    },
    'for_continue': {
        'template': "  # Loop Iteration: {iter_var} is now {iter_val} (iteration {iter_count})",
    },
    'for_end': {
        'template': "  # Loop End: Iteration finished",
    },
    'while_start': {
        'template': "  # while Loop Start: Condition is true",
    },
    'while_continue': {
        'template': "  # while Loop Iteration: Condition is still true",
    },
    'while_end': {
        'template': "  # while Loop End: Condition is false",
    },
    'if_true': {
        'template': "  # Condition: True, entering 'if' block",
    },
    'if_false': {
        'template': "  # Condition: False, skipping 'if' block",
    },
    'else': {
        'template': "  # Entering 'else' block",
    },
    'elif_true': {
        'template': "  # 'elif' Condition: True, entering block",
    },
    'elif_false': {
        'template': "  # 'elif' Condition: False, checking next",
    },
    'return': {
        'template': "  # Return: {value}",
    },
    'function_def': {
        'template': "  # Define function: {func_name}",
    },
    'print_statement': {
        'template': "  # Output: {print_content}",
    },
}

# -----------------------------------------------------------------
# 中文COT模板 (ZH)
# -----------------------------------------------------------------

HEADER_TEMPLATES_ZH = "目标: 求[第{target_line}行]执行后变量 {target_var} 的值\n"
FOOTER_TEMPLATES_ZH = "\n答案: {target_var} = {final_value} (最后在{source_info}更新)"
VAR_SOURCE_TEMPLATES_ZH = "[第{def_line}行]"
VAR_SOURCE_UNKNOWN_ZH = "未知来源"

INLINE_COT_TEMPLATES_ZH = {
    'assign_constant': {
        'template': "  # 赋值: {var} = {value}",
    },
    'assign_expr': {
        'template': "  # 计算: {expr_detail} = {result}",
    },
    'aug_assign': {
        'template': "  # 更新: {var} 从{def_line}的 {old_val} 变为 {old_val}{op}{operand} = {result}",
    },
    'for_start': {
        'template': "  # 开始循环: {iter_var} 取第一个值 {iter_val}",
    },
    'for_continue': {
        'template': "  # 继续循环: {iter_var} 取下一个值 {iter_val} (第{iter_count}次)",
    },
    'for_end': {
        'template': "  # 循环结束: 已遍历完所有元素",
    },
    'while_start': {
        'template': "  # while循环开始: 条件为真",
    },
    'while_continue': {
        'template': "  # while循环继续: 条件仍为真",
    },
    'while_end': {
        'template': "  # while循环结束: 条件为假",
    },
    'if_true': {
        'template': "  # 条件判断: 为真，进入if分支",
    },
    'if_false': {
        'template': "  # 条件判断: 为假，跳过if分支",
    },
    'else': {
        'template': "  # 进入else分支",
    },
    'elif_true': {
        'template': "  # elif条件: 为真，进入该分支",
    },
    'elif_false': {
        'template': "  # elif条件: 为假，继续检查",
    },
    'return': {
        'template': "  # 返回: {value}",
    },
    'function_def': {
        'template': "  # 定义函数: {func_name}",
    },
    'print_statement': {
        'template': "  # 输出: {print_content}",
    },
}

# -----------------------------------------------------------------
# 模板选择器
# -----------------------------------------------------------------

TEMPLATES = {
    'en': {
        'header': HEADER_TEMPLATES_EN,
        'footer': FOOTER_TEMPLATES_EN,
        'var_source': VAR_SOURCE_TEMPLATES_EN,
        'var_unknown': VAR_SOURCE_UNKNOWN_EN,
        'inline': INLINE_COT_TEMPLATES_EN,
    },
    'zh': {
        'header': HEADER_TEMPLATES_ZH,
        'footer': FOOTER_TEMPLATES_ZH,
        'var_source': VAR_SOURCE_TEMPLATES_ZH,
        'var_unknown': VAR_SOURCE_UNKNOWN_ZH,
        'inline': INLINE_COT_TEMPLATES_ZH,
    }
}
```

#### cot_generator.py

```py
"""
基于行内注释的COT生成器 - 最终修复版
- 支持中英双语
- 支持长循环总结
- 支持 [line n] + [explain] 双行格式
"""

import ast
import re
from config import TEMPLATES


class CodeClassifier:
    """代码行分类器"""
    
    def __init__(self):
        self.loop_counters = {}
        self.loop_body_lines = {}  # 记录每个循环的循环体行号集合
    
    def classify(self, line, prev_line=None, next_line=None):
        """分类代码行"""
        code = line.code.strip()
        lineno = line.lineno
        
        if code.startswith('print('):
            return 'print_statement'
        
        # For循环处理 - 修复版
        if code.startswith('for '):
            if lineno not in self.loop_counters:
                # 第一次遇到
                self.loop_counters[lineno] = 1
                self.loop_body_lines[lineno] = set()
                # 记录下一行作为循环体的一部分
                if next_line and next_line.lineno > lineno:
                    self.loop_body_lines[lineno].add(next_line.lineno)
                return 'for_start'
            else:
                # 再次遇到
                self.loop_counters[lineno] += 1
                
                if next_line:
                    next_lineno = next_line.lineno
                    # 判断下一行是否是循环体的一部分
                    if next_lineno in self.loop_body_lines.get(lineno, set()):
                        # 下一行在循环体中，继续循环
                        return 'for_continue'
                    else:
                        # 下一行不在循环体中，循环结束
                        return 'for_end'
                else:
                    return 'for_end'
        
        # 如果当前行的前一行是for循环，记录当前行为循环体
        if prev_line and prev_line.code.strip().startswith('for '):
            prev_lineno = prev_line.lineno
            if prev_lineno in self.loop_body_lines and lineno > prev_lineno:
                self.loop_body_lines[prev_lineno].add(lineno)
        
        if code.startswith('while '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                return 'while_start'
            else:
                self.loop_counters[lineno] += 1
                if next_line and next_line.lineno > lineno:
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
        
        # 赋值语句
        if '=' in code and not code.startswith('='):
            # 先检查真正的增强赋值 +=, -=, *=, /=
            if re.search(r'\w+\s*\+=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*-=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*\*=\s*', code):
                return 'aug_assign'
            if re.search(r'\w+\s*/=\s*', code):
                return 'aug_assign'
            
            # 对于 d = d + 1 这种形式，只有当操作数是数字字面量时才视为增强赋值
            # d = d + a 应该被识别为普通表达式赋值
            match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(\d+(?:\.\d+)?)\s*$', code)
            if match:
                # 只有 d = d + 1 这种形式（操作数是数字）视为增强赋值
                return 'aug_assign'
            
            # 普通赋值
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
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


class VariableTracker:
    """变量来源追踪器 (支持多语言)"""
    
    def __init__(self, lang='en'):
        self.var_definitions = {}
        self.var_history = {}
        self.lang = lang
        self.templates = TEMPLATES[lang]
    
    def update_var(self, var_name, lineno, value):
        """更新变量定义"""
        self.var_definitions[var_name] = lineno
        if var_name not in self.var_history:
            self.var_history[var_name] = []
        self.var_history[var_name].append((lineno, value))
    
    def get_def_line(self, var_name):
        """获取变量最后定义的行号"""
        return self.var_definitions.get(var_name)
    
    def get_var_source_info(self, var_name):
        """获取变量来源信息"""
        def_line = self.var_definitions.get(var_name)
        if def_line:
            # 格式化: "[line n]" 或 "[第n行]"
            # **注意**: 这里的格式是用于 *注释内部* 的, 不是行首的
            return self.templates['var_source'].format(def_line=def_line)
        return self.templates['var_unknown']


class ParameterExtractor:
    """参数提取器 (支持多语言)"""
    
    def __init__(self, var_tracker, lang='en'):
        self.var_tracker = var_tracker
        self.lang = lang
    
    def extract(self, line, line_type, classifier, prev_var_dict=None):
        """提取模板参数"""
        params = {
            'line': line.lineno,
            'code': line.code.strip(),
        }
        
        var_dict = line.get_var_dict()
        
        # Print语句
        if line_type == 'print_statement':
            match = re.search(r'print\((.*)\)', line.code)
            if match:
                print_arg = match.group(1).strip()
                if print_arg in var_dict:
                    source = self.var_tracker.get_var_source_info(print_arg)
                    params['print_content'] = f"{print_arg}={var_dict[print_arg]} (from {source})"
                else:
                    params['print_content'] = print_arg
        
        # 提取变量名
        if line_type in ['assign_constant', 'assign_expr', 'aug_assign']:
            lvalues = self._extract_lvalue(line.code)
            if lvalues:
                params['var'] = lvalues[0]
                params['value'] = var_dict.get(lvalues[0], '?')
                params['result'] = params['value']
        
        # 表达式展开 - 对于普通赋值
        if line_type == 'assign_expr':
            params['expr_detail'] = self._expand_expression_with_source(
                line.code, var_dict, prev_var_dict
            )
            # 如果左值的值是 '?'，尝试从右边表达式推导
            if 'var' in params and params['value'] == '?':
                parts = line.code.split('=', 1)
                if len(parts) == 2:
                    expr = parts[1].strip()
                    # 如果右边是单个变量名（如 result = sum_val）
                    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', expr):
                        # 从当前行或上一行的变量字典获取值
                        if expr in var_dict:
                            params['value'] = var_dict[expr]
                            params['result'] = params['value']
                        elif prev_var_dict and expr in prev_var_dict:
                            params['value'] = prev_var_dict[expr]
                            params['result'] = params['value']
            # 更新变量追踪
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 常量赋值
        if line_type == 'assign_constant':
            if 'var' in params:
                self.var_tracker.update_var(params['var'], line.lineno, params['value'])
        
        # 增强赋值
        if line_type == 'aug_assign':
            var = params.get('var')
            
            # 检查具体形式
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
                # d = d + 1 形式（操作数是数字）
                match = re.match(r'^\s*(\w+)\s*=\s*\1\s*([+\-*/])\s*(.+)$', line.code)
                if match:
                    params['op'] = match.group(2)
                    operand_expr = match.group(3).strip()
                else:
                    params['op'] = '?'
                    operand_expr = '?'
            
            params['operand'] = operand_expr
            
            # 获取旧值和定义行
            if var and prev_var_dict:
                params['old_val'] = prev_var_dict.get(var, '?')
                # 格式化: "[line n]" 或 "[第n行]"
                def_line_num = self.var_tracker.get_def_line(var)
                params['def_line'] = self.var_tracker.get_var_source_info(var) if def_line_num else '?'
                
                # 兼容中文模板，它只需要行号
                if self.lang == 'zh':
                     params['def_line'] = self.var_tracker.get_var_source_info(var)

            else:
                params['old_val'] = '?'
                params['def_line'] = '?'
            
            # 更新变量追踪
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

                # **新增：更新变量追踪 - 记录循环变量的定义**
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
                params['value'] = f"{return_val}={var_dict[return_val]} (from {source})"
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
        
        # Fallback
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
        
        # 提取左值
        lvalues = self._extract_lvalue(code)
        lvalue_set = set(lvalues)
        
        # 查找表达式中的所有变量
        var_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        variables = re.findall(var_pattern, expr)
        
        # 构建详细说明
        var_details = []
        unique_vars = set() # 确保每个变量只解释一次
        
        for var in variables:
            # 检查是否是Python关键字或内置函数
            if var in ['range', 'len', 'sum', 'max', 'min', 'int', 'str', 'list', 'dict', 'True', 'False', 'None'] or var in unique_vars:
                continue
            unique_vars.add(var)
            
            # 如果变量是左值（在赋值语句左边，如 d = d + 1），使用 prev_var_dict（修改前的值）
            # 如果变量是右值（只在表达式中读取），使用当前行的 var_dict（已经过属性精简）
            if var in lvalue_set:
                # 左值：使用前一次的值（修改前的值）
                if prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(from {source})")
            else:
                # 右值：优先使用当前行的精简值（已根据当前行属性访问精简）
                if var in var_dict:
                    val = var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(from {source})")
                elif prev_var_dict and var in prev_var_dict:
                    val = prev_var_dict[var]
                    source = self.var_tracker.get_var_source_info(var)
                    var_details.append(f"{var}={val}(from {source})")
        
        if var_details:
            detail_str = f", where {', '.join(var_details)}" if self.lang == 'en' else f", 其中 {', '.join(var_details)}"
            return f"{expr}{detail_str}"
        else:
            return expr


class COTGenerator:
    """行内注释式COT生成器"""
    
    def __init__(self, pruned_file, lang='en'):
        self.pruned_file = pruned_file
        self.lang = lang
        self.templates = TEMPLATES[lang]
        self.target_line = None
        self.target_var = None
        self.lines = []
        self.var_tracker = VariableTracker(lang=self.lang)
    
    def load_pruned_trace(self):
        """加载剪枝后的追踪文件"""
        with open(self.pruned_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        self.target_line = int(content[0].strip())
        self.target_var = content[1].strip()
        
        from pruner import TraceLine
        i = 3
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
                values = eval(values_str)
                return names, values
        except:
            pass
        return [], []
    
    def generate(self):
        """生成行内注释式COT（支持长循环总结）"""
        
        # --- 步骤 1: 预计算循环总数 (Dry Run) ---
        total_counts = {}
        dry_classifier = CodeClassifier()
        prev_line = None
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            dry_classifier.classify(line, prev_line, next_line)
            prev_line = line
        total_counts = dry_classifier.loop_counters

        # --- 步骤 2: 实际生成 ---
        classifier = CodeClassifier() # 使用新的分类器进行实际生成
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
        loop_skip_state = {} # 存储循环头的行号: True (正在跳过) / False (正在打印)

        LOOP_SUMMARY_THRESHOLD = 5 # 迭代次数 > 5 才触发总结
        SKIP_AFTER_ITER = 2      # 显示前 2 次
        RESUME_BEFORE_ITER = 2     # 显示后 2 次
        
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            
            # 分类
            line_type = classifier.classify(line, prev_line_obj, next_line)
            
            # --- 循环总结逻辑 ---
            if line_type in ('for_start', 'while_start'):
                current_loop_header = line.lineno
                loop_skip_state[current_loop_header] = False # 默认开始打印
            
            if current_loop_header:
                total_iter = total_counts.get(current_loop_header, 0)
                current_iter = classifier.loop_counters.get(current_loop_header, 0)
                
                # 计算开始跳过和恢复打印的迭代次数
                START_SKIP_ITER = SKIP_AFTER_ITER + 1
                RESUME_ITER = total_iter - RESUME_BEFORE_ITER + 1

                is_summarizable = total_iter > LOOP_SUMMARY_THRESHOLD
                
                if is_summarizable:
                    if current_iter == START_SKIP_ITER:
                        # 这是第3次迭代，打印总结行并开始跳过
                        num_skipped = total_iter - SKIP_AFTER_ITER - RESUME_BEFORE_ITER
                        summary_template = {
                            'en': f"\n... [Line {current_loop_header}] repeats {num_skipped} more times ...\n",
                            'zh': f"\n... [第{current_loop_header}行] 额外循环了 {num_skipped} 次 ...\n"
                        }
                        output_lines.append(summary_template[self.lang].strip()) 
                    
                    elif current_iter == RESUME_ITER:
                        # 这是倒数第2次迭代，停止跳过
                        loop_skip_state[current_loop_header] = False
                        
                # 检查是否应跳过当前行
                if loop_skip_state.get(current_loop_header, False):
                    # 必须更新状态，即使不打印
                    prev_var_dict = line.get_var_dict()
                    prev_line_obj = line
                    if line_type in ('for_end', 'while_end'):
                        current_loop_header = None # 退出循环
                    continue # 跳过本行
            # --- 结束循环总结逻辑 ---

            if line_type == 'unknown':
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            
            # 提取参数
            params = extractor.extract(line, line_type, classifier, prev_var_dict)
            
            # 获取模板
            template_info = inline_templates.get(line_type)
            if not template_info:
                prev_var_dict = line.get_var_dict()
                prev_line_obj = line
                continue
            

            # -------------------------------------------------
            # 目标格式:
            # [line 1]  a = 1
            # [explain] Assign: a = 1
            # -------------------------------------------------
            
            # 1. 获取注释文本 (不带 '#')
            comment_text = ""
            try:
                # 模板格式为: "  # Assign: {var} = {value}"
                comment_with_prefix = template_info['template'].format(**params)
                # 移除前导空格、'#'号和之后的空格
                comment_text = comment_with_prefix.lstrip().lstrip('#').lstrip()
            except KeyError as e:
                comment_text = f"(Missing param: {e})"

            # 2. 格式化代码行和解释行
            if self.lang == 'zh':
                # 中文版
                code_line = f"[第{line.lineno}行]  {line.code}"
                explain_line = f"[解释] {comment_text}"
            else:
                # 英文版
                code_line = f"[line {line.lineno}]  {line.code}"
                explain_line = f"[explain] {comment_text}"
            
            # 3. 添加两行到输出 (并确保解释非空)
            output_lines.append(code_line)
            if comment_text:
                output_lines.append(explain_line)
            # -------------------------------------------------
            
            # 更新prev_var_dict和prev_line_obj
            prev_var_dict = line.get_var_dict()
            prev_line_obj = line
            
            if line_type in ('for_end', 'while_end'):
                current_loop_header = None # 退出循环
        
        # 最终答案
        final_value = self.lines[-1].get_var_dict().get(self.target_var, '?')
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
```

#### main.py

```py
"""
COT生成框架主流程
"""

import os
import argparse
from tracer import PythonTracer
from pruner import TracePruner
from cot_generator import COTGenerator
# from reverse_cot_generator import ReverseCOTGenerator # 注释掉了


class COTFramework:
    """COT生成框架主类"""
    
    def __init__(self, source_file, target_line, target_var, generate_zh=False):
        self.source_file = source_file
        self.target_line = target_line
        self.target_var = target_var
        self.generate_zh = generate_zh # 新增
        
        # 生成文件名和目录
        base_name = os.path.splitext(os.path.basename(source_file))[0]
        self.data_dir = f"data_{base_name}"
        
        # 创建数据目录
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 生成文件路径（存放在data目录中）
        self.trace_file = os.path.join(self.data_dir, f"trace_{base_name}.txt")
        self.pruned_file = os.path.join(self.data_dir, f"trimmed_trace_{base_name}.txt")
        # 默认英文COT文件
        self.cot_file = os.path.join(self.data_dir, f"final_cot_{base_name}.txt") 
        # 新增：中文COT文件路径
        self.cot_file_zh = os.path.join(self.data_dir, f"final_zh_cot_{base_name}.txt")
        # self.reverse_cot_file = os.path.join(self.data_dir, f"reverse_cot_{base_name}.txt")
    
    def run(self):
        """执行完整流程"""
        print("=" * 60)
        print("COT Generation Framework")
        print("=" * 60)
        
        # 步骤1: 代码执行追踪
        print("\n[Step 1/4] Code Execution Tracing...")
        print(f"  Source File: {self.source_file}")
        print(f"  Data Directory: {self.data_dir}/")
        PythonTracer.trace_file(self.source_file, self.trace_file)
        print(f"  ✓ Trace complete, output: {self.trace_file}")
        
        # 步骤2: 目标定位
        print("\n[Step 2/4] Target Localization...")
        print(f"  Target Line: {self.target_line}")
        print(f"  Target Variable: {self.target_var}")
        print(f"  ✓ Target locked")
        
        # 步骤3: 智能回溯与剪枝
        print("\n[Step 3/4] Smart Backtracking & Pruning...")
        TracePruner.prune_trace(
            self.trace_file, 
            self.target_line, 
            self.target_var, 
            self.pruned_file,
            source_file=self.source_file
        )
        print(f"  ✓ Pruning complete, output: {self.pruned_file}")
        
        # 步骤4: 模板化COT生成 (English - 默认)
        print("\n[Step 4/4] Generating COT (English)...")
        COTGenerator.generate_cot(self.pruned_file, self.cot_file, lang='en')
        print(f"  ✓ English COT generated: {self.cot_file}")
        
        # [新增] 步骤5: 模板化COT生成 (Chinese - 可选)
        if self.generate_zh:
            print("\n[Bonus Step] Generating COT (Chinese)...")
            COTGenerator.generate_cot(self.pruned_file, self.cot_file_zh, lang='zh')
            print(f"  ✓ Chinese COT generated: {self.cot_file_zh}")
        
        # 显示结果
        print("\n" + "=" * 60)
        print("Generation Complete!")
        print("=" * 60)
        print(f"\nData Directory: {self.data_dir}/")
        print(f"  ├── {os.path.basename(self.trace_file)}")
        print(f"  ├── {os.path.basename(self.pruned_file)}")
        print(f"  ├── {os.path.basename(self.cot_file)} (English)")
        if self.generate_zh:
            print(f"  └── {os.path.basename(self.cot_file_zh)} (Chinese)")
        
        # 显示英文COT内容
        print("\n" + "-" * 60)
        print("English COT Preview:")
        print("-" * 60)
        with open(self.cot_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        
        # 显示中文COT内容
        if self.generate_zh:
            print("\n" + "-" * 60)
            print("Chinese COT Preview:")
            print("-" * 60)
            with open(self.cot_file_zh, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)
        
        return self.cot_file


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='COT Generation Framework')
    parser.add_argument('source_file', help='Python source code file')
    parser.add_argument('target_line', type=int, help='Target line number')
    parser.add_argument('target_var', help='Target variable name')
    # 新增 --zh 参数
    parser.add_argument('--zh', action='store_true', help='Generate an additional Chinese (zh) COT file')
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.source_file):
        print(f"Error: File '{args.source_file}' not found.")
        return
    
    # 运行框架
    framework = COTFramework(
        args.source_file, 
        args.target_line, 
        args.target_var, 
        generate_zh=args.zh  # 传递参数
    )
    framework.run()


if __name__ == '__main__':
    # 示例用法（无参数时）
    import sys
    if len(sys.argv) == 1:
        print("Example Usage:")
        print("  python main.py test.py 7 d")
        print("  python main.py test.py 7 d --zh  (To generate Chinese version too)")
        print("\nRunning example...")
        
        # 创建示例文件
        with open('test.py', 'w', encoding='utf-8') as f:
            f.write("""a = 1
b = 2
c = a + b
d = 1
for i in range(2):
    d = d + 1
d = d + a
""")
        
        # 运行不带 --zh 的示例
        print("\n--- Running EN-only example ---")
        framework_en = COTFramework('test.py', 7, 'd', generate_zh=False)
        framework_en.run()
        
        # 运行带 --zh 的示例
        print("\n--- Running EN + ZH example ---")
        framework_zh = COTFramework('test.py', 7, 'd', generate_zh=True)
        framework_zh.run()
    else:
        main()
```

#### pruner.py

```py
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
```

#### tracer.py

```py
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
```

