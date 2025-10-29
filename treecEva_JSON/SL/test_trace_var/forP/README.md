# 代码训练集COT生成框架

[toc]

## 背景

我正在构建一系列Python代码训练集,用于提升大模型的代码推理能力。每个数据样本包含以下四个部分:

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

## 已有代码（可参考）

trace_python.py

```py
import sys
import linecache
import os

class PythonTracer:
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
        
        # 如果没有main函数,追踪模块级代码
        if not self.has_main_function and func_name == '<module>':
            if not self.module_started:
                self.module_started = True
            self.trace_active = True
        
        # 如果有main函数但还没进入main,不追踪
        if self.has_main_function and not self.trace_active:
            return self.trace_handler
        
        if event == 'line' and self.trace_active:
            lineno = frame.f_lineno
            source_line = linecache.getline(filename, lineno).rstrip()
            local_vars = frame.f_locals.copy()
            
            # 输出之前待输出的行
            if self.pending_trace:
                self.output_pending_trace(local_vars)
            
            # 保存当前行信息,等待下次输出
            self.pending_trace = {
                'lineno': lineno,
                'source': source_line
            }
        
        elif event == 'return':
            # 函数返回时,输出最后一行
            if self.pending_trace and self.trace_active:
                self.output_pending_trace(frame.f_locals.copy())
                self.pending_trace = None
            
            # 如果是main函数返回,停止追踪
            if func_name == 'main':
                self.trace_active = False
            # 如果是模块级代码返回,停止追踪
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
        """过滤变量,只保留数据变量"""
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
            # 跳过namedtuple类型本身(但保留实例)
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
    
    def save_output(self, output_file='output.txt'):
        """保存输出到文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.output_lines))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python trace_python.py <script.py>")
        sys.exit(1)
    
    script_file = sys.argv[1]
    
    # 检查文件是否有main函数
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
    tracer.save_output()
    print(f"Trace saved to output.txt")
```

auto_trace.bat

```bat
@echo off
chcp 65001 >nul

echo ==================================================
echo Python 自动变量追踪系统
echo ==================================================

REM 检测源文件
set SOURCE_FILE=
if exist test.py (
    set SOURCE_FILE=test.py
) else (
    echo 错误: 找不到 test.py
    pause
    exit /b 1
)

echo.
echo 找到源文件: %SOURCE_FILE%

set OUTPUT_FILE=output.txt

echo.
echo [1/2] 执行追踪...
python trace_python.py %SOURCE_FILE%
if errorlevel 1 (
    echo 追踪失败!
    pause
    exit /b 1
)
echo √ 追踪成功

echo.
echo [2/2] 追踪结果:
echo ==================================================
type %OUTPUT_FILE%
echo ==================================================

echo.
echo 完成! 结果已保存到: %OUTPUT_FILE%
pause
```

