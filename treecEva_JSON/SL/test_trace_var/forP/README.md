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

### 步骤2: 目标定位

**输入**:

- 目标行号(如 `7`)
- 目标变量名(如 `d`)

**说明**: 这一步确定我们需要追踪的最终目标,即"在第X行执行后,变量Y的值是多少?"

---

### 步骤3: 智能回溯与剪枝

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

**输出**: `trimed_trace_原文件名.txt`,格式为:

```asciidoc
{目标行号}
{目标变量名}
---
{精简后的追踪记录}
```

---

### 步骤4: 模板化COT生成

**输入**: `trimed_trace_原文件名.txt`

**处理**: 基于代码AST类型和变量值,使用预定义模板生成COT注释

**核心方法**: 模板匹配与参数填充(无需AI调用)

#### 4.1 代码行分类

通过AST解析或正则匹配,将每一行分类为以下类型之一:

- `assign_constant`: 常量赋值 (如 `a = 1`)
- `assign_expr`: 表达式赋值 (如 `c = a + b`)
- `aug_assign`: 增强赋值 (如 `d += 1`)
- `for_start`: for循环开始
- `for_continue`: for循环继续迭代
- `for_end`: for循环结束检查
- `while_start`: while循环开始
- `if_true`: if条件为真
- `if_false`: if条件为假
- `else`: else分支
- `function_def`: 函数定义
- `return`: 返回语句

#### 4.2 模板定义

每种类型对应固定的COT模板,包含占位符:

**示例模板**:

```python
templates = {
    'assign_constant': 
        "第{line}行: {code}\n→ 将变量{var}赋值为{value}",
    
    'assign_expr': 
        "第{line}行: {code}\n→ 计算右侧表达式: {expr_detail}\n→ 结果: {var} = {result}",
    
    'aug_assign': 
        "第{line}行: {code}\n→ 计算: {var} = {old_val} {op} {operand} = {result}",
    
    'for_start': 
        "第{line}行: {code}\n→ 进入循环,循环变量{iter_var}={iter_val},开始第1次迭代",
    
    'for_continue': 
        "第{line}行: {code}\n→ 继续循环,{iter_var}={iter_val},开始第{iter_count}次迭代",
    
    'for_end': 
        "第{line}行: {code}\n→ 循环结束,已遍历完所有元素",
}
```

#### 4.3 参数提取规则

从追踪数据中提取模板参数:

- `{line}`: 行号(直接读取)
- `{code}`: 代码内容(直接读取)
- `{var}`: 被赋值的变量名(AST解析或正则提取)
- `{value}`: 变量的当前值(从变量列表中查找)
- `{old_val}`: 变量的前一个值(从上一行变量列表中查找)
- `{result}`: 计算结果(从当前行变量列表中查找)
- `{expr_detail}`: 表达式展开(用变量的实际值替换变量名)
- `{iter_var}`: 循环变量名(AST解析)
- `{iter_val}`: 循环变量当前值(从变量列表查找)
- `{iter_count}`: 循环次数计数(通过统计同一行号出现次数)

#### 4.4 特殊处理逻辑

**循环迭代计数**:

- 维护一个字典记录每个循环行的出现次数
- 第一次出现使用`for_start`模板
- 后续出现使用`for_continue`模板,并填充迭代次数
- 最后一次(下一行不是循环体内)使用`for_end`模板

**表达式展开**:

- 对于 `c = a + b`,生成 `a + b = 1 + 2 = 3`
- 从变量列表中查找`a`和`b`的值,进行字符串拼接

**状态汇总**:

- 每个步骤后可选添加"当前状态"行
- 格式: `→ 当前状态: var1={val1}, var2={val2}, ...`
- 只列出关注变量集合中的变量

#### 4.5 输出格式

```apache
目标: 求第{target_line}行执行后变量{target_var}的值

{步骤1标题}
{COT内容行1}
{COT内容行2}
...

{步骤2标题}
{COT内容行1}
...

最终答案: {final_value}
```

**步骤划分规则**:

- 按逻辑结构划分(初始化、循环、最终计算等)
- 或按代码块(每5-10行为一个步骤)
- 步骤标题格式: `步骤{num}: {简要描述}`

**输出**: `final_cot_原文件名.txt`

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
1 ['a'] ['1']
2 b = 2
2 ['a', 'b'] ['1', '2']
3 c = a + b
3 ['a', 'b', 'c'] ['1', '2', '3']
4 d = 1
4 ['a', 'b', 'c', 'd'] ['1', '2', '3', '1']
5 for i in range(2):
5 ['a', 'b', 'c', 'd', 'i'] ['1', '2', '3', '1', '0']
6     d = d + 1
6 ['a', 'b', 'c', 'd', 'i'] ['1', '2', '3', '2', '0']
5 for i in range(2):
5 ['a', 'b', 'c', 'd', 'i'] ['1', '2', '3', '2', '1']
6     d = d + 1
6 ['a', 'b', 'c', 'd', 'i'] ['1', '2', '3', '3', '1']
5 for i in range(2):
5 ['a', 'b', 'c', 'd', 'i'] ['1', '2', '3', '3', '1']
7 d = d + a
7 ['a', 'b', 'c', 'd', 'i'] ['1', '2', '3', '4', '1']
```

### 步骤2输入: 目标定位

```makefile
目标行号: 7
目标变量: d
```

### 步骤3输出: [trimed_trace_test.txt]

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
6     d = d + 1
6 ['a', 'd', 'i'] ['1', '2', '0']
5 for i in range(2):
5 ['a', 'd', 'i'] ['1', '2', '1']
6     d = d + 1
6 ['a', 'd', 'i'] ['1', '3', '1']
5 for i in range(2):
5 ['a', 'd', 'i'] ['1', '3', '1']
7 d = d + a
7 ['d'] ['4']
```

**回溯分析过程**:

- 第7行 `d = d + a`: 目标变量是 `d`,依赖 `d` 和 `a` → 关注集合: `{d, a}`
- 第5-6行循环: 保留所有循环语句,关注集合包含 `{d, a, i}`
- 第4行 `d = 1`: `d` 在关注集合中,保留,关注集合仍包含 `{a}`(因为后续第7行需要)
- 第1行 `a = 1`: `a` 在关注集合中,保留
- 删除第2行和第3行(b和c不在关注集合中)
- **变量传播**: `a` 在第1行被定义后,其值需要一直保留到第7行使用

### 步骤4输出: [final_cot_test.txt]

```apache
目标: 求第7行执行后变量d的值

步骤1: 初始化变量
第1行: a = 1
→ 将变量a赋值为1

第4行: d = 1
→ 将变量d赋值为1
→ 当前状态: a=1, d=1

步骤2: 循环执行
第5行: for i in range(2):
→ 进入循环,循环变量i=0,开始第1次迭代
→ 当前状态: a=1, d=1, i=0

第6行: d = d + 1
→ 计算: d = 1 + 1 = 2
→ 当前状态: a=1, d=2, i=0

第5行: for i in range(2):
→ 继续循环,i=1,开始第2次迭代
→ 当前状态: a=1, d=2, i=1

第6行: d = d + 1
→ 计算: d = 2 + 1 = 3
→ 当前状态: a=1, d=3, i=1

第5行: for i in range(2):
→ 循环结束,已遍历完所有元素
→ 当前状态: a=1, d=3

步骤3: 最终计算
第7行: d = d + a
→ 计算: d = 3 + 1 = 4
→ 当前状态: d=4

最终答案: 4
```

## 技术要点

### 步骤4实现要求

✅ **纯代码实现**: 使用Python的`ast`模块或正则表达式进行模式匹配

✅ **模板驱动**: 所有COT文本都来自预定义模板,不生成自由文本

✅ **参数提取**: 从追踪数据中机械式提取所需参数

✅ **确定性输出**: 相同输入保证相同输出,无随机性

### 需要处理的Python语法特性

✅ 基本赋值和算术运算

✅ 控制流: if/elif/else, for, while

✅ 函数定义与调用

✅ 列表、字典、元组操作

✅ 对象属性访问

✅ 列表推导式

✅ 异常处理: try/except

✅ 生成器和迭代器

✅ 装饰器

✅ 上下文管理器: with语句

✅ 多重赋值和解包

✅ 切片操作

✅ lambda表达式

✅ 嵌套函数和闭包

### 依赖分析算法伪代码

```python
def build_dependency_graph(target_line, target_var, trace):
    关注变量集 = {target_var}
    保留行集 = set()
    变量历史追踪 = {}  # 记录每个变量何时进入关注集合
    
    # 第一遍: 从目标行向上回溯,确定需要保留的行和关注变量
    for 行 in 逆序遍历(trace, from=target_line):
        if 行是控制流语句:
            保留行集.add(行)
            提取控制流中的变量依赖()
        elif 行是赋值语句:
            左值变量 = extract_lvalue(行)
            if 左值变量 in 关注变量集:
                保留行集.add(行)
                右值依赖 = extract_dependencies(行)
                关注变量集.update(右值依赖)
                # 记录新变量的首次出现位置
                for 变量 in 右值依赖:
                    if 变量 not in 变量历史追踪:
                        变量历史追踪[变量] = 行号
    
    # 第二遍: 正向遍历,为每一行构建正确的变量列表
    当前活跃变量集 = set()
    for 行 in 正序遍历(保留行集):
        if 行号 in 变量历史追踪.values():
            # 有新变量在此行被定义,加入活跃集合
            当前活跃变量集.update(在此行定义的变量)
        
        # 此行的变量列表 = 当前活跃变量集
        行.变量列表 = filter_vars(行.原始变量列表, 当前活跃变量集)
        
        # 如果此行重新定义了某个变量,更新活跃集合
        if 行是赋值语句:
            左值 = extract_lvalue(行)
            if 左值 in 当前活跃变量集:
                # 变量被重新赋值,可能需要更新依赖
                pass
    
    return 保留行集, 变量列表映射
```

### COT生成算法伪代码

```python
def generate_cot_from_template(trimmed_trace):
    # 解析输入
    target_line, target_var, trace_lines = parse_trace(trimmed_trace)
    
    # 分类每一行代码
    classified_lines = []
    loop_counters = {}  # 追踪循环迭代次数
    
    for i, line in enumerate(trace_lines):
        line_type = classify_line(line.code)  # AST或正则匹配
        
        # 特殊处理循环
        if line_type.startswith('for'):
            if line.lineno not in loop_counters:
                loop_counters[line.lineno] = 0
                line_type = 'for_start'
            else:
                loop_counters[line.lineno] += 1
                # 判断是否最后一次
                if i+1 < len(trace_lines) and trace_lines[i+1].lineno == line.lineno:
                    line_type = 'for_end'
                else:
                    line_type = 'for_continue'
        
        classified_lines.append((line, line_type))
    
    # 生成COT
    cot_output = [f"目标: 求第{target_line}行执行后变量{target_var}的值\n"]
    
    current_step = 1
    for line, line_type in classified_lines:
        # 获取模板
        template = templates[line_type]
        
        # 提取参数
        params = extract_params(line, line_type, loop_counters)
        
        # 填充模板
        cot_text = template.format(**params)
        
        # 添加到输出
        cot_output.append(cot_text)
        
        # 可选: 添加状态汇总
        if should_add_state(line_type):
            state_text = format_state(line.variables)
            cot_output.append(state_text)
    
    # 添加最终答案
    final_value = get_final_value(trace_lines[-1], target_var)
    cot_output.append(f"\n最终答案: {final_value}")
    
    return '\n'.join(cot_output)
```

### 变量传播的关键逻辑

**问题**: 如何确保每一行都包含下一行所需的变量?

**解决方案**:

1. **双遍历策略**:

   - 第一遍(逆向): 确定哪些行需要保留,哪些变量需要关注
   - 第二遍(正向): 为每一行分配正确的变量列表,确保连续性

2. **变量生命周期管理**:

   - 变量从被加入关注集合的位置开始,一直保留到:
     - 被重新赋值,或
     - 不再被后续任何行使用

3. **示例说明**

   ```less
   第1行: a = 1    → 关注集合: {a}
   第4行: d = 1    → 关注集合: {a, d}  (保留a因为第7行需要)
   第5行: for ...  → 关注集合: {a, d, i}
   第7行: d = d+a  → 前一行必须有a和d
   ```

## 目前代码框架

### 项目结构

```
项目目录/ 
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

#### config.py

```py
"""
配置文件和COT模板定义
"""

# COT生成模板
COT_TEMPLATES = {
    'assign_constant': {
        'template': "第{line}行: {code}\n→ 将变量{var}赋值为{value}",
        'with_state': True
    },
    
    'assign_expr': {
        'template': "第{line}行: {code}\n→ 计算右侧表达式: {expr_detail}\n→ 结果: {var} = {result}",
        'with_state': True
    },
    
    'aug_assign': {
        'template': "第{line}行: {code}\n→ 计算: {var} = {old_val} {op} {operand} = {result}",
        'with_state': True
    },
    
    'for_start': {
        'template': "第{line}行: {code}\n→ 进入循环，循环变量{iter_var}={iter_val}，开始第1次迭代",
        'with_state': True
    },
    
    'for_continue': {
        'template': "第{line}行: {code}\n→ 继续循环，{iter_var}={iter_val}，开始第{iter_count}次迭代",
        'with_state': True
    },
    
    'for_end': {
        'template': "第{line}行: {code}\n→ 循环结束，已遍历完所有元素",
        'with_state': True
    },
    
    'while_start': {
        'template': "第{line}行: {code}\n→ 进入while循环，条件为真",
        'with_state': True
    },
    
    'while_continue': {
        'template': "第{line}行: {code}\n→ 继续while循环，条件仍为真",
        'with_state': True
    },
    
    'while_end': {
        'template': "第{line}行: {code}\n→ while循环结束，条件为假",
        'with_state': True
    },
    
    'if_true': {
        'template': "第{line}行: {code}\n→ 条件为真，进入if分支",
        'with_state': False
    },
    
    'if_false': {
        'template': "第{line}行: {code}\n→ 条件为假，跳过if分支",
        'with_state': False
    },
    
    'else': {
        'template': "第{line}行: {code}\n→ 进入else分支",
        'with_state': False
    },
    
    'elif_true': {
        'template': "第{line}行: {code}\n→ elif条件为真，进入该分支",
        'with_state': False
    },
    
    'elif_false': {
        'template': "第{line}行: {code}\n→ elif条件为假，继续检查",
        'with_state': False
    },
    
    'return': {
        'template': "第{line}行: {code}\n→ 返回值: {value}",
        'with_state': False
    },
    
    'function_def': {
        'template': "第{line}行: {code}\n→ 定义函数{func_name}",
        'with_state': False
    },
    
    'function_call': {
        'template': "第{line}行: {code}\n→ 调用函数，参数: {params}，返回: {result}",
        'with_state': True
    },
    
    'print_statement': {
        'template': "第{line}行: {code}\n→ 打印输出: {print_content}",
        'with_state': True
    },
}

# 步骤划分配置
STEP_CONFIG = {
    'lines_per_step': 8,  # 每个步骤最多包含的行数
    'auto_title': True,   # 是否自动生成步骤标题
}

# 状态输出配置
STATE_CONFIG = {
    'show_state': True,      # 是否显示状态
    'state_frequency': 1,    # 每N行显示一次状态（1表示每行都显示）
}
```

#### cot_generator.py

```py
"""
基于模板的COT生成器
"""

import ast
import re
from config import COT_TEMPLATES, STEP_CONFIG, STATE_CONFIG


class CodeClassifier:
    """代码行分类器"""
    
    def __init__(self):
        self.loop_counters = {}  # 追踪循环迭代次数
        self.last_lineno = None
        self.in_loop_header = {}  # 记录是否在循环头部
    
    def classify(self, line, prev_line=None, next_line=None):
        """分类代码行"""
        code = line.code.strip()
        lineno = line.lineno
        
        # Print语句
        if code.startswith('print('):
            return 'print_statement'
        
        # For循环特殊处理
        if code.startswith('for '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                self.in_loop_header[lineno] = True
                return 'for_start'
            else:
                self.loop_counters[lineno] += 1
                # 检查是否是最后一次迭代
                if next_line and next_line.lineno != lineno:
                    return 'for_end'
                else:
                    return 'for_continue'
        
        # While循环
        if code.startswith('while '):
            if lineno not in self.loop_counters:
                self.loop_counters[lineno] = 1
                return 'while_start'
            else:
                self.loop_counters[lineno] += 1
                if next_line and next_line.lineno != lineno:
                    return 'while_end'
                else:
                    return 'while_continue'
        
        # If语句
        if code.startswith('if '):
            return 'if_true'  # 假设执行到就是True
        
        if code.startswith('elif '):
            return 'elif_true'
        
        if code.startswith('else:'):
            return 'else'
        
        # Return语句
        if code.startswith('return'):
            return 'return'
        
        # 函数定义
        if code.startswith('def '):
            return 'function_def'
        
        # 赋值语句
        if '=' in code:
            # 增强赋值
            if re.search(r'\w+\s*[+\-*/]=', code):
                return 'aug_assign'
            
            # 判断是常量还是表达式
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        # 检查右值
                        if isinstance(node.value, (ast.Constant, ast.Num, ast.Str)):
                            return 'assign_constant'
                        else:
                            return 'assign_expr'
            except:
                # 简单判断
                if re.match(r'^\s*\w+\s*=\s*[\d\'"]+\s*$', code):
                    return 'assign_constant'
                else:
                    return 'assign_expr'
        
        return 'unknown'


class ParameterExtractor:
    """参数提取器"""
    
    def extract(self, line, line_type, classifier):
        """提取模板参数"""
        params = {
            'line': line.lineno,
            'code': line.code.strip(),
        }
        
        var_dict = line.get_var_dict()
        
        # Print语句
        if line_type == 'print_statement':
            # 提取print的内容
            match = re.search(r'print\((.*)\)', line.code)
            if match:
                print_arg = match.group(1).strip()
                # 尝试从变量字典获取值
                if print_arg in var_dict:
                    params['print_content'] = f"{print_arg} = {var_dict[print_arg]}"
                else:
                    # 可能是表达式或常量
                    params['print_content'] = print_arg
        
        # 提取变量名
        if line_type in ['assign_constant', 'assign_expr', 'aug_assign']:
            lvalues = self._extract_lvalue(line.code)
            if lvalues:
                params['var'] = lvalues[0]
                params['value'] = var_dict.get(lvalues[0], '?')
                params['result'] = params['value']
        
        # 表达式展开
        if line_type == 'assign_expr':
            params['expr_detail'] = self._expand_expression(line.code, var_dict)
        
        # 增强赋值
        if line_type == 'aug_assign':
            var = params['var']
            # 提取操作符
            match = re.search(r'([+\-*/])=', line.code)
            if match:
                params['op'] = match.group(1)
            
            # 提取操作数
            parts = line.code.split('=', 1)
            if len(parts) > 1:
                operand = parts[1].strip()
                params['operand'] = operand
            
            # 需要从前一个状态获取old_val
            params['old_val'] = '?'  # 这个需要从前一行获取
        
        # For循环
        if line_type.startswith('for'):
            # 提取循环变量
            match = re.match(r'for\s+(\w+)\s+in', line.code)
            if match:
                iter_var = match.group(1)
                params['iter_var'] = iter_var
                params['iter_val'] = var_dict.get(iter_var, '?')
                params['iter_count'] = classifier.loop_counters.get(line.lineno, 1)
        
        # While循环
        if line_type.startswith('while'):
            params['condition'] = line.code.replace('while', '').replace(':', '').strip()
        
        # Return语句
        if line_type == 'return':
            return_val = line.code.replace('return', '').strip()
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
            match = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[=+\-*/]=', code)
            if match:
                return [match.group(1)]
        return []
    
    def _expand_expression(self, code, var_dict):
        """展开表达式，用实际值替换变量"""
        # 提取右值
        parts = code.split('=', 1)
        if len(parts) < 2:
            return code
        
        expr = parts[1].strip()
        
        # 简单替换变量
        expanded = expr
        for var, val in var_dict.items():
            expanded = re.sub(r'\b' + var + r'\b', str(val), expanded)
        
        # 尝试计算
        try:
            result = eval(expanded)
            return f"{expr} = {expanded} = {result}"
        except:
            return f"{expr} = {expanded}"


class COTGenerator:
    """COT生成器"""
    
    def __init__(self, pruned_file):
        self.pruned_file = pruned_file
        self.target_line = None
        self.target_var = None
        self.lines = []
    
    def load_pruned_trace(self):
        """加载剪枝后的追踪文件"""
        with open(self.pruned_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        # 解析头部
        self.target_line = int(content[0].strip())
        self.target_var = content[1].strip()
        
        # 解析追踪行
        from pruner import TraceLine
        i = 3  # 跳过前三行（目标行、目标变量、---）
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
        """生成COT"""
        classifier = CodeClassifier()
        extractor = ParameterExtractor()
        
        output_lines = []
        output_lines.append(f"目标: 求第{self.target_line}行执行后变量{self.target_var}的值\n")
        
        # 分类并生成
        current_step = 1
        step_lines = []
        prev_var_dict = {}
        
        for i, line in enumerate(self.lines):
            next_line = self.lines[i + 1] if i + 1 < len(self.lines) else None
            
            # 分类
            line_type = classifier.classify(line, None, next_line)
            
            if line_type == 'unknown':
                continue
            
            # 提取参数
            params = extractor.extract(line, line_type, classifier)
            
            # 补充old_val（用于aug_assign）
            if line_type == 'aug_assign' and 'var' in params:
                var = params['var']
                params['old_val'] = prev_var_dict.get(var, '?')
            
            # 获取模板
            template_info = COT_TEMPLATES.get(line_type)
            if not template_info:
                continue
            
            template = template_info['template']
            cot_text = template.format(**params)
            step_lines.append(cot_text)
            
            # 添加状态
            if template_info.get('with_state') and STATE_CONFIG['show_state']:
                state_text = self._format_state(line.get_var_dict())
                step_lines.append(state_text)
            
            # 记录当前变量状态
            prev_var_dict = line.get_var_dict()
            
            # 步骤划分
            if len(step_lines) >= STEP_CONFIG['lines_per_step']:
                step_title = f"步骤{current_step}: {self._generate_step_title(step_lines)}"
                output_lines.append(step_title)
                output_lines.extend(step_lines)
                output_lines.append("")
                step_lines = []
                current_step += 1
        
        # 剩余行
        if step_lines:
            step_title = f"步骤{current_step}: 最终计算"
            output_lines.append(step_title)
            output_lines.extend(step_lines)
            output_lines.append("")
        
        # 最终答案
        final_value = self.lines[-1].get_var_dict().get(self.target_var, '?')
        output_lines.append(f"最终答案: {final_value}")
        
        return '\n'.join(output_lines)
    
    def _format_state(self, var_dict):
        """格式化状态"""
        if not var_dict:
            return ""
        
        items = [f"{k}={v}" for k, v in var_dict.items()]
        return f"→ 当前状态: {', '.join(items)}"
    
    def _generate_step_title(self, step_lines):
        """生成步骤标题"""
        # 简单版本：根据内容判断
        text = '\n'.join(step_lines)
        if '循环' in text:
            return "循环执行"
        elif '初始化' in text or '赋值' in text:
            return "初始化变量"
        elif '打印' in text:
            return "输出结果"
        else:
            return "计算过程"
    
    def save_cot(self, output_file):
        """保存COT"""
        cot_text = self.generate()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cot_text)
        return output_file
    
    @staticmethod
    def generate_cot(pruned_file, output_file):
        """静态方法：生成COT"""
        generator = COTGenerator(pruned_file)
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


class COTFramework:
    """COT生成框架主类"""
    
    def __init__(self, source_file, target_line, target_var):
        self.source_file = source_file
        self.target_line = target_line
        self.target_var = target_var
        
        # 生成文件名和目录
        base_name = os.path.splitext(os.path.basename(source_file))[0]
        self.data_dir = f"data_{base_name}"
        
        # 创建数据目录
        os.makedirs(self.data_dir, exist_ok=True)
        
        # 生成文件路径（存放在data目录中）
        self.trace_file = os.path.join(self.data_dir, f"trace_{base_name}.txt")
        self.pruned_file = os.path.join(self.data_dir, f"trimmed_trace_{base_name}.txt")
        self.cot_file = os.path.join(self.data_dir, f"final_cot_{base_name}.txt")
    
    def run(self):
        """执行完整流程"""
        print("=" * 60)
        print("COT生成框架")
        print("=" * 60)
        
        # 步骤1: 代码执行追踪
        print("\n[步骤1/4] 代码执行追踪...")
        print(f"  源文件: {self.source_file}")
        print(f"  数据目录: {self.data_dir}/")
        PythonTracer.trace_file(self.source_file, self.trace_file)
        print(f"  ✓ 追踪完成，输出: {self.trace_file}")
        
        # 步骤2: 目标定位
        print("\n[步骤2/4] 目标定位...")
        print(f"  目标行号: {self.target_line}")
        print(f"  目标变量: {self.target_var}")
        print(f"  ✓ 目标已确定")
        
        # 步骤3: 智能回溯与剪枝
        print("\n[步骤3/4] 智能回溯与剪枝...")
        TracePruner.prune_trace(self.trace_file, self.target_line, 
                               self.target_var, self.pruned_file)
        print(f"  ✓ 剪枝完成，输出: {self.pruned_file}")
        
        # 步骤4: 模板化COT生成
        print("\n[步骤4/4] 模板化COT生成...")
        COTGenerator.generate_cot(self.pruned_file, self.cot_file)
        print(f"  ✓ COT生成完成，输出: {self.cot_file}")
        
        # 显示结果
        print("\n" + "=" * 60)
        print("生成完成！")
        print("=" * 60)
        print(f"\n数据目录: {self.data_dir}/")
        print(f"  ├── {os.path.basename(self.trace_file)}")
        print(f"  ├── {os.path.basename(self.pruned_file)}")
        print(f"  └── {os.path.basename(self.cot_file)}")
        
        # 显示COT内容
        print("\n" + "-" * 60)
        print("COT内容预览:")
        print("-" * 60)
        with open(self.cot_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        
        return self.cot_file


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='COT生成框架')
    parser.add_argument('source_file', help='Python源代码文件')
    parser.add_argument('target_line', type=int, help='目标行号')
    parser.add_argument('target_var', help='目标变量名')
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not os.path.exists(args.source_file):
        print(f"错误: 文件 '{args.source_file}' 不存在")
        return
    
    # 运行框架
    framework = COTFramework(args.source_file, args.target_line, args.target_var)
    framework.run()


if __name__ == '__main__':
    # 示例用法（无参数时）
    import sys
    if len(sys.argv) == 1:
        print("示例用法:")
        print("  python main.py test.py 7 d")
        print("\n正在运行示例...")
        
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
        
        framework = COTFramework('test.py', 7, 'd')
        framework.run()
    else:
        main()
```

#### pruner.py

```py
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
```

#### tracer.py

```py
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
```

## 测试与测试记录

### 测试列表

| 编号 | 文件名                         | 目标行 | 目标变量 | 核心特点     | 噪声类型            |
| ---- | ------------------------------ | ------ | -------- | ------------ | ------------------- |
| 1    | test_01_basic_noise.py         | 9      | result   | 基础噪声过滤 | 无关变量+计算       |
| 2    | test_02_loop_noise.py          | 8      | sum_val  | 循环噪声     | 循环内无关累加      |
| 3    | test_03_branch_noise.py        | 10     | result   | 分支噪声     | 未执行分支          |
| 4    | test_04_nested_loop.py         | 8      | total    | 嵌套循环     | 双层噪声            |
| 5    | test_05_dependency_chain.py    | 10     | e        | 长依赖链     | 链中穿插噪声        |
| 6    | test_06_partial_list.py        | 6      | result   | 部分列表使用 | 整个列表噪声        |
| 7    | test_07_conditional_compute.py | 9      | result   | 条件计算     | 分支内噪声          |
| 8    | test_08_dict_noise.py          | 6      | result   | 字典噪声     | 未使用的键          |
| 9    | test_9_function_call.py        | 6      | result   | 函数调用     | 无用参数+函数内噪声 |
| 10   | test_10_while_noise.py         | 7      | count    | While循环    | 循环内噪声          |

### test1

#### 测例

- 测试1: 基础噪声过滤
- test_01_basic_noise.py
- 目标行：9
- 目标变量：result
- 特色：多个无关噪声标量与多个无关噪声计算
- 测试命令： `python main.py test_01_basic_noise.py 9 result`

```python
a = 1
b = 2
noise1 = 100
noise2 = 200
c = a + b
noise3 = noise1 + noise2
d = c * 2
noise4 = d - 5
result = d + a
```

#### 测试结果

剪枝后，顺利去掉噪声行和噪声变量，符合预期

```
9
result
---
1 a = 1
1 ['a'] ['1']
2 b = 2
2 ['a', 'b'] ['1', '2']
5 c = a + b
5 ['a', 'b', 'c'] ['1', '2', '3']
7 d = c * 2
7 ['a', 'c', 'd'] ['1', '3', '6']
9 result = d + a
9 ['a', 'd', 'result'] ['1', '6', '7']
```

同时这里的cot也符合预期

```
目标: 求第9行执行后变量result的值

步骤1: 初始化变量
第1行: a = 1
→ 将变量a赋值为1
→ 当前状态: a=1
第2行: b = 2
→ 将变量b赋值为2
→ 当前状态: a=1, b=2
第5行: c = a + b
→ 计算右侧表达式: a + b = 1 + 2 = 3
→ 结果: c = 3
→ 当前状态: a=1, b=2, c=3
第7行: d = c * 2
→ 计算右侧表达式: c * 2 = 3 * 2 = 6
→ 结果: d = 6
→ 当前状态: a=1, c=3, d=6

步骤2: 最终计算
第9行: result = d + a
→ 计算右侧表达式: d + a = 6 + 1 = 7
→ 结果: result = 7
→ 当前状态: a=1, d=6, result=7

最终答案: 7
```

### test2

#### 测例

- 测试2: 循环中的噪声
- test_02_loop_noise.py
- 目标行：8
- 目标变量：sum_val
- 特色：循环内有无关计算,测试循环展开后的剪枝
- 测试命令： `python main.py test_02_loop_noise.py 8 sum_val`

```
sum_val = 0
noise_sum = 0
for i in range(5):
    temp = i * 2
    sum_val = sum_val + temp
    noise_sum = noise_sum + i
    useless = i ** 2
result = sum_val
```

#### 测试结果

剪枝掉了循环中的噪声赋值与计算

```
8
sum_val
---
1 sum_val = 0
1 ['sum_val'] ['0']
3 for i in range(5):
3 ['sum_val', 'i'] ['0', '0']
4 temp = i * 2
4 ['sum_val', 'i', 'temp'] ['0', '0', '0']
5 sum_val = sum_val + temp
5 ['sum_val', 'i', 'temp'] ['0', '0', '0']
3 for i in range(5):
3 ['sum_val', 'i', 'temp'] ['0', '1', '0']
4 temp = i * 2
4 ['sum_val', 'i', 'temp'] ['0', '1', '2']
5 sum_val = sum_val + temp
5 ['sum_val', 'i', 'temp'] ['2', '1', '2']
3 for i in range(5):
3 ['sum_val', 'i', 'temp'] ['2', '2', '2']
4 temp = i * 2
4 ['sum_val', 'i', 'temp'] ['2', '2', '4']
5 sum_val = sum_val + temp
5 ['sum_val', 'i', 'temp'] ['6', '2', '4']
3 for i in range(5):
3 ['sum_val', 'i', 'temp'] ['6', '3', '4']
4 temp = i * 2
4 ['sum_val', 'i', 'temp'] ['6', '3', '6']
5 sum_val = sum_val + temp
5 ['sum_val', 'i', 'temp'] ['12', '3', '6']
3 for i in range(5):
3 ['sum_val', 'i', 'temp'] ['12', '4', '6']
4 temp = i * 2
4 ['sum_val', 'i', 'temp'] ['12', '4', '8']
5 sum_val = sum_val + temp
5 ['sum_val', 'i', 'temp'] ['20', '4', '8']
3 for i in range(5):
3 ['sum_val', 'i'] ['20', '4']
8 result = sum_val
8 ['sum_val'] ['20']
```

### test3

#### 测例

- 测试3: 分支噪声 
- test_03_branch_noise.py
- 目标行：10
- 目标变量：result
- 特点: 包含不执行的分支,测试分支剪枝
- 测试命令： `python main.py test_03_branch_noise.py 10 result`

```
x = 10
y = 5
noise = 100
if x > y:
    x = x + 1
    noise = noise * 2
else:
    x = x - 1
    noise = noise / 2
result = x
```

#### 测试结果

剪枝去掉了不会进入的噪声分支，也去掉了对应的噪声行，符合预期

```
10
result
---
1 x = 10
1 ['x'] ['10']
2 y = 5
2 ['x', 'y'] ['10', '5']
4 if x > y:
4 ['x', 'y'] ['10', '5']
5 x = x + 1
5 ['x'] ['11']
10 result = x
10 ['x', 'result'] ['11', '11']
```

最终的cot也符合预期

```
目标: 求第10行执行后变量result的值

步骤1: 初始化变量
第1行: x = 10
→ 将变量x赋值为10
→ 当前状态: x=10
第2行: y = 5
→ 将变量y赋值为5
→ 当前状态: x=10, y=5
第4行: if x > y:
→ 条件为真，进入if分支
第5行: x = x + 1
→ 计算右侧表达式: x + 1 = 11 + 1 = 12
→ 结果: x = 11
→ 当前状态: x=11
第10行: result = x
→ 计算右侧表达式: x = 11 = 11
→ 结果: result = 11
→ 当前状态: x=11, result=11

最终答案: 11
```

### test4

#### 测例

- 测试4：嵌套循环噪声
- test_04_nested_loop.py
- 目标行：8
- 目标变量：total
- 特点: 双层循环,外层有噪声,内层有计算
- 测试命令： `python main.py test_04_nested_loop.py 8 total`

```
total = 0
outer_noise = 0
for i in range(3):
    outer_noise += i
    for j in range(2):
        total = total + i * j
        inner_noise = j ** 2
result = total
```

#### 测试结果

剪枝结果符合预期

```
8
total
---
1 total = 0
1 ['total'] ['0']
3 for i in range(3):
3 ['total', 'i'] ['0', '0']
5 for j in range(2):
5 ['total', 'i', 'j'] ['0', '0', '0']
6 total = total + i * j
6 ['total', 'i', 'j'] ['0', '0', '0']
5 for j in range(2):
5 ['total', 'i', 'j'] ['0', '0', '1']
6 total = total + i * j
6 ['total', 'i', 'j'] ['0', '0', '1']
5 for j in range(2):
5 ['total', 'i', 'j'] ['0', '0', '1']
3 for i in range(3):
3 ['total', 'i', 'j'] ['0', '1', '1']
5 for j in range(2):
5 ['total', 'i', 'j'] ['0', '1', '0']
6 total = total + i * j
6 ['total', 'i', 'j'] ['0', '1', '0']
5 for j in range(2):
5 ['total', 'i', 'j'] ['0', '1', '1']
6 total = total + i * j
6 ['total', 'i', 'j'] ['1', '1', '1']
5 for j in range(2):
5 ['total', 'i', 'j'] ['1', '1', '1']
3 for i in range(3):
3 ['total', 'i', 'j'] ['1', '2', '1']
5 for j in range(2):
5 ['total', 'i', 'j'] ['1', '2', '0']
6 total = total + i * j
6 ['total', 'i', 'j'] ['1', '2', '0']
5 for j in range(2):
5 ['total', 'i', 'j'] ['1', '2', '1']
6 total = total + i * j
6 ['total', 'i', 'j'] ['3', '2', '1']
5 for j in range(2):
5 ['total', 'i', 'j'] ['3', '2', '1']
3 for i in range(3):
3 ['total', 'i'] ['3', '2']
8 result = total
8 ['total'] ['3']
```

同时生成的cot也符合预期

```
目标: 求第8行执行后变量total的值

步骤1: 循环执行
第1行: total = 0
→ 将变量total赋值为0
→ 当前状态: total=0
第3行: for i in range(3):
→ 进入循环，循环变量i=0，开始第1次迭代
→ 当前状态: total=0, i=0
第5行: for j in range(2):
→ 进入循环，循环变量j=0，开始第1次迭代
→ 当前状态: total=0, i=0, j=0
第6行: total = total + i * j
→ 计算右侧表达式: total + i * j = 0 + 0 * 0 = 0
→ 结果: total = 0
→ 当前状态: total=0, i=0, j=0

步骤2: 循环执行
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=0, i=0, j=1
第6行: total = total + i * j
→ 计算右侧表达式: total + i * j = 0 + 0 * 1 = 0
→ 结果: total = 0
→ 当前状态: total=0, i=0, j=1
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=0, i=0, j=1
第3行: for i in range(3):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=0, i=1, j=1

步骤3: 循环执行
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=0, i=1, j=0
第6行: total = total + i * j
→ 计算右侧表达式: total + i * j = 0 + 1 * 0 = 0
→ 结果: total = 0
→ 当前状态: total=0, i=1, j=0
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=0, i=1, j=1
第6行: total = total + i * j
→ 计算右侧表达式: total + i * j = 1 + 1 * 1 = 2
→ 结果: total = 1
→ 当前状态: total=1, i=1, j=1

步骤4: 循环执行
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=1, i=1, j=1
第3行: for i in range(3):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=1, i=2, j=1
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=1, i=2, j=0
第6行: total = total + i * j
→ 计算右侧表达式: total + i * j = 1 + 2 * 0 = 1
→ 结果: total = 1
→ 当前状态: total=1, i=2, j=0

步骤5: 循环执行
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=1, i=2, j=1
第6行: total = total + i * j
→ 计算右侧表达式: total + i * j = 3 + 2 * 1 = 5
→ 结果: total = 3
→ 当前状态: total=3, i=2, j=1
第5行: for j in range(2):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=3, i=2, j=1
第3行: for i in range(3):
→ 循环结束，已遍历完所有元素
→ 当前状态: total=3, i=2

步骤6: 最终计算
第8行: result = total
→ 计算右侧表达式: total = 3 = 3
→ 结果: result = ?
→ 当前状态: total=3

最终答案: 3
```

### test5

#### 测例

- 测试5：传递依赖链
- test_05_dependency_chain.py
- 目标行：10
- 目标变量：e
- 特点: 长依赖链,中间穿插噪声
- 测试命令： `python main.py test_05_dependency_chain.py 10 e`

```
a = 1
noise1 = 999
b = a + 2
noise2 = noise1 * 2
c = b + 3
noise3 = noise2 - noise1
d = c + 4
noise4 = 888
e = d + 5
```

#### 测试结果

结果符合预期，剪枝掉了噪声行和不需要的变量

```
10
e
---
1 a = 1
1 ['a'] ['1']
3 b = a + 2
3 ['a', 'b'] ['1', '3']
5 c = b + 3
5 ['b', 'c'] ['3', '6']
7 d = c + 4
7 ['c', 'd'] ['6', '10']
9 e = d + 5
9 ['d', 'e'] ['10', '15']
```

生成的cot也符合预期

```
目标: 求第10行执行后变量e的值

步骤1: 初始化变量
第1行: a = 1
→ 将变量a赋值为1
→ 当前状态: a=1
第3行: b = a + 2
→ 计算右侧表达式: a + 2 = 1 + 2 = 3
→ 结果: b = 3
→ 当前状态: a=1, b=3
第5行: c = b + 3
→ 计算右侧表达式: b + 3 = 3 + 3 = 6
→ 结果: c = 6
→ 当前状态: b=3, c=6
第7行: d = c + 4
→ 计算右侧表达式: c + 4 = 6 + 4 = 10
→ 结果: d = 10
→ 当前状态: c=6, d=10

步骤2: 最终计算
第9行: e = d + 5
→ 计算右侧表达式: d + 5 = 10 + 5 = 15
→ 结果: e = 15
→ 当前状态: d=10, e=15

最终答案: 15
```

### test6

#### 测例

- 测试6：噪声列表
- test_06_partial_list.py
- 目标行：6
- 目标变量：result
- 特点: 列表中只用部分元素
- 测试命令： `python main.py test_06_partial_list.py 6 result`

```
lst = [1, 2, 3, 4, 5]
noise_lst = [10, 20, 30]
a = lst[0]
b = lst[2]
noise_val = noise_lst[1]
result = a + b
```

#### 测试结果

结果符合预期，剪枝掉了不要的噪声列表和噪声行

```
6
result
---
1 lst = [1, 2, 3, 4, 5]
1 ['lst'] ['[1, 2, 3, 4, 5]']
3 a = lst[0]
3 ['lst', 'a'] ['[1, 2, 3, 4, 5]', '1']
4 b = lst[2]
4 ['lst', 'a', 'b'] ['[1, 2, 3, 4, 5]', '1', '3']
6 result = a + b
6 ['a', 'b', 'result'] ['1', '3', '4']
```

cot也符合预期

```
目标: 求第6行执行后变量result的值

步骤1: 计算过程
第1行: lst = [1, 2, 3, 4, 5]
→ 计算右侧表达式: [1, 2, 3, 4, 5] = [1, 2, 3, 4, 5] = [1, 2, 3, 4, 5]
→ 结果: lst = [1, 2, 3, 4, 5]
→ 当前状态: lst=[1, 2, 3, 4, 5]
第3行: a = lst[0]
→ 计算右侧表达式: lst[0] = [1, 2, 3, 4, 5][0] = 1
→ 结果: a = 1
→ 当前状态: lst=[1, 2, 3, 4, 5], a=1
第4行: b = lst[2]
→ 计算右侧表达式: lst[2] = [1, 2, 3, 4, 5][2] = 3
→ 结果: b = 3
→ 当前状态: lst=[1, 2, 3, 4, 5], a=1, b=3
第6行: result = a + b
→ 计算右侧表达式: a + b = 1 + 3 = 4
→ 结果: result = 4
→ 当前状态: a=1, b=3, result=4

最终答案: 4
```

### test7

#### 测例

- 测试7：条件内的选择性计算
- test_07_conditional_compute.py
- 目标行：9
- 目标变量：result
- 特点: 不同分支定义同一变量
- 测试命令： `python main.py test_07_conditional_compute.py 9 result`

```
x = 10
noise = 0
if x > 5:
    temp = x * 2
    noise = 100
else:
    temp = x + 2
    noise = 200
result = temp
```

#### 测试结果

结果符合预期，选择了正确的分支和定义

```
9
result
---
1 x = 10
1 ['x'] ['10']
3 if x > 5:
3 ['x'] ['10']
4 temp = x * 2
4 ['x', 'temp'] ['10', '20']
9 result = temp
9 ['temp', 'result'] ['20', '20']
```

cot也是符合预期

```
目标: 求第9行执行后变量result的值

步骤1: 最终计算
第1行: x = 10
→ 将变量x赋值为10
→ 当前状态: x=10
第3行: if x > 5:
→ 条件为真，进入if分支
第4行: temp = x * 2
→ 计算右侧表达式: x * 2 = 10 * 2 = 20
→ 结果: temp = 20
→ 当前状态: x=10, temp=20
第9行: result = temp
→ 计算右侧表达式: temp = 20 = 20
→ 结果: result = 20
→ 当前状态: temp=20, result=20

最终答案: 20
```

### test8

#### 测例

- 测试8：字典操作噪声
- test_08_dict_noise.py
- 目标行：6
- 目标变量：result
- 特点: 字典中只用部分键
- 测试命令： `python main.py test_08_dict_noise.py 6 result`

```
data = {'a': 10, 'b': 20, 'c': 30}
noise_dict = {'x': 100, 'y': 200}
val1 = data['a']
val2 = data['b']
noise_val = noise_dict['x']
result = val1 + val2
```

#### 测试结果

剪枝符合预期

```
6
result
---
1 data = {'a': 10, 'b': 20, 'c': 30}
1 ['data'] ["{'a': 10, 'b': 20, 'c': 30}"]
3 val1 = data['a']
3 ['data', 'val1'] ["{'a': 10, 'b': 20, 'c': 30}", '10']
4 val2 = data['b']
4 ['data', 'val1', 'val2'] ["{'a': 10, 'b': 20, 'c': 30}", '10', '20']
6 result = val1 + val2
6 ['val1', 'val2', 'result'] ['10', '20', '30']
```

cot生成也符合预期

```
目标: 求第6行执行后变量result的值

步骤1: 计算过程
第1行: data = {'a': 10, 'b': 20, 'c': 30}
→ 计算右侧表达式: {'a': 10, 'b': 20, 'c': 30} = {'a': 10, 'b': 20, 'c': 30} = {'a': 10, 'b': 20, 'c': 30}
→ 结果: data = {'a': 10, 'b': 20, 'c': 30}
→ 当前状态: data={'a': 10, 'b': 20, 'c': 30}
第3行: val1 = data['a']
→ 计算右侧表达式: data['a'] = {'a': 10, 'b': 20, 'c': 30}['a'] = 10
→ 结果: val1 = 10
→ 当前状态: data={'a': 10, 'b': 20, 'c': 30}, val1=10
第4行: val2 = data['b']
→ 计算右侧表达式: data['b'] = {'a': 10, 'b': 20, 'c': 30}['b'] = 20
→ 结果: val2 = 20
→ 当前状态: data={'a': 10, 'b': 20, 'c': 30}, val1=10, val2=20
第6行: result = val1 + val2
→ 计算右侧表达式: val1 + val2 = 10 + 20 = 30
→ 结果: result = 30
→ 当前状态: val1=10, val2=20, result=30

最终答案: 30
```

### test9

#### 测例

- 测试9：函数调用(内联视角)
- test_09_function_call.py
- 目标行：6
- 目标变量：result
- 特点: 简单函数,有噪声参数
- 测试命令： `python main.py test_09_function_call.py 6 result`

```
def add(a, b, c):
    noise = a * b
    return a + b

x = 5
result = add(x, 3, 999) 
```

#### 测试结果

去掉噪声参数和噪声行都很符合预期

```
6
result
---
1 def add(a, b, c):
1 [] []
5 x = 5
5 ['x'] ['5']
6 result = add(x, 3, 999)
6 ['a', 'b'] ['5', '3']
3 return a + b
3 ['a', 'b'] ['5', '3']
```

同时cot也符合预期

```
目标: 求第6行执行后变量result的值

步骤1: 最终计算
第1行: def add(a, b, c):
→ 定义函数add
第5行: x = 5
→ 将变量x赋值为5
→ 当前状态: x=5
第6行: result = add(x, 3, 999)
→ 计算右侧表达式: add(x, 3, 999) = add(x, 3, 999)
→ 结果: result = ?
→ 当前状态: a=5, b=3
第3行: return a + b
→ 返回值: a + b
```

### test10

#### 测例

- 测试10： While循环噪声
- test_10_while_noise.py
- 目标行：7
- 目标变量：count
- 特点: while循环,有噪声变量
- 测试命令： `python main.py test_10_while_noise.py 7 count`

```
count = 0
noise_count = 100
while count < 5:
    count = count + 1
    noise_count = noise_count - 1
    temp = count * 2
result = count
```

#### 测试结果

剪枝顺利去掉了噪声行和噪声变量

```
7
count
---
1 count = 0
1 ['count'] ['0']
3 while count < 5:
3 ['count'] ['0']
4 count = count + 1
4 ['count'] ['1']
3 while count < 5:
3 ['count'] ['1']
4 count = count + 1
4 ['count'] ['2']
3 while count < 5:
3 ['count'] ['2']
4 count = count + 1
4 ['count'] ['3']
3 while count < 5:
3 ['count'] ['3']
4 count = count + 1
4 ['count'] ['4']
3 while count < 5:
3 ['count'] ['4']
4 count = count + 1
4 ['count'] ['5']
3 while count < 5:
3 ['count'] ['5']
7 result = count
7 ['count'] ['5']
```

cot也符合预期

```
7
count
---
1 count = 0
1 ['count'] ['0']
3 while count < 5:
3 ['count'] ['0']
4 count = count + 1
4 ['count'] ['1']
3 while count < 5:
3 ['count'] ['1']
4 count = count + 1
4 ['count'] ['2']
3 while count < 5:
3 ['count'] ['2']
4 count = count + 1
4 ['count'] ['3']
3 while count < 5:
3 ['count'] ['3']
4 count = count + 1
4 ['count'] ['4']
3 while count < 5:
3 ['count'] ['4']
4 count = count + 1
4 ['count'] ['5']
3 while count < 5:
3 ['count'] ['5']
7 result = count
7 ['count'] ['5']
```

