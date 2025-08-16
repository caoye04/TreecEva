# TreecEva （763）

> CAOYE

[toc]

## 问题背景

|              | CodeSense论文结论回顾                                        |
| ------------ | ------------------------------------------------------------ |
| 数据来源     | 744个真实世界GitHub项目                                      |
| 数据集规模   | Python 2125 \| C 876 \| JAVA 875每个测试数据 3-516 行        |
| 评估任务分层 | Task 1: 代码块级语义 (Block-level)  [预测代码块的执行结果，输入到输出 or 输出到输入]Task 2: 语句级语义 (Statement-level) [ 判断某个语句执行后影响，算数、布尔、第三方库调用、变量赋值、常量赋值]Task 3: 代码属性 (Code Properties) [循环属性、指针属性、分支属性]Task 4: 语义近似 (Approximation) [抽象值预测] |
| 独特之处     | 真实的项目数据、细粒度评估、多编程语言、数目多               |
| 缺陷         | 【复杂性干扰】：真实项目包含大量依赖和无关路径，难以精确定位模型失败的根本原因，也难以有学习价值【不均衡】：可以看到每个task的分配很不均衡，以及语言分布也很不均衡 |
| INSIGHT      | 基于这种评估任务分层的设计与真实世界代码的例子，设计出一颗评估树测试集——TreecEva。<br />思路为：根据分层的逻辑，将代码评估任务分为几类，每类再细分到子类，最终对每个子类给出真实世界代码案例，再人工去设计此案例的其他语言，其他情况，极限的边界情况的变式，最终一步一步地构建出完备的数据集它有如下优势 |

|                               | TreecEva思路展开——具体构建流                                 |
| ----------------------------- | ------------------------------------------------------------ |
| 【阶段1】评估树结构设计       | 1.1. 主干设计 ——> 1.2. 分支设计                              |
| 【阶段2】种子任务收集与分析   | 2.1 CodeSense中寻找种子，稍作改造                            |
| 【阶段3】变式生成策略         | 3.1 为每个分支设计变式生成                                   |
| 【阶段4】自动化生成流水线设计 | 4.1 结合分支种子代码与任务+变式生成范例4.2 设计mutiagent 生成结构 [数据集生成+数据集完备性检查+单数据质量检查]4.3 生成最终数据集 |
| 【阶段5】汇总与整理           | 5.1 将所有数据集按树形结构存储，有完备编号，并维护好树形结构5.2 进行实验验证数据集的训练能力与评估能力 |

## 评估体系建立

TreecEva 

- 语句级推理 [ Statement-Level ]
  - 算数运算 [ Arithmetic ]（四则运算、高级运算、位运算、复合运算）
  - 布尔运算 [ Boolean ] （比较运算、逻辑运算、短路求值）
  - API/函数调用 [ API/Function Call ] （内置函数、数学库、字符串操作、容器操作）
  - 变量赋值 [ Assignment ] （简单赋值、多重赋值、解包赋值）
  -  
  - 大混合
- 代码块级推理（Block-Level）
  - 线性代码块 [ Linear ]（顺序语句、独立语句、依赖语句）
  - 条件代码块 [ Conditional ] （if条件块、switch条件块、嵌套条件块）
  - 迭代代码块 [ Iterative ]（for循环块、While循环快、递归调用块）
  - 大混合
- 代码属性推理（Property-Level）
  - 循环属性 [ Loop ]（迭代计数、变量追踪、终止条件）
  - 分支属性 [ Branch ]（条件求值、路径选择、分支效果）
  - 内存属性 [ Memory ] （引用关系、生命周期、访问模式）
  - 作用域属性 [ Scope ]（可见性、生存期、变量遮蔽）
  - 大混合
- 跨函数推理（MultiFunc-Level）
  - 函数调用链推理 [ Call Chain ]（直接调用、链式调用、递归调用、回归调用）
  - 参数传递推理 [ Parameter Passing ]（值传递、引用传递）
  - 状态传播推理 [ State Propagation ]（全局变量、静态变量、闭包捕获、对象状态）
  - 副作用推理 [ Side Effect ] （I/O操作、异常处理、内存操作、时间依赖）
  - 大混合

## 种子任务构建 (114 SEED)

### 1 - 语句级推理 [ Statement-Level ] (31)

####  1A - 算数运算 [ Arithmetic ] (6)

```json
{
    "id": "SL-AR-S001",
    "metadata": {
        "name": "StatementLevel-Arithmetic-Seed1",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "seed",
        "source": "CodeSense",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = mid + 1`?",
        "code": "a = [1, 2, 4, 4, 5, 6, 7, 23, 8, 9, 20, 11, 13, 34, 66]\naux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\nlo = 0\nmid = 3\nhi = 7\ni = lo\nj = mid + 1\nfor k in range(lo, hi + 1):\n    aux[k] = a[k]\nfor k in range(lo, hi + 1):\n    if i > mid:\n        a[k] = aux[j]\n        j += 1\n    elif j > hi:\n        a[k] = aux[i]\n        i += 1\n    elif util.less(aux[i], aux[j]):\n        a[k] = aux[i]\n        i += 1\n    else:\n        a[k] = aux[j]\n        j += 1",
        "answer": 4
    }
}
```

```json
{
    "id": "SL-AR-S002",
    "metadata": {
        "name": "StatementLevel-Arithmetic-Seed2",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = total // count`?",
        "code": "items = [15, 25, 30, 20]\ntotal = sum(items)\ncount = len(items)\nresult = total // count\nremainder = total % count",
        "answer": 22
    }
}
```

```json
{
    "id": "SL-AR-S003",
    "metadata": {
        "name": "StatementLevel-Arithmetic-Seed3",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = 3.14159 * radius ** 2`?",
        "code": "import math\nradius = 5\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = 3.14159 * radius ** 2\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 78.53975
    }
}
```

```json
{
    "id": "SL-AR-S004",
    "metadata": {
        "name": "StatementLevel-Arithmetic-Seed4",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags | (1 << position)`?",
        "code": "flags = 0b1010\nposition = 2\nmask = flags | (1 << position)\ncheck = mask & (1 << position)\ntoggle = flags ^ (1 << position)",
        "answer": 14
    }
}
```

```json
{
    "id": "SL-AR-S005",
    "metadata": {
        "name": "StatementLevel-Arithmetic-Seed5",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base * 2 + offset // 3 - power ** 2 % 5`?",
        "code": "base = 10\noffset = 17\npower = 3\ntemp1 = base * 2\ntemp2 = offset // 3\ntemp3 = power ** 2\ntemp4 = temp3 % 5\nresult = base * 2 + offset // 3 - power ** 2 % 5",
        "answer": 21
    }
}
```

```json
{
    "id": "SL-AR-S006",
    "metadata": {
        "name": "StatementLevel-Arithmetic-TypeConversion",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(average * weight + bonus)`?",
        "code": "scores = [85, 92, 78, 96]\naverage = sum(scores) / len(scores)\nweight = 0.8\nbonus = 5.5\nfinal_score = int(average * weight + bonus)\nrounded_score = round(average * weight + bonus)",
        "answer": 75
    }
}
```

#### 1B - 布尔运算 [ Boolean ] (5)

```json
{
    "id": "SL-BL-S001",
    "metadata": {
        "name": "StatementLevel-Boolean-Seed1",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "seed",
        "source": "CodeSense-libjpeg-turbo",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `inbuffer == NULL || insize == 0` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nif (inbuffer == NULL || insize == 0) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": false
    }
}
```

```json
{
    "id": "SL-BL-S002",
    "metadata": {
        "name": "StatementLevel-Boolean-Seed2",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "seed",
        "source": "CodeSense-cryptsetup",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!data` when `data` is NULL?",
        "code": "void *data = NULL;\nsize_t size = 1024;\nif (!data) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": true
    }
}
```

```json
{
    "id": "SL-BL-S003",
    "metadata": {
        "name": "StatementLevel-Boolean-Seed3",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "seed",
        "source": "CodeSense-libdwarf",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `res != DW_DLV_OK` when `res` is -1 and `DW_DLV_OK` is 0?",
        "code": "int res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nif (res != DW_DLV_OK) {\n    printf(\"Operation failed\");\n    return DW_DLV_ERROR;\n}",
        "answer": true
    }
}
```

```json
{
    "id": "SL-BL-S004",
    "metadata": {
        "name": "StatementLevel-Boolean-Seed4",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "seed",
        "source": "CodeSense-krb5",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `c < 0x80` when `c` is 65 (ASCII 'A')?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nif (c < 0x80) {\n    printf(\"ASCII character\");\n} else {\n    printf(\"Non-ASCII character\");\n}",
        "answer": true
    }
}
```

```json
{
    "id": "SL-BL-S005",
    "metadata": {
        "name": "StatementLevel-Boolean-Seed5",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "seed",
        "source": "CodeSense-postfix",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `state == IN_CHAR || state == IN_CHAR_SPACE` when `state` is 1, `IN_CHAR` is 1, and `IN_CHAR_SPACE` is 2?",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\nint state = 1;\nint len = 5;\nif (state == IN_CHAR || state == IN_CHAR_SPACE) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
}
```

#### 1C - API/函数调用 [ API/Function Call ] (7)

```json
{
    "id": "SL-API-S001",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "seed",
        "source": "CodeSense",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of the function call `strlen(str)` when `str` is \"hello\"?",
        "code": "#include <string.h>\nchar *str = \"hello\";\nsize_t len = strlen(str);\nprintf(\"Length: %zu\\n\", len);",
        "answer": 5
    }
}
```

```json
{
    "id": "SL-API-S002",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "seed",
        "source": "CodeSense",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of the function call `pow(2.0, 3)` when called with base 2.0 and exponent 3?",
        "code": "#include <math.h>\ndouble base = 2.0;\nint exponent = 3;\ndouble result = pow(base, exponent);\nprintf(\"Result: %.1f\\n\", result);",
        "answer": 8.0
    }
}
```

```json
{
    "id": "SL-API-S003",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the exact number of bytes requested by the function call `malloc(sizeof(int) * 10)` assuming sizeof(int) is 4?",
        "code": "#include <stdlib.h>\n// Assume sizeof(int) = 4 bytes\nint *arr = (int *)malloc(sizeof(int) * 10);\nif (arr != NULL) {\n    arr[0] = 42;\n    printf(\"Memory allocated successfully\\n\");\n}",
        "answer": 40
    }
}
```

```json
{
    "id": "SL-API-S004",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "seed",
        "source": "CodeSense",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what type of value does the function call `getpid()` return?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\npid_t current_pid = getpid();\nprintf(\"Process ID: %d\\n\", current_pid);",
        "answer": "pid_t"
    }
}
```

```json
{
    "id": "SL-API-S005",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "seed",
        "source": "CodeSense",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strcmp(str1, str2)` when `str1` is \"apple\" and `str2` is \"banana\"?",
        "code": "#include <string.h>\nchar *str1 = \"apple\";\nchar *str2 = \"banana\";\nint result = strcmp(str1, str2);\nprintf(\"Comparison result: %d\\n\", result);",
        "answer": -1
    }
}
```

```json
{
    "id": "SL-API-S006",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `fopen(filename, \"r\")` when the file \"data.txt\" does NOT exist?",
        "code": "#include <stdio.h>\nchar *filename = \"nonexistent.txt\";  // This file does not exist\nFILE *fp = fopen(filename, \"r\");\nif (fp == NULL) {\n    printf(\"File could not be opened\\n\");\n} else {\n    printf(\"File opened successfully\\n\");\n    fclose(fp);\n}",
        "answer": "NULL"
    }
}
```

```json
{
    "id": "SL-API-S007",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "seed",
        "source": "CodeSense",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `snprintf(buffer, size, format, value)` when buffer size is 10, format is \"%d\", and value is 12345?",
        "code": "#include <stdio.h>\nchar buffer[10];\nint size = sizeof(buffer);\nconst char *format = \"%d\";\nint value = 12345;\nint result = snprintf(buffer, size, format, value);\nprintf(\"Buffer: %s, Result: %d\\n\", buffer, result);",
        "answer": 5
    }
}
```

#### 1D - 变量赋值 [ Assignment ] (8)

```json
{
    "id": "SL-AS-S001",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "CodeSense",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable x after executing the assignment statement `x = y`?",
        "code": "y = 42\nz = 100\nx = y\nprint(f\"x = {x}\")",
        "answer": 42
    }
}
```

```json
{
    "id": "SL-AS-S002",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "CodeSense",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable a after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 10\nb = 20\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 20
    }
}
```

```json
{
    "id": "SL-AS-S003",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable first after executing the unpacking assignment `first, second, *rest = numbers`?",
        "code": "numbers = [1, 2, 3, 4, 5]\nfirst, second, *rest = numbers\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 1
    }
}
```

```json
{
    "id": "SL-AS-S004",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "CodeSense",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value that *ptr points to after executing the assignment statement `ptr = &value`?",
        "code": "int value = 100;\nint *ptr;\nptr = &value;\nprintf(\"Value: %d, Address: %p\\n\", *ptr, ptr);",
        "answer": 100
    }
}
```

```json
{
    "id": "SL-AS-S005",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable x after executing the chained assignment `x = y = z = 5`?",
        "code": "x = 1\ny = 2\nz = 3\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = 5\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": 5
    }
}
```

```json
{
    "id": "SL-AS-S006",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable count after executing the compound assignment statement `count += increment * 2`?",
        "code": "count = 10\nincrement = 3\nmultiplier = 2\nprint(f\"Initial count: {count}\")\ncount += increment * 2\nprint(f\"Final count: {count}\")",
        "answer": 16
    }
}
```

```json
{
    "id": "SL-AS-S007",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 10\nb = 20\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 10
    }
}
```

```json
{
    "id": "SL-AS-S008",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = numbers`?",
        "code": "numbers = [1, 2, 3, 4, 5]\nfirst, second, *rest = numbers\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 3
    }
}
```

#### 1E - 常量赋值 [Constant ] (5)

```json
{
    "id": "SL-CT-S001",
    "metadata": {
        "name": "StatementLevel-Constant-Seed1",
        "category": "Statement-Level",
        "subcategory": "Constant",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = 42`?",
        "code": "num = 42\nprint(f\"Number: {num}\")\nprint(f\"Type: {type(num)}\")",
        "answer": 42
    }
}
```

```json
{
    "id": "SL-CT-S002",
    "metadata": {
        "name": "StatementLevel-Constant-Seed2",
        "category": "Statement-Level",
        "subcategory": "Constant",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value assigned to variable message in the statement `message = \"Hello, World!\"`?",
        "code": "message = \"Hello, World!\"\nprint(f\"Message: {message}\")\nprint(f\"Length: {len(message)}\")",
        "answer": "Hello, World!"
    }
}
```

```json
{
    "id": "SL-CT-S003",
    "metadata": {
        "name": "StatementLevel-Constant-Seed3",
        "category": "Statement-Level",
        "subcategory": "Constant",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value assigned to variable is_valid in the statement `is_valid = True`?",
        "code": "is_valid = True\nprint(f\"Valid: {is_valid}\")\nprint(f\"Type: {type(is_valid)}\")",
        "answer": true
    }
}
```

```json
{
    "id": "SL-CT-S004",
    "metadata": {
        "name": "StatementLevel-Constant-Seed4",
        "category": "Statement-Level",
        "subcategory": "Constant",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value assigned to variable pi in the statement `pi = 3.14159`?",
        "code": "pi = 3.14159\nradius = 5\narea = pi * radius ** 2\nprint(f\"Pi: {pi}\")\nprint(f\"Area: {area}\")",
        "answer": 3.14159
    }
}
```

```json
{
    "id": "SL-CT-S005",
    "metadata": {
        "name": "StatementLevel-Constant-Seed5",
        "category": "Statement-Level",
        "subcategory": "Constant",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the integer value of the pointer status after executing the statement `status = NULL`?",
        "code": "#include <stdio.h>\nvoid *status = NULL;\nint value = 100;\nif (status == NULL) {\n    printf(\"Status is null\\n\");\n} else {\n    printf(\"Status is not null\\n\");\n}",
        "answer": 0
    }
}
```

#### 1F - 大混合 [ mix ] (2)

```json
{
    "id": "SL-MIX-S001",
    "metadata": {
        "name": "StatementLevel-Mix-Seed1",
        "category": "Statement-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following complex code snippet involving arithmetic operations, boolean logic, API calls, variable assignments, and constants, what is the final value of variable result after executing all statements?",
        "code": "import math\nimport random\n\n# Constants initialization\nPI = 3.14159265359\nMAX_SIZE = 1024\nDEBUG_MODE = True\nERROR_CODE = -1\nSUCCESS_CODE = 0\n\n# Data structures initialization\nnumbers = [15, 42, 87, 23, 91, 56, 34, 78, 12, 65]\nweights = [0.1, 0.2, 0.15, 0.25, 0.3]\nconfig = {'threshold': 50, 'multiplier': 2.5, 'enabled': True}\nmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n\n# Variable assignments and arithmetic operations\ntotal_sum = sum(numbers)\naverage = total_sum / len(numbers)\nmax_value = max(numbers)\nmin_value = min(numbers)\nrange_value = max_value - min_value\n\n# Boolean operations and conditional logic\nis_above_threshold = average > config['threshold']\nis_enabled = config['enabled'] and DEBUG_MODE\nhas_valid_range = range_value > 0 and range_value < MAX_SIZE\n\n# API/Function calls with complex parameters\nsquared_numbers = [x ** 2 for x in numbers if x > min_value]\nfiltered_sum = sum(squared_numbers)\nsqrt_result = math.sqrt(filtered_sum)\nlog_result = math.log10(sqrt_result) if sqrt_result > 0 else 0\n\n# Complex arithmetic with multiple operations\nweighted_score = sum(w * n for w, n in zip(weights, numbers[:len(weights)]))\nnormalized_score = weighted_score / sum(weights)\nbonus_multiplier = config['multiplier'] if is_above_threshold else 1.0\nfinal_score = normalized_score * bonus_multiplier\n\n# Bitwise operations\nflags = 0b1010\nposition = 3\nmask = flags | (1 << position)\ncheck_bit = (mask & (1 << position)) != 0\ntoggled_flags = flags ^ (1 << position)\n\n# String operations and API calls\nstatus_message = \"Processing\" if is_enabled else \"Disabled\"\nmessage_length = len(status_message)\nuppercase_message = status_message.upper()\nreversed_message = status_message[::-1]\n\n# Multiple assignments and tuple unpacking\nfirst, second, *rest = numbers\na, b = b if 'b' in locals() else 10, a if 'a' in locals() else 20\ntemp_x, temp_y, temp_z = 1, 2, 3\ntemp_x, temp_y = temp_y, temp_x  # Swap\n\n# Complex expression evaluation\ncomplex_expr = (final_score * 0.8 + log_result * 0.2) ** 0.5\nrounded_expr = round(complex_expr, 2)\nint_expr = int(complex_expr * 100) % 1000\n\n# Array operations and slicing\nsliced_numbers = numbers[2:8:2]\nreversed_slice = sliced_numbers[::-1]\nsum_slice = sum(reversed_slice)\n\n# Matrix operations\nmatrix_sum = sum(sum(row) for row in matrix)\ndiagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))\nmatrix_flatten = [item for row in matrix for item in row]\n\n# Conditional assignments\nstatus_code = SUCCESS_CODE if all([is_enabled, has_valid_range, check_bit]) else ERROR_CODE\nerror_count = 0 if status_code == SUCCESS_CODE else 1\n\n# Final result calculation combining all elements\nresult = (\n    int_expr + \n    sum_slice + \n    diagonal_sum + \n    (status_code * 100) + \n    error_count + \n    len(rest) + \n    message_length + \n    (toggles_flags if 'toggles_flags' in locals() else toggled_flags)\n) % 10000\n\nprint(f\"Final result: {result}\")",
        "answer": 307
    }
}
```

```json
{
    "id": "SL-MIX-S002",
    "metadata": {
        "name": "StatementLevel-Mix-Seed2",
        "category": "Statement-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Given the following comprehensive C code snippet involving memory management, pointer arithmetic, struct operations, bit manipulation, and complex calculations, what is the final value stored in result->final_value?",
        "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <math.h>\n#include <time.h>\n\n#define MAX_BUFFER_SIZE 256\n#define MAGIC_NUMBER 0xDEADBEEF\n#define SUCCESS 0\n#define FAILURE -1\n#define PI 3.14159265359\n#define E 2.71828182846\n\ntypedef struct {\n    int id;\n    double value;\n    char name[32];\n    int flags;\n    void *data;\n} DataNode;\n\ntypedef struct {\n    DataNode *nodes;\n    int count;\n    int capacity;\n    double average;\n    int final_value;\n} ResultSet;\n\n// Function prototypes\nint calculate_hash(const char *str);\ndouble compute_statistics(int *array, int size);\nint validate_data(const DataNode *node);\n\nint main() {\n    // Memory allocation and initialization\n    ResultSet *result = (ResultSet *)malloc(sizeof(ResultSet));\n    if (!result) return FAILURE;\n    \n    result->capacity = 10;\n    result->nodes = (DataNode *)calloc(result->capacity, sizeof(DataNode));\n    if (!result->nodes) {\n        free(result);\n        return FAILURE;\n    }\n    \n    // Constants and variables initialization\n    const int PRIME_NUMBERS[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};\n    const double COEFFICIENTS[] = {1.5, 2.3, 0.8, 1.2, 3.1};\n    int data_array[20] = {0};\n    char buffer[MAX_BUFFER_SIZE];\n    unsigned int seed = 12345;\n    \n    // Initialize data array with computed values\n    for (int i = 0; i < 20; i++) {\n        data_array[i] = (PRIME_NUMBERS[i % 10] * (i + 1)) % 100;\n    }\n    \n    // Node initialization with complex operations\n    result->count = 5;\n    for (int i = 0; i < result->count; i++) {\n        DataNode *node = &result->nodes[i];\n        \n        // ID calculation with bit operations\n        node->id = (MAGIC_NUMBER >> (i * 4)) & 0xFF;\n        \n        // Value calculation with mathematical functions\n        node->value = sin(i * PI / 4) * cos(i * PI / 6) * COEFFICIENTS[i];\n        node->value += sqrt(data_array[i * 2] + data_array[i * 2 + 1]);\n        node->value = round(node->value * 1000) / 1000.0;\n        \n        // Name generation and string operations\n        snprintf(node->name, sizeof(node->name), \"Node_%d_%X\", i, node->id);\n        \n        // Flags computation with bitwise operations\n        node->flags = 0;\n        if (node->value > 0) node->flags |= (1 << 0);  // Positive flag\n        if (node->id % 2 == 0) node->flags |= (1 << 1); // Even ID flag\n        if (strlen(node->name) > 8) node->flags |= (1 << 2); // Long name flag\n        \n        // Conditional memory allocation\n        if (validate_data(node)) {\n            node->data = malloc(sizeof(double) * 10);\n            if (node->data) {\n                double *data_ptr = (double *)node->data;\n                for (int j = 0; j < 10; j++) {\n                    data_ptr[j] = node->value * (j + 1) + COEFFICIENTS[j % 5];\n                }\n            }\n        } else {\n            node->data = NULL;\n        }\n    }\n    \n    // Statistical calculations\n    double sum = 0.0;\n    int valid_count = 0;\n    int hash_sum = 0;\n    \n    for (int i = 0; i < result->count; i++) {\n        DataNode *node = &result->nodes[i];\n        \n        if (node->data != NULL) {\n            sum += node->value;\n            valid_count++;\n            hash_sum += calculate_hash(node->name);\n        }\n    }\n    \n    // Average calculation with error handling\n    result->average = (valid_count > 0) ? (sum / valid_count) : 0.0;\n    \n    // Complex final value computation\n    int temp_value = 0;\n    \n    // Add statistical components\n    temp_value += (int)(result->average * 100);\n    temp_value += hash_sum % 1000;\n    temp_value += valid_count * 50;\n    \n    // Add array statistics\n    double array_stats = compute_statistics(data_array, 20);\n    temp_value += (int)(array_stats * 10);\n    \n    // Add bit manipulation results\n    unsigned int combined_flags = 0;\n    for (int i = 0; i < result->count; i++) {\n        combined_flags ^= result->nodes[i].flags;\n    }\n    temp_value += combined_flags;\n    \n    // Add prime number operations\n    int prime_sum = 0;\n    for (int i = 0; i < 10; i++) {\n        prime_sum += PRIME_NUMBERS[i];\n    }\n    temp_value += (prime_sum % 256);\n    \n    // Memory pattern analysis\n    int memory_pattern = 0;\n    for (int i = 0; i < result->count; i++) {\n        if (result->nodes[i].data != NULL) {\n            memory_pattern += (int)((uintptr_t)result->nodes[i].data & 0xFF);\n        }\n    }\n    temp_value += (memory_pattern % 128);\n    \n    // String operations contribution\n    strcpy(buffer, \"ResultCalculation\");\n    int str_contrib = strlen(buffer);\n    for (int i = 0; buffer[i]; i++) {\n        str_contrib += (int)buffer[i];\n    }\n    temp_value += (str_contrib % 512);\n    \n    // Final modular arithmetic\n    result->final_value = temp_value % 9999;\n    \n    // Cleanup memory\n    for (int i = 0; i < result->count; i++) {\n        if (result->nodes[i].data) {\n            free(result->nodes[i].data);\n        }\n    }\n    free(result->nodes);\n    \n    printf(\"Final value: %d\\n\", result->final_value);\n    int return_value = result->final_value;\n    free(result);\n    \n    return return_value;\n}\n\n// Helper function implementations\nint calculate_hash(const char *str) {\n    unsigned int hash = 5381;\n    int c;\n    while ((c = *str++)) {\n        hash = ((hash << 5) + hash) + c;\n    }\n    return hash % 1000;\n}\n\ndouble compute_statistics(int *array, int size) {\n    if (!array || size <= 0) return 0.0;\n    \n    int sum = 0;\n    int max_val = array[0];\n    int min_val = array[0];\n    \n    for (int i = 0; i < size; i++) {\n        sum += array[i];\n        if (array[i] > max_val) max_val = array[i];\n        if (array[i] < min_val) min_val = array[i];\n    }\n    \n    double mean = (double)sum / size;\n    double variance = 0.0;\n    \n    for (int i = 0; i < size; i++) {\n        variance += (array[i] - mean) * (array[i] - mean);\n    }\n    variance /= size;\n    \n    return sqrt(variance) + (max_val - min_val) * 0.1;\n}\n\nint validate_data(const DataNode *node) {\n    if (!node) return 0;\n    return (node->id > 0 && node->value >= -1000.0 && node->value <= 1000.0);\n}",
        "answer": 2875
    }
}
```

### 2 -  代码块级推理 [ Block-Level ] (24)

#### 2A - 线性代码块 [ Linear ]（6）

```json
{
    "id": "BL-LN-S001",
    "metadata": {
        "name": "BlockLevel-Linear-Sequential",
        "category": "Block-Level",
        "subcategory": "Linear",
        "type": "seed",
        "source": "CodeSense-krb5",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following sequential code block, what is the final value of buf->len after executing all statements?",
        "code": "void k5_buf_init_dynamic(struct k5buf *buf) {\n    buf->buftype = K5BUF_DYNAMIC;\n    buf->space = 128;\n    buf->data = malloc(buf->space);\n    if (buf->data == NULL) {\n        set_error(buf);\n        return;\n    }\n    buf->len = 0;\n}",
        "answer": 0
    }
}
```

```json
{
    "id": "BL-LN-S002",
    "metadata": {
        "name": "BlockLevel-Linear-Independent",
        "category": "Block-Level",
        "subcategory": "Linear",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following independent statements block, what is the final value of max_retries?",
        "code": "max_retries = 3\ntimeout_seconds = 30.0\nlog_level = 'INFO'\nis_debug = False\ndefault_encoding = 'utf-8'",
        "answer": 3
    }
}
```

```json
{
    "id": "BL-LN-S003",
    "metadata": {
        "name": "BlockLevel-Linear-Dependent",
        "category": "Block-Level",
        "subcategory": "Linear",
        "type": "seed",
        "source": "CodeSense-util-linux",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following dependent statements block, what is the return value when blkid_do_safeprobe returns 0?",
        "code": "static int process_file(const char *name) {\n    int rc = -1;\n    blkid_probe pr = blkid_new_probe_from_filename(name);\n    if (pr != NULL) {\n        blkid_probe_enable_partitions(pr, TRUE);\n        rc = blkid_do_safeprobe(pr) == -1 ? -1 : 0;\n    }\n    blkid_free_probe(pr);\n    return rc;\n}",
        "answer": 0
    }
}
```

```json
{
    "id": "BL-LN-S004",
    "metadata": {
        "name": "BlockLevel-Linear-Chain",
        "category": "Block-Level",
        "subcategory": "Linear",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following calculation chain, what is the final value of result?",
        "code": "base = 10\nmultiplier = 3\noffset = 5\ntemp = base * multiplier\nresult = temp + offset\nprint(f\"Final result: {result}\")",
        "answer": 35
    }
}
```

```json
{
    "id": "BL-LN-S005",
    "metadata": {
        "name": "BlockLevel-Linear-Accumulation",
        "category": "Block-Level",
        "subcategory": "Linear",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following accumulation block, what is the final value of total?",
        "code": "int total = 0;\ntotal += 10;\ntotal += 15;\ntotal += 7;\ntotal *= 2;\nprintf(\"Total: %d\\n\", total);",
        "answer": 64
    }
}
```

```json
{
    "id": "BL-LN-S006",
    "metadata": {
        "name": "BlockLevel-Linear-Transform",
        "category": "Block-Level",
        "subcategory": "Linear",
        "type": "seed",
        "source": "CodeSense-tmux",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following data transformation block, what is the final value of s->ccolour?",
        "code": "void screen_init(struct screen *s, u_int sx, u_int sy, u_int hlimit) {\n    s->grid = grid_create(sx, sy, hlimit);\n    s->saved_grid = NULL;\n    s->cstyle = SCREEN_CURSOR_DEFAULT;\n    s->default_cstyle = SCREEN_CURSOR_DEFAULT;\n    s->ccolour = -1;\n    s->default_ccolour = -1;\n}",
        "answer": -1
    }
}
```

#### 2B - 条件代码块 [ Conditional ] (8)

```json
{
    "id": "BL-CD-S001",
    "metadata": {
        "name": "BlockLevel-Conditional-SimpleIf",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "CodeSense-cryptsetup",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following conditional block where sysconf returns 4096, what is the return value?",
        "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else {\n        return (size_t)r;\n    }\n}",
        "answer": 4096
    }
}
```

```json
{
    "id": "BL-CD-S002",
    "metadata": {
        "name": "BlockLevel-Conditional-NestedIf",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following nested conditional block where score is 85, what is the final value of grade?",
        "code": "score = 85\nif score >= 90:\n    if score >= 95:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80:\n        grade = 'B'\n    else:\n        grade = 'C'\nprint(f\"Grade: {grade}\")",
        "answer": "B"
    }
}
```

```json
{
    "id": "BL-CD-S003",
    "metadata": {
        "name": "BlockLevel-Conditional-ElseIf",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following else-if chain where value is 15, what is the final value of category?",
        "code": "int value = 15;\nchar *category;\nif (value < 10) {\n    category = \"low\";\n} else if (value < 20) {\n    category = \"medium\";\n} else if (value < 30) {\n    category = \"high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
        "answer": "medium"
    }
}
```

```json
{
    "id": "BL-CD-S004",
    "metadata": {
        "name": "BlockLevel-Conditional-Switch",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following switch block where day is 3, what is the final value of day_name?",
        "code": "int day = 3;\nchar *day_name;\nswitch (day) {\n    case 1: day_name = \"Monday\"; break;\n    case 2: day_name = \"Tuesday\"; break;\n    case 3: day_name = \"Wednesday\"; break;\n    case 4: day_name = \"Thursday\"; break;\n    case 5: day_name = \"Friday\"; break;\n    default: day_name = \"Weekend\";\n}\nprintf(\"Day: %s\\n\", day_name);",
        "answer": "Wednesday"
    }
}
```

```json
{
    "id": "BL-CD-S005",
    "metadata": {
        "name": "BlockLevel-Conditional-SwitchFallthrough",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following switch block with fallthrough where input is 2, what is the final value of flags?",
        "code": "int input = 2;\nint flags = 0;\nswitch (input) {\n    case 1:\n        flags |= 0x01;\n    case 2:\n        flags |= 0x02;\n    case 3:\n        flags |= 0x04;\n        break;\n    default:\n        flags = -1;\n}\nprintf(\"Flags: 0x%02X\\n\", flags);",
        "answer": 6
    }
}
```

```json
{
    "id": "BL-CD-S006",
    "metadata": {
        "name": "BlockLevel-Conditional-TernaryChain",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following ternary conditional chain where x is 7 and y is 5, what is the final value of result?",
        "code": "int x = 7, y = 5;\nint result = (x > y) ? ((x % 2 == 0) ? x * 2 : x + 10) : ((y % 2 == 0) ? y * 3 : y - 2);\nprintf(\"Result: %d\\n\", result);",
        "answer": 17
    }
}
```

```json
{
    "id": "BL-CD-S007",
    "metadata": {
        "name": "BlockLevel-Conditional-NullCheck",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "CodeSense-libssh",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following null check block where malloc succeeds, what is the final value of ptr after the block execution?",
        "code": "ssh_poll_handle ssh_poll_new(socket_t fd, short events) {\n    ssh_poll_handle p;\n    p = malloc(sizeof(struct ssh_poll_handle_struct));\n    if (p == NULL) {\n        return NULL;\n    }\n    p->x.fd = fd;\n    p->events = events;\n    return p;\n}",
        "answer": "valid_pointer"
    }
}
```

```json
{
    "id": "BL-CD-S008",
    "metadata": {
        "name": "BlockLevel-Conditional-ComplexLogic",
        "category": "Block-Level",
        "subcategory": "Conditional",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Given the following complex conditional logic where age is 25, income is 50000, and has_degree is True, what is the final value of status?",
        "code": "age = 25\nincome = 50000\nhas_degree = True\nstatus = None\n\nif age >= 18 and age <= 65:\n    if income > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
        "answer": "approved_premium"
    }
}
```

#### 2C - 迭代代码块 [ Iterative ] (8)

```json
{
    "id": "BL-IT-S001",
    "metadata": {
        "name": "BlockLevel-Iterative-SimpleFor",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following simple for loop block, what is the final value of sum?",
        "code": "int sum = 0;\nfor (int i = 1; i <= 5; i++) {\n    sum += i;\n}\nprintf(\"Sum: %d\\n\", sum);",
        "answer": 15
    }
}
```

```json
{
    "id": "BL-IT-S002",
    "metadata": {
        "name": "BlockLevel-Iterative-ArrayInit",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "CodeSense-apache-httpd",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following array initialization loop where GB_SIZE is 5, what is the value of pointer_arr[3] after execution?",
        "code": "void af_gb_init() {\n    pointer_idx = 0;\n    for (int i = 0; i < GB_SIZE; i++) {\n        pointer_arr[i] = NULL;\n    }\n}",
        "answer": "NULL"
    }
}
```

```json
{
    "id": "BL-IT-S003",
    "metadata": {
        "name": "BlockLevel-Iterative-WhileLoop",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following while loop block where initial value is 16, what is the final value of count?",
        "code": "int value = 16;\nint count = 0;\nwhile (value > 1) {\n    value = value / 2;\n    count++;\n}\nprintf(\"Count: %d\\n\", count);",
        "answer": 4
    }
}
```

```json
{
    "id": "BL-IT-S004",
    "metadata": {
        "name": "BlockLevel-Iterative-NestedLoop",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following nested loop block, what is the final value of total?",
        "code": "total = 0\nfor i in range(3):\n    for j in range(2):\n        total += (i + 1) * (j + 1)\nprint(f\"Total: {total}\")",
        "answer": 18
    }
}
```

```json
{
    "id": "BL-IT-S005",
    "metadata": {
        "name": "BlockLevel-Iterative-BreakContinue",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Given the following loop with break and continue, what is the final value of sum?",
        "code": "int sum = 0;\nfor (int i = 1; i <= 10; i++) {\n    if (i % 2 == 0) {\n        continue;\n    }\n    if (i > 7) {\n        break;\n    }\n    sum += i;\n}\nprintf(\"Sum: %d\\n\", sum);",
        "answer": 16
    }
}
```

```json
{
    "id": "BL-IT-S006",
    "metadata": {
        "name": "BlockLevel-Iterative-DoWhile",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following do-while loop where initial n is 0, what is the final value of n?",
        "code": "int n = 0;\ndo {\n    n += 3;\n} while (n < 10);\nprintf(\"n: %d\\n\", n);",
        "answer": 12
    }
}
```

```json
{
    "id": "BL-IT-S007",
    "metadata": {
        "name": "BlockLevel-Iterative-RecursiveFunction",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Given the following recursive function call factorial(4), what is the return value?",
        "code": "int factorial(int n) {\n    if (n <= 1) {\n        return 1;\n    }\n    return n * factorial(n - 1);\n}\n\nint result = factorial(4);\nprintf(\"Result: %d\\n\", result);",
        "answer": 24
    }
}
```

```json
{
    "id": "BL-IT-S008",
    "metadata": {
        "name": "BlockLevel-Iterative-ComplexAccumulation",
        "category": "Block-Level",
        "subcategory": "Iterative",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Given the following complex iterative accumulation with filtering, what is the final value of result?",
        "code": "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nresult = 0\nmultiplier = 1\n\nfor num in numbers:\n    if num % 2 == 0:\n        result += num * multiplier\n        multiplier += 1\n    else:\n        result -= num\n        \nprint(f\"Result: {result}\")",
        "answer": 15
    }
}
```

#### 2D - 大混合 (2)

```json
{
    "id": "BL-MIX-S001",
    "metadata": {
        "name": "BlockLevel-Mix-Comprehensive",
        "category": "Block-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Given the following comprehensive block mixing linear, conditional, and iterative patterns, what is the final value of status_code?",
        "code": "int process_data_batch(int *data, int size) {\n    // Linear initialization\n    int processed = 0;\n    int errors = 0;\n    int status_code = 0;\n    \n    // Conditional validation\n    if (data == NULL || size <= 0) {\n        return -1;\n    }\n    \n    // Iterative processing with nested conditions\n    for (int i = 0; i < size; i++) {\n        if (data[i] < 0) {\n            errors++;\n            continue;\n        }\n        \n        // Linear computation\n        data[i] = data[i] * 2 + 1;\n        processed++;\n        \n        // Conditional break\n        if (errors > size / 2) {\n            status_code = -2;\n            break;\n        }\n    }\n    \n    // Final conditional status\n    if (status_code == 0) {\n        status_code = (processed > 0) ? 1 : 0;\n    }\n    \n    return status_code;\n}\n\n// Test case\nint test_data[] = {1, 2, 3, 4, 5};\nint result = process_data_batch(test_data, 5);",
        "answer": 1
    }
}
```

```json
{
    "id": "BL-MIX-S002",
    "metadata": {
        "name": "BlockLevel-Mix-RealWorld",
        "category": "Block-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "CodeSense-libssh",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Given the following real-world configuration parsing block, what is the final value of parser_flags when input contains 3 lines?",
        "code": "int ssh_bind_config_parse_string(ssh_bind bind, const char *input) {\n    char line[MAX_LINE_SIZE] = {0};\n    const char *c = input, *line_start = input;\n    unsigned int line_num = 0, line_len;\n    uint32_t parser_flags;\n    int rv;\n    \n    // Linear initialization\n    uint8_t seen[BIND_CFG_MAX] = {0};\n    parser_flags = PARSING;\n    \n    // Iterative line processing\n    while (1) {\n        line_num++;\n        line_start = c;\n        c = strchr(line_start, '\\n');\n        \n        // Conditional end detection\n        if (c == NULL) {\n            c = strchr(line_start, '\\0');\n        }\n        if (c == NULL) {\n            return SSH_ERROR;\n        }\n        \n        // Linear line processing\n        line_len = c - line_start;\n        if (line_len > MAX_LINE_SIZE - 1) {\n            return SSH_ERROR;\n        }\n        \n        // Process line\n        memcpy(line, line_start, line_len);\n        line[line_len] = '\\0';\n        \n        // Conditional parsing\n        rv = ssh_bind_config_parse_line(bind, line, line_num, &parser_flags, seen, 0);\n        if (rv < 0) {\n            return SSH_ERROR;\n        }\n        \n        // Break condition\n        if (*c == '\\0') {\n            break;\n        }\n        c++;\n    }\n    \n    return SSH_OK;\n}\n\n// Assuming input has 3 valid lines and PARSING = 1\nconst char *test_input = \"line1\\nline2\\nline3\";\nint result = ssh_bind_config_parse_string(NULL, test_input);",
        "answer": 0
    }
}
```

### 3 - 代码属性推理 [ Property-Level ] (27)

#### 3A - 循环属性 [ Loop ] （6）

> （迭代计数、变量追踪、终止条件）

```json
{
    "id": "PL-LP-S001",
    "metadata": {
        "name": "PropertyLevel-Loop-IterationCount",
        "category": "Property-Level",
        "subcategory": "Loop",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following nested loop structure, how many total iterations will the inner loop execute across all outer loop iterations?",
        "code": "int total_iterations = 0;\nfor (int i = 1; i <= 4; i++) {\n    for (int j = i; j <= 6; j++) {\n        total_iterations++;\n        printf(\"i=%d, j=%d\\n\", i, j);\n    }\n}\nprintf(\"Total inner iterations: %d\\n\", total_iterations);",
        "answer": 18
    }
}
```

```JSON
{
    "id": "PL-LP-S002",
    "metadata": {
        "name": "PropertyLevel-Loop-VariableTracking",
        "category": "Property-Level",
        "subcategory": "Loop",
        "type": "seed",
        "source": "CodeSense-openssl",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "In this loop that processes a buffer, trace the evolution of variable 'remaining' - what is its value at the start of the 3rd iteration?",
        "code": "int process_buffer(unsigned char *buf, int len) {\n    int remaining = len;\n    int processed = 0;\n    int chunk_size;\n    \n    while (remaining > 0) {\n        chunk_size = (remaining > 64) ? 64 : remaining;\n        processed += chunk_size;\n        remaining -= chunk_size;\n        printf(\"Iteration: processed=%d, remaining=%d\\n\", processed, remaining);\n    }\n    return processed;\n}\n\n// Called with len = 200\nint result = process_buffer(buffer, 200);",
        "answer": 72
    }
}
```

```json
{
    "id": "PL-LP-S003",
    "metadata": {
        "name": "PropertyLevel-Loop-TerminationCondition",
        "category": "Property-Level",
        "subcategory": "Loop",
        "type": "seed",
        "source": "CodeSense-tmux",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Analyze this loop's termination condition - given the initial state, on which iteration number will the loop terminate?",
        "code": "int find_convergence(double initial_value) {\n    double x = initial_value;\n    double prev_x;\n    int iteration = 0;\n    double tolerance = 0.01;\n    \n    do {\n        prev_x = x;\n        x = (x + 2.0/x) / 2.0;  // Newton's method for sqrt(2)\n        iteration++;\n        printf(\"Iteration %d: x = %.6f, diff = %.6f\\n\", iteration, x, fabs(x - prev_x));\n    } while (fabs(x - prev_x) >= tolerance && iteration < 10);\n    \n    return iteration;\n}\n\n// Called with initial_value = 1.0\nint result = find_convergence(1.0);",
        "answer": 4
    }
}
```

```json
{
    "id": "PL-LP-S004",
    "metadata": {
        "name": "PropertyLevel-Loop-ConditionalCounting",
        "category": "Property-Level",
        "subcategory": "Loop",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "In this loop with conditional processing, how many times is the variable 'special_count' incremented?",
        "code": "numbers = [1, 7, 3, 14, 8, 21, 5, 28, 9, 35]\nspecial_count = 0\nsum_special = 0\n\nfor i, num in enumerate(numbers):\n    if num % 7 == 0:  # Multiples of 7\n        special_count += 1\n        sum_special += num\n        print(f\"Found special number {num} at index {i}\")\n    elif num > 10:\n        print(f\"Large number {num} at index {i}\")\n        \nprint(f\"Special count: {special_count}, Sum: {sum_special}\")",
        "answer": 4
    }
}
```

```json
{
    "id": "PL-LP-S005",
    "metadata": {
        "name": "PropertyLevel-Loop-AccumulatorPattern",
        "category": "Property-Level",
        "subcategory": "Loop",
        "type": "seed",
        "source": "CodeSense-postgresql",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Track the accumulator variable 'hash' through this hash computation loop - what is its value after processing the 4th character?",
        "code": "unsigned int compute_hash(const char *str) {\n    unsigned int hash = 5381;\n    int c;\n    int pos = 0;\n    \n    while ((c = str[pos]) != '\\0') {\n        hash = ((hash << 5) + hash) + c;  // hash * 33 + c\n        pos++;\n        printf(\"After char '%c': hash = %u\\n\", c, hash);\n    }\n    \n    return hash;\n}\n\n// Called with str = \"test\"\nunsigned int result = compute_hash(\"test\");",
        "answer": 6385719596
    }
}
```

```json
{
    "id": "PL-LP-S006",
    "metadata": {
        "name": "PropertyLevel-Loop-MultipleExitConditions",
        "category": "Property-Level",
        "subcategory": "Loop",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "This loop has multiple exit conditions. Given the input array, which specific condition will cause the loop to terminate and on which iteration?",
        "code": "int search_with_conditions(int *arr, int size) {\n    int iterations = 0;\n    int sum = 0;\n    int found_target = 0;\n    \n    for (int i = 0; i < size; i++) {\n        iterations++;\n        sum += arr[i];\n        \n        // Condition 1: Found target value\n        if (arr[i] == 42) {\n            found_target = 1;\n            printf(\"Found target at iteration %d\\n\", iterations);\n            break;\n        }\n        \n        // Condition 2: Sum exceeds threshold\n        if (sum > 100) {\n            printf(\"Sum exceeded at iteration %d (sum=%d)\\n\", iterations, sum);\n            break;\n        }\n        \n        // Condition 3: Maximum iterations\n        if (iterations >= 8) {\n            printf(\"Max iterations reached\\n\");\n            break;\n        }\n    }\n    \n    return iterations;\n}\n\n// Test array: [15, 25, 30, 20, 35, 42, 10, 5]\nint test_arr[] = {15, 25, 30, 20, 35, 42, 10, 5};\nint result = search_with_conditions(test_arr, 8);",
        "answer": 4
    }
}
```

#### 3B - 分支属性 [ Branch ] （7）

> （条件求值、路径选择、分支效果）

```json
{
    "id": "PL-BR-S001",
    "metadata": {
        "name": "PropertyLevel-Branch-ConditionEvaluation",
        "category": "Property-Level",
        "subcategory": "Branch",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the specific input values, determine which branch path is taken and what value is returned.",
        "code": "int evaluate_condition(int a, int b, int c) {\n    if (a > 10 && b < 5) {\n        return 1;\n    } else if (a <= 10 && c > 0) {\n        return 2;\n    } else {\n        return 3;\n    }\n}\n// What value is returned when called with evaluate_condition(8, 6, 4)?",
        "answer": 2
    }
}
```

```JSON
{
    "id": "PL-BR-S002",
    "metadata": {
        "name": "PropertyLevel-Branch-ShortCircuit",
        "category": "Property-Level",
        "subcategory": "Branch",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Analyze short-circuit evaluation. How many function calls are actually executed?",
        "code": "int call_count = 0;\nint func_a() { call_count++; return 0; }\nint func_b() { call_count++; return 1; }\nint func_c() { call_count++; return 1; }\n\nint result = func_a() && func_b() && func_c();\n// What is the value of call_count after this expression?",
        "answer": 1
    }
}
```

```json
{
    "id": "PL-BR-S003",
    "metadata": {
        "name": "PropertyLevel-Branch-NestedTernary",
        "category": "Property-Level",
        "subcategory": "Branch",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Evaluate the nested ternary expression with the given values.",
        "code": "int x = 7, y = 3, z = 5;\nint result = (x > y) ? ((z % 2 == 1) ? x + z : x - z) : ((y > z) ? y * 2 : y + z);\n// What is the value of result?",
        "answer": 12
    }
}
```

```json
{
    "id": "PL-BR-S004",
    "metadata": {
        "name": "PropertyLevel-Branch-SwitchFallthrough",
        "category": "Property-Level",
        "subcategory": "Branch",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Calculate the final value considering switch statement fallthrough behavior.",
        "code": "int value = 0;\nint input = 2;\nswitch (input) {\n    case 1: value += 10;\n    case 2: value += 20;\n    case 3: value += 30;\n        break;\n    case 4: value += 40;\n        break;\n    default: value = -1;\n}\n// What is the final value of 'value'?",
        "answer": 50
    }
}
```

```json
{
    "id": "PL-BR-S005",
    "metadata": {
        "name": "PropertyLevel-Branch-ConditionalModification",
        "category": "Property-Level",
        "subcategory": "Branch",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Track variable modification through conditional branches.",
        "code": "x = 10\nif x > 5:\n    x = x * 2\nif x > 15:\n    x = x + 5\nif x < 30:\n    x = x - 3\n# What is the final value of x?",
        "answer": 22
    }
}
```

```json
{
    "id": "PL-BR-S006",
    "metadata": {
        "name": "PropertyLevel-Branch-MultipleConditions",
        "category": "Property-Level",
        "subcategory": "Branch",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Determine the final output value based on multiple conditional checks.",
        "code": "int process_value(int n) {\n    int result = n;\n    if (n % 2 == 0) result += 5;\n    if (n % 3 == 0) result *= 2;\n    if (n % 5 == 0) result -= 10;\n    return result;\n}\n// What value is returned when called with process_value(12)?",
        "answer": 34
    }
}
```

```json
{
    "id": "PL-BR-S007",
    "metadata": {
        "name": "PropertyLevel-Branch-CompoundLogic",
        "category": "Property-Level",
        "subcategory": "Branch",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Evaluate complex compound logical expression and determine the final boolean result.",
        "code": "int a = 5, b = 8, c = 3;\nint result = ((a < b) && (b > c)) || ((a + c) == b) && !(a > c * 2);\n// What is the value of result (1 for true, 0 for false)?",
        "answer": 1
    }
}
```

#### 3C - 内存属性 [ Memory ] （6）

> （引用关系、生命周期、访问模式）

```json
{
    "id": "PL-MEM-S001",
    "metadata": {
        "name": "PropertyLevel-Memory-PointerArithmetic",
        "category": "Property-Level",
        "subcategory": "Memory",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Calculate the final value accessed through pointer arithmetic.",
        "code": "int arr[5] = {10, 20, 30, 40, 50};\nint *ptr = arr + 2;\nptr++;\nint value = *ptr;\n// What is the value of 'value'?",
        "answer": 40
    }
}
```

```json
{
    "id": "PL-MEM-S002",
    "metadata": {
        "name": "PropertyLevel-Memory-ArrayModification",
        "category": "Property-Level",
        "subcategory": "Memory",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Determine the array element value after pointer-based modification.",
        "code": "int data[4] = {1, 2, 3, 4};\nint *p1 = &data[1];\nint *p2 = &data[2];\n*p1 = *p2 + 5;\n*p2 = *p1 * 2;\n// What is the value of data[2] after these operations?",
        "answer": 16
    }
}
```

```json
{
    "id": "PL-MEM-S003",
    "metadata": {
        "name": "PropertyLevel-Memory-StructAccess",
        "category": "Property-Level",
        "subcategory": "Memory",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Calculate the final struct member value after pointer operations.",
        "code": "typedef struct { int x; int y; } Point;\nPoint points[3] = {{1, 2}, {3, 4}, {5, 6}};\nPoint *ptr = points + 1;\nptr->x = ptr->x + points[0].y;\nptr->y = ptr->y * 2;\n// What is the value of points[1].x after these operations?",
        "answer": 5
    }
}
```

```json
{
    "id": "PL-MEM-S004",
    "metadata": {
        "name": "PropertyLevel-Memory-IndirectAccess",
        "category": "Property-Level",
        "subcategory": "Memory",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Trace through multiple levels of indirection to find the final value.",
        "code": "int value = 100;\nint *ptr1 = &value;\nint **ptr2 = &ptr1;\nint ***ptr3 = &ptr2;\n**ptr2 = **ptr2 + 50;\n// What is the value of 'value' after this operation?",
        "answer": 150
    }
}
```

```json
{
    "id": "PL-MEM-S005",
    "metadata": {
        "name": "PropertyLevel-Memory-ArrayCopy",
        "category": "Property-Level",
        "subcategory": "Memory",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Determine array contents after memory copy operations.",
        "code": "int source[5] = {1, 2, 3, 4, 5};\nint dest[5] = {0, 0, 0, 0, 0};\nfor (int i = 0; i < 3; i++) {\n    dest[i + 1] = source[i] * 2;\n}\n// What is the value of dest[3]?",
        "answer": 6
    }
}
```

```json
{
    "id": "PL-MEM-S006",
    "metadata": {
        "name": "PropertyLevel-Memory-OverlappingAccess",
        "category": "Property-Level",
        "subcategory": "Memory",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Calculate the result of overlapping memory access patterns.",
        "code": "int buffer[6] = {10, 20, 30, 40, 50, 60};\nint *p1 = buffer + 1;\nint *p2 = buffer + 3;\nfor (int i = 0; i < 2; i++) {\n    p1[i] = p2[i] + p1[i];\n}\n// What is the value of buffer[2] after the loop?",
        "answer": 70
    }
}
```

#### 3D - 作用域属性 [ Scope ]（6）

> （可见性、生存期、变量遮蔽）

```json
{
    "id": "PL-SC-S001",
    "metadata": {
        "name": "PropertyLevel-Scope-VariableShadowing",
        "category": "Property-Level",
        "subcategory": "Scope",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Determine which variable value is accessed in the innermost scope.",
        "code": "int x = 10;\nvoid test_scope() {\n    int x = 20;\n    {\n        int x = 30;\n        printf(\"%d\", x);\n    }\n}\n// What value is printed by the printf statement?",
        "answer": 30
    }
}
```

```JSON
{
    "id": "PL-SC-S002",
    "metadata": {
        "name": "PropertyLevel-Scope-StaticVariable",
        "category": "Property-Level",
        "subcategory": "Scope",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Calculate the static variable value after multiple function calls.",
        "code": "int get_count() {\n    static int count = 0;\n    count += 5;\n    return count;\n}\n// What value is returned by the third call to get_count()?",
        "answer": 15
    }
}
```

```json
{
    "id": "PL-SC-S003",
    "metadata": {
        "name": "PropertyLevel-Scope-BlockVariable",
        "category": "Property-Level",
        "subcategory": "Scope",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Determine the variable value after exiting the block scope.",
        "code": "int value = 5;\n{\n    int value = 10;\n    value *= 2;\n}\nvalue += 3;\n// What is the final value of the outer 'value' variable?",
        "answer": 8
    }
}
```

```json
{
    "id": "PL-SC-S004",
    "metadata": {
        "name": "PropertyLevel-Scope-GlobalModification",
        "category": "Property-Level",
        "subcategory": "Scope",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Track global variable modification across function calls.",
        "code": "int global_var = 0;\nvoid modify_global(int increment) {\n    global_var += increment;\n}\nvoid test_function() {\n    modify_global(5);\n    modify_global(3);\n    modify_global(-2);\n}\n// What is the value of global_var after calling test_function()?",
        "answer": 6
    }
}
```

```json
{
    "id": "PL-SC-S005",
    "metadata": {
        "name": "PropertyLevel-Scope-ParameterShadowing",
        "category": "Property-Level",
        "subcategory": "Scope",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Determine the final return value considering parameter shadowing.",
        "code": "int x = 100;\nint calculate(int x) {\n    x = x * 2;\n    {\n        int x = 50;\n        x += 10;\n    }\n    return x;\n}\n// What value is returned by calculate(15)?",
        "answer": 30
    }
}
```

```json
{
    "id": "PL-SC-S006",
    "metadata": {
        "name": "PropertyLevel-Scope-NestedFunctions",
        "category": "Property-Level",
        "subcategory": "Scope",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Calculate the final value considering nested function scopes and closures.",
        "code": "def outer_function(x):\n    def inner_function():\n        nonlocal x\n        x = x * 2\n        return x\n    \n    result = inner_function()\n    x = x + 5\n    return x\n\n# What value is returned by outer_function(10)?",
        "answer": 25
    }
}
```

#### 3E - 大混合（2）

```json
{
    "id": "PL-MIX-S001",
    "metadata": {
        "name": "PropertyLevel-Mix-Comprehensive",
        "category": "Property-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Comprehensive analysis combining loops, branches, memory, and scope. What is the final value of result?",
        "code": "int global_counter = 0;\n\nint process_array() {\n    int arr[4] = {2, 4, 6, 8};\n    int *ptr = arr;\n    int result = 0;\n    \n    for (int i = 0; i < 4; i++) {\n        global_counter++;\n        \n        if (arr[i] % 4 == 0) {\n            *ptr = *ptr * 2;\n            result += *ptr;\n        } else {\n            result += arr[i];\n        }\n        \n        ptr++;\n    }\n    \n    {\n        int local_var = global_counter;\n        result = result + local_var;\n    }\n    \n    return result;\n}\n\n// What is the return value of process_array()?",
        "answer": 50
    }
}
```

```json
{
    "id": "PL-MIX-S002",
    "metadata": {
        "name": "PropertyLevel-Mix-Complex",
        "category": "Property-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "master",
        "intervention": 4
    },
    "task": {
        "description": "Complex property interaction analysis. What is the final value stored at memory location pointed to by final_ptr?",
        "code": "static int static_var = 10;\n\nint complex_operations() {\n    int data[5] = {1, 2, 3, 4, 5};\n    int *ptr1 = data + 1;\n    int *ptr2 = data + 3;\n    int *final_ptr;\n    \n    for (int i = 0; i < 3; i++) {\n        static_var++;\n        \n        if (i % 2 == 0) {\n            *ptr1 = *ptr1 + static_var;\n            final_ptr = ptr1;\n        } else {\n            *ptr2 = *ptr2 * 2;\n            final_ptr = ptr2;\n        }\n        \n        {\n            int temp = *final_ptr;\n            if (temp > 10) {\n                *final_ptr = temp - 5;\n            }\n        }\n        \n        ptr1++;\n        if (ptr1 >= data + 4) ptr1 = data + 1;\n    }\n    \n    return *final_ptr;\n}\n\n// What value is returned by complex_operations()?",
        "answer": 8
    }
}
```

### 4 - 跨函数推理 [ MultiFunc-Level ] (32)

#### 4A - 函数调用链推理 [ Call Chain ] （8）

> 直接调用、链式调用、递归调用、回归调用

```json
{
    "id": "MF-CC-S001",
    "metadata": {
        "name": "MultiFunc-CallChain-DirectCall",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "CodeSense-openssl",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Given the following direct function call scenario, what is the return value when process_request is called with buffer_size = 1024?",
        "code": "int validate_buffer_size(int size) {\n    if (size < 64) return 0;\n    if (size > 8192) return 0;\n    return 1;\n}\n\nint allocate_buffer(int size) {\n    if (!validate_buffer_size(size)) {\n        return -1;\n    }\n    return size * 2;\n}\n\nint process_request(int buffer_size) {\n    int allocated = allocate_buffer(buffer_size);\n    if (allocated == -1) {\n        return 0;\n    }\n    return allocated + 100;\n}\n\n// What is returned by process_request(1024)?",
        "answer": 2148
    }
}
```

```json
{
    "id": "MF-CC-S002",
    "metadata": {
        "name": "MultiFunc-CallChain-DirectCall-Error",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Trace the direct function call with error handling. What is the final return value?",
        "code": "def validate_input(value):\n    if value < 0:\n        return False\n    if value > 100:\n        return False\n    return True\n\ndef calculate_score(input_value):\n    if not validate_input(input_value):\n        return -1\n    return input_value * 3 + 10\n\ndef get_final_result(user_input):\n    score = calculate_score(user_input)\n    if score == -1:\n        return 0\n    return score + 5\n\n# What is returned by get_final_result(25)?",
        "answer": 90
    }
}
```

```json
{
    "id": "MF-CC-S003",
    "metadata": {
        "name": "MultiFunc-CallChain-ChainCall",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "CodeSense-postgresql",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Analyze this chain of function calls in a database query processor. What is the final result?",
        "code": "int parse_query(char *query) {\n    if (query == NULL) return 0;\n    return strlen(query) > 0 ? 1 : 0;\n}\n\nint validate_query(char *query) {\n    int parsed = parse_query(query);\n    if (!parsed) return 0;\n    return strlen(query) < 1000 ? 1 : 0;\n}\n\nint optimize_query(char *query) {\n    int valid = validate_query(query);\n    if (!valid) return -1;\n    return strlen(query) / 10 + 1;\n}\n\nint execute_query(char *query) {\n    int optimized = optimize_query(query);\n    if (optimized == -1) return 0;\n    return optimized * 5;\n}\n\n// Given query = \"SELECT * FROM users WHERE id = 1\", what does execute_query return?\n// Note: strlen(\"SELECT * FROM users WHERE id = 1\") = 31",
        "answer": 20
    }
}
```

```json
{
    "id": "MF-CC-S004",
    "metadata": {
        "name": "MultiFunc-CallChain-ChainTransform",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Follow the data transformation chain. What is the final transformed value?",
        "code": "def normalize(value):\n    return value / 100.0\n\ndef apply_coefficient(value):\n    normalized = normalize(value)\n    return normalized * 1.5\n\ndef add_bias(value):\n    transformed = apply_coefficient(value)\n    return transformed + 0.25\n\ndef round_result(value):\n    biased = add_bias(value)\n    return round(biased, 2)\n\n# What is returned by round_result(300)?",
        "answer": 4.75
    }
}
```

```json
{
    "id": "MF-CC-S005",
    "metadata": {
        "name": "MultiFunc-CallChain-Recursive",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Trace through this recursive function call. What is the final return value?",
        "code": "int fibonacci(int n) {\n    if (n <= 1) {\n        return n;\n    }\n    return fibonacci(n - 1) + fibonacci(n - 2);\n}\n\nint calculate_sum(int limit) {\n    int result = 0;\n    for (int i = 0; i < limit; i++) {\n        result += fibonacci(i);\n    }\n    return result;\n}\n\n// What is returned by calculate_sum(6)?\n// Note: fibonacci sequence: 0,1,1,2,3,5...",
        "answer": 12
    }
}
```

```json
{
    "id": "MF-CC-S006",
    "metadata": {
        "name": "MultiFunc-CallChain-TailRecursive",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Analyze this tail-recursive function with accumulator. What is the final result?",
        "code": "def factorial_helper(n, acc):\n    if n <= 1:\n        return acc\n    return factorial_helper(n - 1, acc * n)\n\ndef factorial(n):\n    return factorial_helper(n, 1)\n\ndef calculate_combination(n, r):\n    numerator = factorial(n)\n    denominator = factorial(r) * factorial(n - r)\n    return numerator // denominator\n\n# What is returned by calculate_combination(5, 2)?",
        "answer": 10
    }
}
```

```json
{
    "id": "MF-CC-S007",
    "metadata": {
        "name": "MultiFunc-CallChain-Callback",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "CodeSense-libevent",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Trace through callback function execution. What is the final value of result?",
        "code": "typedef int (*callback_func)(int);\n\nint double_value(int x) {\n    return x * 2;\n}\n\nint add_ten(int x) {\n    return x + 10;\n}\n\nint apply_callback(int value, callback_func cb) {\n    return cb(value);\n}\n\nint process_with_callbacks(int initial) {\n    int step1 = apply_callback(initial, double_value);\n    int step2 = apply_callback(step1, add_ten);\n    return step2;\n}\n\n// What is returned by process_with_callbacks(15)?",
        "answer": 40
    }
}
```

```json
{
    "id": "MF-CC-S008",
    "metadata": {
        "name": "MultiFunc-CallChain-HigherOrder",
        "category": "MultiFunc-Level",
        "subcategory": "Call Chain",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Analyze higher-order function composition. What is the final computed result?",
        "code": "def compose(f, g):\n    return lambda x: f(g(x))\n\ndef square(x):\n    return x * x\n\ndef increment(x):\n    return x + 1\n\ndef apply_twice(f):\n    return lambda x: f(f(x))\n\n# Create composed function\ncomposed = compose(square, increment)\ntwice_composed = apply_twice(composed)\n\n# What is returned by twice_composed(3)?",
        "answer": 256
    }
}
```

#### 4B - 参数传递推理 [ Parameter Passing ]（6）

> 值传递、引用传递

```json
{
    "id": "MF-PP-S001",
    "metadata": {
        "name": "MultiFunc-ParameterPassing-ValuePass",
        "category": "MultiFunc-Level",
        "subcategory": "Parameter Passing",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Analyze value passing behavior. What is the value of original_value after function execution?",
        "code": "void modify_value(int value) {\n    value = value * 2 + 10;\n    printf(\"Inside function: %d\\n\", value);\n}\n\nint main() {\n    int original_value = 25;\n    modify_value(original_value);\n    printf(\"After function: %d\\n\", original_value);\n    return 0;\n}\n\n// What is the value of original_value after modify_value is called?",
        "answer": 25
    }
}
```

```json
{
    "id": "MF-PP-S002",
    "metadata": {
        "name": "MultiFunc-ParameterPassing-ValueStructure",
        "category": "MultiFunc-Level",
        "subcategory": "Parameter Passing",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Trace struct value passing. What is the value of p1.x after the function call?",
        "code": "typedef struct {\n    int x;\n    int y;\n} Point;\n\nvoid transform_point(Point p) {\n    p.x = p.x * 2;\n    p.y = p.y + 5;\n}\n\nPoint create_and_transform() {\n    Point p1 = {10, 20};\n    transform_point(p1);\n    return p1;\n}\n\n// What is the x value of the Point returned by create_and_transform()?",
        "answer": 10
    }
}
```

```json
{
    "id": "MF-PP-S003",
    "metadata": {
        "name": "MultiFunc-ParameterPassing-PointerPass",
        "category": "MultiFunc-Level",
        "subcategory": "Parameter Passing",
        "type": "seed",
        "source": "CodeSense-linux-kernel",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Analyze pointer parameter passing with memory modification. What is the final value?",
        "code": "void update_values(int *arr, int size) {\n    for (int i = 0; i < size; i++) {\n        arr[i] = arr[i] * 2 + i;\n    }\n}\n\nvoid process_data() {\n    int data[4] = {5, 10, 15, 20};\n    update_values(data, 4);\n    printf(\"data[2] = %d\\n\", data[2]);\n}\n\n// What is the value of data[2] after update_values is called?",
        "answer": 32
    }
}
```

```json
{
    "id": "MF-PP-S004",
    "metadata": {
        "name": "MultiFunc-ParameterPassing-DoublePointer",
        "category": "MultiFunc-Level",
        "subcategory": "Parameter Passing",
        "type": "seed",
        "source": "CodeSense-tmux",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Track double pointer manipulation. What is the final value pointed to?",
        "code": "void allocate_and_set(int **ptr, int value) {\n    *ptr = malloc(sizeof(int));\n    **ptr = value * 3;\n}\n\nvoid modify_pointer_target(int **ptr) {\n    **ptr = **ptr + 15;\n}\n\nint test_double_pointer() {\n    int *p = NULL;\n    allocate_and_set(&p, 10);\n    modify_pointer_target(&p);\n    int result = *p;\n    free(p);\n    return result;\n}\n\n// What value is returned by test_double_pointer()?",
        "answer": 45
    }
}
```

```json
{
    "id": "MF-PP-S005",
    "metadata": {
        "name": "MultiFunc-ParameterPassing-Reference",
        "category": "MultiFunc-Level",
        "subcategory": "Parameter Passing",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Analyze Python reference passing with mutable objects. What is the final list content?",
        "code": "def modify_list(lst):\n    lst.append(100)\n    lst[0] = lst[0] * 2\n    lst.extend([200, 300])\n\ndef process_data():\n    my_list = [10, 20, 30]\n    modify_list(my_list)\n    return len(my_list)\n\n# What is returned by process_data()?",
        "answer": 6
    }
}
```

```json
{
    "id": "MF-PP-S006",
    "metadata": {
        "name": "MultiFunc-ParameterPassing-MixedTypes",
        "category": "MultiFunc-Level",
        "subcategory": "Parameter Passing",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Complex parameter passing with mixed types. What is the final computed value?",
        "code": "typedef struct {\n    int *data;\n    int count;\n} DataContainer;\n\nvoid process_container(DataContainer *container, int multiplier) {\n    for (int i = 0; i < container->count; i++) {\n        container->data[i] *= multiplier;\n    }\n    container->count++;\n}\n\nint calculate_sum(DataContainer container) {\n    int sum = 0;\n    for (int i = 0; i < container.count; i++) {\n        sum += container.data[i];\n    }\n    return sum;\n}\n\nint test_mixed_passing() {\n    int values[5] = {2, 4, 6, 8, 10};\n    DataContainer dc = {values, 4};\n    process_container(&dc, 3);\n    return calculate_sum(dc);\n}\n\n// What value is returned by test_mixed_passing()?",
        "answer": 60
    }
}
```

#### 4C - 状态传播推理 [ State Propagation ] （8）

> 全局变量、静态变量、闭包捕获、对象状态

```json
{
    "id": "MF-SP-S001",
    "metadata": {
        "name": "MultiFunc-StatePropagation-GlobalVar",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "CodeSense-apache-httpd",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Track global variable state across multiple function calls. What is the final value?",
        "code": "int global_counter = 0;\nint global_multiplier = 2;\n\nvoid increment_counter(int value) {\n    global_counter += value * global_multiplier;\n}\n\nvoid reset_and_multiply() {\n    global_counter = 0;\n    global_multiplier *= 3;\n}\n\nint process_sequence() {\n    increment_counter(5);\n    increment_counter(3);\n    reset_and_multiply();\n    increment_counter(4);\n    return global_counter;\n}\n\n// What value is returned by process_sequence()?",
        "answer": 24
    }
}
```

```json
{
    "id": "MF-SP-S002",
    "metadata": {
        "name": "MultiFunc-StatePropagation-GlobalArray",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Analyze global array modification across functions. What is the sum of all elements?",
        "code": "int shared_array[5] = {1, 2, 3, 4, 5};\nint array_size = 5;\n\nvoid double_elements() {\n    for (int i = 0; i < array_size; i++) {\n        shared_array[i] *= 2;\n    }\n}\n\nvoid add_index_to_elements() {\n    for (int i = 0; i < array_size; i++) {\n        shared_array[i] += i;\n    }\n}\n\nint calculate_total() {\n    double_elements();\n    add_index_to_elements();\n    int sum = 0;\n    for (int i = 0; i < array_size; i++) {\n        sum += shared_array[i];\n    }\n    return sum;\n}\n\n// What value is returned by calculate_total()?",
        "answer": 40
    }
}
```

```json
{
    "id": "MF-SP-S003",
    "metadata": {
        "name": "MultiFunc-StatePropagation-StaticVar",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "CodeSense-openssl",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Track static variable persistence across function calls. What is the final accumulated value?",
        "code": "int get_next_id() {\n    static int id_counter = 100;\n    id_counter += 10;\n    return id_counter;\n}\n\nint calculate_checksum() {\n    static int checksum = 0;\n    int id = get_next_id();\n    checksum += id;\n    return checksum;\n}\n\nint process_multiple_items() {\n    int total = 0;\n    total += calculate_checksum();\n    total += calculate_checksum();\n    total += calculate_checksum();\n    return total;\n}\n\n// What value is returned by process_multiple_items()?",
        "answer": 480
    }
}
```

```json
{
    "id": "MF-SP-S004",
    "metadata": {
        "name": "MultiFunc-StatePropagation-StaticArray",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Analyze static array state management across multiple function invocations. What is the final array element value?",
        "code": "int add_to_cache(int value) {\n    static int cache[3] = {0, 0, 0};\n    static int index = 0;\n    \n    cache[index] = value;\n    index = (index + 1) % 3;\n    \n    int sum = 0;\n    for (int i = 0; i < 3; i++) {\n        sum += cache[i];\n    }\n    return sum;\n}\n\nint test_cache_operations() {\n    add_to_cache(10);\n    add_to_cache(20);\n    add_to_cache(30);\n    return add_to_cache(40);\n}\n\n// What value is returned by test_cache_operations()?",
        "answer": 90
    }
}
```

```json
{
    "id": "MF-SP-S005",
    "metadata": {
        "name": "MultiFunc-StatePropagation-Closure",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Trace closure variable capture and modification. What is the final captured value?",
        "code": "def create_accumulator(initial):\n    total = initial\n    \n    def add_value(value):\n        nonlocal total\n        total += value\n        return total\n    \n    return add_value\n\ndef test_closure():\n    acc1 = create_accumulator(10)\n    acc2 = create_accumulator(20)\n    \n    result1 = acc1(5)\n    result2 = acc2(15)\n    result3 = acc1(10)\n    \n    return result3\n\n# What value is returned by test_closure()?",
        "answer": 25
    }
}
```

```json
{
    "id": "MF-SP-S006",
    "metadata": {
        "name": "MultiFunc-StatePropagation-NestedClosure",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Analyze nested closure state propagation. What is the final computed result?",
        "code": "def create_calculator(base):\n    def create_operation(operation_type):\n        def calculate(value):\n            if operation_type == 'add':\n                return base + value\n            elif operation_type == 'multiply':\n                return base * value\n            else:\n                return value\n        return calculate\n    return create_operation\n\ndef test_nested_closure():\n    calc = create_calculator(10)\n    adder = calc('add')\n    multiplier = calc('multiply')\n    \n    result1 = adder(5)\n    result2 = multiplier(3)\n    \n    return result1 + result2\n\n# What value is returned by test_nested_closure()?",
        "answer": 45
    }
}
```

```json
{
    "id": "MF-SP-S007",
    "metadata": {
        "name": "MultiFunc-StatePropagation-ObjectState",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Track object state changes across method calls. What is the final balance?",
        "code": "class BankAccount:\n    def __init__(self, initial_balance):\n        self.balance = initial_balance\n        self.transaction_count = 0\n    \n    def deposit(self, amount):\n        self.balance += amount\n        self.transaction_count += 1\n        return self.balance\n    \n    def withdraw(self, amount):\n        if self.balance >= amount:\n            self.balance -= amount\n            self.transaction_count += 1\n        return self.balance\n    \n    def apply_interest(self):\n        if self.transaction_count >= 3:\n            self.balance = int(self.balance * 1.05)\n        return self.balance\n\ndef test_account_operations():\n    account = BankAccount(100)\n    account.deposit(50)\n    account.withdraw(30)\n    account.deposit(20)\n    return account.apply_interest()\n\n# What value is returned by test_account_operations()?",
        "answer": 147
    }
}
```

```json
{
    "id": "MF-SP-S008",
    "metadata": {
        "name": "MultiFunc-StatePropagation-SharedObject",
        "category": "MultiFunc-Level",
        "subcategory": "State Propagation",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Analyze shared object state across multiple functions. What is the final computed value?",
        "code": "class SharedCounter:\n    def __init__(self):\n        self.value = 0\n        self.multiplier = 1\n    \n    def increment(self, amount=1):\n        self.value += amount * self.multiplier\n    \n    def set_multiplier(self, mult):\n        self.multiplier = mult\n    \n    def get_value(self):\n        return self.value\n\ncounter = SharedCounter()\n\ndef operation_a():\n    counter.increment(5)\n    counter.set_multiplier(2)\n\ndef operation_b():\n    counter.increment(3)\n    counter.increment(4)\n\ndef operation_c():\n    counter.set_multiplier(3)\n    counter.increment(2)\n\ndef test_shared_state():\n    operation_a()\n    operation_b()\n    operation_c()\n    return counter.get_value()\n\n# What value is returned by test_shared_state()?",
        "answer": 25
    }
}
```

#### 4D - 副作用推理 [ Side Effect ] （8）

> I/O操作、异常处理、内存操作、时间依赖

```json
{
    "id": "MF-SE-S001",
    "metadata": {
        "name": "MultiFunc-SideEffect-IOOperation",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "CodeSense-util-linux",
        "language": "c",
        "difficulty": "medium",
        "intervention": 1
    },
    "task": {
        "description": "Analyze I/O side effects on global state. What is the final value of bytes_written?",
        "code": "int bytes_written = 0;\n\nint write_data(const char* data) {\n    int len = strlen(data);\n    bytes_written += len;\n    // Simulated file write\n    printf(\"Writing %d bytes\\n\", len);\n    return len;\n}\n\nint log_operation(const char* operation, int value) {\n    char buffer[100];\n    sprintf(buffer, \"%s: %d\", operation, value);\n    return write_data(buffer);\n}\n\nint process_with_logging() {\n    log_operation(\"START\", 100);\n    log_operation(\"PROCESS\", 200);\n    log_operation(\"END\", 300);\n    return bytes_written;\n}\n\n// What value is returned by process_with_logging()?",
        "answer": 33
    }
}
```

```json
{
    "id": "MF-SE-S002",
    "metadata": {
        "name": "MultiFunc-SideEffect-FileOperations",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Track file operation side effects on program state. What is the final line count?",
        "code": "line_count = 0\n\ndef write_line(content):\n    global line_count\n    line_count += 1\n    # Simulated file write\n    print(f\"Line {line_count}: {content}\")\n    return line_count\n\ndef write_header(title):\n    write_line(f\"=== {title} ===\")\n    write_line(\"\")\n    return line_count\n\ndef write_content(items):\n    for item in items:\n        write_line(f\"- {item}\")\n    return line_count\n\ndef generate_report():\n    write_header(\"Report\")\n    write_content([\"Item 1\", \"Item 2\", \"Item 3\"])\n    write_line(\"End of report\")\n    return line_count\n\n# What value is returned by generate_report()?",
        "answer": 6
    }
}
```

```JSON
{
    "id": "MF-SE-S003",
    "metadata": {
        "name": "MultiFunc-SideEffect-ExceptionHandling",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Analyze exception handling side effects on program state. What is the final error_count?",
        "code": "error_count = 0\nsuccess_count = 0\n\ndef risky_operation(value):\n    global error_count, success_count\n    try:\n        if value < 0:\n            raise ValueError(\"Negative value\")\n        if value > 100:\n            raise ValueError(\"Value too large\")\n        success_count += 1\n        return value * 2\n    except ValueError:\n        error_count += 1\n        return 0\n\ndef process_batch(values):\n    results = []\n    for value in values:\n        result = risky_operation(value)\n        results.append(result)\n    return error_count\n\n# What value is returned by process_batch([10, -5, 150, 25, 200])?",
        "answer": 3
    }
}
```

```json
{
    "id": "MF-SE-S004",
    "metadata": {
        "name": "MultiFunc-SideEffect-NestedExceptions",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Track nested exception handling effects. What is the final cleanup_count?",
        "code": "cleanup_count = 0\nprocessed_count = 0\n\ndef cleanup_resource():\n    global cleanup_count\n    cleanup_count += 1\n\ndef process_item(item):\n    global processed_count\n    try:\n        if item['type'] == 'error':\n            raise Exception(\"Processing error\")\n        processed_count += 1\n        return item['value'] * 2\n    finally:\n        cleanup_resource()\n\ndef safe_process(item):\n    try:\n        return process_item(item)\n    except Exception:\n        return 0\n\ndef batch_process():\n    items = [\n        {'type': 'normal', 'value': 10},\n        {'type': 'error', 'value': 20},\n        {'type': 'normal', 'value': 30},\n        {'type': 'error', 'value': 40}\n    ]\n    for item in items:\n        safe_process(item)\n    return cleanup_count\n\n# What value is returned by batch_process()?",
        "answer": 4
    }
}
```

```json
{
    "id": "MF-SE-S005",
    "metadata": {
        "name": "MultiFunc-SideEffect-MemoryOps",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "CodeSense-glibc",
        "language": "c",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Track memory allocation side effects. What is the final allocation count?",
        "code": "int allocation_count = 0;\nint total_allocated_bytes = 0;\n\nvoid* allocate_memory(size_t size) {\n    allocation_count++;\n    total_allocated_bytes += size;\n    return malloc(size);\n}\n\nvoid free_memory(void* ptr) {\n    if (ptr != NULL) {\n        allocation_count--;\n        free(ptr);\n    }\n}\n\nint process_data_blocks() {\n    void* block1 = allocate_memory(100);\n    void* block2 = allocate_memory(200);\n    void* block3 = allocate_memory(150);\n    \n    free_memory(block1);\n    \n    void* block4 = allocate_memory(300);\n    \n    free_memory(block2);\n    free_memory(block3);\n    \n    return allocation_count;\n}\n\n// What value is returned by process_data_blocks()?",
        "answer": 1
    }
}
```

```json
{
    "id": "MF-SE-S006",
    "metadata": {
        "name": "MultiFunc-SideEffect-MemoryModification",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Analyze complex memory modification side effects. What is the final value at global_buffer[2]?",
        "code": "int global_buffer[5] = {1, 2, 3, 4, 5};\nint modification_count = 0;\n\nvoid modify_buffer_element(int index, int value) {\n    if (index >= 0 && index < 5) {\n        global_buffer[index] = value;\n        modification_count++;\n    }\n}\n\nvoid apply_transformation(int multiplier) {\n    for (int i = 0; i < 5; i++) {\n        modify_buffer_element(i, global_buffer[i] * multiplier);\n    }\n}\n\nvoid selective_update() {\n    for (int i = 1; i < 4; i++) {\n        modify_buffer_element(i, global_buffer[i] + i * 10);\n    }\n}\n\nint process_buffer() {\n    apply_transformation(2);\n    selective_update();\n    return global_buffer[2];\n}\n\n// What value is returned by process_buffer()?",
        "answer": 26
    }
}
```

```json
{
    "id": "MF-SE-S007",
    "metadata": {
        "name": "MultiFunc-SideEffect-TimeDependency",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "hard",
        "intervention": 2
    },
    "task": {
        "description": "Simulate time-dependent operations. What is the final timestamp difference?",
        "code": "import time\n\nclass TimeTracker:\n    def __init__(self):\n        self.start_time = 100  # Simulated timestamp\n        self.operations = []\n    \n    def record_operation(self, name, duration):\n        # Simulate time passage\n        self.start_time += duration\n        self.operations.append({\n            'name': name,\n            'timestamp': self.start_time,\n            'duration': duration\n        })\n        return self.start_time\n\ntracker = TimeTracker()\n\ndef operation_a():\n    return tracker.record_operation('A', 5)\n\ndef operation_b():\n    return tracker.record_operation('B', 10)\n\ndef operation_c():\n    return tracker.record_operation('C', 7)\n\ndef execute_sequence():\n    start = tracker.start_time\n    operation_a()\n    operation_b()\n    operation_c()\n    end = tracker.start_time\n    return end - start\n\n# What value is returned by execute_sequence()?",
        "answer": 22
    }
}
```

```json
{
    "id": "MF-SE-S008",
    "metadata": {
        "name": "MultiFunc-SideEffect-ConcurrentAccess",
        "category": "MultiFunc-Level",
        "subcategory": "Side Effect",
        "type": "seed",
        "source": "Manual",
        "language": "python",
        "difficulty": "expert",
        "intervention": 3
    },
    "task": {
        "description": "Simulate concurrent access effects on shared state. What is the final counter value?",
        "code": "class SharedResource:\n    def __init__(self):\n        self.counter = 0\n        self.lock_count = 0\n    \n    def acquire_lock(self):\n        self.lock_count += 1\n    \n    def release_lock(self):\n        if self.lock_count > 0:\n            self.lock_count -= 1\n    \n    def safe_increment(self, value):\n        self.acquire_lock()\n        self.counter += value\n        self.release_lock()\n        return self.counter\n\nresource = SharedResource()\n\ndef worker_a():\n    result = 0\n    result += resource.safe_increment(5)\n    result += resource.safe_increment(3)\n    return result\n\ndef worker_b():\n    result = 0\n    result += resource.safe_increment(7)\n    result += resource.safe_increment(2)\n    return result\n\ndef simulate_concurrent_work():\n    worker_a()\n    worker_b()\n    return resource.counter\n\n# What value is returned by simulate_concurrent_work()?",
        "answer": 17
    }
}
```

#### 4E - 大混合 （2）

```json
{
    "id": "MF-MIX-S001",
    "metadata": {
        "name": "MultiFunc-Mix-Comprehensive",
        "category": "MultiFunc-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "Manual",
        "language": "c",
        "difficulty": "master",
        "intervention": 4
    },
    "task": {
        "description": "Comprehensive multi-function analysis combining call chains, parameter passing, state propagation, and side effects. What is the final computed result?",
        "code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// Global state\nstatic int global_operation_count = 0;\nstatic char global_log[256] = \"\";\n\n// Function pointer type\ntypedef int (*processor_func)(int);\n\n// Callback functions\nint double_processor(int value) {\n    return value * 2;\n}\n\nint square_processor(int value) {\n    return value * value;\n}\n\n// State management functions\nvoid log_operation(const char* op_name, int value) {\n    char temp[64];\n    sprintf(temp, \"%s:%d;\", op_name, value);\n    strcat(global_log, temp);\n    global_operation_count++;\n}\n\n// Recursive function with state modification\nint recursive_calculate(int n, int depth) {\n    log_operation(\"REC\", n);\n    \n    if (depth <= 0 || n <= 1) {\n        return n;\n    }\n    \n    return n + recursive_calculate(n - 1, depth - 1);\n}\n\n// Function with complex parameter passing\nint process_array_with_callback(int *arr, int size, processor_func processor) {\n    int sum = 0;\n    for (int i = 0; i < size; i++) {\n        int processed = processor(arr[i]);\n        arr[i] = processed;  // Side effect: modify original array\n        sum += processed;\n        log_operation(\"PROC\", processed);\n    }\n    return sum;\n}\n\n// Function with multiple side effects\nint* allocate_and_process(int initial_value) {\n    static int allocation_count = 0;\n    allocation_count++;\n    \n    int *result = malloc(sizeof(int) * 3);\n    if (result == NULL) {\n        log_operation(\"ERROR\", -1);\n        return NULL;\n    }\n    \n    result[0] = recursive_calculate(initial_value, 2);\n    result[1] = process_array_with_callback(&result[0], 1, double_processor);\n    result[2] = allocation_count;\n    \n    log_operation(\"ALLOC\", allocation_count);\n    return result;\n}\n\n// Main computation function\nint complex_computation() {\n    int test_array[3] = {3, 4, 5};\n    \n    // Chain of operations with various effects\n    int sum1 = process_array_with_callback(test_array, 3, square_processor);\n    \n    int *dynamic_data = allocate_and_process(4);\n    if (dynamic_data == NULL) {\n        return -1;\n    }\n    \n    int sum2 = dynamic_data[0] + dynamic_data[1] + dynamic_data[2];\n    \n    // Modify array through pointer\n    test_array[1] = test_array[1] + dynamic_data[2];\n    \n    int final_result = sum1 + sum2 + global_operation_count;\n    \n    free(dynamic_data);\n    log_operation(\"FINAL\", final_result);\n    \n    return final_result;\n}\n\n// What value is returned by complex_computation()?",
        "answer": 160
    }
}
```

```json
{
    "id": "MF-MIX-S002",
    "metadata": {
        "name": "MultiFunc-Mix-RealWorld",
        "category": "MultiFunc-Level",
        "subcategory": "Mix",
        "type": "seed",
        "source": "CodeSense-postgresql",
        "language": "python",
        "difficulty": "grandmaster",
        "intervention": 5
    },
    "task": {
        "description": "Real-world scenario: Database transaction processing system with complex inter-function dependencies. What is the final transaction_id?",
        "code": "class TransactionManager:\n    def __init__(self):\n        self.next_transaction_id = 1000\n        self.active_transactions = {}\n        self.completed_transactions = []\n        self.error_count = 0\n    \n    def begin_transaction(self, user_id):\n        tx_id = self.next_transaction_id\n        self.next_transaction_id += 1\n        self.active_transactions[tx_id] = {\n            'user_id': user_id,\n            'operations': [],\n            'status': 'active'\n        }\n        return tx_id\n    \n    def add_operation(self, tx_id, operation):\n        if tx_id in self.active_transactions:\n            self.active_transactions[tx_id]['operations'].append(operation)\n            return True\n        return False\n    \n    def commit_transaction(self, tx_id):\n        if tx_id in self.active_transactions:\n            tx = self.active_transactions.pop(tx_id)\n            tx['status'] = 'committed'\n            self.completed_transactions.append(tx)\n            return len(tx['operations'])\n        return 0\n    \n    def rollback_transaction(self, tx_id):\n        if tx_id in self.active_transactions:\n            self.active_transactions.pop(tx_id)\n            self.error_count += 1\n            return True\n        return False\n\n# Global transaction manager\ntm = TransactionManager()\n\n# Account management\naccounts = {\n    'alice': 1000,\n    'bob': 500,\n    'charlie': 750\n}\n\ndef validate_transfer(from_account, to_account, amount):\n    if from_account not in accounts or to_account not in accounts:\n        return False\n    if accounts[from_account] < amount:\n        return False\n    if amount <= 0:\n        return False\n    return True\n\ndef execute_transfer(tx_id, from_account, to_account, amount):\n    try:\n        if not validate_transfer(from_account, to_account, amount):\n            tm.rollback_transaction(tx_id)\n            return False\n        \n        # Record operations\n        tm.add_operation(tx_id, f\"debit:{from_account}:{amount}\")\n        tm.add_operation(tx_id, f\"credit:{to_account}:{amount}\")\n        \n        # Execute transfer\n        accounts[from_account] -= amount\n        accounts[to_account] += amount\n        \n        return True\n    except Exception:\n        tm.rollback_transaction(tx_id)\n        return False\n\ndef batch_transfer(transfers):\n    results = []\n    \n    for transfer in transfers:\n        from_acc, to_acc, amount = transfer\n        \n        # Begin transaction\n        tx_id = tm.begin_transaction(from_acc)\n        \n        # Execute transfer\n        success = execute_transfer(tx_id, from_acc, to_acc, amount)\n        \n        if success:\n            operation_count = tm.commit_transaction(tx_id)\n            results.append(operation_count)\n        else:\n            results.append(0)\n    \n    return results\n\ndef calculate_statistics():\n    total_completed = len(tm.completed_transactions)\n    total_operations = sum(len(tx['operations']) for tx in tm.completed_transactions)\n    error_rate = tm.error_count / max(tm.next_transaction_id - 1000, 1)\n    \n    return {\n        'completed': total_completed,\n        'operations': total_operations,\n        'error_rate': error_rate,\n        'next_id': tm.next_transaction_id\n    }\n\ndef process_banking_scenario():\n    # Define transfer batch\n    transfers = [\n        ('alice', 'bob', 200),      # Valid\n        ('bob', 'charlie', 100),    # Valid\n        ('charlie', 'alice', 1000), # Invalid - insufficient funds\n        ('alice', 'charlie', 300),  # Valid\n        ('bob', 'alice', 800),      # Invalid - insufficient funds\n        ('charlie', 'bob', 50)      # Valid\n    ]\n    \n    # Process transfers\n    batch_results = batch_transfer(transfers)\n    \n    # Calculate final statistics\n    stats = calculate_statistics()\n    \n    # Complex calculation combining all factors\n    final_result = (\n        stats['next_id'] +\n        stats['completed'] * 10 +\n        stats['operations'] * 5 +\n        int(stats['error_rate'] * 100) +\n        sum(batch_results)\n    )\n    \n    return final_result\n\n# What value is returned by process_banking_scenario()?",
        "answer": 1114
    }
}
```

## 变式生成叶子任务构建

### 1 - 语句级推理 [ Statement-Level ] （323）

#### 1A - 算数运算 [ Arithmetic ] （49）

> 提示词
>
> 任务目标
>
> 基于给定的算术运算种子任务，生成多样化的变式任务来扩展测试覆盖面，确保对大模型算术推理能力进行全面评估。
>
> 变式生成维度
>
> 1. 运算复杂度变式
>
> - **简化变式**: 将复合运算分解为单一运算
> - **复杂化变式**: 增加运算层数和嵌套深度
> - **混合运算变式**: 组合不同类型的算术运算（四则运算+位运算+幂运算）
>
> 2. 数据类型变式
>
> - **整数变式**: 使用不同范围的整数（小整数、大整数、负数、零）
> - **浮点数变式**: 精度变化、科学计数法、极值处理
> - **类型转换变式**: int/float/decimal互转，截断/舍入行为
> - **特殊值变式**: NaN、Infinity、极小值、边界值
>
> 3. 运算符优先级变式
>
> - **括号变式**: 添加/移除括号改变运算顺序
> - **优先级混淆变式**: 故意设计易错的优先级组合
> - **链式运算变式**: 多个同级运算符连续使用
>
> 4. 位运算特化变式
>
> - **位操作变式**: 左移、右移、与、或、异或、取反
> - **掩码操作变式**: 位掩码设置、清除、检查
> - **二进制表示变式**: 不同进制表示（0b、0o、0x）
>
> 5. 变量依赖变式
>
> - **直接计算变式**: 所有值都是字面量
> - **单级依赖变式**: 使用一层变量引用
> - **多级依赖变式**: 变量间存在复杂依赖关系
> - **循环依赖变式**: 变量更新后的累积效果
>
> 6. 语言移植变式
>
> - **Python -> Java**: 考虑类型声明、除法行为差异
> - **Python -> C++**: 考虑类型转换、溢出行为
> - **Python -> JavaScript**: 考虑弱类型转换规则
>
> 7. 边界条件变式
>
> - **溢出变式**: 整数溢出、浮点溢出
> - **精度损失变式**: 浮点精度问题
> - **除零变式**: 除法和取模的特殊情况
> - **负数变式**: 负数的幂运算、位运算
>
> 8. 错误导向变式
>
> - **常见错误变式**: 设计容易产生错误理解的表达式
> - **陷阱变式**: 利用运算符优先级、类型转换等设置陷阱
> - **边界错误变式**: 边界值的特殊行为
>
> 生成规则
>
> 基本要求
>
> 1. 每个种子任务生成8-12个变式
> 2. 确保每个变式维度至少覆盖2-3个变式
> 3. 保持原始问题的核心语义，但改变实现细节
> 4. 变式难度应该涵盖easy/medium/hard三个等级
>
> 难度分级标准
>
> - **Easy**: 单一运算类型，直接字面量，无类型转换
> - **Medium**: 2-3种运算类型组合，1-2层变量依赖，简单类型转换
> - **Hard**: 复杂运算嵌套，多层变量依赖，特殊值处理，跨类型操作
>
> 输出格式
>
> 为每个变式生成完整的JSON格式，包含：
> - 唯一ID（基于种子ID + 变式类型）
> - 完整的metadata（标注变式类型和难度）
> - 清晰的task描述和代码
> - 正确且唯一的答案
>
> 质量检查要点
>
> 1. **正确性**: 确保答案计算正确
> 2. **多样性**: 避免简单的数值替换，要有结构性变化
> 3. **代表性**: 每个变式应该测试特定的推理能力
> 4. **渐进性**: 从简单到复杂有合理的难度梯度
>
> 示例变式生成
>
> 基于种子任务SL-AR-S005，生成以下变式：
> - 简化变式: 分解为单个运算步骤
> - 类型转换变式: 引入浮点数和类型转换
> - 位运算变式: 替换部分算术运算为位运算
> - 边界值变式: 使用可能导致溢出的大数值
> - 优先级陷阱变式: 设计容易误解的运算符组合
>
> 请基于此提示词，为给定的种子任务生成完整的变式集合。
>
> 下面是6个种子任务

```json
{
    "id": "SL-AR-S001-V1",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-Simplified",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "simplified"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = mid + 1`?",
        "code": "mid = 3\nj = mid + 1",
        "answer": 4
    }
},
{
    "id": "SL-AR-S001-V2",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-NegativeNumbers",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "data_type"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = mid + 1`?",
        "code": "a = [-5, -2, 0, 1, 3, 8, 12]\nlo = 0\nmid = -2\nhi = 4\ni = lo\nj = mid + 1",
        "answer": -1
    }
},
{
    "id": "SL-AR-S001-V3",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-FloatConversion",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "type_conversion"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = int(mid + 1.5)`?",
        "code": "a = [1.5, 2.3, 4.7, 5.1, 6.8]\nlo = 0\nmid = 2.7\nhi = 4\ni = lo\nj = int(mid + 1.5)",
        "answer": 4
    }
},
{
    "id": "SL-AR-S001-V4",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-ComplexExpression",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "complexity"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = (mid + 1) * 2 - lo // 2`?",
        "code": "a = [1, 2, 4, 4, 5, 6, 7, 23, 8, 9]\nlo = 4\nmid = 3\nhi = 7\ni = lo\nj = (mid + 1) * 2 - lo // 2",
        "answer": 6
    }
},
{
    "id": "SL-AR-S001-V5",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-BitOperations",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "bit_operations"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = (mid | 1) + 1`?",
        "code": "a = [1, 2, 4, 4, 5, 6, 7, 23, 8, 9]\nlo = 0\nmid = 2\nhi = 7\ni = lo\nj = (mid | 1) + 1",
        "answer": 4
    }
},
{
    "id": "SL-AR-S001-V6",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-Overflow",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = mid + 1`?",
        "code": "a = list(range(1000))\nlo = 0\nmid = 999999999999\nhi = 1000000000000\ni = lo\nj = mid + 1",
        "answer": 1000000000000
    }
},
{
    "id": "SL-AR-S001-V7",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-PrecedenceTrap",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "precedence_trap"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = mid + 1 * 2 + 3`?",
        "code": "a = [1, 2, 4, 4, 5, 6, 7, 23, 8, 9]\nlo = 0\nmid = 3\nhi = 7\ni = lo\nj = mid + 1 * 2 + 3",
        "answer": 8
    }
},
{
    "id": "SL-AR-S001-V8",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-MultiLevel",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "multi_dependency"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = offset + 1`?",
        "code": "a = [1, 2, 4, 4, 5, 6, 7, 23, 8, 9]\nlo = 0\nbase = 3\nmid = base + lo\noffset = mid\nhi = 7\ni = lo\nj = offset + 1",
        "answer": 4
    }
},
{
    "id": "SL-AR-S001-V9",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S001-ZeroEdge",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable j after executing the assignment statement `j = mid + 1`?",
        "code": "a = [0, 0, 0, 0, 0]\nlo = 0\nmid = -1\nhi = 3\ni = lo\nj = mid + 1",
        "answer": 0
    }
},
{
    "id": "SL-AR-S002-V1",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-Simplified",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "simplified"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = total // count`?",
        "code": "total = 90\ncount = 4\nresult = total // count",
        "answer": 22
    }
},
{
    "id": "SL-AR-S002-V2",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-FloatDivision",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "type_conversion"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = total / count`?",
        "code": "items = [15, 25, 30, 20]\ntotal = sum(items)\ncount = len(items)\nresult = total / count\nremainder = total % count",
        "answer": 22.5
    }
},
{
    "id": "SL-AR-S002-V3",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-NegativeNumbers",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "data_type"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = total // count`?",
        "code": "items = [-15, -25, 30, 20]\ntotal = sum(items)\ncount = len(items)\nresult = total // count\nremainder = total % count",
        "answer": 2
    }
},
{
    "id": "SL-AR-S002-V4",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-ComplexCalculation",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "complexity"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = (total * 2 + bonus) // (count + extra)`?",
        "code": "items = [15, 25, 30, 20]\ntotal = sum(items)\ncount = len(items)\nbonus = 10\nextra = 1\nresult = (total * 2 + bonus) // (count + extra)\nremainder = total % count",
        "answer": 38
    }
},
{
    "id": "SL-AR-S002-V5",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-ZeroDivision",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = total // count` when count is non-zero?",
        "code": "items = [100]\ntotal = sum(items)\ncount = len(items)\nresult = total // count\nremainder = total % count",
        "answer": 100
    }
},
{
    "id": "SL-AR-S002-V6",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-BitShift",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "bit_operations"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = total >> shift`?",
        "code": "items = [16, 32, 48, 64]\ntotal = sum(items)\nshift = 2\nresult = total >> shift\nremainder = total % (1 << shift)",
        "answer": 40
    }
},
{
    "id": "SL-AR-S002-V7",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-Precision",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "precision_loss"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = int(total // count)`?",
        "code": "items = [15.7, 25.3, 30.1, 20.9]\ntotal = sum(items)\ncount = len(items)\nresult = int(total // count)\nremainder = total % count",
        "answer": 22
    }
},
{
    "id": "SL-AR-S002-V8",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S002-LargeNumbers",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = total // count`?",
        "code": "items = [1500000, 2500000, 3000000, 2000000]\ntotal = sum(items)\ncount = len(items)\nresult = total // count\nremainder = total % count",
        "answer": 2250000
    }
},
{
    "id": "SL-AR-S003-V1",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-Simplified",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "simplified"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = 3.14159 * radius ** 2`?",
        "code": "radius = 5\narea = 3.14159 * radius ** 2",
        "answer": 78.53975
    }
},
{
    "id": "SL-AR-S003-V2",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-IntegerRadius",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "data_type"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = int(3.14159 * radius ** 2)`?",
        "code": "import math\nradius = 3\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = int(3.14159 * radius ** 2)\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 28
    }
},
{
    "id": "SL-AR-S003-V3",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-HighPrecision",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "precision_enhancement"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = math.pi * radius ** 2`?",
        "code": "import math\nradius = 5\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = math.pi * radius ** 2\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 78.53981633974483
    }
},
{
    "id": "SL-AR-S003-V4",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-ComplexFormula",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "complexity"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = 3.14159 * (radius + offset) ** 2 - 3.14159 * offset ** 2`?",
        "code": "import math\nradius = 3\noffset = 2\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = 3.14159 * (radius + offset) ** 2 - 3.14159 * offset ** 2\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 40.840299999999996
    }
},
{
    "id": "SL-AR-S003-V5",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-NegativeRadius",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = 3.14159 * radius ** 2`?",
        "code": "import math\nradius = -5\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = 3.14159 * radius ** 2\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 78.53975
    }
},
{
    "id": "SL-AR-S003-V6",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-FloatRadius",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "data_type"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = 3.14159 * radius ** 2`?",
        "code": "import math\nradius = 2.5\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = 3.14159 * radius ** 2\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 19.634937500000002
    }
},
{
    "id": "SL-AR-S003-V7",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-ZeroRadius",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = 3.14159 * radius ** 2`?",
        "code": "import math\nradius = 0\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = 3.14159 * radius ** 2\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 0.0
    }
},
{
    "id": "SL-AR-S003-V8",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S003-PowerVariation",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "complexity"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = 3.14159 * radius ** (1 + 1)`?",
        "code": "import math\nradius = 5\ndiameter = 2 * radius\ncircumference = 2 * math.pi * radius\narea = 3.14159 * radius ** (1 + 1)\nvolume = (4/3) * math.pi * radius ** 3",
        "answer": 78.53975
    }
},
{
    "id": "SL-AR-S004-V1",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-Simplified",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "simplified"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags | 4`?",
        "code": "flags = 0b1010\nmask = flags | 4",
        "answer": 14
    }
},
{
    "id": "SL-AR-S004-V2",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-HexRepresentation",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "data_representation"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags | (1 << position)`?",
        "code": "flags = 0xA\nposition = 2\nmask = flags | (1 << position)\ncheck = mask & (1 << position)\ntoggle = flags ^ (1 << position)",
        "answer": 14
    }
},
{
    "id": "SL-AR-S004-V3",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-XOROperation",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "bit_operations"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags ^ (1 << position)`?",
        "code": "flags = 0b1010\nposition = 2\nmask = flags ^ (1 << position)\ncheck = mask & (1 << position)\ntoggle = flags ^ (1 << position)",
        "answer": 14
    }
},
{
    "id": "SL-AR-S004-V4",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-ANDOperation",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "bit_operations"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags & ~(1 << position)`?",
        "code": "flags = 0b1110\nposition = 2\nmask = flags & ~(1 << position)\ncheck = mask & (1 << position)\ntoggle = flags ^ (1 << position)",
        "answer": 10
    }
},
{
    "id": "SL-AR-S004-V5",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-MultiplePositions",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "complexity"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags | (1 << position1) | (1 << position2)`?",
        "code": "flags = 0b1010\nposition1 = 2\nposition2 = 0\nmask = flags | (1 << position1) | (1 << position2)\ncheck = mask & (1 << position1)\ntoggle = flags ^ (1 << position1)",
        "answer": 15
    }
},
{
    "id": "SL-AR-S004-V6",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-NegativePosition",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags | (1 << abs(position))`?",
        "code": "flags = 0b1010\nposition = -2\nmask = flags | (1 << abs(position))\ncheck = mask & (1 << abs(position))\ntoggle = flags ^ (1 << abs(position))",
        "answer": 14
    }
},
{
    "id": "SL-AR-S004-V7",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-LargeShift",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags | (1 << position)`?",
        "code": "flags = 0b1010\nposition = 8\nmask = flags | (1 << position)\ncheck = mask & (1 << position)\ntoggle = flags ^ (1 << position)",
        "answer": 266
    }
},
{
    "id": "SL-AR-S004-V8",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S004-ZeroFlags",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable mask after executing the statement `mask = flags | (1 << position)`?",
        "code": "flags = 0b0000\nposition = 2\nmask = flags | (1 << position)\ncheck = mask & (1 << position)\ntoggle = flags ^ (1 << position)",
        "answer": 4
    }
},
{
    "id": "SL-AR-S005-V1",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-Simplified",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "simplified"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base * 2`?",
        "code": "base = 10\nresult = base * 2",
        "answer": 20
    }
},
{
    "id": "SL-AR-S005-V2",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-ParenthesesChange",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "precedence_trap"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = (base * 2 + offset // 3 - power ** 2) % 5`?",
        "code": "base = 10\noffset = 17\npower = 3\ntemp1 = base * 2\ntemp2 = offset // 3\ntemp3 = power ** 2\ntemp4 = temp3 % 5\nresult = (base * 2 + offset // 3 - power ** 2) % 5",
        "answer": 2
    }
},
{
    "id": "SL-AR-S005-V3",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-FloatOperations",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "type_conversion"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base * 2.0 + offset / 3.0 - power ** 2 % 5`?",
        "code": "base = 10\noffset = 17\npower = 3\ntemp1 = base * 2.0\ntemp2 = offset / 3.0\ntemp3 = power ** 2\ntemp4 = temp3 % 5\nresult = base * 2.0 + offset / 3.0 - power ** 2 % 5",
        "answer": 21.666666666666668
    }
},
{
    "id": "SL-AR-S005-V4",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-NegativeNumbers",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "data_type"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base * 2 + offset // 3 - power ** 2 % 5`?",
        "code": "base = -10\noffset = 17\npower = 3\ntemp1 = base * 2\ntemp2 = offset // 3\ntemp3 = power ** 2\ntemp4 = temp3 % 5\nresult = base * 2 + offset // 3 - power ** 2 % 5",
        "answer": -19
    }
},
{
    "id": "SL-AR-S005-V5",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-BitOperations",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "bit_operations"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base << 1 + offset // 3 - power ** 2 % 5`?",
        "code": "base = 10\noffset = 17\npower = 3\ntemp1 = base << 1\ntemp2 = offset // 3\ntemp3 = power ** 2\ntemp4 = temp3 % 5\nresult = base << 1 + offset // 3 - power ** 2 % 5",
        "answer": 21
    }
},
{
    "id": "SL-AR-S005-V6",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-LargeNumbers",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base * 2 + offset // 3 - power ** 2 % 5`?",
        "code": "base = 1000000\noffset = 17\npower = 3\ntemp1 = base * 2\ntemp2 = offset // 3\ntemp3 = power ** 2\ntemp4 = temp3 % 5\nresult = base * 2 + offset // 3 - power ** 2 % 5",
        "answer": 2000001
    }
},
{
    "id": "SL-AR-S005-V7",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-ZeroValues",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base * 2 + offset // 3 - power ** 2 % 5`?",
        "code": "base = 0\noffset = 17\npower = 3\ntemp1 = base * 2\ntemp2 = offset // 3\ntemp3 = power ** 2\ntemp4 = temp3 % 5\nresult = base * 2 + offset // 3 - power ** 2 % 5",
        "answer": 1
    }
},
{
    "id": "SL-AR-S005-V8",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S005-DependencyChain",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "multi_dependency"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = final_base * 2 + final_offset // 3 - final_power ** 2 % 5`?",
        "code": "initial = 5\nbase = initial * 2\noffset = 17\npower = 3\nfinal_base = base\nfinal_offset = offset\nfinal_power = power\ntemp1 = final_base * 2\ntemp2 = final_offset // 3\ntemp3 = final_power ** 2\ntemp4 = temp3 % 5\nresult = final_base * 2 + final_offset // 3 - final_power ** 2 % 5",
        "answer": 21
    }
},
{
    "id": "SL-AR-S006-V1",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-Simplified",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0,
        "variant_type": "simplified"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(70.4)`?",
        "code": "average = 70.4\nfinal_score = int(average)",
        "answer": 70
    }
},
{
    "id": "SL-AR-S006-V2",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-RoundingBehavior",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "type_conversion"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = round(average * weight + bonus)`?",
        "code": "scores = [85, 92, 78, 96]\naverage = sum(scores) / len(scores)\nweight = 0.8\nbonus = 5.5\nfinal_score = round(average * weight + bonus)\nrounded_score = round(average * weight + bonus)",
        "answer": 76
    }
},
{
    "id": "SL-AR-S006-V3",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-FloorDivision",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "type_conversion"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(average * weight // 1 + bonus)`?",
        "code": "scores = [85, 92, 78, 96]\naverage = sum(scores) / len(scores)\nweight = 0.8\nbonus = 5.5\nfinal_score = int(average * weight // 1 + bonus)\nrounded_score = round(average * weight + bonus)",
        "answer": 75
    }
},
{
    "id": "SL-AR-S006-V4",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-NegativeBonus",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "data_type"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(average * weight + bonus)`?",
        "code": "scores = [85, 92, 78, 96]\naverage = sum(scores) / len(scores)\nweight = 0.8\nbonus = -5.5\nfinal_score = int(average * weight + bonus)\nrounded_score = round(average * weight + bonus)",
        "answer": 64
    }
},
{
    "id": "SL-AR-S006-V5",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-HighPrecision",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "precision_enhancement"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(average * weight * precision + bonus * precision) // precision`?",
        "code": "scores = [85, 92, 78, 96]\naverage = sum(scores) / len(scores)\nweight = 0.8\nbonus = 5.5\nprecision = 1000\nfinal_score = int(average * weight * precision + bonus * precision) // precision\nrounded_score = round(average * weight + bonus)",
        "answer": 75
    }
},
{
    "id": "SL-AR-S006-V6",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-MultipleWeights",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "complexity"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(average * weight1 * weight2 + bonus)`?",
        "code": "scores = [85, 92, 78, 96]\naverage = sum(scores) / len(scores)\nweight1 = 0.9\nweight2 = 0.8\nbonus = 5.5\nfinal_score = int(average * weight1 * weight2 + bonus)\nrounded_score = round(average * weight1 * weight2 + bonus)",
        "answer": 68
    }
},
{
    "id": "SL-AR-S006-V7",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-EmptyScores",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0,
        "variant_type": "boundary_conditions"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(average * weight + bonus)`?",
        "code": "scores = [100]\naverage = sum(scores) / len(scores)\nweight = 0.8\nbonus = 5.5\nfinal_score = int(average * weight + bonus)\nrounded_score = round(average * weight + bonus)",
        "answer": 85
    }
},
{
    "id": "SL-AR-S006-V8",
    "metadata": {
        "name": "StatementLevel-Arithmetic-S006-BitShiftConversion",
        "category": "Statement-Level",
        "subcategory": "Arithmetic",
        "type": "variant",
        "source": "Generated",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0,
        "variant_type": "bit_operations"
    },
    "task": {
        "description": "Given the following code snippet, what is the value of variable final_score after executing the statement `final_score = int(average) >> 0 + int(bonus)`?",
        "code": "scores = [80, 90, 70, 100]\naverage = sum(scores) / len(scores)\nweight = 0.8\nbonus = 5.5\nfinal_score = int(average) >> 0 + int(bonus)\nrounded_score = round(average * weight + bonus)",
        "answer": 90
    }
}
```

#### 1B - 布尔运算 [ Boolean ] (50)

> 提示词：
>
> ```
> 
> ## 任务目标
> 基于给定的布尔运算种子任务，生成多样化的变式任务来全面测试大模型的布尔逻辑推理能力，涵盖比较运算、逻辑运算和短路求值等核心场景。
> 
> ## 变式生成维度
> 
> ### 1. 比较运算变式
> - **比较运算符变式**: ==, !=, <, <=, >, >= 的各种替换和组合
> - **数值范围变式**: 边界值比较（0, -1, 1, 最大值, 最小值）
> - **类型比较变式**: 不同数据类型间的比较行为
> - **特殊值比较变式**: NULL/nullptr, 0, EOF等特殊值的比较
> - **十六进制比较变式**: 0x80, 0xFF等十六进制常量比较
> 
> ### 2. 逻辑运算变式
> - **逻辑运算符变式**: &&(and), ||(or), !(not) 的组合使用
> - **德摩根定律变式**: !(A && B) ↔ (!A || !B) 等价转换
> - **运算符优先级变式**: 混合使用 &&/|| 时的优先级测试
> - **嵌套逻辑变式**: 多层括号的复杂逻辑表达式
> - **三元运算符变式**: condition ? true_val : false_val
> 
> ### 3. 短路求值变式
> - **OR短路变式**: 第一个条件为真时，第二个条件不被计算
> - **AND短路变式**: 第一个条件为假时，第二个条件不被计算
> - **副作用短路变式**: 包含函数调用或变量修改的短路情况
> - **复合短路变式**: 多个短路条件的组合
> 
> ### 4. 空值和指针变式
> - **空指针检查变式**: NULL判断的各种形式
> - **指针比较变式**: 指针地址的比较运算
> - **空值逻辑变式**: NULL在逻辑运算中的行为
> - **指针转换变式**: void*指针的比较和转换
> 
> ### 5. 常量和宏变式
> - **宏定义变式**: #define常量的比较和逻辑运算
> - **枚举变式**: 枚举值的比较运算
> - **常量表达式变式**: const常量的布尔运算
> - **字面量变式**: 直接使用数字字面量vs使用命名常量
> 
> ### 6. 语言移植变式
> - **C -> Python变式**: 考虑Truth值、None vs NULL等差异
> - **C -> Java变式**: 考虑boolean类型、null vs NULL等差异
> - **C -> JavaScript变式**: 考虑truthy/falsy值、类型转换等差异
> 
> ### 7. 复杂度变式
> - **简化变式**: 将复合条件分解为单一比较
> - **复杂化变式**: 增加更多逻辑运算符和条件
> - **链式比较变式**: a < b < c 形式的连续比较
> - **多分支变式**: if-else if-else的复杂条件判断
> 
> ### 8. 边界和错误变式
> - **边界值变式**: 临界值的比较（如127 vs 128对于signed char）
> - **溢出边界变式**: 整数溢出时的比较行为
> - **精度问题变式**: 浮点数比较的精度问题
> - **类型转换变式**: 隐式类型转换对比较结果的影响
> 
> ### 9. 上下文依赖变式
> - **条件上下文变式**: 改变if语句的上下文环境
> - **返回值变式**: 不同返回值类型的布尔表达式
> - **函数参数变式**: 作为函数参数的布尔表达式
> - **循环条件变式**: 作为循环条件的布尔表达式
> 
> ## 生成规则
> 
> ### 基本要求
> 1. 每个种子任务生成10-15个变式
> 2. 确保每个变式维度至少覆盖2-3个变式
> 3. 保持原始布尔逻辑的核心，但改变具体实现
> 4. 变式难度应该涵盖easy/medium/hard三个等级
> 
> ### 难度分级标准
> - **Easy**: 单一比较运算，直接值比较，无复杂逻辑
> - **Medium**: 2-3个逻辑运算符组合，简单短路求值，基础指针比较
> - **Hard**: 复杂嵌套逻辑，多重短路求值，特殊值处理，类型转换陷阱
> 
> ### 特殊考虑点
> 1. **C语言特性**: 指针运算、宏定义、类型转换规则
> 2. **真值表验证**: 确保逻辑运算结果符合真值表
> 3. **短路行为**: 准确模拟短路求值的执行顺序
> 4. **边界情况**: 特别关注NULL、0、EOF等特殊值
> 
> ### 输出格式
> 为每个变式生成完整的JSON格式，包含：
> - 唯一ID（SL-BL-S00X-VYY格式）
> - 完整的metadata（标注变式类型和源种子）
> - 清晰的task描述和代码
> - 正确的布尔值答案（true/false）
> 
> ### 质量检查要点
> 1. **逻辑正确性**: 确保布尔表达式计算正确
> 2. **语法合规性**: 确保C语言语法正确
> 3. **测试价值**: 每个变式应该测试特定的布尔推理能力
> 4. **陷阱设计**: 适当设计容易出错的逻辑陷阱
> 
> ## 示例变式类型
> 
> ### 基于SL-BL-S001的变式示例：
> - **逻辑运算符变式**: 将 || 改为 &&
> - **德摩根变式**: !(inbuffer != NULL && insize != 0)
> - **短路求值变式**: 调换条件顺序测试短路行为
> - **边界值变式**: insize使用0、1、-1等边界值
> - **语言移植变式**: 转换为Python的None和0比较
> 
> ### 基于SL-BL-S005的变式示例：
> - **复杂化变式**: 增加第三个状态的OR条件
> - **宏展开变式**: 直接使用数字替代宏定义
> - **嵌套变式**: (state == IN_CHAR || state == IN_CHAR_SPACE) && len > 0
> - **三元运算符变式**: 使用?:运算符重写
> - **类型转换变式**: 使用不同的整数类型
> 
> 请基于此提示词，为给定的布尔运算种子任务生成完整的变式集合，确保全面覆盖布尔逻辑推理的各个方面。
> ```

```json
{
    "id": "SL-BL-S001-V01",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant1",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "logical_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `inbuffer == NULL && insize == 0` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nif (inbuffer == NULL && insize == 0) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S001-V02",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant2",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "demorgan_law",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!(inbuffer != NULL && insize != 0)` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nif (!(inbuffer != NULL && insize != 0)) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S001-V03",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant3",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "boundary_value",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `inbuffer == NULL || insize == 0` when `inbuffer` is NULL and `insize` is 0?",
        "code": "const unsigned char *inbuffer = NULL;\nunsigned long insize = 0;\nif (inbuffer == NULL || insize == 0) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S001-V04",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant4",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "short_circuit",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `insize == 0 || inbuffer == NULL` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nif (insize == 0 || inbuffer == NULL) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S001-V05",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant5",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "comparison_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `inbuffer != NULL && insize > 0` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nif (inbuffer != NULL && insize > 0) {\n    printf(\"Input is valid\");\n} else {\n    printf(\"Input validation failed\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S001-V06",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant6",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "ternary_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `inbuffer == NULL || insize == 0` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nint result = (inbuffer == NULL || insize == 0) ? 1 : 0;\nprintf(\"Result: %d\\n\", result);",
        "answer": false
    }
},
{
    "id": "SL-BL-S001-V07",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant7",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "nested_logic",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `(inbuffer == NULL || insize == 0) && validate` when `inbuffer` points to a valid buffer, `insize` is 1024, and `validate` is 1?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nint validate = 1;\nif ((inbuffer == NULL || insize == 0) && validate) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S001-V08",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant8",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "language_port_python",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code snippet, what is the value of the boolean expression `inbuffer is None or insize == 0` when `inbuffer` is a valid object and `insize` is 1024?",
        "code": "inbuffer = b'\\x01\\x02\\x03'  # Valid bytes object\ninsize = 1024\nif inbuffer is None or insize == 0:\n    print(\"Input validation failed\")\nelse:\n    print(\"Input is valid\")",
        "answer": false
    }
},
{
    "id": "SL-BL-S001-V09",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant9",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "macro_definition",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `inbuffer == INVALID_BUFFER || insize == INVALID_SIZE` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "#define INVALID_BUFFER NULL\n#define INVALID_SIZE 0\nconst unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nif (inbuffer == INVALID_BUFFER || insize == INVALID_SIZE) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S001-V10",
    "metadata": {
        "name": "StatementLevel-Boolean-S001-Variant10",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S001",
        "variant_type": "type_conversion",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!inbuffer || !insize` when `inbuffer` points to a valid buffer and `insize` is 1024?",
        "code": "const unsigned char *inbuffer = (const unsigned char *)0x10687f9;\nunsigned long insize = 1024;\nif (!inbuffer || !insize) {\n    printf(\"Input validation failed\");\n} else {\n    printf(\"Input is valid\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S002-V01",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant1",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "logical_negation",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!!data` when `data` is NULL?",
        "code": "void *data = NULL;\nsize_t size = 1024;\nif (!!data) {\n    memset(data, 0, size);\n} else {\n    return;\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S002-V02",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant2",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "comparison_operator",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `data == NULL` when `data` is NULL?",
        "code": "void *data = NULL;\nsize_t size = 1024;\nif (data == NULL) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V03",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant3",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "special_value",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!data` when `data` points to address 0x0?",
        "code": "void *data = (void *)0x0;\nsize_t size = 1024;\nif (!data) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V04",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant4",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "pointer_comparison",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!data` when `data` points to a valid memory address?",
        "code": "void *data = (void *)0x10000000;\nsize_t size = 1024;\nif (!data) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S002-V05",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant5",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "compound_condition",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!data || size == 0` when `data` is NULL and `size` is 1024?",
        "code": "void *data = NULL;\nsize_t size = 1024;\nif (!data || size == 0) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V06",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant6",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "language_port_java",
        "language": "java",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Java code snippet, what is the value of the boolean expression `data == null` when `data` is null?",
        "code": "Object data = null;\nint size = 1024;\nif (data == null) {\n    return;\n} else {\n    System.out.println(\"Processing data\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V06",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant6",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "language_port_java",
        "language": "java",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Java code snippet, what is the value of the boolean expression `data == null` when `data` is null?",
        "code": "Object data = null;\nint size = 1024;\nif (data == null) {\n    return;\n} else {\n    System.out.println(\"Processing data\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V07",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant7",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "macro_definition",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `IS_INVALID(data)` when `data` is NULL?",
        "code": "#define IS_INVALID(ptr) (!(ptr))\nvoid *data = NULL;\nsize_t size = 1024;\nif (IS_INVALID(data)) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V08",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant8",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "type_cast",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!(char *)data` when `data` is NULL?",
        "code": "void *data = NULL;\nsize_t size = 1024;\nif (!(char *)data) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V09",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant9",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "ternary_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!data` when `data` is NULL?",
        "code": "void *data = NULL;\nsize_t size = 1024;\nint should_return = !data ? 1 : 0;\nif (should_return) {\n    return;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S002-V10",
    "metadata": {
        "name": "StatementLevel-Boolean-S002-Variant10",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S002",
        "variant_type": "short_circuit_side_effect",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!data || ++counter > 0` when `data` is NULL and `counter` is 0?",
        "code": "void *data = NULL;\nsize_t size = 1024;\nint counter = 0;\nif (!data || ++counter > 0) {\n    return;\n} else {\n    memset(data, 0, size);\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S003-V01",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant1",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "comparison_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `res == DW_DLV_OK` when `res` is -1 and `DW_DLV_OK` is 0?",
        "code": "int res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nif (res == DW_DLV_OK) {\n    printf(\"Operation succeeded\");\n} else {\n    printf(\"Operation failed\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S003-V02",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant2",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "boundary_value",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `res != DW_DLV_OK` when `res` is 0 and `DW_DLV_OK` is 0?",
        "code": "int res = 0;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nif (res != DW_DLV_OK) {\n    printf(\"Operation failed\");\n    return DW_DLV_ERROR;\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S003-V03",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant3",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "compound_condition",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `res != DW_DLV_OK && res != DW_DLV_NO_ENTRY` when `res` is -1, `DW_DLV_OK` is 0, and `DW_DLV_NO_ENTRY` is 1?",
        "code": "int res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nconst int DW_DLV_NO_ENTRY = 1;\nif (res != DW_DLV_OK && res != DW_DLV_NO_ENTRY) {\n    printf(\"Operation failed with error\");\n    return DW_DLV_ERROR;\n}",
        "answer": true
    }
}, 
{
    "id": "SL-BL-S003-V04",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant4",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "enum_comparison",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `res != DW_DLV_OK` when `res` is DW_DLV_ERROR and `DW_DLV_OK` is 0?",
        "code": "typedef enum {\n    DW_DLV_OK = 0,\n    DW_DLV_ERROR = -1,\n    DW_DLV_NO_ENTRY = 1\n} Dwarf_Error;\nDwarf_Error res = DW_DLV_ERROR;\nif (res != DW_DLV_OK) {\n    printf(\"Operation failed\");\n    return DW_DLV_ERROR;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S003-V05",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant5",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "negative_comparison",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `res < 0` when `res` is -1?",
        "code": "int res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nif (res < 0) {\n    printf(\"Operation failed\");\n    return DW_DLV_ERROR;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S003-V06",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant6",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "macro_expansion",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `IS_ERROR(res)` when `res` is -1?",
        "code": "#define IS_ERROR(x) ((x) != 0)\nint res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nif (IS_ERROR(res)) {\n    printf(\"Operation failed\");\n    return DW_DLV_ERROR;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S003-V07",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant7",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "logical_negation",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!(res == DW_DLV_OK)` when `res` is -1 and `DW_DLV_OK` is 0?",
        "code": "int res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nif (!(res == DW_DLV_OK)) {\n    printf(\"Operation failed\");\n    return DW_DLV_ERROR;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S003-V08",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant8",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "ternary_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `res != DW_DLV_OK` when `res` is -1 and `DW_DLV_OK` is 0?",
        "code": "int res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nint result = (res != DW_DLV_OK) ? DW_DLV_ERROR : DW_DLV_OK;\nprintf(\"Result: %d\\n\", result);",
        "answer": true
    }
},
{
    "id": "SL-BL-S003-V09",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant9",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "language_port_python",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code snippet, what is the value of the boolean expression `res != DW_DLV_OK` when `res` is -1 and `DW_DLV_OK` is 0?",
        "code": "res = -1\nDW_DLV_OK = 0\nDW_DLV_ERROR = -1\nif res != DW_DLV_OK:\n    print(\"Operation failed\")\n    return DW_DLV_ERROR",
        "answer": true
    }
},
{
    "id": "SL-BL-S003-V10",
    "metadata": {
        "name": "StatementLevel-Boolean-S003-Variant10",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S003",
        "variant_type": "type_conversion",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `(unsigned int)res != (unsigned int)DW_DLV_OK` when `res` is -1 and `DW_DLV_OK` is 0?",
        "code": "int res = -1;\nconst int DW_DLV_OK = 0;\nconst int DW_DLV_ERROR = -1;\nif ((unsigned int)res != (unsigned int)DW_DLV_OK) {\n    printf(\"Operation failed\");\n    return DW_DLV_ERROR;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V01",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant1",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "comparison_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `c >= 0x80` when `c` is 65 (ASCII 'A')?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nif (c >= 0x80) {\n    printf(\"Non-ASCII character\");\n} else {\n    printf(\"ASCII character\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S004-V02",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant2",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "boundary_value",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `c < 0x80` when `c` is 128 (0x80)?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 128;  // 0x80\nif (c < 0x80) {\n    printf(\"ASCII character\");\n} else {\n    printf(\"Non-ASCII character\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S004-V03",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant3",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "hex_comparison",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `c < 0xFF` when `c` is 65 (ASCII 'A')?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nif (c < 0xFF) {\n    printf(\"Single byte character\");\n} else {\n    printf(\"Multi-byte character\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V04",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant4",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "range_check",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `c >= 0x20 && c < 0x80` when `c` is 65 (ASCII 'A')?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nif (c >= 0x20 && c < 0x80) {\n    printf(\"Printable ASCII character\");\n} else {\n    printf(\"Non-printable or non-ASCII character\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V05",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant5",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "logical_negation",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!(c >= 0x80)` when `c` is 65 (ASCII 'A')?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nif (!(c >= 0x80)) {\n    printf(\"ASCII character\");\n} else {\n    printf(\"Non-ASCII character\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V06",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant6",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "macro_definition",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `IS_ASCII(c)` when `c` is 65 (ASCII 'A')?",
        "code": "#define ASCII_MAX 0x80\n#define IS_ASCII(x) ((x) < ASCII_MAX)\ntypedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nif (IS_ASCII(c)) {\n    printf(\"ASCII character\");\n} else {\n    printf(\"Non-ASCII character\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V07",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant7",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "type_conversion",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `(char)c < (char)0x80` when `c` is 65 (ASCII 'A')?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nif ((char)c < (char)0x80) {\n    printf(\"ASCII character\");\n} else {\n    printf(\"Non-ASCII character\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V08",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant8",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "ternary_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `c < 0x80` when `c` is 65 (ASCII 'A')?",
        "code": "typedef unsigned int krb5_ucs4;\nkrb5_ucs4 c = 65;  // ASCII 'A'\nconst char* type = (c < 0x80) ? \"ASCII\" : \"Non-ASCII\";\nprintf(\"%s character\\n\", type);",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V09",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant9",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "language_port_javascript",
        "language": "javascript",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following JavaScript code snippet, what is the value of the boolean expression `c < 0x80` when `c` is 65 (ASCII 'A')?",
        "code": "let c = 65;  // ASCII 'A'\nif (c < 0x80) {\n    console.log(\"ASCII character\");\n} else {\n    console.log(\"Non-ASCII character\");\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S004-V10",
    "metadata": {
        "name": "StatementLevel-Boolean-S004-Variant10",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S004",
        "variant_type": "overflow_boundary",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `c < 0x80` when `c` is 255 (0xFF)?",
        "code": "typedef unsigned char krb5_ucs4;\nkrb5_ucs4 c = 255;  // 0xFF\nif (c < 0x80) {\n    printf(\"ASCII character\");\n} else {\n    printf(\"Non-ASCII character\");\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S005-V01",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant1",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "logical_operator",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `state == IN_CHAR && state == IN_CHAR_SPACE` when `state` is 1, `IN_CHAR` is 1, and `IN_CHAR_SPACE` is 2?",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\nint state = 1;\nint len = 5;\nif (state == IN_CHAR && state == IN_CHAR_SPACE) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": false
    }
},
{
    "id": "SL-BL-S005-V02",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant2",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "macro_expansion",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `state == 1 || state == 2` when `state` is 1?",
        "code": "int state = 1;\nint len = 5;\nif (state == 1 || state == 2) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V03",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant3",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "complexity_increase",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `state == IN_CHAR || state == IN_CHAR_SPACE || state == IN_WORD` when `state` is 1, `IN_CHAR` is 1, `IN_CHAR_SPACE` is 2, and `IN_WORD` is 3?",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\n#define IN_WORD 3\nint state = 1;\nint len = 5;\nif (state == IN_CHAR || state == IN_CHAR_SPACE || state == IN_WORD) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V04",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant4",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "nested_logic",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `(state == IN_CHAR || state == IN_CHAR_SPACE) && len > 0` when `state` is 1, `IN_CHAR` is 1, `IN_CHAR_SPACE` is 2, and `len` is 5?",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\nint state = 1;\nint len = 5;\nif ((state == IN_CHAR || state == IN_CHAR_SPACE) && len > 0) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V05",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant5",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "short_circuit",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `state == IN_CHAR_SPACE || state == IN_CHAR` when `state` is 1, `IN_CHAR` is 1, and `IN_CHAR_SPACE` is 2?",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\nint state = 1;\nint len = 5;\nif (state == IN_CHAR_SPACE || state == IN_CHAR) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V06",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant6",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "enum_definition",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `state == IN_CHAR || state == IN_CHAR_SPACE` when `state` is IN_CHAR?",
        "code": "typedef enum {\n    IN_CHAR = 1,\n    IN_CHAR_SPACE = 2,\n    OUT_WORD = 0\n} State;\nState state = IN_CHAR;\nint len = 5;\nif (state == IN_CHAR || state == IN_CHAR_SPACE) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V07",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant7",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "ternary_operator",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `state == IN_CHAR || state == IN_CHAR_SPACE` when `state` is 1, `IN_CHAR` is 1, and `IN_CHAR_SPACE` is 2?",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\nint state = 1;\nint len = 5;\nint result = (state == IN_CHAR || state == IN_CHAR_SPACE) ? len : 0;\nreturn result;",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V08",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant8",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "logical_negation",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `!(state != IN_CHAR && state != IN_CHAR_SPACE)` when `state` is 1, `IN_CHAR` is 1, and `IN_CHAR_SPACE` is 2?",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\nint state = 1;\nint len = 5;\nif (!(state != IN_CHAR && state != IN_CHAR_SPACE)) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V09",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant9",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "language_port_python",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code snippet, what is the value of the boolean expression `state == IN_CHAR or state == IN_CHAR_SPACE` when `state` is 1, `IN_CHAR` is 1, and `IN_CHAR_SPACE` is 2?",
        "code": "IN_CHAR = 1\nIN_CHAR_SPACE = 2\nstate = 1\nlength = 5\nif state == IN_CHAR or state == IN_CHAR_SPACE:\n    return length\nelse:\n    return 0",
        "answer": true
    }
},
{
    "id": "SL-BL-S005-V10",
    "metadata": {
        "name": "StatementLevel-Boolean-S005-Variant10",
        "category": "Statement-Level",
        "subcategory": "Boolean",
        "type": "variant",
        "source_seed": "SL-BL-S005",
        "variant_type": "chain_comparison",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the value of the boolean expression `IN_CHAR <= state <= IN_CHAR_SPACE` when `state` is 1, `IN_CHAR` is 1, and `IN_CHAR_SPACE` is 2? (Note: This is not valid C syntax, but evaluates as `(IN_CHAR <= state) <= IN_CHAR_SPACE`)",
        "code": "#define IN_CHAR 1\n#define IN_CHAR_SPACE 2\nint state = 1;\nint len = 5;\n// This evaluates as: (IN_CHAR <= state) <= IN_CHAR_SPACE\n// Which is: (1 <= 1) <= 2, i.e., 1 <= 2\nif (IN_CHAR <= state <= IN_CHAR_SPACE) {\n    return len;\n} else {\n    return 0;\n}",
        "answer": true
    }
}
```

#### 1C - API/函数调用 [ API/Function Call ] (57)

> ```
> ## 任务目标
> 基于给定的API/函数调用种子任务，生成多样化的变式任务来全面测试大模型对函数调用行为、返回值、参数传递和API语义的理解能力。
> 
> ## 变式生成维度
> 
> ### 1. 函数类别变式
> - **标准库函数变式**: string.h, math.h, stdio.h, stdlib.h等标准库函数
> - **系统调用变式**: unistd.h, sys/types.h等系统级API
> - **内存管理变式**: malloc, calloc, realloc, free等内存相关函数
> - **文件操作变式**: fopen, fread, fwrite, fclose等文件I/O函数
> - **字符串处理变式**: strlen, strcmp, strcpy, strcat等字符串函数
> - **数学函数变式**: pow, sqrt, sin, cos, log等数学计算函数
> 
> ### 2. 参数类型变式
> - **基础类型参数**: int, float, double, char等基础数据类型
> - **指针参数变式**: char*, void*, 函数指针等指针类型参数
> - **结构体参数变式**: 传递结构体、结构体指针作为参数
> - **数组参数变式**: 数组作为参数的传递和处理
> - **可变参数变式**: printf, scanf等可变参数函数
> - **常量参数变式**: const修饰的参数传递
> 
> ### 3. 返回值类型变式
> - **基础返回值变式**: 返回int, float, double等基础类型
> - **指针返回值变式**: 返回指针（包括NULL的情况）
> - **特殊返回值变式**: 返回typedef定义的类型（如pid_t, size_t）
> - **错误码返回变式**: 返回错误状态码或成功/失败标志
> - **无返回值变式**: void函数的副作用分析
> - **复合返回值变式**: 返回结构体或联合体
> 
> ### 4. 边界条件变式
> - **空值输入变式**: NULL指针、空字符串、零长度参数
> - **边界值变式**: 最大值、最小值、临界值作为参数
> - **缓冲区边界变式**: 缓冲区大小限制相关的函数调用
> - **内存不足变式**: malloc等函数在内存不足时的行为
> - **文件不存在变式**: 文件操作函数处理不存在文件的情况
> - **权限错误变式**: 权限不足时的函数行为
> 
> ### 5. 错误处理变式
> - **成功场景变式**: 函数正常执行的返回值和行为
> - **失败场景变式**: 函数执行失败时的错误处理
> - **异常输入变式**: 非法参数、越界访问等异常情况
> - **资源限制变式**: 系统资源限制导致的函数失败
> - **并发问题变式**: 多线程环境下的函数行为
> 
> ### 6. 副作用分析变式
> - **内存修改变式**: 函数对传入指针指向内存的修改
> - **全局状态变式**: 函数对全局变量或系统状态的影响
> - **文件状态变式**: 文件操作函数对文件状态的改变
> - **缓冲区修改变式**: 函数对缓冲区内容的修改和影响
> - **输出副作用变式**: printf等输出函数的副作用
> 
> ### 7. 精度和格式变式
> - **数值精度变式**: 浮点数计算的精度问题
> - **格式字符串变式**: printf/scanf格式说明符的变化
> - **类型转换变式**: 参数类型转换对函数行为的影响
> - **编码变式**: 字符编码相关的函数行为
> - **字节序变式**: 大小端对函数行为的影响
> 
> ### 8. 平台相关变式
> - **sizeof变式**: 不同平台下sizeof的不同结果
> - **类型大小变式**: int, long, pointer等类型在不同平台的大小
> - **路径分隔符变式**: 文件路径在不同系统下的表示
> - **换行符变式**: 不同系统的换行符处理
> - **API可用性变式**: 某些API在特定平台的可用性
> 
> ### 9. 语言移植变式
> - **C -> Python变式**: 对应Python内置函数或标准库
> - **C -> Java变式**: 对应Java标准库方法
> - **C -> JavaScript变式**: 对应JavaScript内置函数
> - **跨语言语义变式**: 相同功能在不同语言中的行为差异
> 
> ### 10. 复杂度变式
> - **简化变式**: 单一函数调用，直接参数
> - **复合变式**: 嵌套函数调用，函数作为参数
> - **链式调用变式**: 函数返回值作为另一个函数的参数
> - **条件调用变式**: 基于条件的函数调用选择
> 
> ## 生成规则
> 
> ### 基本要求
> 1. 每个种子任务生成8-12个变式
> 2. 确保每个变式维度至少覆盖2-3个变式
> 3. 保持API调用的核心语义，但改变具体场景
> 4. 变式难度应该涵盖easy/medium/hard三个等级
> 
> ### 难度分级标准
> - **Easy**: 标准库基础函数，常见参数，正常返回值
> - **Medium**: 复杂参数类型，错误处理，边界条件
> - **Hard**: 嵌套调用，特殊场景，平台相关行为，复杂副作用
> 
> ### 特殊考虑点
> 1. **API文档准确性**: 确保函数行为符合标准库文档
> 2. **平台一致性**: 明确指定假设的平台环境（如sizeof值）
> 3. **错误处理**: 准确模拟各种错误情况的函数行为
> 4. **内存安全**: 正确处理指针和内存相关的函数调用
> 
> ### 输出格式
> 为每个变式生成完整的JSON格式，包含：
> - 唯一ID（SL-API-S00X-VYY格式）
> - 完整的metadata（标注变式类型和源种子）
> - 清晰的task描述和代码
> - 准确的答案（数值、字符串、类型名或特殊值如NULL）
> 
> ### 质量检查要点
> 1. **API正确性**: 确保函数调用语法和语义正确
> 2. **返回值准确性**: 确保返回值计算和类型正确
> 3. **边界情况**: 充分测试各种边界和异常情况
> 4. **实用性**: 每个变式应该测试实际编程中的常见场景
> 
> ## 示例变式类型
> 
> ### 基于SL-API-S001（strlen）的变式示例：
> - **边界值变式**: 空字符串""的strlen返回值
> - **复合调用变式**: strlen(strcpy(dest, src))的嵌套调用
> - **内存安全变式**: strlen(NULL)的未定义行为
> - **编码变式**: 包含多字节字符的字符串长度
> - **语言移植变式**: Python的len()函数对应行为
> 
> ### 基于SL-API-S003（malloc）的变式示例：
> - **失败场景变式**: malloc(SIZE_MAX)返回NULL
> - **零大小变式**: malloc(0)的实现定义行为
> - **对齐变式**: malloc返回内存的对齐要求
> - **calloc比较变式**: calloc vs malloc的区别
> - **内存泄漏变式**: 忘记free的后果分析
> 
> ### 基于SL-API-S007（snprintf）的变式示例：
> - **缓冲区溢出变式**: 格式化字符串超过缓冲区大小
> - **格式说明符变式**: 不同的%格式符的行为
> - **返回值语义变式**: 返回值的精确含义
> - **NULL缓冲区变式**: 缓冲区为NULL时的行为
> - **精度控制变式**: %.2f等精度控制的效果
> 
> 请基于此提示词，为给定的API/函数调用种子任务生成完整的变式集合，确保全面覆盖函数调用推理的各个方面。
> ```

```json
{
    "id": "SL-API-S001-V01",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "边界条件变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of the function call `strlen(str)` when `str` is an empty string \"\"?",
        "code": "#include <string.h>\nchar *str = \"\";\nsize_t len = strlen(str);\nprintf(\"Length: %zu\\n\", len);",
        "answer": 0
    }
},
{
    "id": "SL-API-S001-V02",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "复合调用变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of the nested function call `strlen(strcpy(dest, src))` when `src` is \"world\"?",
        "code": "#include <string.h>\nchar src[] = \"world\";\nchar dest[10];\nsize_t len = strlen(strcpy(dest, src));\nprintf(\"Length: %zu\\n\", len);",
        "answer": 5
    }
},
{
    "id": "SL-API-S001-V03",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "错误处理变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what happens when `strlen(NULL)` is called?",
        "code": "#include <string.h>\nchar *str = NULL;\n// strlen(str); // This would cause undefined behavior\nprintf(\"This is undefined behavior\\n\");",
        "answer": "undefined behavior"
    }
},
{
    "id": "SL-API-S001-V04",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "字符串处理变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strlen(str)` when `str` contains escape characters \"hello\\nworld\"?",
        "code": "#include <string.h>\nchar *str = \"hello\\nworld\";\nsize_t len = strlen(str);\nprintf(\"Length: %zu\\n\", len);",
        "answer": 11
    }
},
{
    "id": "SL-API-S001-V05",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "数组参数变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with a character array, what is the return value of `strlen(arr)`?",
        "code": "#include <string.h>\nchar arr[] = {'h', 'e', 'l', 'l', 'o', '\\0'};\nsize_t len = strlen(arr);\nprintf(\"Length: %zu\\n\", len);",
        "answer": 5
    }
},
{
    "id": "SL-API-S001-V06",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "常量参数变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with a const string, what is the return value of `strlen(str)`?",
        "code": "#include <string.h>\nconst char *str = \"programming\";\nsize_t len = strlen(str);\nprintf(\"Length: %zu\\n\", len);",
        "answer": 11
    }
},
{
    "id": "SL-API-S001-V07",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "返回值类型变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the data type returned by `strlen(str)`?",
        "code": "#include <string.h>\nchar *str = \"test\";\nauto len = strlen(str); // What type is len?\nprintf(\"Length: %zu\\n\", len);",
        "answer": "size_t"
    }
},
{
    "id": "SL-API-S001-V08",
    "metadata": {
        "name": "StatementLevel-APICall-Seed1-Variant8",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S001",
        "variant_type": "语言移植变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code equivalent to the C strlen function, what is the return value of `len(s)` when `s` is \"hello\"?",
        "code": "s = \"hello\"\nlength = len(s)\nprint(f\"Length: {length}\")",
        "answer": 5
    }
},
{
    "id": "SL-API-S002-V01",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "边界值变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `pow(2.0, 0)` when the exponent is 0?",
        "code": "#include <math.h>\ndouble base = 2.0;\nint exponent = 0;\ndouble result = pow(base, exponent);\nprintf(\"Result: %.1f\\n\", result);",
        "answer": 1.0
    }
},
{
    "id": "SL-API-S002-V02",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "负数指数变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `pow(2.0, -2)` when the exponent is negative?",
        "code": "#include <math.h>\ndouble base = 2.0;\nint exponent = -2;\ndouble result = pow(base, exponent);\nprintf(\"Result: %.2f\\n\", result);",
        "answer": 0.25
    }
},
{
    "id": "SL-API-S002-V03",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "特殊值变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `pow(0.0, 0.0)`?",
        "code": "#include <math.h>\ndouble base = 0.0;\ndouble exponent = 0.0;\ndouble result = pow(base, exponent);\nprintf(\"Result: %.1f\\n\", result);",
        "answer": 1.0
    }
},
{
    "id": "SL-API-S002-V04",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "浮点精度变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `pow(1.5, 3.0)` with floating point precision?",
        "code": "#include <math.h>\ndouble base = 1.5;\ndouble exponent = 3.0;\ndouble result = pow(base, exponent);\nprintf(\"Result: %.3f\\n\", result);",
        "answer": 3.375
    }
},
{
    "id": "SL-API-S002-V05",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "错误处理变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `pow(-1.0, 0.5)` when taking square root of negative number?",
        "code": "#include <math.h>\n#include <math.h>\ndouble base = -1.0;\ndouble exponent = 0.5;\ndouble result = pow(base, exponent);\n// This returns NaN (Not a Number)\nprintf(\"Result: %f\\n\", result);",
        "answer": "NaN"
    }
},
{
    "id": "SL-API-S002-V06",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "链式调用变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of the nested `pow(pow(2.0, 2), 2)` call?",
        "code": "#include <math.h>\ndouble result = pow(pow(2.0, 2), 2);\nprintf(\"Result: %.0f\\n\", result);",
        "answer": 16.0
    }
},
{
    "id": "SL-API-S002-V07",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "类型转换变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with integer arguments, what is the return value of `pow(3, 4)`?",
        "code": "#include <math.h>\nint base = 3;\nint exponent = 4;\ndouble result = pow(base, exponent); // integers promoted to double\nprintf(\"Result: %.0f\\n\", result);",
        "answer": 81.0
    }
},
{
    "id": "SL-API-S002-V08",
    "metadata": {
        "name": "StatementLevel-APICall-Seed2-Variant8",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S002",
        "variant_type": "语言移植变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code equivalent to the C pow function, what is the return value of `pow(2.0, 3)` or `2.0 ** 3`?",
        "code": "base = 2.0\nexponent = 3\nresult = pow(base, exponent)\n# or result = base ** exponent\nprint(f\"Result: {result}\")",
        "answer": 8.0
    }
},
{
    "id": "SL-API-S003-V01",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "零大小变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the behavior of `malloc(0)` when requesting zero bytes?",
        "code": "#include <stdlib.h>\nvoid *ptr = malloc(0);\nif (ptr == NULL) {\n    printf(\"malloc(0) returned NULL\\n\");\n} else {\n    printf(\"malloc(0) returned non-NULL\\n\");\n    free(ptr);\n}",
        "answer": "implementation-defined"
    }
},
{
    "id": "SL-API-S003-V02",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "失败场景变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what does `malloc(SIZE_MAX)` return when requesting maximum possible size?",
        "code": "#include <stdlib.h>\n#include <stdint.h>\nvoid *ptr = malloc(SIZE_MAX);\nif (ptr == NULL) {\n    printf(\"Memory allocation failed\\n\");\n} else {\n    printf(\"Memory allocation succeeded\\n\");\n    free(ptr);\n}",
        "answer": "NULL"
    }
},
{
    "id": "SL-API-S003-V03",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "calloc比较变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, how many bytes does `calloc(10, sizeof(int))` allocate, assuming sizeof(int) is 4?",
        "code": "#include <stdlib.h>\n// Assume sizeof(int) = 4 bytes\nint *arr = (int *)calloc(10, sizeof(int));\nif (arr != NULL) {\n    printf(\"Memory allocated and initialized to zero\\n\");\n    free(arr);\n}",
        "answer": 40
    }
},
{
    "id": "SL-API-S003-V04",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "对齐变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the minimum alignment guarantee for the pointer returned by `malloc(1)`?",
        "code": "#include <stdlib.h>\nvoid *ptr = malloc(1);\nif (ptr != NULL) {\n    printf(\"Pointer alignment: suitable for any object\\n\");\n    free(ptr);\n}",
        "answer": "max_align_t"
    }
},
{
    "id": "SL-API-S003-V05",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "realloc变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, how many bytes does `realloc(ptr, 80)` allocate when expanding from 40 bytes?",
        "code": "#include <stdlib.h>\nint *ptr = (int *)malloc(sizeof(int) * 10); // 40 bytes\nptr = (int *)realloc(ptr, sizeof(int) * 20);  // Expand to 20 ints\nif (ptr != NULL) {\n    printf(\"Memory reallocated\\n\");\n    free(ptr);\n}",
        "answer": 80
    }
},
{
    "id": "SL-API-S003-V06",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "平台相关变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet on a 64-bit platform, how many bytes does `malloc(sizeof(long) * 5)` allocate assuming sizeof(long) is 8?",
        "code": "#include <stdlib.h>\n// Assume 64-bit platform: sizeof(long) = 8 bytes\nlong *arr = (long *)malloc(sizeof(long) * 5);\nif (arr != NULL) {\n    printf(\"Memory allocated for 5 longs\\n\");\n    free(arr);\n}",
        "answer": 40
    }
},
{
    "id": "SL-API-S003-V07",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "结构体参数变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with a struct, how many bytes does `malloc(sizeof(struct Point) * 3)` allocate?",
        "code": "#include <stdlib.h>\nstruct Point {\n    int x;  // 4 bytes\n    int y;  // 4 bytes\n}; // Total: 8 bytes per struct\nstruct Point *points = (struct Point *)malloc(sizeof(struct Point) * 3);\nif (points != NULL) {\n    printf(\"Memory allocated for 3 points\\n\");\n    free(points);\n}",
        "answer": 24
    }
},
{
    "id": "SL-API-S003-V08",
    "metadata": {
        "name": "StatementLevel-APICall-Seed3-Variant8",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S003",
        "variant_type": "返回值类型变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return type of the `malloc()` function?",
        "code": "#include <stdlib.h>\nvoid *ptr = malloc(100);\nif (ptr != NULL) {\n    printf(\"malloc returns void pointer\\n\");\n    free(ptr);\n}",
        "answer": "void *"
    }
},
{
    "id": "SL-API-S004-V01",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "相关系统调用变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what type of value does the function call `getppid()` return?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\npid_t parent_pid = getppid();\nprintf(\"Parent Process ID: %d\\n\", parent_pid);",
        "answer": "pid_t"
    }
},
{
    "id": "SL-API-S004-V02",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "用户ID变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what type of value does the function call `getuid()` return?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\nuid_t user_id = getuid();\nprintf(\"User ID: %d\\n\", user_id);",
        "answer": "uid_t"
    }
},
{
    "id": "SL-API-S004-V03",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "组ID变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what type of value does the function call `getgid()` return?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\ngid_t group_id = getgid();\nprintf(\"Group ID: %d\\n\", group_id);",
        "answer": "gid_t"
    }
},
{
    "id": "SL-API-S004-V04",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "错误处理变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, can the function call `getpid()` ever fail and return an error?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\npid_t current_pid = getpid();\n// getpid() never fails\nprintf(\"Process ID: %d\\n\", current_pid);",
        "answer": "no"
    }
},
{
    "id": "SL-API-S004-V05",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "fork变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what type of value does the function call `fork()` return to identify the child process?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\npid_t child_pid = fork();\nif (child_pid == 0) {\n    printf(\"This is the child process\\n\");\n} else if (child_pid > 0) {\n    printf(\"This is the parent, child PID: %d\\n\", child_pid);\n}",
        "answer": "pid_t"
    }
},
{
    "id": "SL-API-S004-V06",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "参数传递变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, how many parameters does the function call `getpid()` take?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\npid_t current_pid = getpid(); // No parameters\nprintf(\"Process ID: %d\\n\", current_pid);",
        "answer": 0
    }
},
{
    "id": "SL-API-S004-V07",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "平台相关变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the typical size of `pid_t` on most modern Unix systems?",
        "code": "#include <unistd.h>\n#include <sys/types.h>\npid_t current_pid = getpid();\nprintf(\"PID size: %zu bytes\\n\", sizeof(pid_t));",
        "answer": 4
    }
},
{
    "id": "SL-API-S004-V08",
    "metadata": {
        "name": "StatementLevel-APICall-Seed4-Variant8",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S004",
        "variant_type": "语言移植变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code equivalent to the C getpid function, what type does `os.getpid()` return?",
        "code": "import os\ncurrent_pid = os.getpid()\nprint(f\"Process ID: {current_pid}\")",
        "answer": "int"
    }
},
{
    "id": "SL-API-S005-V01",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "相等字符串变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strcmp(str1, str2)` when both strings are identical?",
        "code": "#include <string.h>\nchar *str1 = \"hello\";\nchar *str2 = \"hello\";\nint result = strcmp(str1, str2);\nprintf(\"Comparison result: %d\\n\", result);",
        "answer": 0
    }
},
{
    "id": "SL-API-S005-V02",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "大小写敏感变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strcmp(str1, str2)` when comparing \"Hello\" and \"hello\"?",
        "code": "#include <string.h>\nchar *str1 = \"Hello\";\nchar *str2 = \"hello\";\nint result = strcmp(str1, str2);\nprintf(\"Comparison result: %d\\n\", result);",
        "answer": -1
    }
},
{
    "id": "SL-API-S005-V03",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "空字符串变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strcmp(str1, str2)` when `str1` is empty and `str2` is \"test\"?",
        "code": "#include <string.h>\nchar *str1 = \"\";\nchar *str2 = \"test\";\nint result = strcmp(str1, str2);\nprintf(\"Comparison result: %d\\n\", result);",
        "answer": -1
    }
},
{
    "id": "SL-API-S005-V04",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "strncmp变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strncmp(str1, str2, 3)` when comparing first 3 characters?",
        "code": "#include <string.h>\nchar *str1 = \"application\";\nchar *str2 = \"apple\";\nint result = strncmp(str1, str2, 3);\nprintf(\"Comparison result: %d\\n\", result);",
        "answer": 0
    }
},
{
    "id": "SL-API-S005-V05",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "strcasecmp变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strcasecmp(str1, str2)` when doing case-insensitive comparison?",
        "code": "#include <string.h>\n#include <strings.h>\nchar *str1 = \"Hello\";\nchar *str2 = \"HELLO\";\nint result = strcasecmp(str1, str2);\nprintf(\"Case-insensitive comparison: %d\\n\", result);",
        "answer": 0
    }
},
{
    "id": "SL-API-S005-V06",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "错误处理变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what happens when `strcmp(NULL, \"test\")` is called?",
        "code": "#include <string.h>\nchar *str1 = NULL;\nchar *str2 = \"test\";\n// strcmp(str1, str2); // This would cause undefined behavior\nprintf(\"Comparing NULL pointer is undefined behavior\\n\");",
        "answer": "undefined behavior"
    }
},
{
    "id": "SL-API-S005-V07",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "数值字符串变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `strcmp(str1, str2)` when comparing \"10\" and \"2\"?",
        "code": "#include <string.h>\nchar *str1 = \"10\";\nchar *str2 = \"2\";\nint result = strcmp(str1, str2);\n// Lexicographic comparison, not numeric\nprintf(\"Comparison result: %d\\n\", result);",
        "answer": -1
    }
},
{
    "id": "SL-API-S005-V08",
    "metadata": {
        "name": "StatementLevel-APICall-Seed5-Variant8",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S005",
        "variant_type": "语言移植变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code equivalent to C strcmp function, what does the comparison `str1 < str2` return when `str1` is \"apple\" and `str2` is \"banana\"?",
        "code": "str1 = \"apple\"\nstr2 = \"banana\"\nresult = str1 < str2  # Returns boolean, not integer\nprint(f\"Comparison result: {result}\")",
        "answer": "True"
    }
},
{
    "id": "SL-API-S006-V01",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "成功场景变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what type of value does `fopen(filename, \"w\")` return when successfully creating a new file?",
        "code": "#include <stdio.h>\nchar *filename = \"output.txt\";\nFILE *fp = fopen(filename, \"w\");\nif (fp != NULL) {\n    printf(\"File opened successfully for writing\\n\");\n    fclose(fp);\n}",
        "answer": "FILE *"
    }
},
{
    "id": "SL-API-S006-V02",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "权限错误变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what does `fopen(\"/root/file.txt\", \"w\")` return when a regular user lacks write permission to /root?",
        "code": "#include <stdio.h>\nchar *filename = \"/root/file.txt\";  // No write permission for regular user\nFILE *fp = fopen(filename, \"w\");\nif (fp == NULL) {\n    printf(\"Permission denied\\n\");\n} else {\n    fclose(fp);\n}",
        "answer": "NULL"
    }
},
{
    "id": "SL-API-S006-V03",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "不同模式变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what does `fopen(filename, \"a\")` do when the file already exists?",
        "code": "#include <stdio.h>\nchar *filename = \"existing.txt\";\nFILE *fp = fopen(filename, \"a\");  // Append mode\nif (fp != NULL) {\n    printf(\"File opened in append mode\\n\");\n    fclose(fp);\n}",
        "answer": "opens for appending"
    }
},
{
    "id": "SL-API-S006-V04",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "二进制模式变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the difference between `fopen(filename, \"r\")` and `fopen(filename, \"rb\")`?",
        "code": "#include <stdio.h>\nchar *filename = \"data.bin\";\nFILE *fp1 = fopen(filename, \"r\");   // Text mode\nFILE *fp2 = fopen(filename, \"rb\");  // Binary mode\nif (fp1) fclose(fp1);\nif (fp2) fclose(fp2);",
        "answer": "binary mode vs text mode"
    }
},
{
    "id": "SL-API-S006-V05",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "路径分隔符变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet on Windows, what should the path separator be in the filename for `fopen()`?",
        "code": "#include <stdio.h>\n// On Windows\nchar *filename = \"C:\\\\Users\\\\file.txt\";  // Correct Windows path\nFILE *fp = fopen(filename, \"r\");\nif (fp != NULL) {\n    printf(\"File opened on Windows\\n\");\n    fclose(fp);\n}",
        "answer": "\\\\"
    }
},
{
    "id": "SL-API-S006-V06",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "freopen变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what does `freopen(filename, \"w\", stdout)` do to the stdout stream?",
        "code": "#include <stdio.h>\nchar *filename = \"output.txt\";\nFILE *fp = freopen(filename, \"w\", stdout);\nprintf(\"This goes to the file\\n\");\nif (fp != NULL) {\n    // stdout is now redirected to file\n}",
        "answer": "redirects stdout to file"
    }
},
{
    "id": "SL-API-S006-V07",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "tmpfile变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what type of file does `tmpfile()` create?",
        "code": "#include <stdio.h>\nFILE *temp_fp = tmpfile();\nif (temp_fp != NULL) {\n    printf(\"Temporary file created\\n\");\n    // File is automatically deleted when closed\n    fclose(temp_fp);\n}",
        "answer": "temporary file"
    }
},
{
    "id": "SL-API-S006-V08",
    "metadata": {
        "name": "StatementLevel-APICall-Seed6-Variant8",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S006",
        "variant_type": "语言移植变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code equivalent to C fopen function, what does `open(filename, 'r')` return when the file doesn't exist?",
        "code": "filename = \"nonexistent.txt\"\ntry:\n    fp = open(filename, 'r')\n    print(\"File opened successfully\")\n    fp.close()\nexcept FileNotFoundError:\n    print(\"File not found\")",
        "answer": "FileNotFoundError"
    }
},
{
    "id": "SL-API-S007-V01",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant1",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "缓冲区溢出变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `snprintf(buffer, size, format, value)` when the formatted string exceeds buffer size?",
        "code": "#include <stdio.h>\nchar buffer[5];\nint size = sizeof(buffer);\nconst char *format = \"%d\";\nint value = 123456789;  // This will exceed buffer size\nint result = snprintf(buffer, size, format, value);\nprintf(\"Buffer: %.4s, Result: %d\\n\", buffer, result);",
        "answer": 9
    }
},
{
    "id": "SL-API-S007-V02",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant2",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "格式说明符变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `snprintf()` when formatting a float with precision?",
        "code": "#include <stdio.h>\nchar buffer[20];\nint size = sizeof(buffer);\nconst char *format = \"%.2f\";\ndouble value = 3.14159;\nint result = snprintf(buffer, size, format, value);\nprintf(\"Buffer: %s, Result: %d\\n\", buffer, result);",
        "answer": 4
    }
},
{
    "id": "SL-API-S007-V03",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant3",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "NULL缓冲区变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `snprintf(NULL, 0, format, value)` when buffer is NULL and size is 0?",
        "code": "#include <stdio.h>\nconst char *format = \"%s %d\";\nchar *str = \"Hello\";\nint num = 42;\nint result = snprintf(NULL, 0, format, str, num);\n// This returns the number of characters that would be written\nprintf(\"Required buffer size: %d\\n\", result);",
        "answer": 8
    }
},
{
    "id": "SL-API-S007-V04",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant4",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "sprintf比较变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the key safety difference between `sprintf()` and `snprintf()`?",
        "code": "#include <stdio.h>\nchar buffer[10];\n// sprintf(buffer, \"%d\", 123456789);  // Unsafe - no bounds checking\nint result = snprintf(buffer, sizeof(buffer), \"%d\", 123456789);  // Safe\nprintf(\"snprintf is bounds-checked\\n\");",
        "answer": "bounds checking"
    }
},
{
    "id": "SL-API-S007-V05",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant5",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "多参数变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `snprintf()` with multiple format specifiers?",
        "code": "#include <stdio.h>\nchar buffer[30];\nint size = sizeof(buffer);\nconst char *format = \"%s: %d years old\";\nchar *name = \"Alice\";\nint age = 25;\nint result = snprintf(buffer, size, format, name, age);\nprintf(\"Buffer: %s, Result: %d\\n\", buffer, result);",
        "answer": 17
    }
},
{
    "id": "SL-API-S007-V06",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant6",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "十六进制格式变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what is the return value of `snprintf()` when formatting an integer as hexadecimal?",
        "code": "#include <stdio.h>\nchar buffer[20];\nint size = sizeof(buffer);\nconst char *format = \"0x%x\";\nint value = 255;\nint result = snprintf(buffer, size, format, value);\nprintf(\"Buffer: %s, Result: %d\\n\", buffer, result);",
        "answer": 4
    }
},
{
    "id": "SL-API-S007-V07",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant7",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "零大小缓冲区变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what happens when `snprintf()` is called with size = 1 (only space for null terminator)?",
        "code": "#include <stdio.h>\nchar buffer[1];\nint size = 1;  // Only space for null terminator\nconst char *format = \"%d\";\nint value = 42;\nint result = snprintf(buffer, size, format, value);\nprintf(\"Buffer contains: '%s', Result: %d\\n\", buffer, result);",
        "answer": 2
    }
},
{
    "id": "SL-API-S007-V08",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant8",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "语言移植变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following Python code equivalent to C snprintf function, what does string formatting with f-strings return?",
        "code": "value = 12345\nformatted = f\"{value}\"\nprint(f\"Formatted: {formatted}, Length: {len(formatted)}\")",
        "answer": "string object"
    }
},
{
    "id": "SL-API-S007-V09",
    "metadata": {
        "name": "StatementLevel-APICall-Seed7-Variant9",
        "category": "Statement-Level",
        "subcategory": "API Call",
        "type": "variant",
        "source_seed": "SL-API-S007",
        "variant_type": "vsnprintf变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet, what additional parameter does `vsnprintf()` require compared to `snprintf()`?",
        "code": "#include <stdio.h>\n#include <stdarg.h>\nint my_printf(char *buffer, size_t size, const char *format, ...) {\n    va_list args;\n    va_start(args, format);\n    int result = vsnprintf(buffer, size, format, args);\n    va_end(args);\n    return result;\n}",
        "answer": "va_list"
    }
}
```

#### 1D - 变量赋值 [ Assignment ] (80)

> ```
> # 变量赋值变式生成提示词
> 
> ## 任务目标
> 基于给定的变量赋值种子任务，生成多样化的变式任务来全面测试大模型对赋值操作语义、变量状态变化、内存引用和数据流的理解能力。
> 
> ## 变式生成维度
> 
> ### 1. 赋值类型变式
> - **简单赋值变式**: 基础的 x = value 形式赋值
> - **复合赋值变式**: +=, -=, *=, /=, %=, |=, &=, ^= 等复合运算符
> - **链式赋值变式**: x = y = z = value 的连续赋值
> - **多重赋值变式**: a, b = value1, value2 的并行赋值
> - **解包赋值变式**: 序列解包、字典解包、星号表达式
> - **条件赋值变式**: 三元运算符或条件表达式的赋值
> 
> ### 2. 数据类型变式
> - **基础类型变式**: int, float, string, boolean 的赋值
> - **容器类型变式**: list, tuple, dict, set 的赋值和解包
> - **引用类型变式**: 对象引用、别名效应的理解
> - **可变/不可变变式**: 可变对象vs不可变对象的赋值行为差异
> - **指针赋值变式**: C语言中指针的赋值和解引用
> - **类型转换变式**: 隐式/显式类型转换的赋值
> 
> ### 3. 内存和引用变式
> - **值拷贝变式**: 值类型的深拷贝行为
> - **引用拷贝变式**: 引用类型的浅拷贝行为
> - **别名效应变式**: 多个变量指向同一对象的情况
> - **指针运算变式**: 指针赋值、地址运算、解引用
> - **内存共享变式**: 多个变量共享内存时的修改影响
> - **作用域变式**: 不同作用域中的变量赋值和可见性
> 
> ### 4. 解包和展开变式
> - **列表解包变式**: [a, b, c] = [1, 2, 3] 的各种形式
> - **元组解包变式**: 嵌套元组的解包赋值
> - **星号表达式变式**: *args, **kwargs 的收集和展开
> - **忽略变量变式**: 使用 _ 忽略不需要的值
> - **不匹配长度变式**: 解包时左右两边数量不匹配的情况
> - **嵌套解包变式**: 多层嵌套结构的解包
> 
> ### 5. 复合运算变式
> - **算术复合变式**: +=, -=, *=, /= 等数学运算符
> - **位运算复合变式**: |=, &=, ^=, <<=, >>= 等位运算符
> - **字符串复合变式**: += 对字符串的连接操作
> - **列表复合变式**: += 对列表的扩展操作
> - **原地修改变式**: 原地修改vs创建新对象的区别
> - **运算优先级变式**: 复合赋值中的运算优先级
> 
> ### 6. 错误和边界变式
> - **类型不匹配变式**: 不兼容类型间的赋值尝试
> - **解包错误变式**: 解包数量不匹配的错误情况
> - **只读变量变式**: 尝试修改常量或只读变量
> - **未定义变量变式**: 使用未定义变量进行赋值
> - **空值赋值变式**: None, NULL, undefined 的赋值
> - **循环引用变式**: 自引用或循环引用的赋值
> 
> ### 7. 作用域和生命周期变式
> - **局部变量变式**: 函数内部的局部变量赋值
> - **全局变量变式**: 全局变量的修改和访问
> - **闭包变量变式**: 闭包中的变量捕获和修改
> - **静态变量变式**: 静态变量的赋值和持久性
> - **临时变量变式**: 临时对象的赋值和生命周期
> - **变量遮蔽变式**: 同名变量在不同作用域的遮蔽
> 
> ### 8. 语言特性变式
> - **Python特性变式**: 多重赋值、解包、walrus运算符
> - **C语言特性变式**: 指针赋值、结构体赋值、数组赋值
> - **Java特性变式**: 对象引用赋值、原始类型赋值
> - **JavaScript特性变式**: var/let/const、解构赋值
> - **跨语言对比变式**: 相同操作在不同语言中的行为差异
> 
> ### 9. 性能和优化变式
> - **内存效率变式**: 大对象的赋值和拷贝成本
> - **引用计数变式**: 引用计数变化对内存的影响
> - **写时拷贝变式**: copy-on-write机制的赋值优化
> - **原地操作变式**: 原地修改vs重新赋值的性能差异
> - **缓存效应变式**: 变量赋值对缓存的影响
> 
> ### 10. 复杂场景变式
> - **嵌套赋值变式**: 多层嵌套的复杂赋值操作
> - **条件赋值变式**: 基于条件的选择性赋值
> - **循环赋值变式**: 循环中的变量赋值和累积
> - **递归赋值变式**: 递归函数中的变量赋值
> - **并发赋值变式**: 多线程环境下的变量赋值安全性
> 
> ## 生成规则
> 
> ### 基本要求
> 1. 每个种子任务生成10-15个变式
> 2. 确保每个变式维度至少覆盖2-3个变式
> 3. 保持赋值操作的核心语义，但改变具体场景
> 4. 变式难度应该涵盖easy/medium/hard三个等级
> 
> ### 难度分级标准
> - **Easy**: 简单赋值，基础数据类型，直接值赋值
> - **Medium**: 复合赋值，容器解包，引用类型，类型转换
> - **Hard**: 复杂解包，嵌套赋值，内存引用，错误处理，跨语言特性
> 
> ### 特殊考虑点
> 1. **语义准确性**: 确保赋值操作的语义正确
> 2. **内存模型**: 正确理解值传递和引用传递
> 3. **类型系统**: 考虑强类型和弱类型语言的差异
> 4. **执行顺序**: 理解赋值操作的执行顺序和副作用
> 
> ### 输出格式
> 为每个变式生成完整的JSON格式，包含：
> - 唯一ID（SL-BL-S00X-VYY格式）
> - 完整的metadata（标注变式类型和源种子）
> - 清晰的task描述和代码
> - 准确且唯一的答案
> 
> 请基于此提示词，为给定的种子任务生成完整的变式集合，确保全面覆盖布尔逻辑推理的各个方面。
> ```

```
{
    "id": "SL-AS-S001-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "数据类型变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with string assignment, what is the value of variable x after executing the assignment statement `x = y`?",
        "code": "y = \"hello\"\nz = \"world\"\nx = y\nprint(f\"x = {x}\")",
        "answer": "hello"
    }
},
{
    "id": "SL-AS-S001-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "数据类型变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with boolean assignment, what is the value of variable x after executing the assignment statement `x = y`?",
        "code": "y = True\nz = False\nx = y\nprint(f\"x = {x}\")",
        "answer": true
    }
},
{
    "id": "SL-AS-S001-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "数据类型变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with float assignment, what is the value of variable x after executing the assignment statement `x = y`?",
        "code": "y = 3.14\nz = 2.71\nx = y\nprint(f\"x = {x}\")",
        "answer": 3.14
    }
},
{
    "id": "SL-AS-S001-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "容器类型变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with list assignment, what is the length of list x after executing the assignment statement `x = y`?",
        "code": "y = [1, 2, 3, 4]\nz = [5, 6]\nx = y\nprint(f\"x = {x}, length = {len(x)}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S001-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "引用类型变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with list reference assignment, what is the value of x[0] after modifying y[0]?",
        "code": "y = [1, 2, 3]\nz = [4, 5, 6]\nx = y\ny[0] = 999\nprint(f\"x = {x}, y = {y}\")",
        "answer": 999
    }
},
{
    "id": "SL-AS-S001-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "类型转换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with type conversion assignment, what is the type of variable x after executing the assignment statement `x = int(y)`?",
        "code": "y = \"42\"\nz = \"100\"\nx = int(y)\nprint(f\"x = {x}, type = {type(x).__name__}\")",
        "answer": "int"
    }
},
{
    "id": "SL-AS-S001-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "空值赋值变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with None assignment, what is the value of variable x after executing the assignment statement `x = y`?",
        "code": "y = None\nz = 100\nx = y\nprint(f\"x = {x}\")",
        "answer": null
    }
},
{
    "id": "SL-AS-S001-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "条件赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with conditional assignment, what is the value of variable x after executing the assignment statement `x = y if condition else z`?",
        "code": "y = 42\nz = 100\ncondition = True\nx = y if condition else z\nprint(f\"x = {x}\")",
        "answer": 42
    }
},
{
    "id": "SL-AS-S001-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "嵌套赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with nested assignment, what is the value of variable x after executing the assignment statement `x = data['key']`?",
        "code": "data = {'key': 42, 'other': 100}\ny = data['key']\nx = y\nprint(f\"x = {x}\")",
        "answer": 42
    }
},
{
    "id": "SL-AS-S001-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed1-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S001",
        "variant_type": "多变量赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with multiple variable assignment, what is the value of variable x after executing all assignment statements?",
        "code": "y = 42\nz = 100\nw = 200\nx = y\nx = z\nprint(f\"x = {x}\")",
        "answer": 100
    }
},
{
    "id": "SL-AS-S002-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "数据类型变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with string swap, what is the value of variable a after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = \"hello\"\nb = \"world\"\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": "world"
    }
},
{
    "id": "SL-AS-S002-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "三元交换变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with three-variable swap, what is the value of variable a after executing the multiple assignment statement `a, b, c = b, c, a`?",
        "code": "a = 1\nb = 2\nc = 3\nprint(f\"Before swap: a={a}, b={b}, c={c}\")\na, b, c = b, c, a\nprint(f\"After swap: a={a}, b={b}, c={c}\")",
        "answer": 2
    }
},
{
    "id": "SL-AS-S002-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "列表交换变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with list swap, what is the first element of list a after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = [1, 2, 3]\nb = [4, 5, 6]\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S002-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "表达式交换变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with expression swap, what is the value of variable a after executing the multiple assignment statement `a, b = b + 1, a * 2`?",
        "code": "a = 5\nb = 3\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b + 1, a * 2\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S002-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "部分交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with partial assignment, what is the value of variable a after executing the multiple assignment statement `a, _ = b, a`?",
        "code": "a = 10\nb = 20\nprint(f\"Before swap: a={a}, b={b}\")\na, _ = b, a\nprint(f\"After partial swap: a={a}, b={b}\")",
        "answer": 20
    }
},
{
    "id": "SL-AS-S002-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "嵌套解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with nested unpacking, what is the value of variable x after executing the multiple assignment statement `(x, y), (z, w) = (z, w), (x, y)`?",
        "code": "x, y = 1, 2\nz, w = 3, 4\nprint(f\"Before swap: x={x}, y={y}, z={z}, w={w}\")\n(x, y), (z, w) = (z, w), (x, y)\nprint(f\"After swap: x={x}, y={y}, z={z}, w={w}\")",
        "answer": 3
    }
},
{
    "id": "SL-AS-S002-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "同值交换变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with same value swap, what is the value of variable a after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 42\nb = 42\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 42
    }
},
{
    "id": "SL-AS-S002-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "元组交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with tuple swap, what is the second element of tuple a after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = (1, 2)\nb = (3, 4)\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S002-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "链式交换变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with chained swap, what is the value of variable a after executing both swap operations?",
        "code": "a = 1\nb = 2\nc = 3\nprint(f\"Initial: a={a}, b={b}, c={c}\")\na, b = b, a\nb, c = c, b\nprint(f\"After swaps: a={a}, b={b}, c={c}\")",
        "answer": 2
    }
},
{
    "id": "SL-AS-S002-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed2-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S002",
        "variant_type": "类型混合交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with mixed type swap, what is the type of variable a after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 42\nb = \"hello\"\nprint(f\"Before swap: a={a} ({type(a).__name__}), b={b} ({type(b).__name__})\")\na, b = b, a\nprint(f\"After swap: a={a} ({type(a).__name__}), b={b} ({type(b).__name__})\")",
        "answer": "str"
    }
},
{
    "id": "SL-AS-S003-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "字符串解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with string unpacking, what is the value of variable first after executing the unpacking assignment `first, second, *rest = text`?",
        "code": "text = \"hello\"\nfirst, second, *rest = text\nprint(f\"first='{first}', second='{second}', rest={rest}\")",
        "answer": "h"
    }
},
{
    "id": "SL-AS-S003-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "元组解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with tuple unpacking, what is the value of variable first after executing the unpacking assignment `first, second, *rest = data`?",
        "code": "data = (10, 20, 30, 40, 50)\nfirst, second, *rest = data\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 10
    }
},
{
    "id": "SL-AS-S003-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "末尾解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with tail unpacking, what is the value of variable last after executing the unpacking assignment `*front, second_last, last = numbers`?",
        "code": "numbers = [1, 2, 3, 4, 5]\n*front, second_last, last = numbers\nprint(f\"front={front}, second_last={second_last}, last={last}\")",
        "answer": 5
    }
},
{
    "id": "SL-AS-S003-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "中间解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with middle unpacking, what is the length of list middle after executing the unpacking assignment `first, *middle, last = numbers`?",
        "code": "numbers = [1, 2, 3, 4, 5]\nfirst, *middle, last = numbers\nprint(f\"first={first}, middle={middle}, last={last}\")",
        "answer": 3
    }
},
{
    "id": "SL-AS-S003-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "嵌套解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with nested unpacking, what is the value of variable first after executing the unpacking assignment `(first, second), *rest = data`?",
        "code": "data = [(1, 2), (3, 4), (5, 6)]\n(first, second), *rest = data\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 1
    }
},
{
    "id": "SL-AS-S003-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "空序列解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with empty sequence unpacking, what is the length of list rest after executing the unpacking assignment `first, second, *rest = numbers`?",
        "code": "numbers = [1, 2]\nfirst, second, *rest = numbers\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 0
    }
},
{
    "id": "SL-AS-S003-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "忽略变量变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with ignored variables, what is the value of variable first after executing the unpacking assignment `first, _, *rest = numbers`?",
        "code": "numbers = [1, 2, 3, 4, 5]\nfirst, _, *rest = numbers\nprint(f\"first={first}, rest={rest}\")",
        "answer": 1
    }
},
{
    "id": "SL-AS-S003-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "字典解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with dictionary unpacking, what is the value of variable first after executing the unpacking assignment `first, second, *rest = data.values()`?",
        "code": "data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}\nfirst, second, *rest = data.values()\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 1
    }
},
{
    "id": "SL-AS-S003-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "生成器解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with generator unpacking, what is the value of variable first after executing the unpacking assignment `first, second, *rest = gen`?",
        "code": "gen = (x * 2 for x in range(1, 6))\nfirst, second, *rest = gen\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 2
    }
},
{
    "id": "SL-AS-S003-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed3-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S003",
        "variant_type": "范围解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with range unpacking, what is the value of variable first after executing the unpacking assignment `first, second, *rest = range(1, 6)`?",
        "code": "numbers = range(1, 6)\nfirst, second, *rest = numbers\nprint(f\"first={first}, second={second}, rest={list(rest)}\")",
        "answer": 1
    }
},
{
    "id": "SL-AS-S004-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "多级指针变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with double pointer, what is the value that **ptr2 points to after executing the assignment statements?",
        "code": "int value = 100;\nint *ptr1 = &value;\nint **ptr2 = &ptr1;\nprintf(\"Value: %d\\n\", **ptr2);",
        "answer": 100
    }
},
{
    "id": "SL-AS-S004-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "数组指针变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with array pointer, what is the value that ptr[1] points to after executing the assignment statement `ptr = arr`?",
        "code": "int arr[] = {10, 20, 30, 40};\nint *ptr;\nptr = arr;\nprintf(\"ptr[1] = %d\\n\", ptr[1]);",
        "answer": 20
    }
},
{
    "id": "SL-AS-S004-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "指针算术变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with pointer arithmetic, what is the value that *(ptr + 2) points to after executing the assignment statements?",
        "code": "int arr[] = {100, 200, 300, 400};\nint *ptr = arr;\nprintf(\"*(ptr + 2) = %d\\n\", *(ptr + 2));",
        "answer": 300
    }
},
{
    "id": "SL-AS-S004-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "结构体指针变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with struct pointer, what is the value of ptr->x after executing the assignment statement `ptr = &point`?",
        "code": "struct Point { int x, y; };\nstruct Point point = {100, 200};\nstruct Point *ptr;\nptr = &point;\nprintf(\"ptr->x = %d\\n\", ptr->x);",
        "answer": 100
    }
},
{
    "id": "SL-AS-S004-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "空指针变式",
        "language": "c",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with NULL pointer, what is the value of ptr after executing the assignment statement `ptr = NULL`?",
        "code": "int value = 100;\nint *ptr = &value;\nptr = NULL;\nprintf(\"ptr = %p\\n\", ptr);",
        "answer": null
    }
},
{
    "id": "SL-AS-S004-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "函数指针变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with function pointer, what is the return value when calling the function through ptr after executing the assignment statement `ptr = &add`?",
        "code": "int add(int a, int b) { return a + b; }\nint (*ptr)(int, int);\nptr = &add;\nint result = ptr(30, 70);\nprintf(\"Result: %d\\n\", result);",
        "answer": 100
    }
},
{
    "id": "SL-AS-S004-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "字符串指针变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with string pointer, what is the first character that ptr points to after executing the assignment statement `ptr = str`?",
        "code": "char str[] = \"Hello\";\nchar *ptr;\nptr = str;\nprintf(\"First char: %c\\n\", *ptr);",
        "answer": "H"
    }
},
{
    "id": "SL-AS-S004-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "指针交换变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with pointer swap, what is the value that ptr1 points to after the swap?",
        "code": "int a = 100, b = 200;\nint *ptr1 = &a, *ptr2 = &b;\nint *temp = ptr1;\nptr1 = ptr2;\nptr2 = temp;\nprintf(\"*ptr1 = %d\\n\", *ptr1);",
        "answer": 200
    }
},
{
    "id": "SL-AS-S004-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "动态内存变式",
        "language": "c",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with dynamic memory, what is the value that ptr points to after executing the assignment and memory allocation?",
        "code": "int *ptr;\nptr = (int*)malloc(sizeof(int));\n*ptr = 100;\nprintf(\"*ptr = %d\\n\", *ptr);",
        "answer": 100
    }
},
{
    "id": "SL-AS-S004-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed4-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S004",
        "variant_type": "常量指针变式",
        "language": "c",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with constant pointer, what is the value that ptr points to after executing the assignment statement `ptr = &value`?",
        "code": "const int value = 100;\nconst int *ptr;\nptr = &value;\nprintf(\"*ptr = %d\\n\", *ptr);",
        "answer": 100
    }
},
{
    "id": "SL-AS-S005-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "四变量链式赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with four-variable chained assignment, what is the value of variable x after executing the chained assignment `x = y = z = w = 10`?",
        "code": "x = 1\ny = 2\nz = 3\nw = 4\nprint(f\"Before: x={x}, y={y}, z={z}, w={w}\")\nx = y = z = w = 10\nprint(f\"After: x={x}, y={y}, z={z}, w={w}\")",
        "answer": 10
    }
},
{
    "id": "SL-AS-S005-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "表达式链式赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with expression chained assignment, what is the value of variable x after executing the chained assignment `x = y = z = 2 * 3 + 1`?",
        "code": "x = 1\ny = 2\nz = 3\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = 2 * 3 + 1\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": 7
    }
},
{
    "id": "SL-AS-S005-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "列表链式赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with list chained assignment, what is the first element of list x after executing the chained assignment `x = y = z = [1, 2, 3]`?",
        "code": "x = []\ny = []\nz = []\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = [1, 2, 3]\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": 1
    }
},
{
    "id": "SL-AS-S005-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "字符串链式赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with string chained assignment, what is the value of variable x after executing the chained assignment `x = y = z = \"hello\"`?",
        "code": "x = \"a\"\ny = \"b\"\nz = \"c\"\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = \"hello\"\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": "hello"
    }
},
{
    "id": "SL-AS-S005-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "函数调用链式赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with function call chained assignment, what is the value of variable x after executing the chained assignment `x = y = z = max(3, 7, 2)`?",
        "code": "x = 0\ny = 0\nz = 0\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = max(3, 7, 2)\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": 7
    }
},
{
    "id": "SL-AS-S005-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "嵌套链式赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with nested chained assignment, what is the value of variable a after executing both chained assignments?",
        "code": "a = b = 1\nc = d = 2\nprint(f\"Before: a={a}, b={b}, c={c}, d={d}\")\na = b = c = d = 5\nprint(f\"After: a={a}, b={b}, c={c}, d={d}\")",
        "answer": 5
    }
},
{
    "id": "SL-AS-S005-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "布尔链式赋值变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with boolean chained assignment, what is the value of variable x after executing the chained assignment `x = y = z = True`?",
        "code": "x = False\ny = False\nz = False\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = True\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": true
    }
},
{
    "id": "SL-AS-S005-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "字典链式赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with dictionary chained assignment, what is the value of x['key'] after executing the chained assignment `x = y = z = {'key': 42}`?",
        "code": "x = {}\ny = {}\nz = {}\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = {'key': 42}\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": 42
    }
},
{
    "id": "SL-AS-S005-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "None链式赋值变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with None chained assignment, what is the value of variable x after executing the chained assignment `x = y = z = None`?",
        "code": "x = 1\ny = 2\nz = 3\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = None\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": null
    }
},
{
    "id": "SL-AS-S005-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed5-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S005",
        "variant_type": "变量引用链式赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with variable reference chained assignment, what is the value of variable x after executing the chained assignment `x = y = z = existing_var`?",
        "code": "existing_var = 100\nx = 1\ny = 2\nz = 3\nprint(f\"Before: x={x}, y={y}, z={z}\")\nx = y = z = existing_var\nprint(f\"After: x={x}, y={y}, z={z}\")",
        "answer": 100
    }
},
{
    "id": "SL-AS-S006-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "减法复合赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with subtraction compound assignment, what is the value of variable count after executing the compound assignment statement `count -= increment * 2`?",
        "code": "count = 20\nincrement = 3\nmultiplier = 2\nprint(f\"Initial count: {count}\")\ncount -= increment * 2\nprint(f\"Final count: {count}\")",
        "answer": 14
    }
},
{
    "id": "SL-AS-S006-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "乘法复合赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with multiplication compound assignment, what is the value of variable count after executing the compound assignment statement `count *= increment + 1`?",
        "code": "count = 5\nincrement = 2\nprint(f\"Initial count: {count}\")\ncount *= increment + 1\nprint(f\"Final count: {count}\")",
        "answer": 15
    }
},
{
    "id": "SL-AS-S006-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "除法复合赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with division compound assignment, what is the value of variable count after executing the compound assignment statement `count //= divisor`?",
        "code": "count = 20\ndivisor = 3\nprint(f\"Initial count: {count}\")\ncount //= divisor\nprint(f\"Final count: {count}\")",
        "answer": 6
    }
},
{
    "id": "SL-AS-S006-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "模运算复合赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with modulo compound assignment, what is the value of variable count after executing the compound assignment statement `count %= modulus`?",
        "code": "count = 17\nmodulus = 5\nprint(f\"Initial count: {count}\")\ncount %= modulus\nprint(f\"Final count: {count}\")",
        "answer": 2
    }
},
{
    "id": "SL-AS-S006-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "幂运算复合赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with power compound assignment, what is the value of variable count after executing the compound assignment statement `count **= exponent`?",
        "code": "count = 3\nexponent = 2\nprint(f\"Initial count: {count}\")\ncount **= exponent\nprint(f\"Final count: {count}\")",
        "answer": 9
    }
},
{
    "id": "SL-AS-S006-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "字符串复合赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with string compound assignment, what is the length of variable text after executing the compound assignment statement `text += suffix * 2`?",
        "code": "text = \"hello\"\nsuffix = \"!\"\nprint(f\"Initial text: '{text}'\")\ntext += suffix * 2\nprint(f\"Final text: '{text}'\")",
        "answer": 7
    }
},
{
    "id": "SL-AS-S006-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "列表复合赋值变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with list compound assignment, what is the length of list items after executing the compound assignment statement `items += new_items`?",
        "code": "items = [1, 2, 3]\nnew_items = [4, 5]\nprint(f\"Initial items: {items}\")\nitems += new_items\nprint(f\"Final items: {items}\")",
        "answer": 5
    }
},
{
    "id": "SL-AS-S006-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "位运算复合赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with bitwise OR compound assignment, what is the value of variable flags after executing the compound assignment statement `flags |= new_flag`?",
        "code": "flags = 5  # 101 in binary\nnew_flag = 2  # 010 in binary\nprint(f\"Initial flags: {flags} ({bin(flags)})\")\nflags |= new_flag\nprint(f\"Final flags: {flags} ({bin(flags)})\")",
        "answer": 7
    }
},
{
    "id": "SL-AS-S006-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "位与复合赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with bitwise AND compound assignment, what is the value of variable mask after executing the compound assignment statement `mask &= filter_value`?",
        "code": "mask = 15  # 1111 in binary\nfilter_value = 10  # 1010 in binary\nprint(f\"Initial mask: {mask} ({bin(mask)})\")\nmask &= filter_value\nprint(f\"Final mask: {mask} ({bin(mask)})\")",
        "answer": 10
    }
},
{
    "id": "SL-AS-S006-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed6-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S006",
        "variant_type": "链式复合赋值变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with chained compound assignments, what is the value of variable count after executing both compound assignment statements?",
        "code": "count = 10\nincrement = 2\nmultiplier = 3\nprint(f\"Initial count: {count}\")\ncount += increment\ncount *= multiplier\nprint(f\"Final count: {count}\")",
        "answer": 36
    }
},
{
    "id": "SL-AS-S007-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "浮点数交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with float swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 3.14\nb = 2.71\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 3.14
    }
},
{
    "id": "SL-AS-S007-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "负数交换变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with negative number swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = -5\nb = 15\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": -5
    }
},
{
    "id": "SL-AS-S007-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "零值交换变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with zero value swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 0\nb = 42\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 0
    }
},
{
    "id": "SL-AS-S007-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "布尔交换变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with boolean swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = True\nb = False\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": true
    }
},
{
    "id": "SL-AS-S007-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "大数交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with large number swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 1000000\nb = 2000000\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 1000000
    }
},
{
    "id": "SL-AS-S007-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "字符交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with character swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 'x'\nb = 'y'\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": "x"
    }
},
{
    "id": "SL-AS-S007-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "计算结果交换变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with calculated values swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 2 ** 3\nb = 3 ** 2\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 8
    }
},
{
    "id": "SL-AS-S007-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "None值交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with None value swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = None\nb = 100\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": null
    }
},
{
    "id": "SL-AS-S007-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "复数交换变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with complex number swap, what is the real part of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "a = 3 + 4j\nb = 1 + 2j\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 3
    }
},
{
    "id": "SL-AS-S007-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed7-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S007",
        "variant_type": "变量引用交换变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with variable reference swap, what is the value of variable b after executing the multiple assignment statement `a, b = b, a`?",
        "code": "x = 50\ny = 60\na = x\nb = y\nprint(f\"Before swap: a={a}, b={b}\")\na, b = b, a\nprint(f\"After swap: a={a}, b={b}\")",
        "answer": 50
    }
},
{
    "id": "SL-AS-S008-V01",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant1",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "更长序列解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with longer sequence unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = numbers`?",
        "code": "numbers = [1, 2, 3, 4, 5, 6, 7, 8]\nfirst, second, *rest = numbers\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 6
    }
},
{
    "id": "SL-AS-S008-V02",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant2",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "字符串解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with string unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = text`?",
        "code": "text = \"python\"\nfirst, second, *rest = text\nprint(f\"first='{first}', second='{second}', rest={rest}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S008-V03",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant3",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "单元素序列解包变式",
        "language": "python",
        "difficulty": "easy",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with single element unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = numbers`?",
        "code": "numbers = [42]\nfirst, second, *rest = numbers\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 0
    }
},
{
    "id": "SL-AS-S008-V04",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant4",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "元组解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with tuple unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = data`?",
        "code": "data = (10, 20, 30, 40, 50, 60)\nfirst, second, *rest = data\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S008-V05",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant5",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "三变量解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with three-variable unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, third, *rest = numbers`?",
        "code": "numbers = [1, 2, 3, 4, 5]\nfirst, second, third, *rest = numbers\nprint(f\"first={first}, second={second}, third={third}, rest={rest}\")",
        "answer": 2
    }
},
{
    "id": "SL-AS-S008-V06",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant6",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "范围对象解包变式",
        "language": "python",
        "difficulty": "medium",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with range object unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = data`?",
        "code": "data = range(1, 8)\nfirst, second, *rest = data\nprint(f\"first={first}, second={second}, rest={list(rest)}\")",
        "answer": 5
    }
},
{
    "id": "SL-AS-S008-V07",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant7",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "空列表解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet where unpacking an empty list would cause an error, what would happen when executing the unpacking assignment `first, second, *rest = numbers`?",
        "code": "numbers = []\n# This would cause a ValueError\n# first, second, *rest = numbers",
        "answer": "ValueError"
    }
},
{
    "id": "SL-AS-S008-V08",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant8",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "生成器解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with generator unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = gen`?",
        "code": "gen = (x for x in [1, 2, 3, 4, 5, 6])\nfirst, second, *rest = gen\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S008-V09",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant9",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "字典值解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with dictionary values unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = data.values()`?",
        "code": "data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}\nfirst, second, *rest = data.values()\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 4
    }
},
{
    "id": "SL-AS-S008-V10",
    "metadata": {
        "name": "StatementLevel-Assignment-Seed8-Variant10",
        "category": "Statement-Level",
        "subcategory": "Assignment",
        "type": "variant",
        "source": "Generated",
        "source_seed": "SL-AS-S008",
        "variant_type": "嵌套列表解包变式",
        "language": "python",
        "difficulty": "hard",
        "intervention": 0
    },
    "task": {
        "description": "Given the following code snippet with nested list unpacking, what is the length of the list stored in variable rest after executing the unpacking assignment `first, second, *rest = data[0]`?",
        "code": "data = [[1, 2, 3, 4, 5], [6, 7, 8]]\nfirst, second, *rest = data[0]\nprint(f\"first={first}, second={second}, rest={rest}\")",
        "answer": 3
    }
}

```

#### 1E - 常量赋值 [Constant ] (37)

> ```
> # 常量赋值变式生成提示词
> 
> ## 任务目标
> 基于给定的常量赋值种子任务，生成多样化的变式任务来全面测试大模型对常量值语义、字面量表示、类型推断和常量特性的理解能力。
> 
> ## 变式生成维度
> 
> ### 1. 常量类型变式
> - **整数常量变式**: 正整数、负整数、零、不同进制表示（0x, 0o, 0b）
> - **浮点常量变式**: 小数、科学计数法、特殊值（inf, -inf, nan）
> - **字符串常量变式**: 单引号、双引号、三引号、原始字符串、转义字符
> - **布尔常量变式**: True, False 及其在不同语言中的表示
> - **空值常量变式**: None, NULL, null, undefined 等空值表示
> - **字符常量变式**: 单字符、Unicode字符、特殊字符
> 
> ### 2. 字面量表示变式
> - **数值字面量变式**: 整数、浮点数、复数的不同写法
> - **进制表示变式**: 二进制(0b)、八进制(0o)、十六进制(0x)
> - **科学计数法变式**: 1e5, 2.5e-3 等指数表示
> - **字符串字面量变式**: 单引号vs双引号、多行字符串、格式化字符串
> - **转义序列变式**: \n, \t, \\, \", \' 等转义字符
> - **Unicode字面量变式**: \u编码、\x编码、原始Unicode字符
> 
> ### 3. 常量定义变式
> - **const关键字变式**: C/C++/JavaScript中的const声明
> - **final关键字变式**: Java中的final常量
> - **static final变式**: Java中的类常量
> - **#define宏变式**: C预处理器宏定义
> - **enum常量变式**: 枚举类型的常量定义
> - **readonly变式**: 只读属性的常量定义
> 
> ### 4. 类型推断变式
> - **隐式类型变式**: 编译器/解释器自动推断常量类型
> - **显式类型变式**: 明确指定常量的数据类型
> - **类型转换变式**: 常量在赋值时的自动类型转换
> - **精度损失变式**: 高精度常量赋值给低精度变量
> - **溢出变式**: 超出类型范围的常量赋值
> - **类型兼容变式**: 不同但兼容类型间的常量赋值
> 
> ### 5. 特殊值变式
> - **边界值变式**: 最大值、最小值、临界值常量
> - **特殊浮点变式**: NaN, Infinity, -Infinity, 0.0, -0.0
> - **空值变式**: None, NULL, nullptr, null, undefined
> - **默认值变式**: 类型的默认初始值常量
> - **魔数变式**: 具有特殊含义的数字常量
> - **符号常量变式**: 预定义的符号常量
> 
> ### 6. 字符串常量变式
> - **空字符串变式**: "", '', 不同语言的空字符串表示
> - **多行字符串变式**: 三引号字符串、换行符处理
> - **格式化字符串变式**: f-string, format string, template literal
> - **原始字符串变式**: r"string", raw string literal
> - **字节字符串变式**: b"string", bytes literal
> - **Unicode字符串变式**: u"string", unicode literal
> 
> ### 7. 复合常量变式
> - **数组常量变式**: {1, 2, 3}, [1, 2, 3] 等数组字面量
> - **结构体常量变式**: 结构体的字面量初始化
> - **对象字面量变式**: JavaScript/Python的对象字面量
> - **元组常量变式**: (1, 2, 3) 元组字面量
> - **字典常量变式**: {"key": "value"} 字典字面量
> - **集合常量变式**: {1, 2, 3} 集合字面量
> 
> ### 8. 语言特性变式
> - **Python特性变式**: 多种字符串表示、数值类型、True/False/None
> - **C语言特性变式**: 整型常量、字符常量、指针常量、宏定义
> - **Java特性变式**: final常量、字符串常量池、包装类常量
> - **JavaScript特性变式**: const/let、模板字符串、Symbol常量
> - **跨语言对比变式**: 相同常量在不同语言中的表示差异
> 
> ### 9. 常量运算变式
> - **常量表达式变式**: 编译时可计算的常量表达式
> - **常量折叠变式**: 编译器优化的常量计算
> - **常量传播变式**: 常量在代码中的传播和替换
> - **运算结果常量变式**: 常量运算的结果类型和值
> - **短路求值变式**: 常量条件的短路计算
> - **三元运算常量变式**: 条件表达式中的常量选择
> 
> ### 10. 内存和存储变式
> - **字符串常量池变式**: 相同字符串常量的内存共享
> - **静态存储变式**: 常量在静态存储区的分配
> - **栈vs堆变式**: 常量在不同内存区域的存储
> - **只读内存变式**: 常量存储在只读内存段
> - **常量表变式**: 编译器生成的常量表
> - **内联常量变式**: 编译时内联的常量替换
> 
> ## 生成规则
> 
> ### 基本要求
> 1. 每个种子任务生成10-15个变式
> 2. 确保每个变式维度至少覆盖2-3个变式
> 3. 保持常量赋值的核心语义，但改变常量类型和表示形式
> 4. 变式难度应该涵盖easy/medium/hard三个等级
> 
> ### 难度分级标准
> - **Easy**: 基础字面量常量，简单数据类型，直接赋值
> - **Medium**: 特殊表示形式，类型转换，字符串处理，进制转换
> - **Hard**: 特殊值处理，复合常量，跨语言差异，内存模型，编译时计算
> 
> ### 特殊考虑点
> 1. **字面量准确性**: 确保常量字面量的语法正确
> 2. **类型一致性**: 保证常量类型与语言规范一致
> 3. **精度问题**: 注意浮点常量的精度表示
> 4. **字符编码**: 正确处理字符串的编码问题
> 5. **语言差异**: 考虑不同语言的常量表示差异
> 
> ### 输出格式
> 生成的变式应该放在一个JSON数组中，每个变式对象用逗号分隔：
> 
> ```json
> [
>     {
>         "id": "SL-CT-S00X-V001",
>         "metadata": {
>             "name": "变式名称",
>             "category": "Statement-Level",
>             "subcategory": "Constant",
>             "type": "variant",
>             "source": "Generated",
>             "language": "python/c/java/javascript",
>             "difficulty": "easy/medium/hard",
>             "intervention": 0,
>             "variant_type": "变式类型标签"
>         },
>         "task": {
>             "description": "清晰的任务描述",
>             "code": "完整的代码片段",
>             "answer": "准确的常量值"
>         }
>     },
>     {下一个变式...}
> ]
> 质量检查要点
> 常量正确性: 确保常量值的计算和表示正确
> 语法合规性: 确保常量字面量在目标语言中语法正确
> 类型一致性: 确保答案类型与常量类型匹配
> 精度准确性: 浮点常量的精度表示要准确
> 示例变式类型
> 基于SL-CT-S001（整数常量）的变式示例：
> 进制表示变式: num = 0x2A (十六进制42)
> 负数变式: num = -42
> 科学计数法变式: num = 4.2e1
> 类型转换变式: num = int(42.0)
> 边界值变式: num = 2147483647 (最大int值)
> 基于SL-CT-S002（字符串常量）的变式示例：
> 转义字符变式: message = "Hello,\nWorld!"
> 原始字符串变式: message = r"Hello, World!"
> Unicode变式: message = "Hello, 世界!"
> 格式化字符串变式: message = f"Hello, {'World'}!"
> 字节字符串变式: message = b"Hello, World!"
> 基于SL-CT-S005（NULL指针）的变式示例：
> 指针常量变式: status = (void*)0x0
> 不同NULL表示变式: status = 0 vs status = NULL
> nullptr变式: status = nullptr (C++)
> 条件编译变式: #define NULL ((void*)0)
> 
> 
> 请基于此提示词生成完整的变式集合，输出格式为包含所有变式的JSON数组。
> 
> ```

```
[
    {
        "id": "SL-CT-S001-V001",
        "metadata": {
            "name": "十六进制整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "进制表示变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = 0x2A`?",
            "code": "num = 0x2A\nprint(f\"Number: {num}\")\nprint(f\"Type: {type(num)}\")",
            "answer": 42
        }
    },
    {
        "id": "SL-CT-S001-V002",
        "metadata": {
            "name": "二进制整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "进制表示变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = 0b101010`?",
            "code": "num = 0b101010\nprint(f\"Number: {num}\")\nprint(f\"Type: {type(num)}\")",
            "answer": 42
        }
    },
    {
        "id": "SL-CT-S001-V003",
        "metadata": {
            "name": "八进制整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "进制表示变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = 0o52`?",
            "code": "num = 0o52\nprint(f\"Number: {num}\")\nprint(f\"Type: {type(num)}\")",
            "answer": 42
        }
    },
    {
        "id": "SL-CT-S001-V004",
        "metadata": {
            "name": "负整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "负数变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = -42`?",
            "code": "num = -42\nprint(f\"Number: {num}\")\nprint(f\"Type: {type(num)}\")",
            "answer": -42
        }
    },
    {
        "id": "SL-CT-S001-V005",
        "metadata": {
            "name": "科学计数法整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "科学计数法变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = int(4.2e1)`?",
            "code": "num = int(4.2e1)\nprint(f\"Number: {num}\")\nprint(f\"Type: {type(num)}\")",
            "answer": 42
        }
    },
    {
        "id": "SL-CT-S001-V006",
        "metadata": {
            "name": "边界值最大整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "边界值变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = 2147483647`?",
            "code": "#include <stdio.h>\n#include <limits.h>\nint num = 2147483647;\nprintf(\"Number: %d\\n\", num);\nprintf(\"INT_MAX: %d\\n\", INT_MAX);",
            "answer": 2147483647
        }
    },
    {
        "id": "SL-CT-S001-V007",
        "metadata": {
            "name": "零值整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "特殊值变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `num = 0`?",
            "code": "num = 0\nprint(f\"Number: {num}\")\nprint(f\"Type: {type(num)}\")",
            "answer": 0
        }
    },
    {
        "id": "SL-CT-S001-V008",
        "metadata": {
            "name": "Java final整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "常量定义变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable NUM in the statement `final int NUM = 42`?",
            "code": "public class Test {\n    public static void main(String[] args) {\n        final int NUM = 42;\n        System.out.println(\"Number: \" + NUM);\n        System.out.println(\"Class: \" + Integer.class.getSimpleName());\n    }\n}",
            "answer": 42
        }
    },
    {
        "id": "SL-CT-S001-V009",
        "metadata": {
            "name": "JavaScript const整数常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "常量定义变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable num in the statement `const num = 42`?",
            "code": "const num = 42;\nconsole.log(`Number: ${num}`);\nconsole.log(`Type: ${typeof num}`);",
            "answer": 42
        }
    },
    {
        "id": "SL-CT-S001-V010",
        "metadata": {
            "name": "C语言宏定义整数常量",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "宏定义变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value of NUM when used in the statement `int x = NUM`?",
            "code": "#include <stdio.h>\n#define NUM 42\nint main() {\n    int x = NUM;\n    printf(\"Number: %d\\n\", x);\n    return 0;\n}",
            "answer": 42
        }
    },
    {
        "id": "SL-CT-S002-V001",
        "metadata": {
            "name": "单引号字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "字符串字面量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement `message = 'Hello, World!'`?",
            "code": "message = 'Hello, World!'\nprint(f\"Message: {message}\")\nprint(f\"Length: {len(message)}\")",
            "answer": "Hello, World!"
        }
    },
    {
        "id": "SL-CT-S002-V002",
        "metadata": {
            "name": "转义字符字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "转义序列变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement `message = \"Hello,\\nWorld!\"`?",
            "code": "message = \"Hello,\\nWorld!\"\nprint(f\"Message: {repr(message)}\")\nprint(f\"Actual:\\n{message}\")",
            "answer": "Hello,\nWorld!"
        }
    },
    {
        "id": "SL-CT-S002-V003",
        "metadata": {
            "name": "原始字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "原始字符串变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement `message = r\"Hello,\\nWorld!\"`?",
            "code": "message = r\"Hello,\\nWorld!\"\nprint(f\"Message: {message}\")\nprint(f\"Length: {len(message)}\")",
            "answer": "Hello,\\nWorld!"
        }
    },
    {
        "id": "SL-CT-S002-V004",
        "metadata": {
            "name": "Unicode字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "Unicode字面量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement `message = \"Hello, 世界!\"`?",
            "code": "message = \"Hello, 世界!\"\nprint(f\"Message: {message}\")\nprint(f\"Length: {len(message)}\")",
            "answer": "Hello, 世界!"
        }
    },
    {
        "id": "SL-CT-S002-V005",
        "metadata": {
            "name": "格式化字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "格式化字符串变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement `message = f\"Hello, {'World'}!\"`?",
            "code": "message = f\"Hello, {'World'}!\"\nprint(f\"Message: {message}\")\nprint(f\"Length: {len(message)}\")",
            "answer": "Hello, World!"
        }
    },
    {
        "id": "SL-CT-S002-V006",
        "metadata": {
            "name": "字节字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "字节字符串变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the decoded string value of the bytes assigned to variable message in the statement `message = b\"Hello, World!\"`?",
            "code": "message = b\"Hello, World!\"\nprint(f\"Bytes: {message}\")\nprint(f\"Decoded: {message.decode('utf-8')}\")",
            "answer": "Hello, World!"
        }
    },
    {
        "id": "SL-CT-S002-V007",
        "metadata": {
            "name": "空字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "空字符串变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement `message = \"\"`?",
            "code": "message = \"\"\nprint(f\"Message: '{message}'\")\nprint(f\"Length: {len(message)}\")",
            "answer": ""
        }
    },
    {
        "id": "SL-CT-S002-V008",
        "metadata": {
            "name": "多行字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "多行字符串变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement using triple quotes?",
            "code": "message = \"\"\"Hello,\nWorld!\nHow are you?\"\"\"\nprint(f\"Message: {repr(message)}\")\nprint(f\"Lines: {len(message.split(chr(10)))}\")",
            "answer": "Hello,\nWorld!\nHow are you?"
        }
    },
    {
        "id": "SL-CT-S002-V009",
        "metadata": {
            "name": "C语言字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "语言特性变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the string value assigned to variable message in the statement `char message[] = \"Hello, World!\"`?",
            "code": "#include <stdio.h>\n#include <string.h>\nint main() {\n    char message[] = \"Hello, World!\";\n    printf(\"Message: %s\\n\", message);\n    printf(\"Length: %lu\\n\", strlen(message));\n    return 0;\n}",
            "answer": "Hello, World!"
        }
    },
    {
        "id": "SL-CT-S002-V010",
        "metadata": {
            "name": "JavaScript模板字符串常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "模板字符串变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable message in the statement using template literals?",
            "code": "const name = 'World';\nconst message = `Hello, ${name}!`;\nconsole.log(`Message: ${message}`);\nconsole.log(`Length: ${message.length}`);",
            "answer": "Hello, World!"
        }
    },
    {
        "id": "SL-CT-S003-V001",
        "metadata": {
            "name": "False布尔常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "布尔常量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable is_valid in the statement `is_valid = False`?",
            "code": "is_valid = False\nprint(f\"Valid: {is_valid}\")\nprint(f\"Type: {type(is_valid)}\")",
            "answer": false
        }
    },
    {
        "id": "SL-CT-S003-V002",
        "metadata": {
            "name": "C语言真值常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "语言特性变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the integer value assigned to variable is_valid in the statement `int is_valid = 1`?",
            "code": "#include <stdio.h>\nint main() {\n    int is_valid = 1;\n    printf(\"Valid: %d\\n\", is_valid);\n    printf(\"Boolean: %s\\n\", is_valid ? \"true\" : \"false\");\n    return 0;\n}",
            "answer": 1
        }
    },
    {
        "id": "SL-CT-S003-V003",
        "metadata": {
            "name": "Java布尔常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "语言特性变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable isValid in the statement `boolean isValid = true`?",
            "code": "public class Test {\n    public static void main(String[] args) {\n        boolean isValid = true;\n        System.out.println(\"Valid: \" + isValid);\n        System.out.println(\"Class: \" + Boolean.class.getSimpleName());\n    }\n}",
            "answer": true
        }
    },
    {
        "id": "SL-CT-S003-V004",
        "metadata": {
            "name": "JavaScript布尔常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "语言特性变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable isValid in the statement `const isValid = false`?",
            "code": "const isValid = false;\nconsole.log(`Valid: ${isValid}`);\nconsole.log(`Type: ${typeof isValid}`);",
            "answer": false
        }
    },
    {
        "id": "SL-CT-S003-V005",
        "metadata": {
            "name": "条件表达式布尔常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "常量表达式变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable is_valid in the statement `is_valid = 5 > 3`?",
            "code": "is_valid = 5 > 3\nprint(f\"Valid: {is_valid}\")\nprint(f\"Type: {type(is_valid)}\")",
            "answer": true
        }
    },
    {
        "id": "SL-CT-S004-V001",
        "metadata": {
            "name": "科学计数法浮点常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "科学计数法变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable pi in the statement `pi = 3.14159e0`?",
            "code": "pi = 3.14159e0\nradius = 5\narea = pi * radius ** 2\nprint(f\"Pi: {pi}\")\nprint(f\"Area: {area}\")",
            "answer": 3.14159
        }
    },
    {
        "id": "SL-CT-S004-V002",
        "metadata": {
            "name": "负科学计数法浮点常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "科学计数法变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable small_num in the statement `small_num = 2.5e-3`?",
            "code": "small_num = 2.5e-3\nprint(f\"Small number: {small_num}\")\nprint(f\"Scientific: {small_num:.2e}\")",
            "answer": 0.0025
        }
    },
    {
        "id": "SL-CT-S004-V003",
        "metadata": {
            "name": "无穷大浮点常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "特殊浮点变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable infinity in the statement `infinity = float('inf')`?",
            "code": "infinity = float('inf')\nprint(f\"Infinity: {infinity}\")\nprint(f\"Is infinite: {infinity == float('inf')}\")",
            "answer": "inf"
        }
    },
    {
        "id": "SL-CT-S004-V004",
        "metadata": {
            "name": "NaN浮点常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "特殊浮点变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable not_a_number in the statement `not_a_number = float('nan')`?",
            "code": "import math\nnot_a_number = float('nan')\nprint(f\"NaN: {not_a_number}\")\nprint(f\"Is NaN: {math.isnan(not_a_number)}\")",
            "answer": "nan"
        }
    },
    {
        "id": "SL-CT-S004-V005",
        "metadata": {
            "name": "负零浮点常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "特殊浮点变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable neg_zero in the statement `neg_zero = -0.0`?",
            "code": "neg_zero = -0.0\npos_zero = 0.0\nprint(f\"Negative zero: {neg_zero}\")\nprint(f\"Equal to positive zero: {neg_zero == pos_zero}\")",
            "answer": -0.0
        }
    },
    {
        "id": "SL-CT-S004-V006",
        "metadata": {
            "name": "分数表示浮点常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "类型转换变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable pi_approx in the statement `pi_approx = 22/7`?",
            "code": "pi_approx = 22/7\nprint(f\"Pi approximation: {pi_approx}\")\nprint(f\"Rounded: {round(pi_approx, 5)}\")",
            "answer": 3.142857142857143
        }
    },
    {
        "id": "SL-CT-S005-V001",
        "metadata": {
            "name": "整数零指针常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "指针常量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the integer value of the pointer status after executing the statement `status = 0`?",
            "code": "#include <stdio.h>\nvoid *status = 0;\nint value = 100;\nif (status == NULL) {\n    printf(\"Status is null\\n\");\n} else {\n    printf(\"Status is not null\\n\");\n}",
            "answer": 0
        }
    },
    {
        "id": "SL-CT-S005-V002",
        "metadata": {
            "name": "强制转换NULL指针常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "指针常量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the integer value of the pointer status after executing the statement `status = (void*)0x0`?",
            "code": "#include <stdio.h>\nvoid *status = (void*)0x0;\nint value = 100;\nif (status == NULL) {\n    printf(\"Status is null\\n\");\n} else {\n    printf(\"Status is not null\\n\");\n}",
            "answer": 0
        }
    },
    {
        "id": "SL-CT-S005-V003",
        "metadata": {
            "name": "nullptr指针常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "cpp",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "nullptr变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the integer value of the pointer status after executing the statement `status = nullptr`?",
            "code": "#include <iostream>\nusing namespace std;\nint main() {\n    void *status = nullptr;\n    if (status == nullptr) {\n        cout << \"Status is null\" << endl;\n    } else {\n        cout << \"Status is not null\" << endl;\n    }\n    return 0;\n}",
            "answer": 0
        }
    },
    {
        "id": "SL-CT-S005-V004",
        "metadata": {
            "name": "Python None常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "空值常量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable status in the statement `status = None`?",
            "code": "status = None\nprint(f\"Status: {status}\")\nprint(f\"Type: {type(status)}\")\nprint(f\"Is None: {status is None}\")",
            "answer": null
        }
    },
    {
        "id": "SL-CT-S005-V005",
        "metadata": {
            "name": "JavaScript null常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "空值常量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable status in the statement `const status = null`?",
            "code": "const status = null;\nconsole.log(`Status: ${status}`);\nconsole.log(`Type: ${typeof status}`);\nconsole.log(`Is null: ${status === null}`);",
            "answer": null
        }
    },
    {
        "id": "SL-CT-S005-V006",
        "metadata": {
            "name": "JavaScript undefined常量赋值",
            "category": "Statement-Level",
            "subcategory": "Constant",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "空值常量变式"
        },
        "task": {
            "description": "Given the following code snippet, what is the value assigned to variable status in the statement `const status = undefined`?",
            "code": "const status = undefined;\nconsole.log(`Status: ${status}`);\nconsole.log(`Type: ${typeof status}`);\nconsole.log(`Is undefined: ${status === undefined}`);",
            "answer": "undefined"
        }
    }
]
```

#### 1F - 大混合（50）

> ```
> # 语句级推理混合变式生成提示词
> 
> ## 任务目标
> 基于给定的语句级推理种子任务，生成融合多种语句级推理类型的综合变式任务，全面测试大模型对算术运算、布尔运算、API/函数调用、变量赋值和常量赋值等多种语句级推理能力的综合理解和交叉应用。
> 
> ## 核心设计理念
> 不局限于单一推理类型，而是创造包含多种语句级推理元素的复合场景，测试模型在复杂语句环境下的综合推理能力。
> 
> ## 混合变式生成维度
> 
> ### 1. 运算与赋值混合变式
> - **算术运算+变量赋值**: 复杂表达式的计算结果赋值给变量
> - **布尔运算+条件赋值**: 基于布尔表达式结果的条件性赋值
> - **位运算+复合赋值**: 位运算符与复合赋值运算符的组合
> - **运算优先级+多重赋值**: 复杂运算优先级与多变量同时赋值
> - **类型转换+算术运算**: 隐式/显式类型转换与数学计算的结合
> 
> ### 2. 函数调用与运算混合变式
> - **函数返回值+算术运算**: 函数调用结果参与数学计算
> - **嵌套函数调用+布尔判断**: 多层函数调用的返回值用于逻辑判断
> - **API调用+错误处理**: 函数调用失败时的错误码与布尔逻辑结合
> - **参数计算+函数调用**: 复杂表达式作为函数参数
> - **函数副作用+变量状态**: 函数调用对全局变量的影响
> 
> ### 3. 常量与变量交互变式
> - **常量定义+变量运算**: 使用常量参与变量的算术运算
> - **魔数替换+表达式简化**: 将魔数提取为常量对表达式的影响
> - **常量折叠+运行时计算**: 编译时常量计算与运行时变量计算的区别
> - **枚举常量+逻辑判断**: 枚举值在条件判断中的使用
> - **宏定义+复杂表达式**: 宏展开对复杂表达式计算的影响
> 
> ### 4. 控制流与推理混合变式
> - **条件表达式+多类型运算**: if-else中包含不同类型的运算
> - **短路求值+函数调用**: 逻辑短路与函数调用副作用的结合
> - **循环计数+累积运算**: 循环变量与累积计算的结合
> - **break/continue+状态变化**: 控制流改变对变量状态的影响
> - **异常处理+资源管理**: try-catch与内存/文件资源的管理
> 
> ### 5. 内存与引用混合变式
> - **指针运算+数组访问**: 指针算术与数组元素访问的结合
> - **引用传递+函数修改**: 引用参数在函数中的修改对原变量的影响
> - **动态分配+计算使用**: malloc/new的结果用于后续计算
> - **别名效应+赋值操作**: 多个变量指向同一内存时的赋值影响
> - **作用域+生命周期**: 变量作用域与对象生命周期的交互
> 
> ### 6. 类型系统混合变式
> - **隐式转换+运算精度**: 类型自动转换对计算精度的影响
> - **泛型+具体类型**: 泛型函数在具体类型下的行为
> - **多态+方法调用**: 对象多态性与方法调用结果的关系
> - **联合类型+类型检查**: Union类型在运行时的类型检查
> - **void指针+类型转换**: void*指针的类型转换与使用
> 
> ### 7. 并发与同步混合变式
> - **原子操作+共享变量**: 原子操作对共享变量状态的影响
> - **锁机制+资源访问**: 同步锁与共享资源访问的结合
> - **线程局部+全局状态**: 线程局部存储与全局变量的交互
> - **信号量+条件判断**: 信号量状态与条件逻辑的结合
> - **竞态条件+结果预测**: 多线程竞态对计算结果的影响
> 
> ### 8. 错误处理混合变式
> - **边界检查+运算结果**: 数组边界检查与索引计算的结合
> - **空值检查+函数调用**: NULL检查与后续函数调用的安全性
> - **溢出检测+数值运算**: 整数溢出检测与算术运算的结合
> - **资源泄漏+状态跟踪**: 内存泄漏与程序状态跟踪的结合
> - **异常传播+错误码**: 异常处理与错误码返回的混合使用
> 
> ### 9. 平台与环境混合变式
> - **字节序+数据解释**: 大小端字节序对数据解释的影响
> - **编译器优化+代码行为**: 编译器优化对代码执行结果的影响
> - **运行时环境+API行为**: 不同运行时环境下API的行为差异
> - **内存对齐+结构体布局**: 内存对齐要求对结构体布局的影响
> - **操作系统+系统调用**: 不同操作系统下系统调用的行为差异
> 
> ### 10. 语言特性混合变式
> - **语法糖+底层实现**: 语言语法糖与其底层实现的对应关系
> - **运算符重载+自定义行为**: 运算符重载对表达式计算的影响
> - **闭包+变量捕获**: 闭包对外部变量的捕获和修改
> - **装饰器+函数行为**: 装饰器对函数行为的修改
> - **元编程+代码生成**: 元编程技术对代码执行的影响
> 
> ## 复杂度层次设计
> 
> ### 简单混合 (Easy)
> - 2种推理类型的基础组合
> - 线性执行流程，无复杂控制逻辑
> - 明确的输入输出关系
> - 基础数据类型，无特殊边界情况
> 
> ### 中等混合 (Medium)
> - 3-4种推理类型的中度组合
> - 包含条件分支或简单循环
> - 涉及类型转换或简单错误处理
> - 中等复杂度的表达式和函数调用
> 
> ### 复杂混合 (Hard)
> - 4种以上推理类型的深度融合
> - 复杂控制流和嵌套结构
> - 多层次的类型转换和错误处理
> - 涉及内存管理、并发或平台相关特性
> - 需要深入理解语言语义和执行模型
> 
> ## 生成策略
> 
> ### 种子分析策略
> 1. **识别核心推理类型**: 分析种子任务的主要推理类型(A/B/C/D/E)
> 2. **提取关键特征**: 识别种子中的关键语言特性和计算模式
> 3. **设计融合点**: 确定可以融合其他推理类型的切入点
> 4. **保持核心复杂度**: 在添加新元素时保持原有难度层次
> 
> ### 变式设计原则
> 1. **渐进式复杂化**: 从简单混合逐步增加到复杂混合
> 2. **语义一致性**: 确保混合后的代码语义清晰且正确
> 3. **测试价值最大化**: 每个混合变式都应测试特定的推理能力组合
> 4. **现实场景导向**: 优先设计在实际编程中常见的混合场景
> 
> ### 质量保证机制
> 1. **多维度验证**: 从语法、语义、逻辑多个维度验证变式正确性
> 2. **边界情况覆盖**: 确保包含各种边界和异常情况
> 3. **跨语言一致性**: 在语言移植时保持推理逻辑的一致性
> 4. **难度梯度合理**: 确保easy/medium/hard的难度分布合理
> 
> ## 输出格式要求
> 
> 生成的混合变式应该放在一个JSON数组中：
> 
> ```json
> [
>     {
>         "id": "SL-MIX-S00X-V001",
>         "metadata": {
>             "name": "混合变式名称",
>             "category": "Statement-Level",
>             "subcategory": "Mixed",
>             "type": "variant",
>             "source": "Generated",
>             "language": "目标语言",
>             "difficulty": "easy/medium/hard",
>             "intervention": 0,
>             "variant_type": "推理类型组合标签",
>             "mixed_types": ["Arithmetic", "Boolean", "API Call", "Assignment", "Constant"]
>         },
>         "task": {
>             "description": "综合性任务描述",
>             "code": "包含多种推理类型的代码片段",
>             "answer": "准确的答案"
>         }
>     },
>     {下一个变式...}
> ]
> 特殊字段说明
> mixed_types: 标识该变式包含的推理类型组合
> variant_type: 描述具体的混合模式(如"arithmetic_assignment", "boolean_api_call"等)
> 
> 生成目标
> 生成50-100个混合变式，确保：
> 每种难度等级至少包含4-6个变式
> 涵盖至少8-10种不同的推理类型组合
> 包含2-3个跨语言的混合变式
> 至少包含3-4个现实编程场景的复杂混合案例
> 请基于此提示词，为给定的种子任务生成全面的混合变式集合，输出格式为包含所有变式的JSON数组
> ```

```json
[
    {
        "id": "SL-MIX-S001-V001",
        "metadata": {
            "name": "Arithmetic Operation and Variable Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "arithmetic_assignment",
            "mixed_types": ["Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = base * 2 + offset`?",
            "code": "base = 15\noffset = 7\ntemp = base * 2\nresult = base * 2 + offset\nprint(f\"Result: {result}\")",
            "answer": 37
        }
    },
    {
        "id": "SL-MIX-S001-V002",
        "metadata": {
            "name": "Boolean Operation and Function Call Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boolean_api_call",
            "mixed_types": ["Boolean", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of the boolean expression `len(text) > 0 and text.isdigit()`?",
            "code": "text = \"12345\"\nlength = len(text)\nis_digit = text.isdigit()\nresult = len(text) > 0 and text.isdigit()\nprint(f\"Result: {result}\")",
            "answer": true
        }
    },
    {
        "id": "SL-MIX-S001-V003",
        "metadata": {
            "name": "Constant and Arithmetic Operation Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "constant_arithmetic",
            "mixed_types": ["Constant", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable area after executing the statement `area = PI * radius ** 2`?",
            "code": "PI = 3.14159\nradius = 3\ndiameter = 2 * radius\narea = PI * radius ** 2\nprint(f\"Area: {area}\")",
            "answer": 28.27431
        }
    },
    {
        "id": "SL-MIX-S001-V004",
        "metadata": {
            "name": "Function Call and Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "api_call_assignment",
            "mixed_types": ["API Call", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable min_val after executing the multiple assignment `max_val, min_val = max(numbers), min(numbers)`?",
            "code": "numbers = [8, 3, 15, 1, 9, 12]\nsum_val = sum(numbers)\nmax_val, min_val = max(numbers), min(numbers)\nprint(f\"Max: {max_val}, Min: {min_val}\")",
            "answer": 1
        }
    },
    {
        "id": "SL-MIX-S001-V005",
        "metadata": {
            "name": "Bitwise Operation and Boolean Logic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "bitwise_boolean",
            "mixed_types": ["Arithmetic", "Boolean"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of the boolean expression `(flags & mask) != 0 and position < 8`?",
            "code": "flags = 0b1010\nposition = 3\nmask = 1 << position\ncheck = (flags & mask) != 0 and position < 8\nprint(f\"Check: {check}\")",
            "answer": false
        }
    },
    {
        "id": "SL-MIX-S001-V006",
        "metadata": {
            "name": "Type Conversion and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "type_conversion_arithmetic",
            "mixed_types": ["Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = int(average * weight) + bonus`?",
            "code": "scores = [85, 90, 78]\naverage = sum(scores) / len(scores)\nweight = 0.9\nbonus = 5\nresult = int(average * weight) + bonus\nprint(f\"Result: {result}\")",
            "answer": 81
        }
    },
    {
        "id": "SL-MIX-S001-V007",
        "metadata": {
            "name": "Nested Function Call and Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "nested_api_assignment",
            "mixed_types": ["API Call", "Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = len(str(max(numbers) + min(numbers)))`?",
            "code": "numbers = [15, 8, 23, 4, 19]\nmax_num = max(numbers)\nmin_num = min(numbers)\nsum_extremes = max_num + min_num\nresult = len(str(max(numbers) + min(numbers)))\nprint(f\"Result: {result}\")",
            "answer": 2
        }
    },
    {
        "id": "SL-MIX-S001-V008",
        "metadata": {
            "name": "Conditional Expression Multi-Type Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "conditional_multi_type",
            "mixed_types": ["Boolean", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = value * 2 if value > threshold else value // 2`?",
            "code": "value = 15\nthreshold = 10\ndouble_val = value * 2\nhalf_val = value // 2\nresult = value * 2 if value > threshold else value // 2\nprint(f\"Result: {result}\")",
            "answer": 30
        }
    },
    {
        "id": "SL-MIX-S001-V009",
        "metadata": {
            "name": "String Operation and Boolean Logic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "string_boolean",
            "mixed_types": ["API Call", "Boolean", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable is_valid after executing the statement `is_valid = text.startswith('A') and len(text) >= 5`?",
            "code": "text = \"Apple\"\nfirst_char = text[0]\nlength = len(text)\nstarts_with_a = text.startswith('A')\nis_valid = text.startswith('A') and len(text) >= 5\nprint(f\"Valid: {is_valid}\")",
            "answer": true
        }
    },
    {
        "id": "SL-MIX-S001-V010",
        "metadata": {
            "name": "Compound Assignment and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "compound_assignment_arithmetic",
            "mixed_types": ["Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable counter after executing the statement `counter *= step + 1`?",
            "code": "counter = 8\nstep = 2\nincrement = step + 1\ncounter *= step + 1\nprint(f\"Counter: {counter}\")",
            "answer": 24
        }
    },
    {
        "id": "SL-MIX-S001-V011",
        "metadata": {
            "name": "List Comprehension and Boolean Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "list_comprehension_boolean",
            "mixed_types": ["API Call", "Boolean", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable count after executing the statement `count = len([x for x in numbers if x % 2 == 0 and x > 5])`?",
            "code": "numbers = [2, 7, 8, 3, 12, 4, 15, 6]\neven_numbers = [x for x in numbers if x % 2 == 0]\nlarge_numbers = [x for x in numbers if x > 5]\ncount = len([x for x in numbers if x % 2 == 0 and x > 5])\nprint(f\"Count: {count}\")",
            "answer": 3
        }
    },
    {
        "id": "SL-MIX-S001-V012",
        "metadata": {
            "name": "Dictionary Access and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "dict_access_arithmetic",
            "mixed_types": ["Assignment", "Arithmetic", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable total after executing the statement `total = data['price'] * data['quantity'] + data['tax']`?",
            "code": "data = {'price': 25, 'quantity': 3, 'tax': 5}\nbase_cost = data['price'] * data['quantity']\ntax_amount = data['tax']\ntotal = data['price'] * data['quantity'] + data['tax']\nprint(f\"Total: {total}\")",
            "answer": 80
        }
    },
    {
        "id": "SL-MIX-S001-V013",
        "metadata": {
            "name": "Short Circuit Evaluation Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "short_circuit_evaluation",
            "mixed_types": ["Boolean", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of the boolean expression `len(data) > 0 and data[0] > 10`?",
            "code": "data = [15, 8, 3]\nlength = len(data)\nfirst_element = data[0] if len(data) > 0 else None\nresult = len(data) > 0 and data[0] > 10\nprint(f\"Result: {result}\")",
            "answer": true
        }
    },
    {
        "id": "SL-MIX-S001-V014",
        "metadata": {
            "name": "Mathematical Function and Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "math_function_assignment",
            "mixed_types": ["API Call", "Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = round(math.sqrt(value), 2)`?",
            "code": "import math\nvalue = 50\nsquare_root = math.sqrt(value)\nresult = round(math.sqrt(value), 2)\nprint(f\"Result: {result}\")",
            "answer": 7.07
        }
    },
    {
        "id": "SL-MIX-S001-V015",
        "metadata": {
            "name": "String Formatting and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "string_format_arithmetic",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the length of the string stored in variable formatted after executing the statement `formatted = f'{value:.2f}%'`?",
            "code": "value = 85.6789\nrounded_value = round(value, 2)\nformatted = f'{value:.2f}%'\nlength = len(formatted)\nprint(f\"Formatted: {formatted}, Length: {length}\")",
            "answer": 6
        }
    },
    {
        "id": "SL-MIX-S001-V016",
        "metadata": {
            "name": "Range and Sum Function Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "range_sum_mix",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable total after executing the statement `total = sum(range(start, end, step))`?",
            "code": "start = 2\nend = 10\nstep = 2\nrange_values = list(range(start, end, step))\ntotal = sum(range(start, end, step))\nprint(f\"Total: {total}\")",
            "answer": 20
        }
    },
    {
        "id": "SL-MIX-S001-V017",
        "metadata": {
            "name": "Complex Boolean and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "complex_boolean_arithmetic",
            "mixed_types": ["Boolean", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = (a + b) * 2 if (a > 5 and b < 10) or (a == b) else (a - b) ** 2`?",
            "code": "a = 7\nb = 3\nsum_ab = a + b\ndiff_ab = a - b\ncondition1 = a > 5 and b < 10\ncondition2 = a == b\nresult = (a + b) * 2 if (a > 5 and b < 10) or (a == b) else (a - b) ** 2\nprint(f\"Result: {result}\")",
            "answer": 20
        }
    },
    {
        "id": "SL-MIX-S001-V018",
        "metadata": {
            "name": "Nested Function Calls and Type Conversion Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "nested_functions_type_conversion",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = int(str(abs(min(numbers) - max(numbers)))[1:])`?",
            "code": "numbers = [12, -5, 8, 3, -15, 7]\nmin_val = min(numbers)\nmax_val = max(numbers)\ndifference = min_val - max_val\nabs_diff = abs(difference)\nresult = int(str(abs(min(numbers) - max(numbers)))[1:])\nprint(f\"Result: {result}\")",
            "answer": 7
        }
    },
    {
        "id": "SL-MIX-S001-V019",
        "metadata": {
            "name": "Bitwise Operations and Conditional Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "bitwise_conditional_assignment",
            "mixed_types": ["Arithmetic", "Boolean", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = (flags | mask) if (flags & mask) == 0 else (flags ^ mask)`?",
            "code": "flags = 0b1100\nmask = 0b0011\nand_result = flags & mask\nor_result = flags | mask\nxor_result = flags ^ mask\ncondition = (flags & mask) == 0\nresult = (flags | mask) if (flags & mask) == 0 else (flags ^ mask)\nprint(f\"Result: {result}\")",
            "answer": 15
        }
    },
    {
        "id": "SL-MIX-S001-V020",
        "metadata": {
            "name": "List Slicing and Mathematical Operations Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "list_slicing_math",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = sum(numbers[::2]) - sum(numbers[1::2])`?",
            "code": "numbers = [10, 3, 8, 5, 12, 7, 4]\neven_indices = numbers[::2]\nodd_indices = numbers[1::2]\nsum_even = sum(even_indices)\nsum_odd = sum(odd_indices)\nresult = sum(numbers[::2]) - sum(numbers[1::2])\nprint(f\"Result: {result}\")",
            "answer": 19
        }
    },
    {
        "id": "SL-MIX-S001-V021",
        "metadata": {
            "name": "C Pointer Arithmetic and Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "pointer_arithmetic_assignment",
            "mixed_types": ["Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following C code snippet, what is the value that ptr points to after executing the statement `ptr = arr + 3`?",
            "code": "#include <stdio.h>\nint arr[] = {10, 20, 30, 40, 50};\nint *ptr = arr;\nprintf(\"Initial: %d\\n\", *ptr);\nptr = arr + 3;\nprintf(\"After: %d\\n\", *ptr);",
            "answer": 40
        }
    },
    {
        "id": "SL-MIX-S001-V022",
        "metadata": {
            "name": "C Function Call and Boolean Logic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "c_function_boolean",
            "mixed_types": ["API Call", "Boolean", "Assignment"]
        },
        "task": {
            "description": "Given the following C code snippet, what is the value of the boolean expression `strlen(str) > 3 && str[0] == 'T'` when str is \"Test\"?",
            "code": "#include <stdio.h>\n#include <string.h>\nchar *str = \"Test\";\nsize_t length = strlen(str);\nchar first_char = str[0];\nint result = strlen(str) > 3 && str[0] == 'T';\nprintf(\"Result: %d\\n\", result);",
            "answer": 1
        }
    },
    {
        "id": "SL-MIX-S001-V023",
        "metadata": {
            "name": "C Struct Access and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 0,
            "variant_type": "struct_access_arithmetic",
            "mixed_types": ["Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following C code snippet, what is the value of variable area after executing the statement `area = rect.width * rect.height`?",
            "code": "#include <stdio.h>\ntypedef struct {\n    int width;\n    int height;\n} Rectangle;\nRectangle rect = {8, 5};\nint perimeter = 2 * (rect.width + rect.height);\nint area = rect.width * rect.height;\nprintf(\"Area: %d\\n\", area);",
            "answer": 40
        }
    },
    {
        "id": "SL-MIX-S001-V024",
        "metadata": {
            "name": "C Memory Allocation and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "memory_allocation_arithmetic",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following C code snippet, what is the number of bytes allocated by the statement `ptr = malloc(count * sizeof(double))` when count is 6?",
            "code": "#include <stdio.h>\n#include <stdlib.h>\nint count = 6;\nsize_t element_size = sizeof(double);\nsize_t total_size = count * sizeof(double);\ndouble *ptr = malloc(count * sizeof(double));\nprintf(\"Allocated: %zu bytes\\n\", total_size);",
            "answer": 48
        }
    },
    {
        "id": "SL-MIX-S001-V025",
        "metadata": {
            "name": "Dictionary Comprehension and Boolean Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "dict_comprehension_boolean",
            "mixed_types": ["API Call", "Boolean", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the number of items in the dictionary after executing the statement `result = {k: v for k, v in data.items() if v > 10 and k.startswith('item')}`?",
            "code": "data = {'item1': 15, 'test2': 8, 'item3': 25, 'item4': 5, 'item5': 20}\nfiltered_by_value = {k: v for k, v in data.items() if v > 10}\nfiltered_by_key = {k: v for k, v in data.items() if k.startswith('item')}\nresult = {k: v for k, v in data.items() if v > 10 and k.startswith('item')}\ncount = len(result)\nprint(f\"Count: {count}\")",
            "answer": 3
        }
    },
    {
        "id": "SL-MIX-S001-V026",
        "metadata": {
            "name": "Generator Expression and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "generator_arithmetic",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = sum(x**2 for x in range(1, 5) if x % 2 == 1)`?",
            "code": "numbers = list(range(1, 5))\nodd_numbers = [x for x in numbers if x % 2 == 1]\nsquared_odds = [x**2 for x in odd_numbers]\nresult = sum(x**2 for x in range(1, 5) if x % 2 == 1)\nprint(f\"Result: {result}\")",
            "answer": 10
        }
    },
    {
        "id": "SL-MIX-S001-V027",
        "metadata": {
            "name": "Exception Handling and Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "exception_assignment",
            "mixed_types": ["Assignment", "Boolean", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the try-except block when divisor is 0?",
            "code": "dividend = 10\ndivisor = 0\nresult = 0\ntry:\n    result = dividend / divisor\nexcept ZeroDivisionError:\n    result = -1\nfinally:\n    result += 1\nprint(f\"Result: {result}\")",
            "answer": 0
        }
    },
    {
        "id": "SL-MIX-S001-V028",
        "metadata": {
            "name": "Lambda Function and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "lambda_arithmetic",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable result after executing the statement `result = list(map(lambda x: x * 2 + 1, [1, 2, 3, 4]))[2]`?",
            "code": "numbers = [1, 2, 3, 4]\ntransform = lambda x: x * 2 + 1\nmapped_values = list(map(transform, numbers))\nresult = list(map(lambda x: x * 2 + 1, [1, 2, 3, 4]))[2]\nprint(f\"Result: {result}\")",
            "answer": 7
        }
    },
    {
        "id": "SL-MIX-S001-V029",
        "metadata": {
            "name": "Class Property and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "class_property_arithmetic",
            "mixed_types": ["Assignment", "Arithmetic", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable total after executing the statement `total = circle.radius * 2 * PI + circle.area()`?",
            "code": "import math\nPI = 3.14159\n\nclass Circle:\n    def __init__(self, radius):\n        self.radius = radius\n    \n    def area(self):\n        return PI * self.radius ** 2\n\ncircle = Circle(3)\ncircumference = circle.radius * 2 * PI\narea_value = circle.area()\ntotal = circle.radius * 2 * PI + circle.area()\nprint(f\"Total: {total}\")",
            "answer": 47.12385
        }
    },
    {
        "id": "SL-MIX-S001-V030",
        "metadata": {
            "name": "Multiple Inheritance and Method Call Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "inheritance_method_call",
            "mixed_types": ["API Call", "Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value returned by the method call `obj.calculate(5, 3)`?",
            "code": "class BaseA:\n    def calculate(self, x, y):\n        return x + y\n\nclass BaseB:\n    def calculate(self, x, y):\n        return x * y\n\nclass Combined(BaseA, BaseB):\n    def calculate(self, x, y):\n        return super().calculate(x, y) + 10\n\nobj = Combined()\nbase_result = BaseA.calculate(obj, 5, 3)\nfinal_result = obj.calculate(5, 3)\nprint(f\"Result: {final_result}\")",
            "answer": 18
        }
    },
    {
        "id": "SL-MIX-S001-V031",
        "metadata": {
            "name": "Decorator and Function Call Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "decorator_function_call",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet with decorator, what is the value returned by the function call `multiply_by_two(7)`?",
            "code": "def double_result(func):\n    def wrapper(*args, **kwargs):\n        result = func(*args, **kwargs)\n        return result * 2\n    return wrapper\n\n@double_result\ndef multiply_by_two(x):\n    return x * 2\n\noriginal_result = 7 * 2\ndecorated_result = multiply_by_two(7)\nprint(f\"Result: {decorated_result}\")",
            "answer": 28
        }
    },
    {
        "id": "SL-MIX-S001-V032",
        "metadata": {
            "name": "Context Manager and Assignment Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "context_manager_assignment",
            "mixed_types": ["Assignment", "API Call", "Boolean"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable content_length after the with block when the file contains 'Hello World'?",
            "code": "import tempfile\nimport os\n\n# Create a temporary file with content\nwith tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:\n    temp_file.write('Hello World')\n    temp_name = temp_file.name\n\ncontent_length = 0\nwith open(temp_name, 'r') as file:\n    content = file.read()\n    content_length = len(content)\n\nos.unlink(temp_name)\nprint(f\"Content length: {content_length}\")",
            "answer": 11
        }
    },
    {
        "id": "SL-MIX-S001-V033",
        "metadata": {
            "name": "Regular Expression and Boolean Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "regex_boolean",
            "mixed_types": ["API Call", "Boolean", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of the boolean expression `bool(re.search(pattern, text)) and len(text) > 5`?",
            "code": "import re\npattern = r'\\d{3}'\ntext = 'abc123def'\nmatch_found = re.search(pattern, text)\ntext_length = len(text)\nresult = bool(re.search(pattern, text)) and len(text) > 5\nprint(f\"Result: {result}\")",
            "answer": true
        }
    },
    {
        "id": "SL-MIX-S001-V034",
        "metadata": {
            "name": "JSON Processing and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "json_arithmetic",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet, what is the value of variable total after executing the statement `total = sum(item['price'] * item['qty'] for item in data['items'])`?",
            "code": "import json\njson_string = '{\"items\": [{\"price\": 10, \"qty\": 2}, {\"price\": 15, \"qty\": 3}, {\"price\": 8, \"qty\": 1}]}'\ndata = json.loads(json_string)\nitem_costs = [item['price'] * item['qty'] for item in data['items']]\ntotal = sum(item['price'] * item['qty'] for item in data['items'])\nprint(f\"Total: {total}\")",
            "answer": 73
        }
    },
    {
        "id": "SL-MIX-S001-V035",
        "metadata": {
            "name": "Threading and Shared Variable Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "threading_shared_variable",
            "mixed_types": ["Assignment", "Arithmetic", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet with thread-safe operations, what is the final value of counter.value after all operations?",
            "code": "import threading\n\nclass ThreadSafeCounter:\n    def __init__(self):\n        self.value = 0\n        self.lock = threading.Lock()\n    \n    def increment(self, amount=1):\n        with self.lock:\n            self.value += amount\n\ncounter = ThreadSafeCounter()\ncounter.increment(5)\ncounter.increment(3)\ncounter.increment(-2)\nfinal_value = counter.value\nprint(f\"Final value: {final_value}\")",
            "answer": 6
        }
    },
    {
        "id": "SL-MIX-S001-V036",
        "metadata": {
            "name": "C Array Manipulation and Pointer Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "c_array_pointer_mix",
            "mixed_types": ["Assignment", "Arithmetic", "API Call"]
        },
        "task": {
            "description": "Given the following C code snippet, what is the value stored at arr[2] after executing the statement `*(ptr + 2) = *(ptr + 1) + *(ptr + 3)`?",
            "code": "#include <stdio.h>\nint main() {\n    int arr[] = {10, 20, 30, 40, 50};\n    int *ptr = arr;\n    int sum = *(ptr + 1) + *(ptr + 3);\n    *(ptr + 2) = *(ptr + 1) + *(ptr + 3);\n    printf(\"arr[2] = %d\\n\", arr[2]);\n    return 0;\n}",
            "answer": 60
        }
    },
    {
        "id": "SL-MIX-S001-V037",
        "metadata": {
            "name": "C String Manipulation and Length Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "c_string_manipulation",
            "mixed_types": ["API Call", "Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following C code snippet, what is the value of variable result after executing the statement `result = strlen(dest) + strlen(src)`?",
            "code": "#include <stdio.h>\n#include <string.h>\nint main() {\n    char dest[20] = \"Hello\";\n    char src[] = \" World\";\n    size_t dest_len = strlen(dest);\n    size_t src_len = strlen(src);\n    strcat(dest, src);\n    int result = strlen(dest) + strlen(src);\n    printf(\"Result: %d\\n\", result);\n    return 0;\n}",
            "answer": 17
        }
    },
    {
        "id": "SL-MIX-S001-V038",
        "metadata": {
            "name": "C File I/O and Error Handling Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "c_file_io_error",
            "mixed_types": ["API Call", "Boolean", "Assignment"]
        },
        "task": {
            "description": "Given the following C code snippet, what is the value of variable bytes_read when attempting to read from a valid file containing 'Test Data'?",
            "code": "#include <stdio.h>\n#include <string.h>\nint main() {\n    FILE *file = fopen(\"test.txt\", \"w\");\n    if (file) {\n        fprintf(file, \"Test Data\");\n        fclose(file);\n    }\n    \n    file = fopen(\"test.txt\", \"r\");\n    char buffer[100];\n    size_t bytes_read = 0;\n    if (file != NULL) {\n        bytes_read = fread(buffer, 1, sizeof(buffer), file);\n        fclose(file);\n    }\n    printf(\"Bytes read: %zu\\n\", bytes_read);\n    return 0;\n}",
            "answer": 9
        }
    },
    {
        "id": "SL-MIX-S001-V039",
        "metadata": {
            "name": "Async Programming and Arithmetic Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "async_arithmetic",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet with async function, what is the value returned by calling `asyncio.run(calculate_sum(10, 15))`?",
            "code": "import asyncio\n\nasync def calculate_sum(a, b):\n    await asyncio.sleep(0)  # Simulate async operation\n    result = a + b\n    multiplied = result * 2\n    return multiplied\n\n# Direct calculation for comparison\ndirect_result = (10 + 15) * 2\nfinal_result = asyncio.run(calculate_sum(10, 15))\nprint(f\"Result: {final_result}\")",
            "answer": 50
        }
    },
    {
        "id": "SL-MIX-S001-V040",
        "metadata": {
            "name": "Metaclass and Method Resolution Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "metaclass_method_resolution",
            "mixed_types": ["API Call", "Assignment", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet with metaclass, what is the value returned by calling `instance.compute(4)`?",
            "code": "class MetaClass(type):\n    def __new__(cls, name, bases, attrs):\n        if 'compute' in attrs:\n            original_compute = attrs['compute']\n            def enhanced_compute(self, x):\n                return original_compute(self, x) + 10\n            attrs['compute'] = enhanced_compute\n        return super().__new__(cls, name, bases, attrs)\n\nclass Calculator(metaclass=MetaClass):\n    def compute(self, x):\n        return x * 3\n\ninstance = Calculator()\noriginal_calculation = 4 * 3\nenhanced_result = instance.compute(4)\nprint(f\"Result: {enhanced_result}\")",
            "answer": 22
        }
    },
    {
        "id": "SL-MIX-S001-V041",
        "metadata": {
            "name": "Numpy Array Operations Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "numpy_array_operations",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet using numpy operations, what is the sum of all elements in the result array after executing `result = arr1 * 2 + arr2`?",
            "code": "# Simulating numpy-like operations without importing numpy\nclass SimpleArray:\n    def __init__(self, data):\n        self.data = data\n    \n    def __mul__(self, scalar):\n        return SimpleArray([x * scalar for x in self.data])\n    \n    def __add__(self, other):\n        return SimpleArray([a + b for a, b in zip(self.data, other.data)])\n    \n    def sum(self):\n        return sum(self.data)\n\narr1 = SimpleArray([1, 2, 3, 4])\narr2 = SimpleArray([5, 6, 7, 8])\nmultiplied = arr1 * 2\nresult = arr1 * 2 + arr2\ntotal_sum = result.sum()\nprint(f\"Sum: {total_sum}\")",
            "answer": 36
        }
    },
    {
        "id": "SL-MIX-S001-V042",
        "metadata": {
            "name": "Database Query Simulation Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "database_query_simulation",
            "mixed_types": ["API Call", "Boolean", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet simulating database operations, what is the value of variable total_salary after executing the query simulation?",
            "code": "# Simulating database operations\nemployees = [\n    {'name': 'Alice', 'dept': 'IT', 'salary': 50000, 'active': True},\n    {'name': 'Bob', 'dept': 'HR', 'salary': 45000, 'active': True},\n    {'name': 'Charlie', 'dept': 'IT', 'salary': 55000, 'active': False},\n    {'name': 'Diana', 'dept': 'IT', 'salary': 60000, 'active': True}\n]\n\n# Query: SELECT SUM(salary) FROM employees WHERE dept='IT' AND active=True\nfiltered_employees = [emp for emp in employees if emp['dept'] == 'IT' and emp['active']]\nsalaries = [emp['salary'] for emp in filtered_employees]\ntotal_salary = sum(emp['salary'] for emp in employees if emp['dept'] == 'IT' and emp['active'])\nprint(f\"Total salary: {total_salary}\")",
            "answer": 110000
        }
    },
    {
        "id": "SL-MIX-S001-V043",
        "metadata": {
            "name": "Graph Algorithm Simulation Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "graph_algorithm_simulation",
            "mixed_types": ["API Call", "Arithmetic", "Boolean"]
        },
        "task": {
            "description": "Given the following code snippet implementing a simple graph traversal, what is the value of variable path_length after finding the shortest path?",
            "code": "# Simple graph representation and path finding\ngraph = {\n    'A': ['B', 'C'],\n    'B': ['A', 'D', 'E'],\n    'C': ['A', 'F'],\n    'D': ['B'],\n    'E': ['B', 'F'],\n    'F': ['C', 'E']\n}\n\ndef find_shortest_path(graph, start, end, path=[]):\n    path = path + [start]\n    if start == end:\n        return path\n    if start not in graph:\n        return None\n    shortest = None\n    for node in graph[start]:\n        if node not in path:\n            newpath = find_shortest_path(graph, node, end, path)\n            if newpath:\n                if not shortest or len(newpath) < len(shortest):\n                    shortest = newpath\n    return shortest\n\nshortest_path = find_shortest_path(graph, 'A', 'F')\npath_length = len(shortest_path) if shortest_path else 0\nprint(f\"Path length: {path_length}\")",
            "answer": 3
        }
    },
    {
        "id": "SL-MIX-S001-V044",
        "metadata": {
            "name": "Memory Pool and Allocation Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "memory_pool_allocation",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following C code snippet with custom memory management, what is the value of variable allocated_blocks after all allocation operations?",
            "code": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct {\n    void *memory;\n    size_t size;\n    int allocated_blocks;\n} MemoryPool;\n\nMemoryPool* create_pool(size_t total_size) {\n    MemoryPool *pool = malloc(sizeof(MemoryPool));\n    pool->memory = malloc(total_size);\n    pool->size = total_size;\n    pool->allocated_blocks = 0;\n    return pool;\n}\n\nvoid* pool_alloc(MemoryPool *pool, size_t size) {\n    if (pool && pool->memory) {\n        pool->allocated_blocks++;\n        return pool->memory;  // Simplified allocation\n    }\n    return NULL;\n}\n\nint main() {\n    MemoryPool *pool = create_pool(1024);\n    void *ptr1 = pool_alloc(pool, 64);\n    void *ptr2 = pool_alloc(pool, 128);\n    void *ptr3 = pool_alloc(pool, 32);\n    \n    int allocated_blocks = pool->allocated_blocks;\n    printf(\"Allocated blocks: %d\\n\", allocated_blocks);\n    \n    free(pool->memory);\n    free(pool);\n    return allocated_blocks;\n}",
            "answer": 3
        }
    },
    {
        "id": "SL-MIX-S001-V045",
        "metadata": {
            "name": "Binary Tree Traversal Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "binary_tree_traversal",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet with binary tree operations, what is the value of variable node_count after traversing the tree?",
            "code": "class TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef count_nodes(root):\n    if not root:\n        return 0\n    return 1 + count_nodes(root.left) + count_nodes(root.right)\n\n# Create binary tree: 1-2-4, 1-3-5-6\nroot = TreeNode(1)\nroot.left = TreeNode(2)\nroot.right = TreeNode(3)\nroot.left.left = TreeNode(4)\nroot.right.left = TreeNode(5)\nroot.right.right = TreeNode(6)\n\nnode_count = count_nodes(root)\nprint(f\"Node count: {node_count}\")",
            "answer": 6
        }
    },
    {
        "id": "SL-MIX-S001-V046",
        "metadata": {
            "name": "Recursive Fibonacci with Memoization Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "recursive_fibonacci_memo",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet with memoized fibonacci, what is the value returned by calling `fibonacci(7)`?",
            "code": "def fibonacci(n, memo={}):\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)\n    return memo[n]\n\n# Calculate some values\nfib_5 = fibonacci(5)\nfib_6 = fibonacci(6)\nfib_7 = fibonacci(7)\nprint(f\"Fibonacci(7): {fib_7}\")",
            "answer": 13
        }
    },
    {
        "id": "SL-MIX-S001-V047",
        "metadata": {
            "name": "Closure Variable Capture Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "closure_variable_capture",
            "mixed_types": ["Assignment", "Arithmetic", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet with closure, what is the value returned by calling `multiplier(4)`?",
            "code": "def create_multiplier(factor):\n    base_value = 10\n    def multiplier(x):\n        nonlocal base_value\n        base_value += 1\n        return x * factor + base_value\n    return multiplier\n\nmult_func = create_multiplier(3)\nresult1 = mult_func(2)  # base_value becomes 11, returns 2*3+11=17\nresult2 = mult_func(4)  # base_value becomes 12, returns 4*3+12=24\nprint(f\"Result: {result2}\")",
            "answer": 24
        }
    },
    {
        "id": "SL-MIX-S001-V048",
        "metadata": {
            "name": "Generator Function with State Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "generator_function_state",
            "mixed_types": ["API Call", "Arithmetic", "Assignment"]
        },
        "task": {
            "description": "Given the following code snippet with generator, what is the third value yielded by the generator `sequence_gen()`?",
            "code": "def sequence_gen():\n    value = 1\n    while value <= 10:\n        yield value * 2\n        value += 2\n\ngen = sequence_gen()\nfirst = next(gen)   # value=1, yields 1*2=2, value becomes 3\nsecond = next(gen)  # value=3, yields 3*2=6, value becomes 5\nthird = next(gen)   # value=5, yields 5*2=10, value becomes 7\nprint(f\"Third value: {third}\")",
            "answer": 10
        }
    },
    {
        "id": "SL-MIX-S001-V049",
        "metadata": {
            "name": "Property Descriptor and Validation Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "property_descriptor_validation",
            "mixed_types": ["Assignment", "Boolean", "Arithmetic"]
        },
        "task": {
            "description": "Given the following code snippet with property descriptor, what is the value of `obj.temperature` after setting it to 150?",
            "code": "class TemperatureDescriptor:\n    def __get__(self, obj, objtype=None):\n        return obj._temperature\n    \n    def __set__(self, obj, value):\n        if value < 0:\n            obj._temperature = 0\n        elif value > 100:\n            obj._temperature = 100\n        else:\n            obj._temperature = value\n\nclass Thermostat:\n    temperature = TemperatureDescriptor()\n    \n    def __init__(self):\n        self._temperature = 20\n\nobj = Thermostat()\nobj.temperature = 75   # Sets to 75\nobj.temperature = 150  # Clamps to 100\nfinal_temp = obj.temperature\nprint(f\"Final temperature: {final_temp}\")",
            "answer": 100
        }
    },
    {
        "id": "SL-MIX-S001-V050",
        "metadata": {
            "name": "Complex Number Operations Mix",
            "category": "Statement-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 0,
            "variant_type": "complex_number_operations",
            "mixed_types": ["Arithmetic", "Assignment", "API Call"]
        },
        "task": {
            "description": "Given the following code snippet with complex number operations, what is the real part of variable result after executing `result = (z1 * z2) + z3.conjugate()`?",
            "code": "z1 = complex(3, 4)      # 3 + 4j\nz2 = complex(2, -1)     # 2 - 1j\nz3 = complex(1, 2)      # 1 + 2j\n\n# z1 * z2 = (3+4j) * (2-1j) = 6-3j+8j-4j² = 6+5j+4 = 10+5j\nproduct = z1 * z2\n# z3.conjugate() = 1 - 2j\nconjugate = z3.conjugate()\n# result = (10+5j) + (1-2j) = 11+3j\nresult = (z1 * z2) + z3.conjugate()\nreal_part = result.real\nprint(f\"Real part: {real_part}\")",
            "answer": 11.0
        }
    }
]
```

### 2 - 代码块级推理 [ Block-Level ] （326）

#### 2A - 线性代码块 [ Linear ]（72）

> ```
> # 线性代码块推理变式生成提示词
> 
> ## 任务目标
> 基于给定的线性代码块种子任务，生成多样化的变式任务来全面测试大模型对顺序执行代码块的理解能力，包括变量状态跟踪、数据流分析、执行顺序推理和最终状态预测。
> 
> ## 线性代码块特征分析
> 线性代码块是指按顺序执行、无分支控制结构的代码段，重点测试模型对语句执行顺序、变量状态变化和数据依赖关系的理解。
> 
> ## 变式生成维度
> 
> ### 1. 执行模式变式
> - **顺序执行变式**: 严格按语句顺序执行的代码块
> - **依赖链执行变式**: 后续语句依赖前面语句结果的执行模式
> - **并行无关变式**: 语句间无依赖关系的独立执行
> - **累积执行变式**: 逐步累积计算结果的执行模式
> - **转换管道变式**: 数据经过多步转换的管道式执行
> - **初始化序列变式**: 对象或结构体的初始化执行序列
> 
> ### 2. 数据流模式变式
> - **单向数据流变式**: 数据从输入到输出的单向流动
> - **链式数据流变式**: 数据在变量间的链式传递
> - **累积数据流变式**: 数据逐步累积和聚合
> - **变换数据流变式**: 数据类型或格式的逐步变换
> - **分离数据流变式**: 一个数据源分离成多个变量
> - **合并数据流变式**: 多个数据源合并成一个结果
> 
> ### 3. 变量生命周期变式
> - **变量初始化变式**: 变量的初始赋值和设置
> - **变量更新变式**: 变量值的逐步更新和修改
> - **变量累积变式**: 变量值的累积计算
> - **变量转换变式**: 变量类型或格式的转换
> - **变量传递变式**: 变量值在不同变量间的传递
> - **变量销毁变式**: 变量生命周期的结束和资源释放
> 
> ### 4. 计算复杂度变式
> - **简单计算变式**: 基础算术运算的线性计算
> - **复合计算变式**: 多步骤的复合数学计算
> - **字符串处理变式**: 字符串操作的线性处理
> - **数组处理变式**: 数组元素的线性处理（非循环）
> - **结构体操作变式**: 结构体字段的逐一设置
> - **指针操作变式**: 指针和地址的线性操作
> 
> ### 5. 内存管理变式
> - **内存分配变式**: malloc/calloc等内存分配操作
> - **内存初始化变式**: 分配内存的初始化设置
> - **指针赋值变式**: 指针变量的赋值和重新指向
> - **内存拷贝变式**: memcpy/strcpy等内存拷贝操作
> - **内存释放变式**: free等内存释放操作
> - **内存状态跟踪变式**: 内存状态在代码块中的变化
> 
> ### 6. 函数调用变式
> - **单函数调用变式**: 单个函数调用及其结果处理
> - **连续函数调用变式**: 多个函数的连续调用
> - **嵌套函数调用变式**: 函数调用结果作为参数的嵌套调用
> - **副作用函数变式**: 有副作用的函数调用对变量的影响
> - **错误处理变式**: 函数返回错误时的处理逻辑
> - **资源管理变式**: 函数调用涉及资源申请和释放
> 
> ### 7. 类型和转换变式
> - **隐式类型转换变式**: 自动类型转换对计算的影响
> - **显式类型转换变式**: 强制类型转换的使用
> - **精度变化变式**: 类型转换导致的精度损失
> - **符号转换变式**: 有符号和无符号类型的转换
> - **指针类型转换变式**: 不同指针类型间的转换
> - **结构体转换变式**: 结构体和基础类型的转换
> 
> ### 8. 错误和异常变式
> - **空指针检查变式**: NULL指针的检查和处理
> - **边界条件变式**: 数组越界、缓冲区溢出等边界情况
> - **资源不足变式**: 内存不足等资源限制情况
> - **参数验证变式**: 输入参数的有效性检查
> - **状态一致性变式**: 对象状态的一致性维护
> - **错误传播变式**: 错误在代码块中的传播
> 
> ### 9. 平台相关变式
> - **字节序变式**: 大小端字节序对数据的影响
> - **对齐变式**: 内存对齐对结构体布局的影响
> - **指针大小变式**: 32位/64位平台的指针大小差异
> - **类型大小变式**: 不同平台上数据类型大小的差异
> - **编译器优化变式**: 编译器优化对代码执行的影响
> - **标准库差异变式**: 不同平台标准库实现的差异
> 
> ### 10. 语言特性变式
> - **Python特性变式**: 动态类型、多重赋值、解包等特性
> - **C语言特性变式**: 指针、结构体、预处理器等特性
> - **Java特性变式**: 对象初始化、引用传递等特性
> - **JavaScript特性变式**: 动态类型、对象属性等特性
> - **跨语言移植变式**: 相同逻辑在不同语言中的实现差异
> 
> ## 复杂度层次设计
> 
> ### 简单线性 (Easy)
> - 3-5条语句的简单顺序执行
> - 基础数据类型的简单操作
> - 明确的数据流向，无复杂依赖
> - 直观的计算过程，易于手工跟踪
> 
> ### 中等线性 (Medium)
> - 6-10条语句的中等复杂度执行
> - 包含函数调用或类型转换
> - 中等复杂度的数据依赖关系
> - 需要仔细跟踪变量状态变化
> 
> ### 复杂线性 (Hard)
> - 10条以上语句的复杂执行序列
> - 涉及内存管理、指针操作或复杂计算
> - 多层次的数据依赖和变换
> - 需要深入理解语言语义和执行模型
> 
> ## 生成策略
> 
> ### 种子分析策略
> 1. **识别执行模式**: 分析种子的执行流程特征
> 2. **提取数据流**: 识别变量间的数据依赖关系
> 3. **分析复杂点**: 找出容易产生理解偏差的关键点
> 4. **确定变式方向**: 选择合适的变式生成维度
> 
> ### 变式设计原则
> 1. **保持线性特征**: 确保所有变式都是线性执行，无分支
> 2. **渐进复杂化**: 从简单变式逐步增加到复杂变式
> 3. **现实场景**: 优先设计实际编程中常见的线性代码模式
> 4. **测试覆盖**: 确保每个变式都测试特定的推理能力
> 
> ### 质量保证
> 1. **执行顺序验证**: 确保语句执行顺序的推理正确
> 2. **状态跟踪验证**: 验证变量状态变化的准确性
> 3. **数据流验证**: 确保数据依赖关系的正确理解
> 4. **边界情况验证**: 包含各种边界和异常情况
> 
> ## 输出格式要求
> 
> ```json
> [
>     {
>         "id": "BL-LN-S00X-V001",
>         "metadata": {
>             "name": "线性代码块变式名称",
>             "category": "Block-Level",
>             "subcategory": "Linear",
>             "type": "variant",
>             "source": "Generated",
>             "language": "目标语言",
>             "difficulty": "easy/medium/hard",
>             "intervention": 0,
>             "variant_type": "变式类型标签",
>             "execution_pattern": "sequential/dependent/accumulative/transform"
>         },
>         "task": {
>             "description": "线性代码块推理任务描述",
>             "code": "线性执行的代码块",
>             "answer": "最终状态或计算结果"
>         }
>     },
>     {下一个变式...}
> ]
> 
> 特殊字段说明
> execution_pattern: 标识代码块的执行模式特征
> variant_type: 描述具体的变式类型
> 生成目标
> 为每个提供的种子任务生成10-15个线性代码块变式，确保：
> 
> 每种难度等级至少包含3-5个变式
> 涵盖至少6-8种不同的执行模式
> 包含2-3个跨语言的变式
> 至少包含3-4个涉及内存管理或复杂数据流的变式
> 请基于此提示词，为给定的线性代码块种子任务生成全面的变式集合，输出格式为包含所有变式的JSON数组。
> ```

```JSON
[
    {
        "id": "BL-LN-S001-V001",
        "metadata": {
            "name": "内存分配简化变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "memory_allocation",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following simplified initialization block, what is the final value of buf->len?",
            "code": "void init_buffer(struct buffer *buf) {\n    buf->size = 64;\n    buf->data = malloc(buf->size);\n    buf->len = 0;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S001-V002",
        "metadata": {
            "name": "Python动态内存变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following Python buffer initialization, what is the final value of buf['length']?",
            "code": "def init_dynamic_buffer(buf):\n    buf['type'] = 'DYNAMIC'\n    buf['capacity'] = 128\n    buf['data'] = [None] * buf['capacity']\n    buf['length'] = 0",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S001-V003",
        "metadata": {
            "name": "错误处理扩展变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "error_handling",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following extended initialization with error checking, what is the final value of buf->len when malloc succeeds?",
            "code": "int k5_buf_init_extended(struct k5buf *buf) {\n    buf->buftype = K5BUF_DYNAMIC;\n    buf->space = 256;\n    buf->data = malloc(buf->space);\n    if (buf->data == NULL) {\n        buf->len = -1;\n        return -1;\n    }\n    memset(buf->data, 0, buf->space);\n    buf->len = 0;\n    return 0;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S001-V004",
        "metadata": {
            "name": "累积初始化变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "accumulative_init",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following cumulative buffer setup, what is the final value of buf->total_allocated?",
            "code": "void setup_buffer_pool(struct buffer_pool *buf) {\n    buf->block_size = 32;\n    buf->num_blocks = 4;\n    buf->total_allocated = buf->block_size * buf->num_blocks;\n    buf->used_blocks = 0;\n    buf->free_blocks = buf->num_blocks;\n}",
            "answer": 128
        }
    },
    {
        "id": "BL-LN-S001-V005",
        "metadata": {
            "name": "指针操作链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "pointer_operations",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following pointer manipulation block, what is the final value pointed by end_ptr?",
            "code": "void setup_buffer_ptrs(struct k5buf *buf) {\n    buf->data = malloc(64);\n    buf->start_ptr = buf->data;\n    buf->current_ptr = buf->start_ptr;\n    buf->end_ptr = buf->start_ptr + 64;\n    buf->len = buf->end_ptr - buf->start_ptr;\n}",
            "answer": 64
        }
    },
    {
        "id": "BL-LN-S001-V006",
        "metadata": {
            "name": "Java对象初始化变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following Java buffer initialization, what is the final value of buffer.length?",
            "code": "public void initDynamicBuffer(DynamicBuffer buffer) {\n    buffer.bufferType = BufferType.DYNAMIC;\n    buffer.capacity = 128;\n    buffer.data = new byte[buffer.capacity];\n    buffer.length = 0;\n    buffer.growthFactor = 2.0;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S001-V007",
        "metadata": {
            "name": "内存对齐变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "memory_alignment",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following aligned memory allocation, what is the final value of buf->aligned_size?",
            "code": "void init_aligned_buffer(struct aligned_buf *buf) {\n    buf->requested_size = 100;\n    buf->alignment = 16;\n    buf->aligned_size = (buf->requested_size + buf->alignment - 1) & ~(buf->alignment - 1);\n    buf->data = aligned_alloc(buf->alignment, buf->aligned_size);\n    buf->len = 0;\n}",
            "answer": 112
        }
    },
    {
        "id": "BL-LN-S001-V008",
        "metadata": {
            "name": "缓冲区状态机变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "state_machine",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following buffer state initialization, what is the final value of buf->state?",
            "code": "void init_buffer_state(struct state_buf *buf) {\n    buf->state = BUF_STATE_UNINITIALIZED;\n    buf->data = malloc(256);\n    buf->state = (buf->data != NULL) ? BUF_STATE_ALLOCATED : BUF_STATE_ERROR;\n    buf->len = 0;\n    buf->state = BUF_STATE_READY;\n}",
            "answer": "BUF_STATE_READY"
        }
    },
    {
        "id": "BL-LN-S001-V009",
        "metadata": {
            "name": "位操作缓冲区变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bitwise_operations",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following bit manipulation buffer setup, what is the final value of buf->flags?",
            "code": "void init_bit_buffer(struct bit_buf *buf) {\n    buf->flags = 0;\n    buf->flags |= FLAG_DYNAMIC;\n    buf->flags |= FLAG_GROWABLE;\n    buf->flags &= ~FLAG_READONLY;\n    buf->len = 0;\n    buf->capacity = 128;\n}",
            "answer": "FLAG_DYNAMIC | FLAG_GROWABLE"
        }
    },
    {
        "id": "BL-LN-S001-V010",
        "metadata": {
            "name": "JavaScript对象变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following JavaScript buffer initialization, what is the final value of buffer.length?",
            "code": "function initDynamicBuffer(buffer) {\n    buffer.type = 'DYNAMIC';\n    buffer.capacity = 128;\n    buffer.data = new ArrayBuffer(buffer.capacity);\n    buffer.length = 0;\n    buffer.view = new Uint8Array(buffer.data);\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S001-V011",
        "metadata": {
            "name": "多重指针变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "multiple_pointers",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following multiple pointer setup, what is the final value of **double_ptr?",
            "code": "void setup_double_ptr(int **double_ptr, int *single_ptr) {\n    *single_ptr = 42;\n    *double_ptr = single_ptr;\n    **double_ptr = **double_ptr + 8;\n    int temp = **double_ptr;\n    **double_ptr = temp * 2;\n}",
            "answer": 100
        }
    },
    {
        "id": "BL-LN-S001-V012",
        "metadata": {
            "name": "内存池分配变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "memory_pool",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following memory pool allocation, what is the final value of pool->used_bytes?",
            "code": "void init_memory_pool(struct mem_pool *pool) {\n    pool->total_size = 1024;\n    pool->block_size = 64;\n    pool->num_blocks = pool->total_size / pool->block_size;\n    pool->used_bytes = 0;\n    pool->allocated_blocks = pool->used_bytes / pool->block_size;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S002-V001",
        "metadata": {
            "name": "配置累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "configuration_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following configuration setup, what is the final value of total_timeout?",
            "code": "connection_timeout = 10\nread_timeout = 5\nwrite_timeout = 8\ntotal_timeout = connection_timeout + read_timeout + write_timeout\nmax_connections = 100",
            "answer": 23
        }
    },
    {
        "id": "BL-LN-S002-V002",
        "metadata": {
            "name": "字符串处理变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "string_processing",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following string configuration block, what is the final length of service_name?",
            "code": "service_prefix = 'web'\nservice_id = '001'\nservice_suffix = 'prod'\nservice_name = f\"{service_prefix}-{service_id}-{service_suffix}\"\nport = 8080",
            "answer": 12
        }
    },
    {
        "id": "BL-LN-S002-V003",
        "metadata": {
            "name": "C语言配置变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following C configuration block, what is the final value of config->retry_count?",
            "code": "void init_config(struct config *config) {\n    config->retry_count = 3;\n    config->timeout_ms = 5000;\n    config->debug_mode = 0;\n    config->buffer_size = 1024;\n}",
            "answer": 3
        }
    },
    {
        "id": "BL-LN-S002-V004",
        "metadata": {
            "name": "数值计算链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "numerical_chain",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following numerical calculation chain, what is the final value of performance_score?",
            "code": "base_score = 100\nlatency_penalty = 15\nthroughput_bonus = 25\nerror_penalty = 5\nperformance_score = base_score - latency_penalty + throughput_bonus - error_penalty",
            "answer": 105
        }
    },
    {
        "id": "BL-LN-S002-V005",
        "metadata": {
            "name": "布尔逻辑变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boolean_logic",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following boolean configuration, what is the final value of system_ready?",
            "code": "auth_enabled = True\nlogging_enabled = True\ncache_enabled = False\ndebug_mode = False\nsystem_ready = auth_enabled and logging_enabled",
            "answer": true
        }
    },
    {
        "id": "BL-LN-S002-V006",
        "metadata": {
            "name": "Java配置对象变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following Java configuration setup, what is the final value of config.maxRetries?",
            "code": "public void setupConfiguration(Configuration config) {\n    config.maxRetries = 3;\n    config.timeoutSeconds = 30;\n    config.logLevel = LogLevel.INFO;\n    config.enableDebug = false;\n    config.encoding = \"UTF-8\";\n}",
            "answer": 3
        }
    },
    {
        "id": "BL-LN-S002-V007",
        "metadata": {
            "name": "环境变量处理变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "environment_processing",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following environment variable processing, what is the final value of worker_count?",
            "code": "default_workers = 4\nenv_workers = '8'\nmax_workers = 16\nworker_count = min(int(env_workers), max_workers)\nthread_pool_size = worker_count * 2",
            "answer": 8
        }
    },
    {
        "id": "BL-LN-S002-V008",
        "metadata": {
            "name": "列表初始化变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "list_initialization",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following list initialization, what is the final length of supported_formats?",
            "code": "image_formats = ['jpg', 'png', 'gif']\nvideo_formats = ['mp4', 'avi']\nsupported_formats = image_formats + video_formats\nmax_file_size = 10485760\nallow_upload = True",
            "answer": 5
        }
    },
    {
        "id": "BL-LN-S002-V009",
        "metadata": {
            "name": "字典配置变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "dictionary_configuration",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following dictionary configuration, what is the final value of config['total_memory']?",
            "code": "config = {}\nconfig['cpu_cores'] = 4\nconfig['memory_per_core'] = 2048\nconfig['total_memory'] = config['cpu_cores'] * config['memory_per_core']\nconfig['disk_space'] = 100000",
            "answer": 8192
        }
    },
    {
        "id": "BL-LN-S002-V010",
        "metadata": {
            "name": "JavaScript配置变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following JavaScript configuration, what is the final value of config.maxRetries?",
            "code": "const config = {};\nconfig.maxRetries = 3;\nconfig.timeoutMs = 5000;\nconfig.debugMode = false;\nconfig.apiVersion = 'v2';",
            "answer": 3
        }
    },
    {
        "id": "BL-LN-S002-V011",
        "metadata": {
            "name": "类型转换配置变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "type_conversion",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following type conversion configuration, what is the final type of port_number?",
            "code": "port_str = '8080'\nport_number = int(port_str)\nhost_name = 'localhost'\nssl_enabled = 'true'\nssl_bool = ssl_enabled.lower() == 'true'",
            "answer": "int"
        }
    },
    {
        "id": "BL-LN-S002-V012",
        "metadata": {
            "name": "C结构体配置变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "struct_configuration",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following C struct configuration, what is the final value of settings->flags?",
            "code": "void configure_system(struct system_settings *settings) {\n    settings->max_connections = 1000;\n    settings->timeout_seconds = 30;\n    settings->log_level = 2;\n    settings->flags = 0x01 | 0x04 | 0x10;\n    settings->buffer_size = 4096;\n}",
            "answer": 21
        }
    },
    {
        "id": "BL-LN-S003-V001",
        "metadata": {
            "name": "简化函数调用变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "function_call_chain",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following simplified file processing, what is the return value when file_open succeeds?",
            "code": "int simple_file_process(const char *filename) {\n    FILE *fp = fopen(filename, \"r\");\n    if (fp == NULL) return -1;\n    int result = process_content(fp);\n    fclose(fp);\n    return result == 0 ? 0 : -1;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V002",
        "metadata": {
            "name": "Python异常处理变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "exception_handling",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following Python file processing, what is the return value when file processing succeeds?",
            "code": "def process_data_file(filename):\n    result = -1\n    try:\n        with open(filename, 'r') as f:\n            data = f.read()\n            parsed = parse_data(data)\n            result = 0 if validate_data(parsed) else -1\n    except IOError:\n        result = -1\n    return result",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V003",
        "metadata": {
            "name": "资源管理链式变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "resource_management",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following resource management chain, what is the final value of ctx->status when all operations succeed?",
            "code": "int init_context(struct context *ctx, const char *config_file) {\n    ctx->status = STATUS_INIT;\n    ctx->config = load_config(config_file);\n    if (ctx->config == NULL) {\n        ctx->status = STATUS_ERROR;\n        return -1;\n    }\n    ctx->resources = allocate_resources(ctx->config);\n    ctx->status = (ctx->resources != NULL) ? STATUS_READY : STATUS_ERROR;\n    return ctx->status == STATUS_READY ? 0 : -1;\n}",
            "answer": "STATUS_READY"
        }
    },
    {
        "id": "BL-LN-S003-V004",
        "metadata": {
            "name": "数据库连接变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "database_connection",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following database connection setup, what is the return value when connection succeeds?",
            "code": "int connect_database(struct db_context *ctx, const char *conn_string) {\n    int result = -1;\n    ctx->connection = db_connect(conn_string);\n    if (ctx->connection != NULL) {\n        ctx->prepared_stmt = db_prepare(ctx->connection, \"SELECT 1\");\n        result = (ctx->prepared_stmt != NULL) ? 0 : -1;\n    }\n    return result;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V005",
        "metadata": {
            "name": "网络套接字变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "network_socket",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following socket setup, what is the return value when socket creation and binding succeed?",
            "code": "int setup_server_socket(int port) {\n    int sockfd = socket(AF_INET, SOCK_STREAM, 0);\n    if (sockfd < 0) return -1;\n    struct sockaddr_in addr;\n    addr.sin_family = AF_INET;\n    addr.sin_port = htons(port);\n    addr.sin_addr.s_addr = INADDR_ANY;\n    int bind_result = bind(sockfd, (struct sockaddr*)&addr, sizeof(addr));\n    return bind_result == 0 ? sockfd : -1;\n}",
            "answer": "sockfd"
        }
    },
    {
        "id": "BL-LN-S003-V006",
        "metadata": {
            "name": "Java资源管理变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following Java resource management, what is the return value when file processing succeeds?",
            "code": "public int processFile(String filename) {\n    int result = -1;\n    try (FileInputStream fis = new FileInputStream(filename)) {\n        byte[] buffer = new byte[1024];\n        int bytesRead = fis.read(buffer);\n        result = (bytesRead > 0) ? 0 : -1;\n    } catch (IOException e) {\n        result = -1;\n    }\n    return result;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V007",
        "metadata": {
            "name": "内存映射文件变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "memory_mapping",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following memory mapping setup, what is the return value when mapping succeeds?",
            "code": "int map_file_to_memory(const char *filename, struct file_map *map) {\n    int fd = open(filename, O_RDONLY);\n    if (fd < 0) return -1;\n    map->size = lseek(fd, 0, SEEK_END);\n    map->data = mmap(NULL, map->size, PROT_READ, MAP_PRIVATE, fd, 0);\n    close(fd);\n    return (map->data != MAP_FAILED) ? 0 : -1;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V008",
        "metadata": {
            "name": "动态库加载变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "dynamic_loading",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following dynamic library loading, what is the return value when loading and symbol resolution succeed?",
            "code": "int load_plugin(const char *lib_path, struct plugin *p) {\n    p->handle = dlopen(lib_path, RTLD_LAZY);\n    if (!p->handle) return -1;\n    p->init_func = dlsym(p->handle, \"plugin_init\");\n    if (!p->init_func) {\n        dlclose(p->handle);\n        return -1;\n    }\n    return p->init_func() == 0 ? 0 : -1;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V009",
        "metadata": {
            "name": "线程同步变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "thread_synchronization",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following thread synchronization setup, what is the return value when mutex initialization succeeds?",
            "code": "int init_thread_sync(struct sync_context *ctx) {\n    int result = pthread_mutex_init(&ctx->mutex, NULL);\n    if (result != 0) return -1;\n    result = pthread_cond_init(&ctx->condition, NULL);\n    if (result != 0) {\n        pthread_mutex_destroy(&ctx->mutex);\n        return -1;\n    }\n    ctx->initialized = 1;\n    return 0;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V010",
        "metadata": {
            "name": "JavaScript Promise变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following JavaScript async setup, what is the return value when file reading succeeds?",
            "code": "async function processFile(filename) {\n    let result = -1;\n    try {\n        const fs = require('fs').promises;\n        const data = await fs.readFile(filename, 'utf8');\n        const parsed = JSON.parse(data);\n        result = parsed.valid ? 0 : -1;\n    } catch (error) {\n        result = -1;\n    }\n    return result;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V011",
        "metadata": {
            "name": "信号处理变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "signal_handling",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following signal handler setup, what is the return value when signal registration succeeds?",
            "code": "int setup_signal_handlers(struct signal_context *ctx) {\n    struct sigaction sa;\n    sa.sa_handler = handle_signal;\n    sigemptyset(&sa.sa_mask);\n    sa.sa_flags = 0;\n    int result = sigaction(SIGTERM, &sa, &ctx->old_term);\n    if (result != 0) return -1;\n    result = sigaction(SIGINT, &sa, &ctx->old_int);\n    return result == 0 ? 0 : -1;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S003-V012",
        "metadata": {
            "name": "Python上下文管理器变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "context_manager",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following Python context manager usage, what is the return value when database operations succeed?",
            "code": "def process_database_transaction(query):\n    result = -1\n    with database_connection() as conn:\n        cursor = conn.cursor()\n        cursor.execute(query)\n        rows = cursor.fetchall()\n        result = 0 if len(rows) > 0 else -1\n        conn.commit()\n    return result",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S004-V001",
        "metadata": {
            "name": "数学计算链扩展变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "mathematical_chain",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following extended calculation chain, what is the final value of final_result?",
            "code": "initial = 5\nstep1 = initial * 2\nstep2 = step1 + 3\nstep3 = step2 ** 2\nstep4 = step3 // 4\nfinal_result = step4 - 1",
            "answer": 41
        }
    },
    {
        "id": "BL-LN-S004-V002",
        "metadata": {
            "name": "类型转换链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "type_conversion",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following type conversion chain, what is the final value of result?",
            "code": "double input = 3.7;\nint step1 = (int)input;\nfloat step2 = step1 * 2.5f;\nlong step3 = (long)step2;\nunsigned int result = (unsigned int)step3;",
            "answer": 7
        }
    },
    {
        "id": "BL-LN-S004-V003",
        "metadata": {
            "name": "字符串变换链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "string_transformation",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following string transformation chain, what is the final length of processed_text?",
            "code": "original = \"  Hello World  \"\ntrimmed = original.strip()\nlowercased = trimmed.lower()\nreplaced = lowercased.replace(\" \", \"_\")\nprocessed_text = replaced.upper()",
            "answer": 11
        }
    },
    {
        "id": "BL-LN-S004-V004",
        "metadata": {
            "name": "科学计算链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "scientific_computation",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following scientific calculation chain, what is the final value of normalized_result?",
            "code": "import math\nangle_degrees = 45\nangle_radians = math.radians(angle_degrees)\nsin_value = math.sin(angle_radians)\nsquared_value = sin_value ** 2\nnormalized_result = round(squared_value, 3)",
            "answer": 0.5
        }
    },
    {
        "id": "BL-LN-S004-V005",
        "metadata": {
            "name": "Java BigDecimal计算变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following Java BigDecimal calculation, what is the final value of result.intValue()?",
            "code": "BigDecimal base = new BigDecimal(\"10.0\");\nBigDecimal multiplier = new BigDecimal(\"3.5\");\nBigDecimal step1 = base.multiply(multiplier);\nBigDecimal step2 = step1.add(new BigDecimal(\"2.5\"));\nBigDecimal result = step2.setScale(0, RoundingMode.HALF_UP);",
            "answer": 38
        }
    },
    {
        "id": "BL-LN-S004-V006",
        "metadata": {
            "name": "位操作计算链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bitwise_operations",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following bitwise calculation chain, what is the final value of result?",
            "code": "unsigned int input = 0xFF;\nunsigned int step1 = input << 4;\nunsigned int step2 = step1 | 0x0F;\nunsigned int step3 = step2 & 0xF0F0;\nunsigned int result = step3 >> 2;",
            "answer": 1020
        }
    },
    {
        "id": "BL-LN-S004-V007",
        "metadata": {
            "name": "JavaScript数值链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following JavaScript number chain, what is the final value of result?",
            "code": "let base = 100;\nlet percentage = 0.15;\nlet increase = base * percentage;\nlet intermediate = base + increase;\nlet discount = intermediate * 0.1;\nlet result = Math.round(intermediate - discount);",
            "answer": 104
        }
    },
    {
        "id": "BL-LN-S004-V008",
        "metadata": {
            "name": "数组索引计算变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "array_indexing",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following array indexing calculation, what is the final value of selected_value?",
            "code": "data = [10, 20, 30, 40, 50]\nindex_base = 2\noffset = 1\ncalculated_index = (index_base + offset) % len(data)\nselected_value = data[calculated_index]",
            "answer": 40
        }
    },
    {
        "id": "BL-LN-S004-V009",
        "metadata": {
            "name": "温度转换链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "unit_conversion",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following temperature conversion chain, what is the final value of kelvin?",
            "code": "celsius = 25\nfahrenheit = celsius * 9/5 + 32\nback_to_celsius = (fahrenheit - 32) * 5/9\nkelvin = back_to_celsius + 273.15\nrounded_kelvin = round(kelvin, 1)",
            "answer": 298.1
        }
    },
    {
        "id": "BL-LN-S004-V010",
        "metadata": {
            "name": "复数计算链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "complex_numbers",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following complex number calculation, what is the final value of magnitude?",
            "code": "z1 = complex(3, 4)\nz2 = complex(1, 2)\nz_sum = z1 + z2\nz_product = z_sum * complex(0, 1)\nmagnitude = abs(z_product)",
            "answer": 7.211102550927978
        }
    },
    {
        "id": "BL-LN-S004-V011",
        "metadata": {
            "name": "金融计算链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "financial_calculation",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following financial calculation chain, what is the final value of final_amount?",
            "code": "principal = 1000\nannual_rate = 0.05\ncompounding_periods = 4\nyears = 2\nperiodic_rate = annual_rate / compounding_periods\ntotal_periods = compounding_periods * years\nfinal_amount = round(principal * (1 + periodic_rate) ** total_periods, 2)",
            "answer": 1104.49
        }
    },
    {
        "id": "BL-LN-S004-V012",
        "metadata": {
            "name": "C浮点精度链变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "floating_precision",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following floating point precision chain, what is the final value of result when cast to int?",
            "code": "float base = 10.0f;\ndouble step1 = base / 3.0;\nfloat step2 = (float)step1;\ndouble step3 = step2 * 3.0;\nfloat step4 = (float)step3;\nint result = (int)(step4 + 0.5f);",
            "answer": 10
        }
    },
    {
        "id": "BL-LN-S005-V001",
        "metadata": {
            "name": "浮点累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "floating_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following floating point accumulation, what is the final value of total (rounded to 1 decimal)?",
            "code": "float total = 0.0f;\ntotal += 10.5f;\ntotal += 15.3f;\ntotal += 7.2f;\ntotal *= 1.5f;\nprintf(\"Total: %.1f\\n\", total);",
            "answer": 49.5
        }
    },
    {
        "id": "BL-LN-S005-V002",
        "metadata": {
            "name": "Python列表累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "cross_language",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following Python list accumulation, what is the final length of items?",
            "code": "items = []\nitems.append('apple')\nitems.append('banana')\nitems.extend(['orange', 'grape'])\nitems.remove('banana')\nprint(f\"Items: {len(items)}\")",
            "answer": 3
        }
    },
    {
        "id": "BL-LN-S005-V003",
        "metadata": {
            "name": "字符串累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "string_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following string accumulation, what is the final length of buffer?",
            "code": "char buffer[100] = \"\";\nstrcat(buffer, \"Hello\");\nstrcat(buffer, \" \");\nstrcat(buffer, \"World\");\nstrcat(buffer, \"!\");\nint length = strlen(buffer);",
            "answer": 12
        }
    },
    {
        "id": "BL-LN-S005-V004",
        "metadata": {
            "name": "位标志累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bitwise_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following bit flag accumulation, what is the final value of flags?",
            "code": "unsigned int flags = 0;\nflags |= 0x01;\nflags |= 0x04;\nflags |= 0x10;\nflags &= ~0x04;\nflags |= 0x08;",
            "answer": 25
        }
    },
    {
        "id": "BL-LN-S005-V005",
        "metadata": {
            "name": "Java StringBuilder累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following Java StringBuilder accumulation, what is the final length of the result?",
            "code": "StringBuilder sb = new StringBuilder();\nsb.append(\"Java\");\nsb.append(\" is\");\nsb.append(\" awesome\");\nsb.delete(4, 7);\nString result = sb.toString();",
            "answer": 11
        }
    },
    {
        "id": "BL-LN-S005-V006",
        "metadata": {
            "name": "数组累积求和变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "array_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following array accumulation, what is the final value of running_sum?",
            "code": "numbers = [5, 10, 15, 20]\nrunning_sum = 0\nfor num in numbers:\n    running_sum += num\naverage = running_sum / len(numbers)",
            "answer": 50
        }
    },
    {
        "id": "BL-LN-S005-V007",
        "metadata": {
            "name": "内存块累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "memory_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following memory accumulation, what is the final value of total_allocated?",
            "code": "size_t total_allocated = 0;\ntotal_allocated += malloc_size(64);\ntotal_allocated += malloc_size(128);\ntotal_allocated += malloc_size(256);\ntotal_allocated *= 2;\nsize_t overhead = total_allocated / 10;",
            "answer": 896
        }
    },
    {
        "id": "BL-LN-S005-V008",
        "metadata": {
            "name": "递增计数器变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "counter_increment",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following counter increment operations, what is the final value of counter?",
            "code": "int counter = 0;\ncounter++;\ncounter += 5;\ncounter *= 2;\ncounter -= 3;\nprintf(\"Counter: %d\\n\", counter);",
            "answer": 9
        }
    },
    {
        "id": "BL-LN-S005-V009",
        "metadata": {
            "name": "JavaScript对象累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following JavaScript object accumulation, what is the final value of stats.total?",
            "code": "const stats = { total: 0, count: 0 };\nstats.total += 100;\nstats.count++;\nstats.total += 200;\nstats.count++;\nstats.average = stats.total / stats.count;",
            "answer": 300
        }
    },
    {
        "id": "BL-LN-S005-V010",
        "metadata": {
            "name": "缓冲区填充累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "buffer_filling",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following buffer filling operations, what is the final value of buf->used?",
            "code": "struct buffer *buf = malloc(sizeof(struct buffer));\nbuf->size = 100;\nbuf->data = malloc(buf->size);\nbuf->used = 0;\nbuf->used += write_data(buf, \"Hello\", 5);\nbuf->used += write_data(buf, \"World\", 5);\nbuf->remaining = buf->size - buf->used;",
            "answer": 10
        }
    },
    {
        "id": "BL-LN-S005-V011",
        "metadata": {
            "name": "统计累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "statistics_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following statistics accumulation, what is the final value of stats['sum']?",
            "code": "stats = {'sum': 0, 'count': 0, 'max': 0}\nvalues = [3, 7, 2, 9, 1]\nfor val in values:\n    stats['sum'] += val\n    stats['count'] += 1\n    stats['max'] = max(stats['max'], val)",
            "answer": 22
        }
    },
    {
        "id": "BL-LN-S005-V012",
        "metadata": {
            "name": "哈希累积变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "hash_accumulation",
            "execution_pattern": "accumulative"
        },
        "task": {
            "description": "Given the following hash accumulation, what is the final value of hash % 1000?",
            "code": "unsigned long hash = 5381;\nconst char *str = \"test\";\nfor (int i = 0; str[i] != '\\0'; i++) {\n    hash = ((hash << 5) + hash) + str[i];\n}\nunsigned int result = hash % 1000;",
            "answer": 178
        }
    },
    {
        "id": "BL-LN-S006-V001",
        "metadata": {
            "name": "简化屏幕初始化变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "simplified_initialization",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following simplified screen initialization, what is the final value of s->cursor_color?",
            "code": "void init_screen(struct screen *s) {\n    s->width = 80;\n    s->height = 25;\n    s->cursor_color = -1;\n    s->background_color = 0;\n}",
            "answer": -1
        }
    },
    {
        "id": "BL-LN-S006-V002",
        "metadata": {
            "name": "Python显示配置变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following Python display configuration, what is the final value of display['cursor_color']?",
            "code": "def setup_display(display):\n    display['grid'] = create_grid(80, 24)\n    display['saved_state'] = None\n    display['cursor_style'] = 'DEFAULT'\n    display['cursor_color'] = -1\n    display['background'] = 'BLACK'",
            "answer": -1
        }
    },
    {
        "id": "BL-LN-S006-V003",
        "metadata": {
            "name": "扩展属性初始化变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "extended_initialization",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following extended screen initialization, what is the final value of s->total_colors?",
            "code": "void init_extended_screen(struct ext_screen *s) {\n    s->primary_grid = create_grid(100, 50);\n    s->backup_grid = NULL;\n    s->cursor_style = CURSOR_BLOCK;\n    s->cursor_color = -1;\n    s->palette_size = 256;\n    s->total_colors = s->palette_size + 16;\n}",
            "answer": 272
        }
    },
    {
        "id": "BL-LN-S006-V004",
        "metadata": {
            "name": "图形上下文变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "graphics_context",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following graphics context initialization, what is the final value of ctx->effective_alpha?",
            "code": "void init_graphics_context(struct gfx_context *ctx) {\n    ctx->surface = create_surface(800, 600, 32);\n    ctx->blend_mode = BLEND_ALPHA;\n    ctx->global_alpha = 0.8;\n    ctx->local_alpha = 0.5;\n    ctx->effective_alpha = ctx->global_alpha * ctx->local_alpha;\n    ctx->color_depth = 24;\n}",
            "answer": 0.4
        }
    },
    {
        "id": "BL-LN-S006-V005",
        "metadata": {
            "name": "Java Swing组件变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "java",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following Java Swing component initialization, what is the final value of panel.getCursorColor()?",
            "code": "public void initPanel(CustomPanel panel) {\n    panel.setLayout(new GridLayout(25, 80));\n    panel.setSavedState(null);\n    panel.setCursorStyle(CursorStyle.DEFAULT);\n    panel.setCursorColor(-1);\n    panel.setDoubleBuffered(true);\n}",
            "answer": -1
        }
    },
    {
        "id": "BL-LN-S006-V006",
        "metadata": {
            "name": "窗口管理器变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "window_manager",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following window manager initialization, what is the final value of wm->active_windows?",
            "code": "void init_window_manager(struct window_mgr *wm) {\n    wm->desktop = create_desktop(1920, 1080);\n    wm->window_list = create_list();\n    wm->focus_window = NULL;\n    wm->max_windows = 64;\n    wm->active_windows = 0;\n    wm->z_order_counter = 1;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-LN-S006-V007",
        "metadata": {
            "name": "颜色管理变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "color_management",
            "execution_pattern": "transform"
        },
        "task": {
            "description": "Given the following color management setup, what is the final value of cm->default_bg?",
            "code": "void setup_color_manager(struct color_mgr *cm) {\n    cm->palette = create_palette(256);\n    cm->default_fg = RGB(255, 255, 255);\n    cm->default_bg = RGB(0, 0, 0);\n    cm->highlight_color = RGB(255, 255, 0);\n    cm->transparency = 255;\n}",
            "answer": "RGB(0, 0, 0)"
        }
    },
    {
        "id": "BL-LN-S006-V008",
        "metadata": {
            "name": "JavaScript Canvas变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "javascript",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cross_language",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following JavaScript Canvas initialization, what is the final value of context.cursorColor?",
            "code": "function initCanvas(canvas, context) {\n    context.canvas = canvas;\n    context.savedImageData = null;\n    context.cursorStyle = 'default';\n    context.cursorColor = -1;\n    context.lineWidth = 1;\n}",
            "answer": -1
        }
    },
    {
        "id": "BL-LN-S006-V009",
        "metadata": {
            "name": "终端仿真器变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "terminal_emulator",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following terminal emulator initialization, what is the final value of term->escape_state?",
            "code": "void init_terminal(struct terminal *term) {\n    term->screen_buffer = malloc(80 * 25 * sizeof(char));\n    term->cursor_x = 0;\n    term->cursor_y = 0;\n    term->cursor_visible = 1;\n    term->escape_state = ESC_NORMAL;\n    term->color_mode = COLOR_16;\n}",
            "answer": "ESC_NORMAL"
        }
    },
    {
        "id": "BL-LN-S006-V010",
        "metadata": {
            "name": "字体渲染器变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "font_renderer",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following font renderer initialization, what is the final value of fr->glyph_cache_size?",
            "code": "void init_font_renderer(struct font_renderer *fr) {\n    fr->font_face = load_font(\"default.ttf\");\n    fr->font_size = 12;\n    fr->dpi = 96;\n    fr->cache_capacity = 1024;\n    fr->glyph_cache_size = fr->cache_capacity * sizeof(struct glyph);\n    fr->antialias = 1;\n}",
            "answer": "1024 * sizeof(struct glyph)"
        }
    },
    {
        "id": "BL-LN-S006-V011",
        "metadata": {
            "name": "Python GUI框架变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "gui_framework",
            "execution_pattern": "sequential"
        },
        "task": {
            "description": "Given the following Python GUI initialization, what is the final value of widget.cursor_blink_rate?",
            "code": "def init_text_widget(widget):\n    widget.buffer = TextBuffer()\n    widget.cursor_position = 0\n    widget.cursor_visible = True\n    widget.cursor_blink_rate = 500\n    widget.selection_start = -1\n    widget.selection_end = -1",
            "answer": 500
        }
    },
    {
        "id": "BL-LN-S006-V012",
        "metadata": {
            "name": "OpenGL上下文变式",
            "category": "Block-Level",
            "subcategory": "Linear",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "opengl_context",
            "execution_pattern": "dependent"
        },
        "task": {
            "description": "Given the following OpenGL context initialization, what is the final value of ctx->max_texture_units?",
            "code": "void init_gl_context(struct gl_context *ctx) {\n    ctx->version_major = 3;\n    ctx->version_minor = 3;\n    ctx->profile = GL_CORE_PROFILE;\n    glGetIntegerv(GL_MAX_TEXTURE_IMAGE_UNITS, &ctx->max_texture_units);\n    ctx->current_program = 0;\n    ctx->vertex_array_binding = 0;\n}",
            "answer": "implementation_dependent"
        }
    }
]
```

#### 2B - 条件代码块 [ Conditional ] (96)

> ```
> # 条件代码块推理变式生成提示词
> 
> ## 任务目标
> 基于给定的条件代码块种子任务，生成多样化的变式任务来全面测试大模型对条件分支逻辑、控制流分析、路径选择和分支执行结果预测的理解能力。
> 
> ## 条件代码块特征分析
> 条件代码块是指包含if-else、switch-case、三元运算符等分支控制结构的代码段，重点测试模型对条件判断、分支选择、执行路径预测和结果状态推理的理解。
> 
> ## 变式生成维度
> 
> ### 1. 条件结构类型变式
> - **简单if-else变式**: 基础的二分支条件判断
> - **多重if-else变式**: if-elif-else的多分支条件链
> - **嵌套条件变式**: 条件语句的多层嵌套结构
> - **switch-case变式**: 多路分支的switch语句
> - **三元运算符变式**: 条件表达式的简化形式
> - **guard子句变式**: 早期返回的条件保护语句
> 
> ### 2. 条件表达式复杂度变式
> - **简单条件变式**: 单一变量的直接比较
> - **复合条件变式**: 使用&&、||、!的复合逻辑表达式
> - **范围判断变式**: 数值范围的边界条件判断
> - **类型检查变式**: 对象类型或NULL的条件检查
> - **位运算条件变式**: 位操作结果的条件判断
> - **函数返回值条件变式**: 基于函数调用结果的条件判断
> 
> ### 3. 分支执行路径变式
> - **单路径执行变式**: 只有一个分支会被执行的情况
> - **多路径可能变式**: 根据不同输入可能执行不同分支
> - **死分支变式**: 由于条件恒定而永不执行的分支
> - **必然分支变式**: 由于条件恒定而必然执行的分支
> - **短路执行变式**: 逻辑短路导致的分支跳过
> - **fallthrough变式**: switch语句中的贯穿执行
> 
> ### 4. 条件依赖关系变式
> - **独立条件变式**: 条件判断之间相互独立
> - **依赖条件变式**: 后续条件依赖前面条件的结果
> - **互斥条件变式**: 条件之间具有互斥关系
> - **包含条件变式**: 一个条件包含于另一个条件
> - **重叠条件变式**: 条件之间存在部分重叠
> - **递进条件变式**: 条件判断具有递进关系
> 
> ### 5. 变量状态变化变式
> - **条件内赋值变式**: 在条件分支内修改变量值
> - **累积状态变式**: 多个分支对同一变量的累积修改
> - **状态重置变式**: 某个分支重置变量到初始状态
> - **条件状态变式**: 变量状态影响后续条件判断
> - **副作用变式**: 条件判断本身产生的副作用
> - **状态传播变式**: 变量状态在分支间的传播
> 
> ### 6. 错误处理和边界变式
> - **空值检查变式**: NULL、None、undefined的条件检查
> - **边界值变式**: 数值边界条件的处理
> - **溢出检查变式**: 数值溢出的条件检测
> - **资源有效性变式**: 资源分配成功与否的条件检查
> - **参数验证变式**: 输入参数有效性的条件验证
> - **异常路径变式**: 异常情况的条件处理路径
> 
> ### 7. 控制流复杂度变式
> - **线性分支变式**: 简单的线性分支结构
> - **树形分支变式**: 层次化的树形分支结构
> - **网状分支变式**: 交叉引用的复杂分支网络
> - **循环内分支变式**: 循环体内的条件分支
> - **递归分支变式**: 递归函数中的条件分支
> - **跳转分支变式**: goto、break、continue的条件跳转
> 
> ### 8. 数据类型特化变式
> - **数值比较变式**: 整数、浮点数的条件比较
> - **字符串比较变式**: 字符串相等性和大小比较
> - **指针比较变式**: 指针地址和指向内容的比较
> - **对象比较变式**: 对象引用和内容的比较
> - **数组比较变式**: 数组长度和元素的条件判断
> - **结构体比较变式**: 结构体字段的条件比较
> 
> ### 9. 优化和性能变式
> - **分支预测变式**: 可预测和不可预测的分支模式
> - **条件消除变式**: 编译器可优化消除的条件
> - **常量折叠变式**: 编译时可确定的条件表达式
> - **跳转表变式**: switch语句的跳转表优化
> - **分支消除变式**: 永不执行分支的消除优化
> - **条件合并变式**: 多个条件的合并优化
> 
> ### 10. 语言特性变式
> - **Python特性变式**: elif、布尔表达式、条件表达式
> - **C语言特性变式**: switch-case、条件运算符、宏条件编译
> - **Java特性变式**: switch表达式、instanceof检查
> - **JavaScript特性变式**: 真值判断、可选链操作符
> - **跨语言移植变式**: 相同逻辑在不同语言中的条件实现
> 
> ## 复杂度层次设计
> 
> ### 简单条件 (Easy)
> - 单层if-else或简单switch-case
> - 基础的比较运算符条件
> - 明确的二分支或三分支选择
> - 直观的条件判断逻辑
> 
> ### 中等条件 (Medium)
> - 2-3层的嵌套条件或中等复杂的条件链
> - 包含逻辑运算符的复合条件
> - 涉及函数调用或简单计算的条件
> - 需要仔细分析分支选择的情况
> 
> ### 复杂条件 (Hard)
> - 3层以上的深度嵌套或复杂条件网络
> - 复杂的逻辑表达式和多重条件依赖
> - 涉及指针、内存管理或复杂数据结构
> - 需要深入理解控制流和执行语义
> 
> ### 专家级条件 (Expert)
> - 极度复杂的嵌套和条件组合
> - 涉及高级语言特性和优化考虑
> - 多重边界条件和异常处理
> - 需要专业级别的代码理解能力
> 
> ## 生成策略
> 
> ### 种子分析策略
> 1. **识别条件模式**: 分析种子的条件结构类型和复杂度
> 2. **提取判断逻辑**: 识别条件表达式和分支选择逻辑
> 3. **分析执行路径**: 追踪不同输入下的执行路径
> 4. **确定关键变量**: 找出影响条件判断的关键变量
> 
> ### 变式设计原则
> 1. **路径完整性**: 确保覆盖所有可能的执行路径
> 2. **边界条件**: 重点测试边界值和特殊情况
> 3. **逻辑一致性**: 保证条件逻辑的正确性和一致性
> 4. **现实相关性**: 优先设计实际编程中常见的条件模式
> 
> ### 质量保证
> 1. **路径验证**: 验证每个分支路径的执行正确性
> 2. **条件覆盖**: 确保所有条件分支都得到测试
> 3. **边界测试**: 包含各种边界和异常条件
> 4. **语义正确**: 保证条件逻辑符合语言语义
> 
> ## 输出格式要求
> 
> ```json
> [
>     {
>         "id": "BL-CD-S00X-V001",
>         "metadata": {
>             "name": "条件代码块变式名称",
>             "category": "Block-Level",
>             "subcategory": "Conditional",
>             "type": "variant",
>             "source": "Generated",
>             "language": "目标语言",
>             "difficulty": "easy/medium/hard/expert",
>             "intervention": 0,
>             "variant_type": "变式类型标签",
>             "condition_pattern": "simple_if/nested_if/switch_case/ternary/complex_logic",
>             "branch_count": "分支数量"
>         },
>         "task": {
>             "description": "条件代码块推理任务描述",
>             "code": "包含条件分支的代码块",
>             "answer": "特定输入下的执行结果"
>         }
>     },
>     {下一个变式...}
> ]
> 
> 特殊字段说明
> condition_pattern: 标识条件结构的模式类型
> branch_count: 记录分支的数量
> variant_type: 描述具体的变式类型
> 生成目标
> 为每个提供的种子任务生成12-18个条件代码块变式，确保：
> 
> 每种难度等级至少包含3-4个变式
> 涵盖至少8-10种不同的条件模式
> 包含2-3个跨语言的变式
> 至少包含4-5个边界条件和错误处理的变式
> 包含不同分支数量的变式（2分支到5+分支）
> 重点测试场景
> 分支选择准确性: 给定特定输入，能否正确选择执行分支
> 嵌套逻辑理解: 对多层嵌套条件的正确理解
> 短路逻辑: 逻辑运算符短路特性的理解
> 边界条件处理: 边界值和特殊情况的正确处理
> 状态变化追踪: 条件分支对程序状态的影响
> 请基于此提示词，为给定的条件代码块种子任务生成全面的变式集合，输出格式为包含所有变式的JSON数组。
> ```

```json
[
    {
        "id": "BL-CD-S001-V001",
        "metadata": {
            "name": "简单条件-边界值测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boundary_condition",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 0, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else {\n        return (size_t)r;\n    }\n}",
            "answer": "DEFAULT_MEM_ALIGNMENT"
        }
    },
    {
        "id": "BL-CD-S001-V002",
        "metadata": {
            "name": "简单条件-负值测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "negative_value",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns -1, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else {\n        return (size_t)r;\n    }\n}",
            "answer": "DEFAULT_MEM_ALIGNMENT"
        }
    },
    {
        "id": "BL-CD-S001-V003",
        "metadata": {
            "name": "条件反转变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "condition_inversion",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 8192, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r > 0) {\n        return (size_t)r;\n    } else {\n        return DEFAULT_MEM_ALIGNMENT;\n    }\n}",
            "answer": 8192
        }
    },
    {
        "id": "BL-CD-S001-V004",
        "metadata": {
            "name": "三元运算符变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "ternary_operator",
            "condition_pattern": "ternary",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following ternary conditional where sysconf returns 2048, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    return (r <= 0) ? DEFAULT_MEM_ALIGNMENT : (size_t)r;\n}",
            "answer": 2048
        }
    },
    {
        "id": "BL-CD-S001-V005",
        "metadata": {
            "name": "多重条件检查变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "multiple_conditions",
            "condition_pattern": "complex_if",
            "branch_count": "3"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 1024, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else if (r < 512) {\n        return 512;\n    } else {\n        return (size_t)r;\n    }\n}",
            "answer": 1024
        }
    },
    {
        "id": "BL-CD-S001-V006",
        "metadata": {
            "name": "范围检查变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "range_check",
            "condition_pattern": "complex_logic",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 16384, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else if (r >= 4096 && r <= 8192) {\n        return (size_t)r;\n    } else if (r > 8192) {\n        return 8192;\n    } else {\n        return 4096;\n    }\n}",
            "answer": 8192
        }
    },
    {
        "id": "BL-CD-S001-V007",
        "metadata": {
            "name": "Python版本转换",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "language_conversion",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following conditional block where get_page_size returns 4096, what is the return value?",
            "code": "def crypt_getpagesize():\n    r = get_page_size()\n    if r <= 0:\n        return DEFAULT_MEM_ALIGNMENT\n    else:\n        return r",
            "answer": 4096
        }
    },
    {
        "id": "BL-CD-S001-V008",
        "metadata": {
            "name": "状态变量累积变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "state_accumulation",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 4096, what is the final value of total_size?",
            "code": "int total_size = 0;\nsize_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        total_size += DEFAULT_MEM_ALIGNMENT;\n        return DEFAULT_MEM_ALIGNMENT;\n    } else {\n        total_size += (size_t)r;\n        return (size_t)r;\n    }\n}",
            "answer": 4096
        }
    },
    {
        "id": "BL-CD-S001-V009",
        "metadata": {
            "name": "嵌套函数调用条件",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "nested_function_calls",
            "condition_pattern": "complex_logic",
            "branch_count": "3"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 4096 and validate_page_size returns 1, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0 || !validate_page_size(r)) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else if (is_power_of_two(r)) {\n        return (size_t)r;\n    } else {\n        return round_to_power_of_two(r);\n    }\n}",
            "answer": 4096
        }
    },
    {
        "id": "BL-CD-S001-V010",
        "metadata": {
            "name": "位运算条件检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bitwise_conditions",
            "condition_pattern": "complex_logic",
            "branch_count": "3"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 4096, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else if ((r & (r - 1)) == 0) {\n        return (size_t)r;\n    } else {\n        return (size_t)(1 << (int)log2(r));\n    }\n}",
            "answer": 4096
        }
    },
    {
        "id": "BL-CD-S001-V011",
        "metadata": {
            "name": "Guard子句变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "guard_clause",
            "condition_pattern": "guard_clause",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following guard clause where sysconf returns 4096, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0)\n        return DEFAULT_MEM_ALIGNMENT;\n    \n    return (size_t)r;\n}",
            "answer": 4096
        }
    },
    {
        "id": "BL-CD-S001-V012",
        "metadata": {
            "name": "溢出检查变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "overflow_check",
            "condition_pattern": "complex_logic",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following conditional block where sysconf returns 4096, what is the return value?",
            "code": "size_t crypt_getpagesize(void) {\n    long r = sysconf(_SC_PAGESIZE);\n    if (r <= 0) {\n        return DEFAULT_MEM_ALIGNMENT;\n    } else if (r > SIZE_MAX) {\n        return SIZE_MAX;\n    } else if (r < 512) {\n        return 512;\n    } else {\n        return (size_t)r;\n    }\n}",
            "answer": 4096
        }
    },

    {
        "id": "BL-CD-S002-V001",
        "metadata": {
            "name": "嵌套条件-边界分数",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "boundary_condition",
            "condition_pattern": "nested_if",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested conditional block where score is 90, what is the final value of grade?",
            "code": "score = 90\nif score >= 90:\n    if score >= 95:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80:\n        grade = 'B'\n    else:\n        grade = 'C'\nprint(f\"Grade: {grade}\")",
            "answer": "A"
        }
    },
    {
        "id": "BL-CD-S002-V002",
        "metadata": {
            "name": "嵌套条件-最高分数",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "maximum_boundary",
            "condition_pattern": "nested_if",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested conditional block where score is 98, what is the final value of grade?",
            "code": "score = 98\nif score >= 90:\n    if score >= 95:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80:\n        grade = 'B'\n    else:\n        grade = 'C'\nprint(f\"Grade: {grade}\")",
            "answer": "A+"
        }
    },
    {
        "id": "BL-CD-S002-V003",
        "metadata": {
            "name": "嵌套条件-低分数段",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "low_score_range",
            "condition_pattern": "nested_if",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested conditional block where score is 75, what is the final value of grade?",
            "code": "score = 75\nif score >= 90:\n    if score >= 95:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80:\n        grade = 'B'\n    else:\n        grade = 'C'\nprint(f\"Grade: {grade}\")",
            "answer": "C"
        }
    },
    {
        "id": "BL-CD-S002-V004",
        "metadata": {
            "name": "三层嵌套变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "three_level_nesting",
            "condition_pattern": "deep_nested_if",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following three-level nested conditional where score is 92, what is the final value of grade?",
            "code": "score = 92\nif score >= 90:\n    if score >= 95:\n        if score >= 98:\n            grade = 'A++'\n        else:\n            grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80:\n        grade = 'B'\n    else:\n        grade = 'C'\nprint(f\"Grade: {grade}\")",
            "answer": "A"
        }
    },
    {
        "id": "BL-CD-S002-V005",
        "metadata": {
            "name": "扩展分级系统",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "extended_grading",
            "condition_pattern": "nested_if",
            "branch_count": "8"
        },
        "task": {
            "description": "Given the following extended grading system where score is 85, what is the final value of grade?",
            "code": "score = 85\nif score >= 90:\n    if score >= 95:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80:\n        if score >= 85:\n            grade = 'B+'\n        else:\n            grade = 'B'\n    else:\n        if score >= 70:\n            grade = 'C'\n        else:\n            grade = 'D'\nprint(f\"Grade: {grade}\")",
            "answer": "B+"
        }
    },
    {
        "id": "BL-CD-S002-V006",
        "metadata": {
            "name": "C语言版本转换",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "language_conversion",
            "condition_pattern": "nested_if",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested conditional block where score is 85, what is the final value of grade?",
            "code": "int score = 85;\nchar grade;\nif (score >= 90) {\n    if (score >= 95) {\n        grade = 'A';\n    } else {\n        grade = 'B';\n    }\n} else {\n    if (score >= 80) {\n        grade = 'C';\n    } else {\n        grade = 'D';\n    }\n}\nprintf(\"Grade: %c\\n\", grade);",
            "answer": "C"
        }
    },
    {
        "id": "BL-CD-S002-V007",
        "metadata": {
            "name": "状态累积变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "state_accumulation",
            "condition_pattern": "nested_if",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested conditional with state tracking where score is 85, what is the final value of bonus_points?",
            "code": "score = 85\nbonus_points = 0\nif score >= 90:\n    bonus_points += 10\n    if score >= 95:\n        bonus_points += 5\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80:\n        bonus_points += 3\n        grade = 'B'\n    else:\n        grade = 'C'\nprint(f\"Grade: {grade}, Bonus: {bonus_points}\")",
            "answer": 3
        }
    },
    {
        "id": "BL-CD-S002-V008",
        "metadata": {
            "name": "复合条件嵌套",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "compound_conditions",
            "condition_pattern": "complex_logic",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following compound conditional where score is 85 and attendance is 0.9, what is the final value of grade?",
            "code": "score = 85\nattendance = 0.9\nif score >= 90 and attendance >= 0.8:\n    if score >= 95 or attendance >= 0.95:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score >= 80 and attendance >= 0.75:\n        grade = 'B'\n    elif score >= 70:\n        grade = 'C'\n    else:\n        grade = 'D'\nprint(f\"Grade: {grade}\")",
            "answer": "B"
        }
    },
    {
        "id": "BL-CD-S002-V009",
        "metadata": {
            "name": "异常处理嵌套",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "exception_handling",
            "condition_pattern": "nested_if",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following nested conditional with validation where score is 85, what is the final value of grade?",
            "code": "score = 85\nif score < 0 or score > 100:\n    grade = 'Invalid'\nelse:\n    if score >= 90:\n        if score >= 95:\n            grade = 'A+'\n        else:\n            grade = 'A'\n    else:\n        if score >= 80:\n            grade = 'B'\n        else:\n            grade = 'C'\nprint(f\"Grade: {grade}\")",
            "answer": "B"
        }
    },
    {
        "id": "BL-CD-S002-V010",
        "metadata": {
            "name": "短路逻辑嵌套",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "short_circuit_logic",
            "condition_pattern": "complex_logic",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested conditional with short-circuit logic where score is None, what is the final value of grade?",
            "code": "score = None\nif score is not None and score >= 90:\n    if score >= 95:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if score is not None and score >= 80:\n        grade = 'B'\n    else:\n        grade = 'Incomplete'\nprint(f\"Grade: {grade}\")",
            "answer": "Incomplete"
        }
    },
    {
        "id": "BL-CD-S002-V011",
        "metadata": {
            "name": "多变量嵌套条件",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "multi_variable",
            "condition_pattern": "nested_if",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following multi-variable nested conditional where exam_score is 85 and project_score is 90, what is the final value of grade?",
            "code": "exam_score = 85\nproject_score = 90\naverage = (exam_score + project_score) / 2\nif average >= 90:\n    if exam_score >= 85 and project_score >= 85:\n        grade = 'A+'\n    else:\n        grade = 'A'\nelse:\n    if average >= 80:\n        if min(exam_score, project_score) >= 75:\n            grade = 'B+'\n        else:\n            grade = 'B'\n    else:\n        grade = 'C'\nprint(f\"Grade: {grade}\")",
            "answer": "A+"
        }
    },
    {
        "id": "BL-CD-S002-V012",
        "metadata": {
            "name": "递归嵌套模式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "recursive_pattern",
            "condition_pattern": "deep_nested_if",
            "branch_count": "8"
        },
        "task": {
            "description": "Given the following deep nested conditional where score is 85, what is the final value of detailed_grade?",
            "code": "score = 85\nif score >= 90:\n    if score >= 95:\n        if score >= 98:\n            detailed_grade = 'Excellent+'\n        else:\n            detailed_grade = 'Excellent'\n    else:\n        if score >= 92:\n            detailed_grade = 'Very Good+'\n        else:\n            detailed_grade = 'Very Good'\nelse:\n    if score >= 80:\n        if score >= 85:\n            if score >= 87:\n                detailed_grade = 'Good+'\n            else:\n                detailed_grade = 'Good'\n        else:\n            detailed_grade = 'Satisfactory'\n    else:\n        detailed_grade = 'Needs Improvement'\nprint(f\"Detailed Grade: {detailed_grade}\")",
            "answer": "Good"
        }
    },

    {
        "id": "BL-CD-S003-V001",
        "metadata": {
            "name": "边界值-10",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boundary_condition",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following else-if chain where value is 10, what is the final value of category?",
            "code": "int value = 10;\nchar *category;\nif (value < 10) {\n    category = \"low\";\n} else if (value < 20) {\n    category = \"medium\";\n} else if (value < 30) {\n    category = \"high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "medium"
        }
    },
    {
        "id": "BL-CD-S003-V002",
        "metadata": {
            "name": "边界值-20",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boundary_condition",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following else-if chain where value is 20, what is the final value of category?",
            "code": "int value = 20;\nchar *category;\nif (value < 10) {\n    category = \"low\";\n} else if (value < 20) {\n    category = \"medium\";\n} else if (value < 30) {\n    category = \"high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "high"
        }
    },
    {
        "id": "BL-CD-S003-V003",
        "metadata": {
            "name": "极值测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "extreme_value",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following else-if chain where value is 35, what is the final value of category?",
            "code": "int value = 35;\nchar *category;\nif (value < 10) {\n    category = \"low\";\n} else if (value < 20) {\n    category = \"medium\";\n} else if (value < 30) {\n    category = \"high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "extreme"
        }
    },
    {
        "id": "BL-CD-S003-V004",
        "metadata": {
            "name": "扩展分类链",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "extended_chain",
            "condition_pattern": "else_if_chain",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following extended else-if chain where value is 15, what is the final value of category?",
            "code": "int value = 15;\nchar *category;\nif (value < 5) {\n    category = \"very_low\";\n} else if (value < 10) {\n    category = \"low\";\n} else if (value < 20) {\n    category = \"medium\";\n} else if (value < 30) {\n    category = \"high\";\n} else if (value < 50) {\n    category = \"very_high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "medium"
        }
    },
    {
        "id": "BL-CD-S003-V005",
        "metadata": {
            "name": "条件顺序变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "condition_reordering",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following reordered else-if chain where value is 15, what is the final value of category?",
            "code": "int value = 15;\nchar *category;\nif (value >= 30) {\n    category = \"extreme\";\n} else if (value >= 20) {\n    category = \"high\";\n} else if (value >= 10) {\n    category = \"medium\";\n} else {\n    category = \"low\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "medium"
        }
    },
    {
        "id": "BL-CD-S003-V006",
        "metadata": {
            "name": "Python版本转换",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "language_conversion",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following elif chain where value is 15, what is the final value of category?",
            "code": "value = 15\nif value < 10:\n    category = \"low\"\nelif value < 20:\n    category = \"medium\"\nelif value < 30:\n    category = \"high\"\nelse:\n    category = \"extreme\"\nprint(f\"Category: {category}\")",
            "answer": "medium"
        }
    },
    {
        "id": "BL-CD-S003-V007",
        "metadata": {
            "name": "浮点数比较变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "floating_point",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following else-if chain where value is 15.5, what is the final value of category?",
            "code": "double value = 15.5;\nchar *category;\nif (value < 10.0) {\n    category = \"low\";\n} else if (value < 20.0) {\n    category = \"medium\";\n} else if (value < 30.0) {\n    category = \"high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "medium"
        }
    },
    {
        "id": "BL-CD-S003-V008",
        "metadata": {
            "name": "状态累积变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "state_accumulation",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following else-if chain with scoring where value is 15, what is the final value of score?",
            "code": "int value = 15;\nint score = 0;\nchar *category;\nif (value < 10) {\n    category = \"low\";\n    score = 1;\n} else if (value < 20) {\n    category = \"medium\";\n    score = 2;\n} else if (value < 30) {\n    category = \"high\";\n    score = 3;\n} else {\n    category = \"extreme\";\n    score = 4;\n}\nprintf(\"Category: %s, Score: %d\\n\", category, score);",
            "answer": 2
        }
    },
    {
        "id": "BL-CD-S003-V009",
        "metadata": {
            "name": "复合条件变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "compound_conditions",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following complex else-if chain where value is 15 and flag is 1, what is the final value of category?",
            "code": "int value = 15;\nint flag = 1;\nchar *category;\nif (value < 10 && flag == 0) {\n    category = \"low_special\";\n} else if (value < 10) {\n    category = \"low\";\n} else if (value < 20 && flag == 1) {\n    category = \"medium_enhanced\";\n} else if (value < 20) {\n    category = \"medium\";\n} else {\n    category = \"high\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "medium_enhanced"
        }
    },
    {
        "id": "BL-CD-S003-V010",
        "metadata": {
            "name": "函数调用条件",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "function_call_conditions",
            "condition_pattern": "else_if_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following else-if chain where get_threshold() returns 15 and value is 15, what is the final value of category?",
            "code": "int value = 15;\nchar *category;\nint threshold = get_threshold();\nif (value < threshold - 5) {\n    category = \"low\";\n} else if (value < threshold + 5) {\n    category = \"medium\";\n} else if (value < threshold + 15) {\n    category = \"high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "medium"
        }
    },
    {
        "id": "BL-CD-S003-V011",
        "metadata": {
            "name": "负值处理变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "negative_value_handling",
            "condition_pattern": "else_if_chain",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following else-if chain where value is -5, what is the final value of category?",
            "code": "int value = -5;\nchar *category;\nif (value < 0) {\n    category = \"negative\";\n} else if (value < 10) {\n    category = \"low\";\n} else if (value < 20) {\n    category = \"medium\";\n} else if (value < 30) {\n    category = \"high\";\n} else {\n    category = \"extreme\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "negative"
        }
    },
    {
        "id": "BL-CD-S003-V012",
        "metadata": {
            "name": "范围重叠检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "range_overlap",
            "condition_pattern": "complex_logic",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following range overlap else-if chain where value is 15, what is the final value of category?",
            "code": "int value = 15;\nchar *category;\nif (value >= 0 && value <= 5) {\n    category = \"range_a\";\n} else if (value > 5 && value <= 15) {\n    category = \"range_b\";\n} else if (value > 10 && value <= 25) {\n    category = \"range_c\";\n} else if (value > 20 && value <= 35) {\n    category = \"range_d\";\n} else {\n    category = \"out_of_range\";\n}\nprintf(\"Category: %s\\n\", category);",
            "answer": "range_b"
        }
    },

    {
        "id": "BL-CD-S004-V001",
        "metadata": {
            "name": "周末测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "default_case",
            "condition_pattern": "switch_case",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following switch block where day is 7, what is the final value of day_name?",
            "code": "int day = 7;\nchar *day_name;\nswitch (day) {\n    case 1: day_name = \"Monday\"; break;\n    case 2: day_name = \"Tuesday\"; break;\n    case 3: day_name = \"Wednesday\"; break;\n    case 4: day_name = \"Thursday\"; break;\n    case 5: day_name = \"Friday\"; break;\n    default: day_name = \"Weekend\";\n}\nprintf(\"Day: %s\\n\", day_name);",
            "answer": "Weekend"
        }
    },
    {
        "id": "BL-CD-S004-V002",
        "metadata": {
            "name": "星期一测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "first_case",
            "condition_pattern": "switch_case",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following switch block where day is 1, what is the final value of day_name?",
            "code": "int day = 1;\nchar *day_name;\nswitch (day) {\n    case 1: day_name = \"Monday\"; break;\n    case 2: day_name = \"Tuesday\"; break;\n    case 3: day_name = \"Wednesday\"; break;\n    case 4: day_name = \"Thursday\"; break;\n    case 5: day_name = \"Friday\"; break;\n    default: day_name = \"Weekend\";\n}\nprintf(\"Day: %s\\n\", day_name);",
            "answer": "Monday"
        }
    },
    {
        "id": "BL-CD-S004-V003",
        "metadata": {
            "name": "字符switch变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "character_switch",
            "condition_pattern": "switch_case",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following character switch where grade is 'B', what is the final value of description?",
            "code": "char grade = 'B';\nchar *description;\nswitch (grade) {\n    case 'A': description = \"Excellent\"; break;\n    case 'B': description = \"Good\"; break;\n    case 'C': description = \"Average\"; break;\n    case 'D': description = \"Poor\"; break;\n    default: description = \"Invalid\";\n}\nprintf(\"Grade: %s\\n\", description);",
            "answer": "Good"
        }
    },
    {
        "id": "BL-CD-S004-V004",
        "metadata": {
            "name": "枚举switch变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "enum_switch",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following enum switch where color is BLUE (value 2), what is the final value of color_name?",
            "code": "enum Color { RED, GREEN, BLUE, YELLOW };\nenum Color color = BLUE;\nchar *color_name;\nswitch (color) {\n    case RED: color_name = \"Red\"; break;\n    case GREEN: color_name = \"Green\"; break;\n    case BLUE: color_name = \"Blue\"; break;\n    case YELLOW: color_name = \"Yellow\"; break;\n    default: color_name = \"Unknown\";\n}\nprintf(\"Color: %s\\n\", color_name);",
            "answer": "Blue"
        }
    },
    {
        "id": "BL-CD-S004-V005",
        "metadata": {
            "name": "嵌套switch变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "nested_switch",
            "condition_pattern": "nested_switch",
            "branch_count": "8"
        },
        "task": {
            "description": "Given the following nested switch where category is 1 and subcategory is 2, what is the final value of result?",
            "code": "int category = 1;\nint subcategory = 2;\nchar *result;\nswitch (category) {\n    case 1:\n        switch (subcategory) {\n            case 1: result = \"Type A1\"; break;\n            case 2: result = \"Type A2\"; break;\n            default: result = \"Type A Unknown\";\n        }\n        break;\n    case 2:\n        switch (subcategory) {\n            case 1: result = \"Type B1\"; break;\n            case 2: result = \"Type B2\"; break;\n            default: result = \"Type B Unknown\";\n        }\n        break;\n    default: result = \"Unknown Category\";\n}\nprintf(\"Result: %s\\n\", result);",
            "answer": "Type A2"
        }
    },
    {
        "id": "BL-CD-S004-V006",
        "metadata": {
            "name": "缺失break的switch",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "missing_break",
            "condition_pattern": "switch_case",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following switch with missing break where day is 2, what is the final value of day_name?",
            "code": "int day = 2;\nchar *day_name;\nswitch (day) {\n    case 1: day_name = \"Monday\";\n    case 2: day_name = \"Tuesday\";\n    case 3: day_name = \"Wednesday\"; break;\n    case 4: day_name = \"Thursday\"; break;\n    case 5: day_name = \"Friday\"; break;\n    default: day_name = \"Weekend\";\n}\nprintf(\"Day: %s\\n\", day_name);",
            "answer": "Wednesday"
        }
    },
    {
        "id": "BL-CD-S004-V007",
        "metadata": {
            "name": "Python match变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "language_conversion",
            "condition_pattern": "match_case",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following match statement where day is 3, what is the final value of day_name?",
            "code": "day = 3\nmatch day:\n    case 1:\n        day_name = \"Monday\"\n    case 2:\n        day_name = \"Tuesday\"\n    case 3:\n        day_name = \"Wednesday\"\n    case 4:\n        day_name = \"Thursday\"\n    case 5:\n        day_name = \"Friday\"\n    case _:\n        day_name = \"Weekend\"\nprint(f\"Day: {day_name}\")",
            "answer": "Wednesday"
        }
    },
    {
        "id": "BL-CD-S004-V008",
        "metadata": {
            "name": "范围case变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "range_case",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following switch with ranges where score is 85, what is the final value of grade using GNU C extension?",
            "code": "int score = 85;\nchar *grade;\nswitch (score / 10) {\n    case 10:\n    case 9: grade = \"A\"; break;\n    case 8: grade = \"B\"; break;\n    case 7: grade = \"C\"; break;\n    default: grade = \"F\";\n}\nprintf(\"Grade: %s\\n\", grade);",
            "answer": "B"
        }
    },
    {
        "id": "BL-CD-S004-V009",
        "metadata": {
            "name": "状态机switch变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "state_machine",
            "condition_pattern": "switch_case",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following state machine switch where state is 1 and input is 'A', what is the final value of next_state?",
            "code": "int state = 1;\nchar input = 'A';\nint next_state;\nswitch (state) {\n    case 0:\n        next_state = (input == 'A') ? 1 : 0;\n        break;\n    case 1:\n        next_state = (input == 'B') ? 2 : ((input == 'A') ? 1 : 0);\n        break;\n    case 2:\n        next_state = (input == 'C') ? 3 : 0;\n        break;\n    case 3:\n        next_state = 0;\n        break;\n    default:\n        next_state = 0;\n}\nprintf(\"Next state: %d\\n\", next_state);",
            "answer": 1
        }
    },
    {
        "id": "BL-CD-S004-V010",
        "metadata": {
            "name": "函数指针switch变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "function_pointer",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following function pointer switch where operation is 2, what is the final value of result when add(5,3) returns 8?",
            "code": "int operation = 2;\nint a = 5, b = 3;\nint result;\nint (*func_ptr)(int, int);\nswitch (operation) {\n    case 1: func_ptr = add; break;\n    case 2: func_ptr = subtract; break;\n    case 3: func_ptr = multiply; break;\n    default: func_ptr = NULL;\n}\nif (func_ptr != NULL) {\n    result = func_ptr(a, b);\n} else {\n    result = 0;\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": 2
        }
    },
    {
        "id": "BL-CD-S004-V011",
        "metadata": {
            "name": "多case标签变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "multiple_case_labels",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following switch with multiple case labels where day is 6, what is the final value of day_type?",
            "code": "int day = 6;\nchar *day_type;\nswitch (day) {\n    case 1:\n    case 2:\n    case 3:\n    case 4:\n    case 5:\n        day_type = \"Weekday\";\n        break;\n    case 6:\n    case 7:\n        day_type = \"Weekend\";\n        break;\n    default:\n        day_type = \"Invalid\";\n}\nprintf(\"Day type: %s\\n\", day_type);",
            "answer": "Weekend"
        }
    },
    {
        "id": "BL-CD-S004-V012",
        "metadata": {
            "name": "宏定义case变式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "macro_case",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following switch with macro cases where cmd is READ_CMD (value 1), what is the final value of action?",
            "code": "#define READ_CMD 1\n#define WRITE_CMD 2\n#define DELETE_CMD 3\nint cmd = READ_CMD;\nchar *action;\nswitch (cmd) {\n    case READ_CMD: action = \"Reading\"; break;\n    case WRITE_CMD: action = \"Writing\"; break;\n    case DELETE_CMD: action = \"Deleting\"; break;\n    default: action = \"Unknown\";\n}\nprintf(\"Action: %s\\n\", action);",
            "answer": "Reading"
        }
    },

    {
        "id": "BL-CD-S005-V001",
        "metadata": {
            "name": "fallthrough起始case",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "fallthrough_start",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following switch block with fallthrough where input is 1, what is the final value of flags?",
            "code": "int input = 1;\nint flags = 0;\nswitch (input) {\n    case 1:\n        flags |= 0x01;\n    case 2:\n        flags |= 0x02;\n    case 3:\n        flags |= 0x04;\n        break;\n    default:\n        flags = -1;\n}\nprintf(\"Flags: 0x%02X\\n\", flags);",
            "answer": 7
        }
    },
    {
        "id": "BL-CD-S005-V002",
        "metadata": {
            "name": "fallthrough最后case",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "fallthrough_end",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following switch block with fallthrough where input is 3, what is the final value of flags?",
            "code": "int input = 3;\nint flags = 0;\nswitch (input) {\n    case 1:\n        flags |= 0x01;\n    case 2:\n        flags |= 0x02;\n    case 3:\n        flags |= 0x04;\n        break;\n    default:\n        flags = -1;\n}\nprintf(\"Flags: 0x%02X\\n\", flags);",
            "answer": 4
        }
    },
    {
        "id": "BL-CD-S005-V003",
        "metadata": {
            "name": "default case fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "default_fallthrough",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following switch block with fallthrough where input is 5, what is the final value of flags?",
            "code": "int input = 5;\nint flags = 0;\nswitch (input) {\n    case 1:\n        flags |= 0x01;\n    case 2:\n        flags |= 0x02;\n    case 3:\n        flags |= 0x04;\n        break;\n    default:\n        flags = -1;\n}\nprintf(\"Flags: 0x%02X\\n\", flags);",
            "answer": -1
        }
    },
    {
        "id": "BL-CD-S005-V004",
        "metadata": {
            "name": "复杂位运算fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "complex_bitwise",
            "condition_pattern": "switch_case",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following complex bitwise switch where input is 2, what is the final value of flags?",
            "code": "int input = 2;\nint flags = 0x10;\nswitch (input) {\n    case 1:\n        flags |= 0x01;\n        flags &= ~0x10;\n    case 2:\n        flags |= 0x02;\n        flags ^= 0x08;\n    case 3:\n        flags |= 0x04;\n        break;\n    case 4:\n        flags = 0;\n        break;\n    default:\n        flags = -1;\n}\nprintf(\"Flags: 0x%02X\\n\", flags);",
            "answer": 30
        }
    },
    {
        "id": "BL-CD-S005-V005",
        "metadata": {
            "name": "累加器fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "accumulator",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following accumulator switch where input is 2, what is the final value of total?",
            "code": "int input = 2;\nint total = 0;\nswitch (input) {\n    case 1:\n        total += 10;\n    case 2:\n        total += 20;\n    case 3:\n        total += 30;\n        break;\n    default:\n        total = 0;\n}\nprintf(\"Total: %d\\n\", total);",
            "answer": 50
        }
    },
    {
        "id": "BL-CD-S005-V006",
        "metadata": {
            "name": "字符串累积fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "string_accumulation",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following string building switch where input is 2, what is the final value of result after strcat operations?",
            "code": "int input = 2;\nchar result[100] = \"\";\nswitch (input) {\n    case 1:\n        strcat(result, \"A\");\n    case 2:\n        strcat(result, \"B\");\n    case 3:\n        strcat(result, \"C\");\n        break;\n    default:\n        strcpy(result, \"INVALID\");\n}\nprintf(\"Result: %s\\n\", result);",
            "answer": "BC"
        }
    },
    {
        "id": "BL-CD-S005-V007",
        "metadata": {
            "name": "计数器fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "counter",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following counter switch where input is 2, what is the final value of count?",
            "code": "int input = 2;\nint count = 0;\nswitch (input) {\n    case 1:\n        count++;\n    case 2:\n        count++;\n    case 3:\n        count++;\n        break;\n    default:\n        count = -1;\n}\nprintf(\"Count: %d\\n\", count);",
            "answer": 2
        }
    },
    {
        "id": "BL-CD-S005-V008",
        "metadata": {
            "name": "权限累积fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "permission_accumulation",
            "condition_pattern": "switch_case",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following permission switch where user_level is 2, what is the final value of permissions?",
            "code": "int user_level = 2;\nint permissions = 0;\nswitch (user_level) {\n    case 3: // Admin\n        permissions |= 0x04; // DELETE\n    case 2: // Manager  \n        permissions |= 0x02; // WRITE\n    case 1: // User\n        permissions |= 0x01; // READ\n        break;\n    case 0: // Guest\n        permissions = 0;\n        break;\n    default:\n        permissions = -1;\n}\nprintf(\"Permissions: 0x%02X\\n\", permissions);",
            "answer": 3
        }
    },
    {
        "id": "BL-CD-S005-V009",
        "metadata": {
            "name": "状态修改fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "state_modification",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following state modification switch where phase is 2, what is the final value of system_state?",
            "code": "int phase = 2;\nint system_state = 0x00;\nswitch (phase) {\n    case 1:\n        system_state |= 0x10; // INIT\n    case 2:\n        system_state |= 0x20; // READY\n    case 3:\n        system_state |= 0x40; // ACTIVE\n        break;\n    default:\n        system_state = 0xFF; // ERROR\n}\nprintf(\"System state: 0x%02X\\n\", system_state);",
            "answer": 96
        }
    },
    {
        "id": "BL-CD-S005-V010",
        "metadata": {
            "name": "嵌套循环fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "nested_loop",
            "condition_pattern": "switch_case",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested loop switch where input is 2, what is the final value of sum?",
            "code": "int input = 2;\nint sum = 0;\nint i;\nswitch (input) {\n    case 1:\n        for (i = 0; i < 1; i++) sum += i + 1;\n    case 2:\n        for (i = 0; i < 2; i++) sum += i + 1;\n    case 3:\n        for (i = 0; i < 3; i++) sum += i + 1;\n        break;\n    default:\n        sum = -1;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 9
        }
    },
    {
        "id": "BL-CD-S005-V011",
        "metadata": {
            "name": "Python模拟fallthrough",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "language_conversion",
            "condition_pattern": "if_elif_chain",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following Python fallthrough simulation where input is 2, what is the final value of flags?",
            "code": "input_val = 2\nflags = 0\nfallthrough = False\n\nif input_val == 1 or fallthrough:\n    flags |= 0x01\n    fallthrough = True\nif input_val == 2 or fallthrough:\n    flags |= 0x02\n    fallthrough = True\nif input_val == 3 or fallthrough:\n    flags |= 0x04\n    fallthrough = False\nif input_val not in [1, 2, 3] and not fallthrough:\n    flags = -1\n    \nprint(f\"Flags: 0x{flags:02X}\")",
            "answer": 6
        }
    },
    {
        "id": "BL-CD-S005-V012",
        "metadata": {
            "name": "多重fallthrough路径",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "multiple_fallthrough",
            "condition_pattern": "switch_case",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the following multi-path fallthrough switch where input is 2, what is the final value of result?",
            "code": "int input = 2;\nint result = 0;\nswitch (input) {\n    case 1:\n        result += 1;\n    case 2:\n        result += 2;\n        if (result > 2) {\n            result *= 2;\n            break;\n        }\n    case 3:\n        result += 4;\n    case 4:\n        result += 8;\n        break;\n    default:\n        result = -1;\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": 4
        }
    },

    {
        "id": "BL-CD-S006-V001",
        "metadata": {
            "name": "简化三元运算",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "simple_ternary",
            "condition_pattern": "ternary",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following simple ternary where x is 7 and y is 5, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint result = (x > y) ? x : y;\nprintf(\"Result: %d\\n\", result);",
            "answer": 7
        }
    },
    {
        "id": "BL-CD-S006-V002",
        "metadata": {
            "name": "条件反转三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "condition_inversion",
            "condition_pattern": "ternary",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following inverted ternary where x is 7 and y is 5, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint result = (x <= y) ? x * 2 : x + 10;\nprintf(\"Result: %d\\n\", result);",
            "answer": 17
        }
    },
    {
        "id": "BL-CD-S006-V003",
        "metadata": {
            "name": "四层嵌套三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "deep_nesting",
            "condition_pattern": "ternary",
            "branch_count": "8"
        },
        "task": {
            "description": "Given the following four-level nested ternary where x is 7 and y is 5, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint result = (x > y) ? \n    ((x % 2 == 0) ? \n        ((x > 10) ? x / 2 : x * 2) : \n        ((x > 8) ? x - 3 : x + 10)) : \n    ((y % 2 == 0) ? \n        ((y > 3) ? y * 3 : y + 5) : \n        ((y > 6) ? y - 2 : y - 2));\nprintf(\"Result: %d\\n\", result);",
            "answer": 17
        }
    },
    {
        "id": "BL-CD-S006-V004",
        "metadata": {
            "name": "函数调用三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "function_calls",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following function call ternary where x is 7, y is 5, and abs() returns absolute value, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint result = (x > y) ? \n    ((abs(x - y) > 1) ? max(x, y) + abs(x - y) : min(x, y)) : \n    ((abs(y - x) > 1) ? max(x, y) - abs(y - x) : min(x, y));\nprintf(\"Result: %d\\n\", result);",
            "answer": 9
        }
    },
    {
        "id": "BL-CD-S006-V005",
        "metadata": {
            "name": "位运算三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bitwise_operations",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following bitwise ternary where x is 7 and y is 5, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint result = (x & 1) ? \n    ((y & 1) ? (x | y) : (x ^ y)) : \n    ((y & 1) ? (x & y) : (x << 1));\nprintf(\"Result: %d\\n\", result);",
            "answer": 7
        }
    },
    {
        "id": "BL-CD-S006-V006",
        "metadata": {
            "name": "Python版本三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "language_conversion",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following Python ternary where x is 7 and y is 5, what is the final value of result?",
            "code": "x, y = 7, 5\nresult = (x * 2 if x % 2 == 0 else x + 10) if x > y else (y * 3 if y % 2 == 0 else y - 2)\nprint(f\"Result: {result}\")",
            "answer": 17
        }
    },
    {
        "id": "BL-CD-S006-V007",
        "metadata": {
            "name": "数组访问三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "array_access",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following array access ternary where x is 7, y is 5, and arr = {1,2,3,4,5,6,7,8}, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint arr[] = {1, 2, 3, 4, 5, 6, 7, 8};\nint result = (x > y) ? \n    ((x < 8) ? arr[x-1] : arr[0]) : \n    ((y < 8) ? arr[y-1] : arr[0]);\nprintf(\"Result: %d\\n\", result);",
            "answer": 7
        }
    },
    {
        "id": "BL-CD-S006-V008",
        "metadata": {
            "name": "指针操作三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "pointer_operations",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following pointer ternary where x is 7, y is 5, and ptr points to x, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint *ptr = &x;\nint result = (ptr != NULL) ? \n    ((*ptr > y) ? (*ptr + *ptr) : (*ptr - y)) : \n    ((y > 0) ? y * 2 : 0);\nprintf(\"Result: %d\\n\", result);",
            "answer": 14
        }
    },
    {
        "id": "BL-CD-S006-V009",
        "metadata": {
            "name": "类型转换三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "type_casting",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following type casting ternary where x is 7 and y is 5, what is the final value of result?",
            "code": "int x = 7, y = 5;\ndouble result = (x > y) ? \n    ((x % 2 == 0) ? (double)x / 2.0 : (double)x + 10.5) : \n    ((y % 2 == 0) ? (double)y * 3.0 : (double)y - 2.5);\nprintf(\"Result: %.1f\\n\", result);",
            "answer": 17.5
        }
    },
    {
        "id": "BL-CD-S006-V010",
        "metadata": {
            "name": "短路逻辑三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "short_circuit",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following short-circuit ternary where x is 7, y is 5, and ptr is NULL, what is the final value of result?",
            "code": "int x = 7, y = 5;\nint *ptr = NULL;\nint result = (ptr != NULL && *ptr > 0) ? \n    ((x % 2 == 0) ? x * 2 : x + 10) : \n    ((y > 0 && y < 10) ? y + x : 0);\nprintf(\"Result: %d\\n\", result);",
            "answer": 12
        }
    },
    {
        "id": "BL-CD-S006-V011",
        "metadata": {
            "name": "宏定义三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "macro_usage",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following macro ternary where x is 7 and y is 5, what is the final value of result?",
            "code": "#define MAX(a,b) ((a) > (b) ? (a) : (b))\n#define MIN(a,b) ((a) < (b) ? (a) : (b))\nint x = 7, y = 5;\nint result = (x > y) ? \n    ((x % 2 == 0) ? MAX(x, 10) : MIN(x + 10, 20)) : \n    ((y % 2 == 0) ? MAX(y, 8) : MIN(y + 5, 12));\nprintf(\"Result: %d\\n\", result);",
            "answer": 17
        }
    },
    {
        "id": "BL-CD-S006-V012",
        "metadata": {
            "name": "结构体字段三元",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "struct_fields",
            "condition_pattern": "ternary",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following struct field ternary where point.x is 7 and point.y is 5, what is the final value of result?",
            "code": "struct Point { int x, y; };\nstruct Point point = {7, 5};\nint result = (point.x > point.y) ? \n    ((point.x % 2 == 0) ? point.x * point.y : point.x + point.y + 5) : \n    ((point.y % 2 == 0) ? point.y * 3 : point.y - 2);\nprintf(\"Result: %d\\n\", result);",
            "answer": 17
        }
    },

    {
        "id": "BL-CD-S007-V001",
        "metadata": {
            "name": "malloc失败检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "null_failure",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following null check block where malloc fails and returns NULL, what is the return value?",
            "code": "ssh_poll_handle ssh_poll_new(socket_t fd, short events) {\n    ssh_poll_handle p;\n    p = malloc(sizeof(struct ssh_poll_handle_struct));\n    if (p == NULL) {\n        return NULL;\n    }\n    p->x.fd = fd;\n    p->events = events;\n    return p;\n}",
            "answer": "NULL"
        }
    },
    {
        "id": "BL-CD-S007-V002",
        "metadata": {
            "name": "多重指针检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "multiple_null_checks",
            "condition_pattern": "complex_if",
            "branch_count": "3"
        },
        "task": {
            "description": "Given the following multiple null checks where both malloc calls succeed, what is the final value of result?",
            "code": "int process_data(void) {\n    char *buffer = malloc(100);\n    char *temp = malloc(50);\n    int result;\n    \n    if (buffer == NULL || temp == NULL) {\n        if (buffer) free(buffer);\n        if (temp) free(temp);\n        return -1;\n    }\n    \n    // Process data\n    result = 42;\n    free(buffer);\n    free(temp);\n    return result;\n}",
            "answer": 42
        }
    },
    {
        "id": "BL-CD-S007-V003",
        "metadata": {
            "name": "嵌套内存分配",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "nested_allocation",
            "condition_pattern": "nested_if",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following nested allocation where first malloc succeeds but second fails, what is the return value?",
            "code": "struct Node* create_list(int size) {\n    struct Node* head = malloc(sizeof(struct Node));\n    if (head == NULL) {\n        return NULL;\n    }\n    \n    head->data = malloc(size * sizeof(int));\n    if (head->data == NULL) {\n        free(head);\n        return NULL;\n    }\n    \n    head->next = NULL;\n    return head;\n}",
            "answer": "NULL"
        }
    },
    {
        "id": "BL-CD-S007-V004",
        "metadata": {
            "name": "文件指针检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "file_pointer_check",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following file pointer check where fopen succeeds, what is the return value?",
            "code": "int read_config(const char* filename) {\n    FILE* fp = fopen(filename, \"r\");\n    if (fp == NULL) {\n        return -1;\n    }\n    \n    // Read configuration\n    int config_value = 100;\n    fclose(fp);\n    return config_value;\n}",
            "answer": 100
        }
    },
    {
        "id": "BL-CD-S007-V005",
        "metadata": {
            "name": "Python None检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "language_conversion",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following None check where data is not None, what is the return value?",
            "code": "def process_data(data):\n    if data is None:\n        return None\n    \n    result = {\n        'processed': True,\n        'value': data * 2\n    }\n    return result",
            "answer": "{'processed': True, 'value': 10}"
        }
    },
    {
        "id": "BL-CD-S007-V006",
        "metadata": {
            "name": "双重检查模式",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "double_check",
            "condition_pattern": "nested_if",
            "branch_count": "3"
        },
        "task": {
            "description": "Given the following double-check pattern where ptr is initially NULL and malloc succeeds, what is the final state of ptr?",
            "code": "static void* shared_ptr = NULL;\nvoid* get_shared_resource(void) {\n    if (shared_ptr == NULL) {\n        shared_ptr = malloc(1024);\n        if (shared_ptr == NULL) {\n            return NULL;\n        }\n        // Initialize resource\n        memset(shared_ptr, 0, 1024);\n    }\n    return shared_ptr;\n}",
            "answer": "valid_pointer"
        }
    },
    {
        "id": "BL-CD-S007-V007",
        "metadata": {
            "name": "错误码检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "error_code_check",
            "condition_pattern": "simple_if",
            "branch_count": "2"
        },
        "task": {
            "description": "Given the following error code check where init_system() returns 0 (success), what is the return value?",
            "code": "int initialize_application(void) {\n    int result = init_system();\n    if (result != 0) {\n        return result;\n    }\n    \n    // Continue initialization\n    return setup_complete();\n}",
            "answer": "setup_complete_return_value"
        }
    },
    {
        "id": "BL-CD-S007-V008",
        "metadata": {
            "name": "资源链式检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "resource_chain",
            "condition_pattern": "complex_if",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following resource chain where all allocations succeed, what is the return value?",
            "code": "int setup_resources(void) {\n    void *mem1 = malloc(100);\n    void *mem2 = malloc(200);\n    void *mem3 = malloc(300);\n    \n    if (!mem1 || !mem2 || !mem3) {\n        if (mem1) free(mem1);\n        if (mem2) free(mem2);\n        if (mem3) free(mem3);\n        return -1;\n    }\n    \n    // Setup successful\n    global_mem1 = mem1;\n    global_mem2 = mem2;\n    global_mem3 = mem3;\n    return 0;\n}",
            "answer": 0
        }
    },
    {
        "id": "BL-CD-S007-V009",
        "metadata": {
            "name": "条件释放检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "conditional_free",
            "condition_pattern": "complex_if",
            "branch_count": "3"
        },
        "task": {
            "description": "Given the following conditional free where ptr is valid and should_free is 1, what happens to ptr?",
            "code": "void cleanup_resource(void** ptr, int should_free) {\n    if (ptr == NULL || *ptr == NULL) {\n        return;\n    }\n    \n    if (should_free) {\n        free(*ptr);\n        *ptr = NULL;\n    }\n}",
            "answer": "freed_and_nulled"
        }
    },
    {
        "id": "BL-CD-S007-V010",
        "metadata": {
            "name": "RAII模式检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "raii_pattern",
            "condition_pattern": "complex_if",
            "branch_count": "4"
        },
        "task": {
            "description": "Given the following RAII-style pattern where resource acquisition succeeds, what is the final state?",
            "code": "typedef struct {\n    void* data;\n    int (*cleanup)(void*);\n} Resource;\n\nResource* acquire_resource(size_t size) {\n    Resource* res = malloc(sizeof(Resource));\n    if (res == NULL) {\n        return NULL;\n    }\n    \n    res->data = malloc(size);\n    if (res->data == NULL) {\n        free(res);\n        return NULL;\n    }\n    \n    res->cleanup = free;\n    return res;\n}",
            "answer": "valid_resource_with_data"
        }
    },
    {
        "id": "BL-CD-S007-V011",
        "metadata": {
            "name": "智能指针模拟",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "smart_pointer",
            "condition_pattern": "complex_if",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following smart pointer simulation where ref_count starts at 0, what is the final ref_count after creation?",
            "code": "typedef struct {\n    void* ptr;\n    int ref_count;\n} SmartPtr;\n\nSmartPtr* create_smart_ptr(size_t size) {\n    SmartPtr* smart = malloc(sizeof(SmartPtr));\n    if (smart == NULL) {\n        return NULL;\n    }\n    \n    smart->ptr = malloc(size);\n    if (smart->ptr == NULL) {\n        free(smart);\n        return NULL;\n    }\n    \n    smart->ref_count = 1;\n    return smart;\n}",
            "answer": 1
        }
    },
    {
        "id": "BL-CD-S007-V012",
        "metadata": {
            "name": "延迟初始化检查",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "lazy_initialization",
            "condition_pattern": "nested_if",
            "branch_count": "3"
        },
        "task": {
            "description": "Given the following lazy initialization where global_resource is NULL and init succeeds, what is the return value?",
            "code": "static void* global_resource = NULL;\n\nvoid* get_global_resource(void) {\n    if (global_resource == NULL) {\n        global_resource = malloc(sizeof(ResourceStruct));\n        if (global_resource == NULL) {\n            return NULL;\n        }\n        \n        if (init_resource(global_resource) != 0) {\n            free(global_resource);\n            global_resource = NULL;\n            return NULL;\n        }\n    }\n    \n    return global_resource;\n}",
            "answer": "valid_initialized_resource"
        }
    },

    {
        "id": "BL-CD-S008-V001",
        "metadata": {
            "name": "最低年龄测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "age_boundary",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following complex conditional logic where age is 18, income is 50000, and has_degree is True, what is the final value of status?",
            "code": "age = 18\nincome = 50000\nhas_degree = True\nstatus = None\n\nif age >= 18 and age <= 65:\n    if income > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_premium"
        }
    },
    {
        "id": "BL-CD-S008-V002",
        "metadata": {
            "name": "低收入高学历",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "low_income_degree",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following complex conditional logic where age is 25, income is 25000, and has_degree is True, what is the final value of status?",
            "code": "age = 25\nincome = 25000\nhas_degree = True\nstatus = None\n\nif age >= 18 and age <= 65:\n    if income > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_basic"
        }
    },
    {
        "id": "BL-CD-S008-V003",
        "metadata": {
            "name": "年龄过高测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "age_overflow",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following complex conditional logic where age is 70, income is 50000, and has_degree is True, what is the final value of status?",
            "code": "age = 70\nincome = 50000\nhas_degree = True\nstatus = None\n\nif age >= 18 and age <= 65:\n    if income > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "not_eligible"
        }
    },
    {
        "id": "BL-CD-S008-V004",
        "metadata": {
            "name": "年轻无学历低收入",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "young_no_degree_low_income",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following complex conditional logic where age is 20, income is 25000, and has_degree is False, what is the final value of status?",
            "code": "age = 20\nincome = 25000\nhas_degree = False\nstatus = None\n\nif age >= 18 and age <= 65:\n    if income > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "pending_review"
        }
    },
    {
        "id": "BL-CD-S008-V005",
        "metadata": {
            "name": "C语言版本转换",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "language_conversion",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the following C version where age is 25, income is 50000, and has_degree is 1, what is the final value of status_code?",
            "code": "int age = 25;\nint income = 50000;\nint has_degree = 1;\nint status_code;\n\nif (age >= 18 && age <= 65) {\n    if (income > 30000) {\n        if (has_degree) {\n            status_code = 1; // approved_premium\n        } else {\n            status_code = 2; // approved_standard\n        }\n    } else {\n        if (age >= 21 && has_degree) {\n            status_code = 3; // approved_basic\n        } else {\n            status_code = 4; // pending_review\n        }\n    }\n} else {\n    status_code = 0; // not_eligible\n}\nprintf(\"Status code: %d\\n\", status_code);",
            "answer": 1
        }
    },
    {
        "id": "BL-CD-S008-V006",
        "metadata": {
            "name": "扩展条件系统",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "extended_conditions",
            "condition_pattern": "complex_logic",
            "branch_count": "8"
        },
        "task": {
            "description": "Given the extended system where age is 25, income is 50000, has_degree is True, and credit_score is 750, what is the final value of status?",
            "code": "age = 25\nincome = 50000\nhas_degree = True\ncredit_score = 750\nstatus = None\n\nif age >= 18 and age <= 65:\n    if income > 50000 and credit_score >= 700:\n        if has_degree:\n            status = \"approved_platinum\"\n        else:\n            status = \"approved_gold\"\n    elif income > 30000:\n        if has_degree and credit_score >= 650:\n            status = \"approved_premium\"\n        elif has_degree:\n            status = \"approved_standard\"\n        else:\n            status = \"approved_basic\"\n    else:\n        if age >= 21 and has_degree and credit_score >= 600:\n            status = \"approved_conditional\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_platinum"
        }
    },
    {
        "id": "BL-CD-S008-V007",
        "metadata": {
            "name": "短路逻辑测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "short_circuit_logic",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the short-circuit logic where age is None, income is 50000, and has_degree is True, what is the final value of status?",
            "code": "age = None\nincome = 50000\nhas_degree = True\nstatus = None\n\nif age is not None and 18 <= age <= 65:\n    if income > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "not_eligible"
        }
    },
    {
        "id": "BL-CD-S008-V008",
        "metadata": {
            "name": "边界值组合测试",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "boundary_combinations",
            "condition_pattern": "complex_logic",
            "branch_count": "5"
        },
        "task": {
            "description": "Given the boundary test where age is 21, income is 30000, and has_degree is True, what is the final value of status?",
            "code": "age = 21\nincome = 30000\nhas_degree = True\nstatus = None\n\nif age >= 18 and age <= 65:\n    if income > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_basic"
        }
    },
    {
        "id": "BL-CD-S008-V009",
        "metadata": {
            "name": "函数调用条件",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "function_call_conditions",
            "condition_pattern": "complex_logic",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the function-based conditions where get_age() returns 25, get_income() returns 50000, and has_valid_degree() returns True, what is the final value of status?",
            "code": "def get_age(): return 25\ndef get_income(): return 50000\ndef has_valid_degree(): return True\ndef get_experience(): return 3\n\nstatus = None\n\nif 18 <= get_age() <= 65:\n    if get_income() > 30000:\n        if has_valid_degree() and get_experience() >= 2:\n            status = \"approved_premium_plus\"\n        elif has_valid_degree():\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if get_age() >= 21 and has_valid_degree():\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_premium_plus"
        }
    },
    {
        "id": "BL-CD-S008-V010",
        "metadata": {
            "name": "异常处理条件",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "exception_handling",
            "condition_pattern": "complex_logic",
            "branch_count": "6"
        },
        "task": {
            "description": "Given the exception handling where age is 25, income is 'invalid', and has_degree is True, what is the final value of status?",
            "code": "age = 25\nincome = 'invalid'\nhas_degree = True\nstatus = None\n\ntry:\n    income_val = int(income)\nexcept (ValueError, TypeError):\n    income_val = 0\n\nif isinstance(age, int) and 18 <= age <= 65:\n    if income_val > 30000:\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    else:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_basic"
        }
    },
    {
        "id": "BL-CD-S008-V011",
        "metadata": {
            "name": "多重验证条件",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "multiple_validations",
            "condition_pattern": "complex_logic",
            "branch_count": "7"
        },
        "task": {
            "description": "Given the multi-validation system where all inputs are valid and age is 25, income is 50000, has_degree is True, what is the final value of status?",
            "code": "age = 25\nincome = 50000\nhas_degree = True\nemployment_status = 'full_time'\nstatus = None\n\n# Input validation\nif not isinstance(age, int) or not isinstance(income, int):\n    status = \"invalid_input\"\nelif age < 0 or income < 0:\n    status = \"invalid_values\"\nelif 18 <= age <= 65:\n    if income > 30000 and employment_status == 'full_time':\n        if has_degree:\n            status = \"approved_premium\"\n        else:\n            status = \"approved_standard\"\n    elif income > 20000:\n        if age >= 21 and has_degree:\n            status = \"approved_basic\"\n        else:\n            status = \"pending_review\"\n    else:\n        status = \"insufficient_income\"\nelse:\n    status = \"not_eligible\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_premium"
        }
    },
    {
        "id": "BL-CD-S008-V012",
        "metadata": {
            "name": "状态机条件系统",
            "category": "Block-Level",
            "subcategory": "Conditional",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "state_machine",
            "condition_pattern": "complex_logic",
            "branch_count": "8"
        },
        "task": {
            "description": "Given the state machine where current_state is 'initial', age is 25, income is 50000, and has_degree is True, what is the final value of status?",
            "code": "age = 25\nincome = 50000\nhas_degree = True\ncurrent_state = 'initial'\nstatus = None\n\nif current_state == 'initial':\n    if 18 <= age <= 65:\n        current_state = 'age_verified'\n    else:\n        status = \"not_eligible\"\n        current_state = 'rejected'\n\nif current_state == 'age_verified':\n    if income > 30000:\n        current_state = 'income_verified'\n    elif income > 15000:\n        current_state = 'income_low'\n    else:\n        status = \"insufficient_income\"\n        current_state = 'rejected'\n\nif current_state == 'income_verified':\n    if has_degree:\n        status = \"approved_premium\"\n    else:\n        status = \"approved_standard\"\nelif current_state == 'income_low':\n    if age >= 21 and has_degree:\n        status = \"approved_basic\"\n    else:\n        status = \"pending_review\"\n\nprint(f\"Status: {status}\")",
            "answer": "approved_premium"
        }
    }
]
```

#### 2C - 迭代代码块 [ Iterative ] (115)

> ```
> # 迭代代码块推理变式生成提示词
> 
> ## 任务目标
> 基于给定的迭代代码块种子任务，生成多样化的变式任务来全面测试大模型对循环结构、迭代过程、状态累积和终止条件的理解能力，包括各种循环类型、嵌套迭代、控制流跳转和递归调用等复杂迭代场景。
> 
> ## 迭代代码块特征分析
> 迭代代码块是指包含for、while、do-while循环以及递归调用等重复执行结构的代码段，重点测试模型对迭代次数计算、状态变化追踪、终止条件判断和累积结果预测的理解。
> 
> ## 变式生成维度
> 
> ### 1. 循环结构类型变式
> - **for循环变式**: 传统的计数循环和范围循环
> - **while循环变式**: 条件驱动的前置判断循环
> - **do-while循环变式**: 后置判断的至少执行一次循环
> - **foreach循环变式**: 基于集合遍历的循环
> - **递归循环变式**: 函数递归调用形成的迭代
> - **goto循环变式**: 使用goto构造的循环结构
> 
> ### 2. 迭代模式变式
> - **计数迭代变式**: 基于计数器的固定次数迭代
> - **条件迭代变式**: 基于条件判断的动态次数迭代
> - **遍历迭代变式**: 遍历数组、列表、字符串等数据结构
> - **搜索迭代变式**: 查找特定元素或条件的迭代
> - **累积迭代变式**: 逐步累积计算结果的迭代
> - **变换迭代变式**: 逐步变换数据状态的迭代
> 
> ### 3. 终止条件变式
> - **计数终止变式**: 基于迭代次数的终止条件
> - **数值终止变式**: 基于数值达到阈值的终止
> - **状态终止变式**: 基于程序状态变化的终止
> - **外部终止变式**: 基于外部输入或事件的终止
> - **异常终止变式**: 因异常或错误导致的提前终止
> - **复合终止变式**: 多个条件组合的复杂终止判断
> 
> ### 4. 嵌套和组合变式
> - **单层循环变式**: 简单的单层迭代结构
> - **双层嵌套变式**: 两层嵌套的循环结构
> - **多层嵌套变式**: 三层及以上的深度嵌套
> - **循环组合变式**: 多个独立循环的顺序组合
> - **交错循环变式**: 循环之间有交互和依赖关系
> - **递归嵌套变式**: 递归调用中包含循环结构
> 
> ### 5. 控制流跳转变式
> - **break跳出变式**: 使用break提前退出循环
> - **continue跳过变式**: 使用continue跳过当前迭代
> - **return返回变式**: 在循环中使用return直接返回
> - **goto跳转变式**: 使用goto跳转改变循环流程
> - **异常跳出变式**: 通过异常机制跳出循环
> - **多层跳出变式**: 从深层嵌套中跳出到外层
> 
> ### 6. 状态累积变式
> - **数值累积变式**: 数值的加法、乘法等累积运算
> - **字符串累积变式**: 字符串的拼接和构建
> - **数组累积变式**: 向数组或列表添加元素
> - **对象累积变式**: 对象属性的逐步设置和修改
> - **状态机变式**: 状态在迭代中的转换和更新
> - **资源累积变式**: 内存、文件等资源的逐步分配
> 
> ### 7. 边界和特殊情况变式
> - **空迭代变式**: 迭代次数为零的边界情况
> - **单次迭代变式**: 只执行一次的迭代
> - **无限循环变式**: 理论上的无限循环及其检测
> - **溢出变式**: 迭代过程中的数值溢出情况
> - **内存限制变式**: 受内存限制的迭代过程
> - **性能边界变式**: 大数据量的迭代性能考虑
> 
> ### 8. 递归模式变式
> - **线性递归变式**: 简单的线性递归结构
> - **分支递归变式**: 多分支的递归调用
> - **尾递归变式**: 尾递归优化的递归模式
> - **相互递归变式**: 函数间的相互递归调用
> - **间接递归变式**: 通过中间函数的间接递归
> - **递归终止变式**: 递归的基础情况和终止条件
> 
> ### 9. 数据结构遍历变式
> - **数组遍历变式**: 一维和多维数组的遍历
> - **链表遍历变式**: 单链表、双链表的遍历
> - **树遍历变式**: 二叉树、多叉树的遍历
> - **图遍历变式**: 图结构的深度和广度遍历
> - **哈希表遍历变式**: 哈希表键值对的遍历
> - **字符串遍历变式**: 字符串字符的逐个处理
> 
> ### 10. 并发和同步变式
> - **并行迭代变式**: 多线程并行执行的迭代
> - **同步迭代变式**: 需要同步的多线程迭代
> - **原子操作变式**: 迭代中的原子操作累积
> - **锁保护变式**: 使用锁保护的共享状态迭代
> - **无锁迭代变式**: 无锁数据结构的迭代访问
> - **分布式迭代变式**: 分布式环境下的迭代处理
> 
> ## 复杂度层次设计
> 
> ### 简单迭代 (Easy)
> - 单层for/while循环，固定次数迭代
> - 简单的计数或累积操作
> - 明确的终止条件，无控制流跳转
> - 基础数据类型的简单操作
> 
> ### 中等迭代 (Medium)
> - 2层嵌套循环或包含简单条件的迭代
> - 涉及break/continue的控制流
> - 数组或字符串的遍历处理
> - 简单的递归调用
> 
> ### 复杂迭代 (Hard)
> - 3层及以上嵌套或复杂的迭代逻辑
> - 复杂的终止条件和状态管理
> - 多重控制流跳转和异常处理
> - 复杂数据结构的遍历
> 
> ### 专家级迭代 (Expert)
> - 极度复杂的嵌套和递归结构
> - 涉及高级算法和数据结构
> - 并发和同步的迭代处理
> - 性能关键的迭代优化
> 
> ## 生成策略
> 
> ### 种子分析策略
> 1. **识别迭代模式**: 分析种子的循环类型和迭代特征
> 2. **提取核心逻辑**: 识别迭代的核心计算和状态变化
> 3. **分析终止条件**: 理解循环的终止机制和边界条件
> 4. **追踪状态变化**: 跟踪变量在迭代过程中的状态演变
> 
> ### 变式设计原则
> 1. **迭代完整性**: 确保能够正确模拟完整的迭代过程
> 2. **状态一致性**: 保证每次迭代的状态变化逻辑正确
> 3. **边界准确性**: 重点测试边界条件和特殊情况
> 4. **性能意识**: 考虑迭代的时间和空间复杂度
> 
> ### 质量保证
> 1. **迭代验证**: 手工验证关键迭代步骤的正确性
> 2. **边界测试**: 确保边界情况得到正确处理
> 3. **终止验证**: 验证所有循环都能正确终止
> 4. **状态追踪**: 确保状态变化的准确跟踪
> 
> ## 输出格式要求
> 
> ```json
> [
>     {
>         "id": "BL-IT-S00X-V001",
>         "metadata": {
>             "name": "迭代代码块变式名称",
>             "category": "Block-Level",
>             "subcategory": "Iterative",
>             "type": "variant",
>             "source": "Generated",
>             "language": "目标语言",
>             "difficulty": "easy/medium/hard/expert",
>             "intervention": 0,
>             "variant_type": "变式类型标签",
>             "loop_pattern": "for/while/do_while/foreach/recursive",
>             "nesting_depth": "嵌套层数",
>             "iteration_count": "预期迭代次数"
>         },
>         "task": {
>             "description": "迭代代码块推理任务描述",
>             "code": "包含迭代结构的代码块",
>             "answer": "迭代执行后的最终结果"
>         }
>     },
>     {下一个变式...}
> ]
> 特殊字段说明
> loop_pattern: 标识主要的循环模式类型
> nesting_depth: 记录循环嵌套的深度
> iteration_count: 预期的迭代执行次数
> variant_type: 描述具体的变式类型
> 生成目标
> 为每个提供的种子任务生成12-18个迭代代码块变式，确保：
> 
> 每种难度等级至少包含3-4个变式
> 涵盖至少6-8种不同的循环模式
> 包含不同嵌套深度的变式（1-4层）
> 至少包含3-4个包含控制流跳转的变式
> 包含2-3个递归相关的变式
> 重点测试场景
> 迭代次数计算: 给定初始条件，准确计算循环执行次数
> 状态变化追踪: 正确追踪变量在迭代过程中的状态变化
> 终止条件判断: 准确判断循环的终止时机和条件
> 嵌套循环理解: 对多层嵌套循环的正确理解和计算
> 控制流处理: 对break、continue等控制流的正确处理
> 递归深度理解: 对递归调用深度和返回值的正确计算
> 常见迭代计算模式
> 累加求和: Σ(i=1 to n) i = n(n+1)/2
> 阶乘计算: n! = n × (n-1)!
> 斐波那契数列: F(n) = F(n-1) + F(n-2)
> 幂次计算: a^n 的迭代计算
> 最大公约数: 欧几里得算法的迭代实现
> 素数判断: 试除法的迭代实现
> 请基于此提示词，为给定的迭代代码块种子任务生成全面的变式集合，输出格式为包含所有变式的JSON数组。
> ```

```json
[
    {
        "id": "BL-IT-S001-V001",
        "metadata": {
            "name": "简单for循环反向计数",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "reverse_counting",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following reverse for loop block, what is the final value of product?",
            "code": "int product = 1;\nfor (int i = 5; i >= 1; i--) {\n    product *= i;\n}\nprintf(\"Product: %d\\n\", product);",
            "answer": 120
        }
    },
    {
        "id": "BL-IT-S001-V002",
        "metadata": {
            "name": "步长为2的for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "step_increment",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following for loop with step 2, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = 1; i <= 6; i += 2) {\n    sum += i * i;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 35
        }
    },
    {
        "id": "BL-IT-S001-V003",
        "metadata": {
            "name": "累积乘法运算",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "multiplicative_accumulation",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following for loop with multiplicative accumulation, what is the final value of result?",
            "code": "int result = 2;\nfor (int i = 1; i <= 4; i++) {\n    result *= (i + 1);\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": 240
        }
    },
    {
        "id": "BL-IT-S001-V004",
        "metadata": {
            "name": "条件累加for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "conditional_accumulation",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following for loop with conditional accumulation, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = 1; i <= 10; i++) {\n    if (i % 3 == 0) {\n        sum += i;\n    }\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 18
        }
    },
    {
        "id": "BL-IT-S001-V005",
        "metadata": {
            "name": "负数范围for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "negative_range",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following for loop with negative range, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = -2; i <= 2; i++) {\n    sum += i * i;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 10
        }
    },
    {
        "id": "BL-IT-S001-V006",
        "metadata": {
            "name": "浮点数累加for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "float_accumulation",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following for loop with float accumulation, what is the final value of sum (rounded to 1 decimal)?",
            "code": "float sum = 0.0;\nfor (int i = 1; i <= 4; i++) {\n    sum += 1.0 / i;\n}\nprintf(\"Sum: %.1f\\n\", sum);",
            "answer": 2.1
        }
    },
    {
        "id": "BL-IT-S001-V007",
        "metadata": {
            "name": "字符ASCII累加",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "char_ascii_sum",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following for loop with character ASCII accumulation, what is the final value of sum?",
            "code": "int sum = 0;\nfor (char c = 'A'; c <= 'E'; c++) {\n    sum += (int)c;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 335
        }
    },
    {
        "id": "BL-IT-S001-V008",
        "metadata": {
            "name": "复合赋值运算for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "compound_assignment",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following for loop with compound assignment, what is the final value of result?",
            "code": "int result = 10;\nfor (int i = 1; i <= 4; i++) {\n    result += i;\n    result *= 2;\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": 120
        }
    },
    {
        "id": "BL-IT-S001-V009",
        "metadata": {
            "name": "位运算累加for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bitwise_accumulation",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following for loop with bitwise operations, what is the final value of result?",
            "code": "int result = 0;\nfor (int i = 1; i <= 4; i++) {\n    result ^= (1 << i);\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": 30
        }
    },
    {
        "id": "BL-IT-S001-V010",
        "metadata": {
            "name": "数组元素累加for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "array_accumulation",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following for loop with array element accumulation, what is the final value of sum?",
            "code": "int arr[] = {2, 4, 6, 8, 10};\nint sum = 0;\nfor (int i = 0; i < 5; i++) {\n    sum += arr[i];\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 30
        }
    },
    {
        "id": "BL-IT-S001-V011",
        "metadata": {
            "name": "最大值查找for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "max_finding",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following for loop to find maximum value, what is the final value of max?",
            "code": "int arr[] = {3, 7, 2, 9, 1, 5};\nint max = arr[0];\nfor (int i = 1; i < 6; i++) {\n    if (arr[i] > max) {\n        max = arr[i];\n    }\n}\nprintf(\"Max: %d\\n\", max);",
            "answer": 9
        }
    },
    {
        "id": "BL-IT-S001-V012",
        "metadata": {
            "name": "计数器for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "counting",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following for loop counting positive numbers, what is the final value of count?",
            "code": "int arr[] = {-1, 3, -2, 5, 0, 7, -4, 2};\nint count = 0;\nfor (int i = 0; i < 8; i++) {\n    if (arr[i] > 0) {\n        count++;\n    }\n}\nprintf(\"Count: %d\\n\", count);",
            "answer": 4
        }
    },
    {
        "id": "BL-IT-S001-V013",
        "metadata": {
            "name": "交替累加for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "alternating_accumulation",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following for loop with alternating accumulation, what is the final value of result?",
            "code": "int result = 0;\nfor (int i = 1; i <= 6; i++) {\n    if (i % 2 == 1) {\n        result += i;\n    } else {\n        result -= i;\n    }\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": -3
        }
    },
    {
        "id": "BL-IT-S001-V014",
        "metadata": {
            "name": "平方和for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "square_sum",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following for loop calculating sum of squares, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = 1; i <= 4; i++) {\n    sum += i * i;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 30
        }
    },
    {
        "id": "BL-IT-S001-V015",
        "metadata": {
            "name": "边界条件for循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boundary_condition",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 0
        },
        "task": {
            "description": "Given the following for loop with boundary condition, what is the final value of sum?",
            "code": "int sum = 5;\nfor (int i = 1; i < 1; i++) {\n    sum += i;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 5
        }
    },
    {
        "id": "BL-IT-S002-V001",
        "metadata": {
            "name": "字符数组初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "char_array_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following character array initialization loop where BUFFER_SIZE is 8, what is the value of buffer[5] after execution?",
            "code": "char buffer[8];\nfor (int i = 0; i < 8; i++) {\n    buffer[i] = 'A' + i;\n}\nprintf(\"buffer[5]: %c\\n\", buffer[5]);",
            "answer": "F"
        }
    },
    {
        "id": "BL-IT-S002-V002",
        "metadata": {
            "name": "整数数组递增初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "int_array_increment",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following integer array initialization where SIZE is 6, what is the value of arr[4] after execution?",
            "code": "int arr[6];\nfor (int i = 0; i < 6; i++) {\n    arr[i] = (i + 1) * 3;\n}\nprintf(\"arr[4]: %d\\n\", arr[4]);",
            "answer": 15
        }
    },
    {
        "id": "BL-IT-S002-V003",
        "metadata": {
            "name": "布尔数组初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "bool_array_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 7
        },
        "task": {
            "description": "Given the following boolean array initialization where SIZE is 7, what is the value of flags[3] after execution?",
            "code": "bool flags[7];\nfor (int i = 0; i < 7; i++) {\n    flags[i] = (i % 2 == 0);\n}\nprintf(\"flags[3]: %s\\n\", flags[3] ? \"true\" : \"false\");",
            "answer": "false"
        }
    },
    {
        "id": "BL-IT-S002-V004",
        "metadata": {
            "name": "二维数组行初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "2d_array_init",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 12
        },
        "task": {
            "description": "Given the following 2D array initialization where ROWS is 3 and COLS is 4, what is the value of matrix[1][2] after execution?",
            "code": "int matrix[3][4];\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 4; j++) {\n        matrix[i][j] = i * 4 + j + 1;\n    }\n}",
            "answer": 7
        }
    },
    {
        "id": "BL-IT-S002-V005",
        "metadata": {
            "name": "浮点数组初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "float_array_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following float array initialization where SIZE is 5, what is the value of arr[2] after execution?",
            "code": "float arr[5];\nfor (int i = 0; i < 5; i++) {\n    arr[i] = (i + 1) * 0.5;\n}\nprintf(\"arr[2]: %.1f\\n\", arr[2]);",
            "answer": 1.5
        }
    },
    {
        "id": "BL-IT-S002-V006",
        "metadata": {
            "name": "指针数组条件初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "pointer_conditional_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following pointer array conditional initialization where SIZE is 8, how many pointers are set to NULL?",
            "code": "int* ptr_arr[8];\nint dummy = 10;\nfor (int i = 0; i < 8; i++) {\n    if (i % 3 == 0) {\n        ptr_arr[i] = NULL;\n    } else {\n        ptr_arr[i] = &dummy;\n    }\n}",
            "answer": 3
        }
    },
    {
        "id": "BL-IT-S002-V007",
        "metadata": {
            "name": "字符串数组初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "string_array_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following string array initialization where SIZE is 4, what is the length of strings[2] after execution?",
            "code": "char strings[4][10];\nfor (int i = 0; i < 4; i++) {\n    for (int j = 0; j <= i; j++) {\n        strings[i][j] = 'X';\n    }\n    strings[i][i+1] = '\\0';\n}",
            "answer": 3
        }
    },
    {
        "id": "BL-IT-S002-V008",
        "metadata": {
            "name": "结构体数组初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "struct_array_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following struct array initialization where SIZE is 5, what is the value of points[3].y after execution?",
            "code": "typedef struct { int x, y; } Point;\nPoint points[5];\nfor (int i = 0; i < 5; i++) {\n    points[i].x = i * 2;\n    points[i].y = i * i;\n}",
            "answer": 9
        }
    },
    {
        "id": "BL-IT-S002-V009",
        "metadata": {
            "name": "矩阵对角线初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "diagonal_init",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 16
        },
        "task": {
            "description": "Given the following diagonal matrix initialization where SIZE is 4, what is the value of matrix[2][2] after execution?",
            "code": "int matrix[4][4];\nfor (int i = 0; i < 4; i++) {\n    for (int j = 0; j < 4; j++) {\n        matrix[i][j] = (i == j) ? i + 1 : 0;\n    }\n}",
            "answer": 3
        }
    },
    {
        "id": "BL-IT-S002-V010",
        "metadata": {
            "name": "数组反向初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "reverse_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following reverse array initialization where SIZE is 6, what is the value of arr[1] after execution?",
            "code": "int arr[6];\nfor (int i = 0; i < 6; i++) {\n    arr[i] = 6 - i;\n}\nprintf(\"arr[1]: %d\\n\", arr[1]);",
            "answer": 5
        }
    },
    {
        "id": "BL-IT-S002-V011",
        "metadata": {
            "name": "累积初始化数组",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cumulative_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following cumulative array initialization where SIZE is 5, what is the value of arr[3] after execution?",
            "code": "int arr[5];\narr[0] = 1;\nfor (int i = 1; i < 5; i++) {\n    arr[i] = arr[i-1] + i;\n}\nprintf(\"arr[3]: %d\\n\", arr[3]);",
            "answer": 7
        }
    },
    {
        "id": "BL-IT-S002-V012",
        "metadata": {
            "name": "位模式数组初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bit_pattern_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following bit pattern array initialization where SIZE is 8, what is the value of arr[5] after execution?",
            "code": "int arr[8];\nfor (int i = 0; i < 8; i++) {\n    arr[i] = 1 << i;\n}\nprintf(\"arr[5]: %d\\n\", arr[5]);",
            "answer": 32
        }
    },
    {
        "id": "BL-IT-S002-V013",
        "metadata": {
            "name": "三维数组初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "3d_array_init",
            "loop_pattern": "for",
            "nesting_depth": 3,
            "iteration_count": 24
        },
        "task": {
            "description": "Given the following 3D array initialization where dimensions are 2x3x4, what is the value of cube[1][1][2] after execution?",
            "code": "int cube[2][3][4];\nfor (int i = 0; i < 2; i++) {\n    for (int j = 0; j < 3; j++) {\n        for (int k = 0; k < 4; k++) {\n            cube[i][j][k] = i * 12 + j * 4 + k;\n        }\n    }\n}",
            "answer": 18
        }
    },
    {
        "id": "BL-IT-S002-V014",
        "metadata": {
            "name": "条件跳过初始化",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "conditional_skip_init",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following conditional skip initialization where SIZE is 10, how many elements are initialized to -1?",
            "code": "int arr[10];\nfor (int i = 0; i < 10; i++) {\n    if (i % 3 == 0) {\n        continue;\n    }\n    arr[i] = -1;\n}",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S003-V001",
        "metadata": {
            "name": "条件递增while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "conditional_increment",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 7
        },
        "task": {
            "description": "Given the following while loop with conditional increment, what is the final value of sum?",
            "code": "int value = 1;\nint sum = 0;\nwhile (value < 100) {\n    sum += value;\n    value *= 2;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 127
        }
    },
    {
        "id": "BL-IT-S003-V002",
        "metadata": {
            "name": "字符串长度计算while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "string_length",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 11
        },
        "task": {
            "description": "Given the following while loop to calculate string length, what is the final value of length?",
            "code": "char str[] = \"Hello World\";\nint length = 0;\nwhile (str[length] != '\\0') {\n    length++;\n}\nprintf(\"Length: %d\\n\", length);",
            "answer": 11
        }
    },
    {
        "id": "BL-IT-S003-V003",
        "metadata": {
            "name": "数字反转while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "number_reversal",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following while loop to reverse a number, what is the final value of reversed?",
            "code": "int num = 1234;\nint reversed = 0;\nwhile (num > 0) {\n    reversed = reversed * 10 + num % 10;\n    num /= 10;\n}\nprintf(\"Reversed: %d\\n\", reversed);",
            "answer": 4321
        }
    },
    {
        "id": "BL-IT-S003-V004",
        "metadata": {
            "name": "最大公约数while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "gcd_calculation",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following while loop to calculate GCD using Euclidean algorithm, what is the final value of a?",
            "code": "int a = 48, b = 18;\nwhile (b != 0) {\n    int temp = b;\n    b = a % b;\n    a = temp;\n}\nprintf(\"GCD: %d\\n\", a);",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S003-V005",
        "metadata": {
            "name": "平方根逼近while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "sqrt_approximation",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following while loop for square root approximation, what is the final value of x (rounded to nearest integer)?",
            "code": "double x = 10.0;\ndouble target = 25.0;\nwhile (x * x - target > 0.1 || target - x * x > 0.1) {\n    x = (x + target / x) / 2.0;\n}\nprintf(\"Result: %.0f\\n\", x);",
            "answer": 5
        }
    },
    {
        "id": "BL-IT-S003-V006",
        "metadata": {
            "name": "斐波那契while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "fibonacci_sequence",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following while loop to generate Fibonacci sequence, what is the final value of current?",
            "code": "int prev = 0, current = 1, next;\nint limit = 20;\nwhile (current <= limit) {\n    next = prev + current;\n    prev = current;\n    current = next;\n}\nprintf(\"Current: %d\\n\", current);",
            "answer": 34
        }
    },
    {
        "id": "BL-IT-S003-V007",
        "metadata": {
            "name": "质数判断while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "prime_check",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following while loop to check if 17 is prime, what is the final value of isPrime?",
            "code": "int num = 17;\nint divisor = 2;\nint isPrime = 1;\nwhile (divisor * divisor <= num && isPrime) {\n    if (num % divisor == 0) {\n        isPrime = 0;\n    }\n    divisor++;\n}\nprintf(\"IsPrime: %d\\n\", isPrime);",
            "answer": 1
        }
    },
    {
        "id": "BL-IT-S003-V008",
        "metadata": {
            "name": "数字位数统计while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "digit_count",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following while loop to count digits, what is the final value of count?",
            "code": "int num = 12345;\nint count = 0;\nwhile (num > 0) {\n    count++;\n    num /= 10;\n}\nprintf(\"Count: %d\\n\", count);",
            "answer": 5
        }
    },
    {
        "id": "BL-IT-S003-V009",
        "metadata": {
            "name": "累积乘积while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cumulative_product",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following while loop for cumulative product, what is the final value of product?",
            "code": "int i = 1;\nint product = 1;\nwhile (i <= 5) {\n    product *= i;\n    i++;\n}\nprintf(\"Product: %d\\n\", product);",
            "answer": 120
        }
    },
    {
        "id": "BL-IT-S003-V010",
        "metadata": {
            "name": "条件累加while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "conditional_sum",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following while loop with conditional sum, what is the final value of sum?",
            "code": "int i = 1;\nint sum = 0;\nwhile (i <= 10) {\n    if (i % 2 == 0) {\n        sum += i;\n    }\n    i++;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 30
        }
    },
    {
        "id": "BL-IT-S003-V011",
        "metadata": {
            "name": "搜索目标while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "target_search",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following while loop to search for target, what is the final value of index?",
            "code": "int arr[] = {10, 20, 30, 40, 50};\nint target = 40;\nint index = 0;\nwhile (index < 5 && arr[index] != target) {\n    index++;\n}\nprintf(\"Index: %d\\n\", index);",
            "answer": 3
        }
    },
    {
        "id": "BL-IT-S003-V012",
        "metadata": {
            "name": "幂运算while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "power_calculation",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following while loop to calculate 3^4, what is the final value of result?",
            "code": "int base = 3;\nint exp = 4;\nint result = 1;\nwhile (exp > 0) {\n    result *= base;\n    exp--;\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": 81
        }
    },
    {
        "id": "BL-IT-S003-V013",
        "metadata": {
            "name": "数组最小值while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "min_finding",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following while loop to find minimum value, what is the final value of min?",
            "code": "int arr[] = {8, 3, 9, 1, 5, 7};\nint min = arr[0];\nint i = 1;\nwhile (i < 6) {\n    if (arr[i] < min) {\n        min = arr[i];\n    }\n    i++;\n}\nprintf(\"Min: %d\\n\", min);",
            "answer": 1
        }
    },
    {
        "id": "BL-IT-S003-V014",
        "metadata": {
            "name": "阶乘计算while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "factorial_calculation",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following while loop to calculate 6!, what is the final value of factorial?",
            "code": "int n = 6;\nint factorial = 1;\nwhile (n > 0) {\n    factorial *= n;\n    n--;\n}\nprintf(\"Factorial: %d\\n\", factorial);",
            "answer": 720
        }
    },
    {
        "id": "BL-IT-S003-V015",
        "metadata": {
            "name": "边界条件while循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boundary_condition",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 0
        },
        "task": {
            "description": "Given the following while loop with boundary condition, what is the final value of count?",
            "code": "int count = 5;\nint condition = 0;\nwhile (condition > 0) {\n    count++;\n    condition--;\n}\nprintf(\"Count: %d\\n\", count);",
            "answer": 5
        }
    },
    {
        "id": "BL-IT-S004-V001",
        "metadata": {
            "name": "三层嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "triple_nested",
            "loop_pattern": "for",
            "nesting_depth": 3,
            "iteration_count": 24
        },
        "task": {
            "description": "Given the following triple nested loop, what is the final value of total?",
            "code": "total = 0\nfor i in range(2):\n    for j in range(3):\n        for k in range(4):\n            total += (i + 1) * (j + 1) * (k + 1)\nprint(f\"Total: {total}\")",
            "answer": 150
        }
    },
    {
        "id": "BL-IT-S004-V002",
        "metadata": {
            "name": "不等长嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "unequal_nested",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following unequal nested loop, what is the final value of total?",
            "code": "total = 0\nfor i in range(4):\n    for j in range(i + 1):\n        total += (i + j)\nprint(f\"Total: {total}\")",
            "answer": 20
        }
    },
    {
        "id": "BL-IT-S004-V003",
        "metadata": {
            "name": "条件嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "conditional_nested",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following conditional nested loop, what is the final value of count?",
            "code": "count = 0\nfor i in range(3):\n    for j in range(3):\n        if i + j >= 2:\n            count += 1\nprint(f\"Count: {count}\")",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S004-V004",
        "metadata": {
            "name": "矩阵乘法嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "matrix_multiplication",
            "loop_pattern": "for",
            "nesting_depth": 3,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following matrix multiplication nested loop for 2x2 matrices, what is the value of result[1][0]?",
            "code": "A = [[1, 2], [3, 4]]\nB = [[2, 0], [1, 3]]\nresult = [[0, 0], [0, 0]]\nfor i in range(2):\n    for j in range(2):\n        for k in range(2):\n            result[i][j] += A[i][k] * B[k][j]\nprint(f\"result[1][0]: {result[1][0]}\")",
            "answer": 10
        }
    },
    {
        "id": "BL-IT-S004-V005",
        "metadata": {
            "name": "对角线累加嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "diagonal_sum",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following nested loop for diagonal sum, what is the final value of diagonal_sum?",
            "code": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\ndiagonal_sum = 0\nfor i in range(3):\n    for j in range(3):\n        if i == j:\n            diagonal_sum += matrix[i][j]\nprint(f\"Diagonal sum: {diagonal_sum}\")",
            "answer": 15
        }
    },
    {
        "id": "BL-IT-S004-V006",
        "metadata": {
            "name": "上三角矩阵嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "upper_triangle",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following nested loop for upper triangle sum, what is the final value of sum_upper?",
            "code": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\nsum_upper = 0\nfor i in range(3):\n    for j in range(i, 3):\n        sum_upper += matrix[i][j]\nprint(f\"Upper triangle sum: {sum_upper}\")",
            "answer": 21
        }
    },
    {
        "id": "BL-IT-S004-V007",
        "metadata": {
            "name": "字符串模式嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "string_pattern",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following nested loop creating string pattern, what is the length of result?",
            "code": "result = \"\"\nfor i in range(4):\n    for j in range(i + 1):\n        result += \"*\"\n    result += \"\\n\"\nprint(f\"Length: {len(result)}\")",
            "answer": 14
        }
    },
    {
        "id": "BL-IT-S004-V008",
        "metadata": {
            "name": "列表推导式等价嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "list_comprehension_equivalent",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 12
        },
        "task": {
            "description": "Given the following nested loop equivalent to list comprehension, what is the sum of all elements in result?",
            "code": "result = []\nfor i in range(3):\n    for j in range(4):\n        result.append(i * j)\ntotal = sum(result)\nprint(f\"Total: {total}\")",
            "answer": 18
        }
    },
    {
        "id": "BL-IT-S004-V009",
        "metadata": {
            "name": "嵌套循环最大值查找",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "nested_max_finding",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following nested loop to find maximum, what is the final value of max_val?",
            "code": "matrix = [[3, 7, 1], [9, 2, 5], [4, 8, 6]]\nmax_val = matrix[0][0]\nfor i in range(3):\n    for j in range(3):\n        if matrix[i][j] > max_val:\n            max_val = matrix[i][j]\nprint(f\"Max: {max_val}\")",
            "answer": 9
        }
    },
    {
        "id": "BL-IT-S004-V010",
        "metadata": {
            "name": "嵌套循环计数器",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "nested_counter",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following nested loop counter, what is the final value of even_count?",
            "code": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\neven_count = 0\nfor i in range(3):\n    for j in range(3):\n        if matrix[i][j] % 2 == 0:\n            even_count += 1\nprint(f\"Even count: {even_count}\")",
            "answer": 4
        }
    },
    {
        "id": "BL-IT-S004-V011",
        "metadata": {
            "name": "乘积表嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "multiplication_table",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following nested loop creating multiplication table, what is the value of table[2][1]?",
            "code": "table = [[0 for _ in range(3)] for _ in range(3)]\nfor i in range(3):\n    for j in range(3):\n        table[i][j] = (i + 1) * (j + 1)\nprint(f\"table[2][1]: {table[2][1]}\")",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S004-V012",
        "metadata": {
            "name": "坐标距离嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "coordinate_distance",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following nested loop calculating Manhattan distances, what is the final value of total_distance?",
            "code": "total_distance = 0\nfor i in range(3):\n    for j in range(3):\n        distance = abs(i - 1) + abs(j - 1)\n        total_distance += distance\nprint(f\"Total distance: {total_distance}\")",
            "answer": 8
        }
    },
    {
        "id": "BL-IT-S004-V013",
        "metadata": {
            "name": "帕斯卡三角嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "pascal_triangle",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following nested loop generating Pascal's triangle, what is the value of triangle[2][1]?",
            "code": "triangle = [[1], [1, 1], [1, 0, 1]]\nfor i in range(1, 3):\n    for j in range(1, i):\n        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]\nprint(f\"triangle[2][1]: {triangle[2][1]}\")",
            "answer": 2
        }
    },
    {
        "id": "BL-IT-S004-V014",
        "metadata": {
            "name": "螺旋矩阵嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "spiral_matrix",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following nested loop for spiral pattern sum, what is the final value of center_sum?",
            "code": "matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]\ncenter_sum = 0\nfor i in range(1, 2):\n    for j in range(1, 2):\n        center_sum += matrix[i][j]\n        for di in [-1, 0, 1]:\n            for dj in [-1, 0, 1]:\n                if 0 <= i+di < 3 and 0 <= j+dj < 3 and (di != 0 or dj != 0):\n                    center_sum += matrix[i+di][j+dj]\nprint(f\"Center sum: {center_sum}\")",
            "answer": 45
        }
    },
    {
        "id": "BL-IT-S005-V001",
        "metadata": {
            "name": "多重break嵌套循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "multiple_break",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following nested loop with multiple breaks, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = 1; i <= 5; i++) {\n    for (int j = 1; j <= 5; j++) {\n        if (i * j > 6) break;\n        sum += i * j;\n    }\n    if (i > 3) break;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 15
        }
    },
    {
        "id": "BL-IT-S005-V002",
        "metadata": {
            "name": "continue跳过偶数",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "continue_even_skip",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following loop with continue skipping even numbers, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = 1; i <= 10; i++) {\n    if (i % 2 == 0) {\n        continue;\n    }\n    sum += i;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 25
        }
    },
    {
        "id": "BL-IT-S005-V003",
        "metadata": {
            "name": "goto替代break循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "goto_break",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following nested loop with goto, what is the final value of count?",
            "code": "int count = 0;\nfor (int i = 1; i <= 3; i++) {\n    for (int j = 1; j <= 3; j++) {\n        count++;\n        if (i + j == 4) goto end;\n    }\n}\nend:\nprintf(\"Count: %d\\n\", count);",
            "answer": 4
        }
    },
    {
        "id": "BL-IT-S005-V004",
        "metadata": {
            "name": "函数返回中断循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "function_return",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following function with return in loop, what value does the function return?",
            "code": "int find_first_multiple(int target) {\n    for (int i = 1; i <= 10; i++) {\n        if (i * 3 >= target) {\n            return i * 3;\n        }\n    }\n    return -1;\n}\nint result = find_first_multiple(8);",
            "answer": 9
        }
    },
    {
        "id": "BL-IT-S005-V005",
        "metadata": {
            "name": "标志变量控制循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "flag_control",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following loop with flag control, what is the final value of i?",
            "code": "int found = 0;\nint i;\nfor (i = 1; i <= 10 && !found; i++) {\n    if (i * i > 30) {\n        found = 1;\n    }\n}\nprintf(\"i: %d\\n\", i);",
            "answer": 7
        }
    },
    {
        "id": "BL-IT-S005-V006",
        "metadata": {
            "name": "switch控制流循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "switch_control",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following loop with switch control flow, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = 1; i <= 5; i++) {\n    switch (i % 3) {\n        case 0:\n            sum += i * 2;\n            break;\n        case 1:\n            sum += i;\n            break;\n        case 2:\n            continue;\n    }\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 7
        }
    },
    {
        "id": "BL-IT-S005-V007",
        "metadata": {
            "name": "多条件break循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "multi_condition_break",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following loop with multiple break conditions, what is the final value of product?",
            "code": "int product = 1;\nfor (int i = 1; i <= 10; i++) {\n    product *= i;\n    if (product > 20 || i >= 4) {\n        break;\n    }\n}\nprintf(\"Product: %d\\n\", product);",
            "answer": 24
        }
    },
    {
        "id": "BL-IT-S005-V008",
        "metadata": {
            "name": "异常模拟控制流",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "exception_simulation",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following loop simulating exception handling, what is the final value of count?",
            "code": "int count = 0;\nint error_flag = 0;\nfor (int i = 1; i <= 10; i++) {\n    if (i == 8) {\n        error_flag = 1;\n        break;\n    }\n    count++;\n}\nif (error_flag) {\n    count = -1;\n}\nprintf(\"Count: %d\\n\", count);",
            "answer": -1
        }
    },
    {
        "id": "BL-IT-S005-V009",
        "metadata": {
            "name": "条件continue累加",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "conditional_continue",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 12
        },
        "task": {
            "description": "Given the following loop with conditional continue, what is the final value of sum?",
            "code": "int sum = 0;\nfor (int i = 1; i <= 12; i++) {\n    if (i % 3 == 0 || i % 4 == 0) {\n        continue;\n    }\n    sum += i;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 30
        }
    },
    {
        "id": "BL-IT-S005-V010",
        "metadata": {
            "name": "嵌套continue控制",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "nested_continue",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following nested loop with continue, what is the final value of count?",
            "code": "int count = 0;\nfor (int i = 1; i <= 3; i++) {\n    for (int j = 1; j <= 3; j++) {\n        if (i == j) {\n            continue;\n        }\n        count++;\n    }\n}\nprintf(\"Count: %d\\n\", count);",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S005-V011",
        "metadata": {
            "name": "do-while中的break",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "do_while_break",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following do-while loop with break, what is the final value of sum?",
            "code": "int sum = 0;\nint i = 1;\ndo {\n    sum += i;\n    i++;\n    if (sum > 5) {\n        break;\n    }\n} while (i <= 10);\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S005-V012",
        "metadata": {
            "name": "while中的continue",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "while_continue",
            "loop_pattern": "while",
            "nesting_depth": 1,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following while loop with continue, what is the final value of sum?",
            "code": "int sum = 0;\nint i = 1;\nwhile (i <= 10) {\n    if (i % 3 == 0) {\n        i++;\n        continue;\n    }\n    sum += i;\n    i++;\n}\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 37
        }
    },
    {
        "id": "BL-IT-S005-V013",
        "metadata": {
            "name": "标签跳转循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "label_jump",
            "loop_pattern": "for",
            "nesting_depth": 2,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following nested loop with label jump, what is the final value of total?",
            "code": "int total = 0;\nouter:\nfor (int i = 1; i <= 3; i++) {\n    for (int j = 1; j <= 3; j++) {\n        total += i + j;\n        if (total > 10) {\n            goto outer_end;\n        }\n    }\n}\nouter_end:\nprintf(\"Total: %d\\n\", total);",
            "answer": 12
        }
    },
    {
        "id": "BL-IT-S005-V014",
        "metadata": {
            "name": "复合控制流循环",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "compound_control_flow",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following loop with compound control flow, what is the final value of result?",
            "code": "int result = 0;\nfor (int i = 1; i <= 15; i++) {\n    if (i % 2 == 0) continue;\n    if (i > 10) break;\n    if (i % 3 == 0) {\n        result += i * 2;\n    } else {\n        result += i;\n    }\n}\nprintf(\"Result: %d\\n\", result);",
            "answer": 34
        }
    },
    {
        "id": "BL-IT-S006-V001",
        "metadata": {
            "name": "do-while递增到阈值",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "threshold_increment",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following do-while loop incrementing to threshold, what is the final value of value?",
            "code": "int value = 2;\ndo {\n    value *= 2;\n} while (value < 20);\nprintf(\"Value: %d\\n\", value);",
            "answer": 32
        }
    },
    {
        "id": "BL-IT-S006-V002",
        "metadata": {
            "name": "do-while字符递增",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "char_increment",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following do-while loop with character increment, what is the final value of ch?",
            "code": "char ch = 'X';\ndo {\n    ch++;\n} while (ch < 'Z');\nprintf(\"Character: %c\\n\", ch);",
            "answer": "Z"
        }
    },
    {
        "id": "BL-IT-S006-V003",
        "metadata": {
            "name": "do-while累积求和",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "cumulative_sum",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following do-while loop with cumulative sum, what is the final value of sum?",
            "code": "int sum = 0;\nint i = 1;\ndo {\n    sum += i * i;\n    i++;\n} while (i <= 4);\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 30
        }
    },
    {
        "id": "BL-IT-S006-V004",
        "metadata": {
            "name": "do-while除法递减",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "division_decrement",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following do-while loop with division, what is the final value of num?",
            "code": "int num = 100;\nint count = 0;\ndo {\n    num /= 2;\n    count++;\n} while (num > 5);\nprintf(\"Count: %d\\n\", count);",
            "answer": 4
        }
    },
    {
        "id": "BL-IT-S006-V005",
        "metadata": {
            "name": "do-while条件累加",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "conditional_accumulation",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following do-while loop with conditional accumulation, what is the final value of result?",
            "code": "int result = 0;\nint i = 1;\ndo {\n    if (i % 2 == 1) {\n        result += i;\n    } else {\n        result -= i;\n    }\n    i++;\n} while (i <= 6);\nprintf(\"Result: %d\\n\", result);",
            "answer": -3
        }
    },
    {
        "id": "BL-IT-S006-V006",
        "metadata": {
            "name": "do-while数组填充",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "array_filling",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following do-while loop filling array, what is the value of arr[3]?",
            "code": "int arr[5];\nint i = 0;\ndo {\n    arr[i] = (i + 1) * 3;\n    i++;\n} while (i < 5);\nprintf(\"arr[3]: %d\\n\", arr[3]);",
            "answer": 12
        }
    },
    {
        "id": "BL-IT-S006-V007",
        "metadata": {
            "name": "do-while浮点递增",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "float_increment",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following do-while loop with float increment, what is the final value of sum (rounded to 1 decimal)?",
            "code": "float sum = 0.0;\nfloat x = 0.5;\ndo {\n    sum += x;\n    x += 0.5;\n} while (x <= 2.5);\nprintf(\"Sum: %.1f\\n\", sum);",
            "answer": 7.5
        }
    },
    {
        "id": "BL-IT-S006-V008",
        "metadata": {
            "name": "do-while最大值查找",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "max_finding",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following do-while loop finding maximum, what is the final value of max?",
            "code": "int arr[] = {3, 8, 2, 9, 1};\nint max = arr[0];\nint i = 1;\ndo {\n    if (arr[i] > max) {\n        max = arr[i];\n    }\n    i++;\n} while (i < 5);\nprintf(\"Max: %d\\n\", max);",
            "answer": 9
        }
    },
    {
        "id": "BL-IT-S006-V009",
        "metadata": {
            "name": "do-while位运算",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "bitwise_operation",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following do-while loop with bitwise operations, what is the final value of result?",
            "code": "int result = 1;\nint shift = 1;\ndo {\n    result |= (1 << shift);\n    shift++;\n} while (shift <= 3);\nprintf(\"Result: %d\\n\", result);",
            "answer": 15
        }
    },
    {
        "id": "BL-IT-S006-V010",
        "metadata": {
            "name": "do-while字符串构建",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "string_building",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following do-while loop building string, what is the length of the resulting string?",
            "code": "char str[10] = \"\";\nint len = 0;\nchar ch = 'A';\ndo {\n    str[len] = ch;\n    len++;\n    ch++;\n} while (ch <= 'C');\nstr[len] = '\\0';\nprintf(\"Length: %d\\n\", len);",
            "answer": 3
        }
    },
    {
        "id": "BL-IT-S006-V011",
        "metadata": {
            "name": "do-while阶乘计算",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "factorial_calculation",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following do-while loop calculating factorial, what is the final value of factorial?",
            "code": "int factorial = 1;\nint n = 5;\ndo {\n    factorial *= n;\n    n--;\n} while (n > 0);\nprintf(\"Factorial: %d\\n\", factorial);",
            "answer": 120
        }
    },
    {
        "id": "BL-IT-S006-V012",
        "metadata": {
            "name": "do-while倒数累加",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "reciprocal_sum",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following do-while loop with reciprocal sum, what is the final value of sum (rounded to 2 decimals)?",
            "code": "double sum = 0.0;\nint i = 1;\ndo {\n    sum += 1.0 / i;\n    i++;\n} while (i <= 4);\nprintf(\"Sum: %.2f\\n\", sum);",
            "answer": 2.08
        }
    },
    {
        "id": "BL-IT-S006-V013",
        "metadata": {
            "name": "do-while模运算计数",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "modulo_counting",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following do-while loop counting with modulo, what is the final value of count?",
            "code": "int count = 0;\nint i = 1;\ndo {\n    if (i % 3 == 0) {\n        count++;\n    }\n    i++;\n} while (i <= 12);\nprintf(\"Count: %d\\n\", count);",
            "answer": 4
        }
    },
    {
        "id": "BL-IT-S006-V014",
        "metadata": {
            "name": "do-while边界测试",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "boundary_test",
            "loop_pattern": "do_while",
            "nesting_depth": 1,
            "iteration_count": 1
        },
        "task": {
            "description": "Given the following do-while loop with false condition, what is the final value of counter?",
            "code": "int counter = 10;\ndo {\n    counter += 5;\n} while (0);\nprintf(\"Counter: %d\\n\", counter);",
            "answer": 15
        }
    },
    {
        "id": "BL-IT-S007-V001",
        "metadata": {
            "name": "尾递归阶乘",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "tail_recursive_factorial",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following tail recursive factorial function called with factorial_tail(5, 1), what is the return value?",
            "code": "int factorial_tail(int n, int acc) {\n    if (n <= 1) {\n        return acc;\n    }\n    return factorial_tail(n - 1, n * acc);\n}\n\nint result = factorial_tail(5, 1);\nprintf(\"Result: %d\\n\", result);",
            "answer": 120
        }
    },
    {
        "id": "BL-IT-S007-V002",
        "metadata": {
            "name": "斐波那契递归",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "fibonacci_recursive",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 9
        },
        "task": {
            "description": "Given the following recursive Fibonacci function called with fibonacci(6), what is the return value?",
            "code": "int fibonacci(int n) {\n    if (n <= 1) {\n        return n;\n    }\n    return fibonacci(n - 1) + fibonacci(n - 2);\n}\n\nint result = fibonacci(6);\nprintf(\"Result: %d\\n\", result);",
            "answer": 8
        }
    },
    {
        "id": "BL-IT-S007-V003",
        "metadata": {
            "name": "递归幂运算",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "recursive_power",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following recursive power function called with power(2, 3), what is the return value?",
            "code": "int power(int base, int exp) {\n    if (exp == 0) {\n        return 1;\n    }\n    return base * power(base, exp - 1);\n}\n\nint result = power(2, 3);\nprintf(\"Result: %d\\n\", result);",
            "answer": 8
        }
    },
    {
        "id": "BL-IT-S007-V004",
        "metadata": {
            "name": "递归数组求和",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "recursive_array_sum",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following recursive array sum function called with array [1,2,3,4,5] and size 5, what is the return value?",
            "code": "int array_sum(int arr[], int size) {\n    if (size == 0) {\n        return 0;\n    }\n    return arr[size - 1] + array_sum(arr, size - 1);\n}\n\nint arr[] = {1, 2, 3, 4, 5};\nint result = array_sum(arr, 5);\nprintf(\"Result: %d\\n\", result);",
            "answer": 15
        }
    },
    {
        "id": "BL-IT-S007-V005",
        "metadata": {
            "name": "递归最大公约数",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "recursive_gcd",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following recursive GCD function called with gcd(48, 18), what is the return value?",
            "code": "int gcd(int a, int b) {\n    if (b == 0) {\n        return a;\n    }\n    return gcd(b, a % b);\n}\n\nint result = gcd(48, 18);\nprintf(\"Result: %d\\n\", result);",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S007-V006",
        "metadata": {
            "name": "递归数字反转",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "recursive_number_reverse",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following recursive number reversal function called with reverse(1234, 0), what is the return value?",
            "code": "int reverse(int num, int rev) {\n    if (num == 0) {\n        return rev;\n    }\n    return reverse(num / 10, rev * 10 + num % 10);\n}\n\nint result = reverse(1234, 0);\nprintf(\"Result: %d\\n\", result);",
            "answer": 4321
        }
    },
    {
        "id": "BL-IT-S007-V007",
        "metadata": {
            "name": "递归数字位数",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "recursive_digit_count",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following recursive digit counting function called with count_digits(1234), what is the return value?",
            "code": "int count_digits(int num) {\n    if (num == 0) {\n        return 0;\n    }\n    return 1 + count_digits(num / 10);\n}\n\nint result = count_digits(1234);\nprintf(\"Result: %d\\n\", result);",
            "answer": 4
        }
    },
    {
        "id": "BL-IT-S007-V008",
        "metadata": {
            "name": "递归回文检查",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "recursive_palindrome",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following recursive palindrome check function called with is_palindrome(\"racecar\", 0, 6), what is the return value?",
            "code": "int is_palindrome(char str[], int start, int end) {\n    if (start >= end) {\n        return 1;\n    }\n    if (str[start] != str[end]) {\n        return 0;\n    }\n    return is_palindrome(str, start + 1, end - 1);\n}\n\nchar str[] = \"racecar\";\nint result = is_palindrome(str, 0, 6);\nprintf(\"Result: %d\\n\", result);",
            "answer": 1
        }
    },
    {
        "id": "BL-IT-S007-V009",
        "metadata": {
            "name": "递归二进制转换",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "recursive_binary",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following recursive binary conversion function called with count_binary_ones(13), what is the return value?",
            "code": "int count_binary_ones(int num) {\n    if (num == 0) {\n        return 0;\n    }\n    return (num & 1) + count_binary_ones(num >> 1);\n}\n\nint result = count_binary_ones(13);\nprintf(\"Result: %d\\n\", result);",
            "answer": 3
        }
    },
    {
        "id": "BL-IT-S007-V010",
        "metadata": {
            "name": "相互递归函数",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "mutual_recursion",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following mutually recursive functions called with is_even(6), what is the return value?",
            "code": "int is_odd(int n);\nint is_even(int n) {\n    if (n == 0) return 1;\n    return is_odd(n - 1);\n}\nint is_odd(int n) {\n    if (n == 0) return 0;\n    return is_even(n - 1);\n}\n\nint result = is_even(6);\nprintf(\"Result: %d\\n\", result);",
            "answer": 1
        }
    },
    {
        "id": "BL-IT-S007-V011",
        "metadata": {
            "name": "递归汉诺塔",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "recursive_hanoi",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 7
        },
        "task": {
            "description": "Given the following recursive Hanoi tower function counting moves for hanoi(3), what is the return value?",
            "code": "int hanoi(int n) {\n    if (n == 1) {\n        return 1;\n    }\n    return 2 * hanoi(n - 1) + 1;\n}\n\nint result = hanoi(3);\nprintf(\"Result: %d\\n\", result);",
            "answer": 7
        }
    },
    {
        "id": "BL-IT-S007-V012",
        "metadata": {
            "name": "递归字符串长度",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "recursive_string_length",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following recursive string length function called with str_length(\"Hello\"), what is the return value?",
            "code": "int str_length(char str[]) {\n    if (str[0] == '\\0') {\n        return 0;\n    }\n    return 1 + str_length(str + 1);\n}\n\nchar str[] = \"Hello\";\nint result = str_length(str);\nprintf(\"Result: %d\\n\", result);",
            "answer": 5
        }
    },
    {
        "id": "BL-IT-S007-V013",
        "metadata": {
            "name": "递归树形结构",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "recursive_tree_sum",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 3
        },
        "task": {
            "description": "Given the following recursive tree sum function, what is the return value for a tree with root value 5 and children 2 and 3?",
            "code": "typedef struct Node {\n    int value;\n    struct Node* left;\n    struct Node* right;\n} Node;\n\nint tree_sum(Node* node) {\n    if (node == NULL) {\n        return 0;\n    }\n    return node->value + tree_sum(node->left) + tree_sum(node->right);\n}\n\n// Tree: root(5) -> left(2), right(3)\nNode left = {2, NULL, NULL};\nNode right = {3, NULL, NULL};\nNode root = {5, &left, &right};\nint result = tree_sum(&root);",
            "answer": 10
        }
    },
    {
        "id": "BL-IT-S007-V014",
        "metadata": {
            "name": "递归快速排序分区",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "recursive_quicksort_partition",
            "loop_pattern": "recursive",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following recursive partition count function called with count_partition([3,1,4,1,5], 5, 3), what is the return value?",
            "code": "int count_partition(int arr[], int size, int pivot) {\n    if (size == 0) {\n        return 0;\n    }\n    int count = (arr[0] <= pivot) ? 1 : 0;\n    return count + count_partition(arr + 1, size - 1, pivot);\n}\n\nint arr[] = {3, 1, 4, 1, 5};\nint result = count_partition(arr, 5, 3);\nprintf(\"Result: %d\\n\", result);",
            "answer": 3
        }
    },
    {
        "id": "BL-IT-S008-V001",
        "metadata": {
            "name": "多重累积过滤器",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "multi_accumulator_filter",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 10
        },
        "task": {
            "description": "Given the following complex iterative accumulation with multiple filters, what is the final value of total_score?",
            "code": "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ntotal_score = 0\nbonus_multiplier = 1\npenalty = 0\n\nfor num in numbers:\n    if num % 2 == 0:\n        total_score += num * bonus_multiplier\n        bonus_multiplier += 0.5\n    elif num % 3 == 0:\n        total_score += num * 2\n        penalty += 1\n    else:\n        total_score -= penalty\n        \nprint(f\"Total Score: {total_score}\")",
            "answer": 51.0
        }
    },
    {
        "id": "BL-IT-S008-V002",
        "metadata": {
            "name": "状态机累积器",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "state_machine_accumulator",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following state machine accumulation, what is the final value of result?",
            "code": "data = [1, 3, 2, 4, 1, 5, 2, 3]\nresult = 0\nstate = 'ADD'\nthreshold = 3\n\nfor value in data:\n    if state == 'ADD':\n        result += value\n        if value >= threshold:\n            state = 'MULTIPLY'\n    elif state == 'MULTIPLY':\n        result *= value\n        if value < threshold:\n            state = 'SUBTRACT'\n    elif state == 'SUBTRACT':\n        result -= value\n        if value >= threshold:\n            state = 'ADD'\n            \nprint(f\"Result: {result}\")",
            "answer": 26
        }
    },
    {
        "id": "BL-IT-S008-V003",
        "metadata": {
            "name": "动态阈值累积",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "dynamic_threshold",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following dynamic threshold accumulation, what is the final value of sum?",
            "code": "values = [10, 5, 15, 8, 20, 3]\nsum = 0\nthreshold = 7\nadjustment = 2\n\nfor i, value in enumerate(values):\n    if value > threshold:\n        sum += value\n        threshold += adjustment\n    else:\n        sum -= value\n        threshold = max(1, threshold - adjustment)\n        \nprint(f\"Sum: {sum}\")",
            "answer": 19
        }
    },
    {
        "id": "BL-IT-S008-V004",
        "metadata": {
            "name": "窗口滑动累积",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "sliding_window",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following sliding window accumulation with window size 3, what is the final value of max_sum?",
            "code": "numbers = [1, 4, 2, 5, 3, 8, 1, 6]\nmax_sum = 0\nwindow_size = 3\n\nfor i in range(len(numbers) - window_size + 1):\n    current_sum = 0\n    for j in range(window_size):\n        current_sum += numbers[i + j]\n    max_sum = max(max_sum, current_sum)\n    \nprint(f\"Max Sum: {max_sum}\")",
            "answer": 16
        }
    },
    {
        "id": "BL-IT-S008-V005",
        "metadata": {
            "name": "优先级权重累积",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "priority_weighted",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following priority weighted accumulation, what is the final value of weighted_sum?",
            "code": "items = [(10, 1), (5, 3), (15, 2), (8, 1), (12, 4), (6, 2)]\nweighted_sum = 0\nbonus_threshold = 10\n\nfor value, priority in items:\n    weight = priority * 2 if value >= bonus_threshold else priority\n    weighted_sum += value * weight\n    \nprint(f\"Weighted Sum: {weighted_sum}\")",
            "answer": 258
        }
    },
    {
        "id": "BL-IT-S008-V006",
        "metadata": {
            "name": "条件分支累积器",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "conditional_branching",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 7
        },
        "task": {
            "description": "Given the following conditional branching accumulation, what is the final value of result?",
            "code": "sequence = [2, 7, 1, 9, 4, 6, 3]\nresult = 100\noperations = 0\n\nfor num in sequence:\n    if num < 5:\n        if operations % 2 == 0:\n            result += num * 3\n        else:\n            result -= num\n    else:\n        result = result // 2 + num\n    operations += 1\n    \nprint(f\"Result: {result}\")",
            "answer": 22
        }
    },
    {
        "id": "BL-IT-S008-V007",
        "metadata": {
            "name": "累积历史追踪",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "history_tracking",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following accumulation with history tracking, what is the final value of current?",
            "code": "values = [3, 8, 2, 5, 7]\ncurrent = 0\nhistory = []\nmax_history = 3\n\nfor value in values:\n    current += value\n    history.append(current)\n    if len(history) > max_history:\n        history.pop(0)\n    if len(history) == max_history:\n        avg = sum(history) / len(history)\n        if current > avg:\n            current = int(avg)\n            \nprint(f\"Current: {current}\")",
            "answer": 16
        }
    },
    {
        "id": "BL-IT-S008-V008",
        "metadata": {
            "name": "指数衰减累积",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "exponential_decay",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 4
        },
        "task": {
            "description": "Given the following exponential decay accumulation, what is the final value of total (rounded to nearest integer)?",
            "code": "inputs = [10, 20, 15, 25]\ntotal = 0\ndecay_factor = 0.8\nweight = 1.0\n\nfor value in inputs:\n    total += value * weight\n    weight *= decay_factor\n    \nprint(f\"Total: {round(total)}\")",
            "answer": 46
        }
    },
    {
        "id": "BL-IT-S008-V009",
        "metadata": {
            "name": "条件重置累积器",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "conditional_reset",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following conditional reset accumulation, what is the final value of accumulator?",
            "code": "data = [3, 7, 2, 9, 1, 8, 4, 6]\naccumulator = 0\nreset_threshold = 15\nmax_value = 0\n\nfor value in data:\n    accumulator += value\n    max_value = max(max_value, value)\n    if accumulator >= reset_threshold:\n        accumulator = max_value\n        max_value = 0\n        \nprint(f\"Accumulator: {accumulator}\")",
            "answer": 6
        }
    },
    {
        "id": "BL-IT-S008-V010",
        "metadata": {
            "name": "多阶段处理器",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "multi_stage_processor",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following multi-stage processing, what is the final value of output?",
            "code": "inputs = [4, 9, 2, 7, 1, 5]\noutput = 0\nstage = 1\nstage_counter = 0\n\nfor value in inputs:\n    if stage == 1:\n        output += value * 2\n    elif stage == 2:\n        output = output * value // 10\n    elif stage == 3:\n        output -= value\n    \n    stage_counter += 1\n    if stage_counter >= 2:\n        stage = (stage % 3) + 1\n        stage_counter = 0\n        \nprint(f\"Output: {output}\")",
            "answer": 8
        }
    },
    {
        "id": "BL-IT-S008-V011",
        "metadata": {
            "name": "反馈控制累积",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "feedback_control",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 5
        },
        "task": {
            "description": "Given the following feedback control accumulation, what is the final value of output?",
            "code": "setpoints = [10, 15, 8, 20, 12]\noutput = 5\nerror_sum = 0\nkp, ki = 0.5, 0.1\n\nfor setpoint in setpoints:\n    error = setpoint - output\n    error_sum += error\n    control = kp * error + ki * error_sum\n    output += control\n    output = max(0, min(25, output))  # clamp between 0 and 25\n    \nprint(f\"Output: {round(output, 1)}\")",
            "answer": 16.4
        }
    },
    {
        "id": "BL-IT-S008-V012",
        "metadata": {
            "name": "分组统计累积",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "grouped_statistics",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 8
        },
        "task": {
            "description": "Given the following grouped statistics accumulation, what is the final value of max_group_sum?",
            "code": "values = [3, 1, 4, 1, 5, 9, 2, 6]\ngroups = [0, 1, 0, 1, 0, 1, 0, 1]\ngroup_sums = [0, 0]\nmax_group_sum = 0\n\nfor i, value in enumerate(values):\n    group = groups[i]\n    group_sums[group] += value\n    max_group_sum = max(max_group_sum, group_sums[group])\n    \nprint(f\"Max Group Sum: {max_group_sum}\")",
            "answer": 17
        }
    },
    {
        "id": "BL-IT-S008-V013",
        "metadata": {
            "name": "时间序列窗口",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "time_series_window",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 7
        },
        "task": {
            "description": "Given the following time series window processing, what is the final value of trend_score?",
            "code": "prices = [100, 105, 98, 110, 95, 115, 102]\ntrend_score = 0\nwindow = []\nwindow_size = 3\n\nfor price in prices:\n    window.append(price)\n    if len(window) > window_size:\n        window.pop(0)\n    \n    if len(window) == window_size:\n        if window[2] > window[0]:  # current > first\n            trend_score += 1\n        elif window[2] < window[0]:\n            trend_score -= 1\n            \nprint(f\"Trend Score: {trend_score}\")",
            "answer": 0
        }
    },
    {
        "id": "BL-IT-S008-V014",
        "metadata": {
            "name": "自适应权重累积",
            "category": "Block-Level",
            "subcategory": "Iterative",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "adaptive_weight",
            "loop_pattern": "for",
            "nesting_depth": 1,
            "iteration_count": 6
        },
        "task": {
            "description": "Given the following adaptive weight accumulation, what is the final value of weighted_avg (rounded to 1 decimal)?",
            "code": "measurements = [8.5, 7.2, 9.1, 6.8, 8.9, 7.5]\nweighted_avg = measurements[0]\nweight = 0.3\nadaptation_rate = 0.05\n\nfor i in range(1, len(measurements)):\n    error = abs(measurements[i] - weighted_avg)\n    if error > 1.0:\n        weight = min(0.8, weight + adaptation_rate)\n    else:\n        weight = max(0.1, weight - adaptation_rate)\n    \n    weighted_avg = weight * measurements[i] + (1 - weight) * weighted_avg\n    \nprint(f\"Weighted Avg: {round(weighted_avg, 1)}\")",
            "answer": 7.9
        }
    }
]
```

#### 2D - 大混合（43）

> ```
> # 代码块级推理混合变式生成提示词
> 
> ## 任务目标
> 基于给定的代码块级推理种子任务，生成融合多种代码块类型的综合变式任务，全面测试大模型对线性代码块、条件代码块和迭代代码块等多种代码块结构的综合理解和交叉应用能力。
> 
> ## 核心设计理念
> 不局限于单一代码块类型，而是创造包含多种代码块推理元素的复合场景，测试模型在复杂代码块环境下的综合推理能力，模拟真实编程中常见的混合代码结构。
> 
> ## 混合变式生成维度
> 
> ### 1. 线性与条件混合变式
> - **顺序+条件分支**: 线性语句序列后跟条件判断
> - **条件+顺序执行**: 条件分支内包含线性语句序列
> - **交替混合**: 线性语句与条件语句交替出现
> - **依赖条件**: 线性语句的结果影响后续条件判断
> - **条件赋值**: 条件分支中的变量赋值影响后续线性计算
> - **多路径线性**: 不同条件分支包含不同的线性语句序列
> 
> ### 2. 线性与迭代混合变式
> - **循环前初始化**: 线性代码为循环做准备和初始化
> - **循环后处理**: 循环结束后的线性代码处理结果
> - **循环内线性**: 循环体内包含线性语句序列
> - **嵌套计算**: 线性计算结果作为循环参数
> - **累积线性**: 循环的累积结果用于后续线性计算
> - **状态传递**: 线性代码与循环之间的状态传递
> 
> ### 3. 条件与迭代混合变式
> - **条件控制循环**: 条件判断决定循环的执行与否
> - **循环内条件**: 循环体内包含条件分支逻辑
> - **条件终止**: 复杂条件表达式控制循环终止
> - **分支循环**: 不同条件分支包含不同的循环结构
> - **循环条件更新**: 循环过程中更新条件判断的变量
> - **条件递归**: 条件判断与递归调用的结合
> 
> ### 4. 三重混合变式
> - **线性+条件+迭代**: 三种代码块类型的完整结合
> - **嵌套三重混合**: 在循环内包含条件和线性代码
> - **序列三重混合**: 三种类型按序列顺序组合
> - **交错三重混合**: 三种类型交错穿插出现
> - **递归三重混合**: 递归函数内包含条件和线性代码
> - **复杂状态管理**: 三种类型共同管理复杂程序状态
> 
> ### 5. 控制流复杂混合变式
> - **跳转与分支**: break/continue与条件分支的组合
> - **异常与循环**: 异常处理与迭代结构的结合
> - **返回与条件**: 函数返回与条件判断的混合
> - **goto与结构**: goto跳转与结构化代码的混合
> - **多层跳出**: 从深层嵌套结构的复杂跳出
> - **状态机模式**: 使用混合结构实现状态机
> 
> ### 6. 数据流复杂混合变式
> - **多源数据流**: 多个数据源通过不同代码块汇聚
> - **分流处理**: 一个数据源分流到不同的处理路径
> - **循环依赖**: 不同代码块间形成数据依赖循环
> - **状态累积**: 跨多种代码块的状态累积过程
> - **数据变换管道**: 数据经过多种代码块的变换处理
> - **反馈循环**: 输出结果反馈影响前面的处理逻辑
> 
> ### 7. 内存与资源混合变式
> - **资源分配+条件+释放**: 资源管理的完整生命周期
> - **循环内存管理**: 循环中的动态内存分配和释放
> - **条件资源分配**: 基于条件的选择性资源分配
> - **递归资源累积**: 递归调用中的资源累积管理
> - **内存泄漏检测**: 复杂控制流中的内存泄漏问题
> - **资源共享**: 多个代码块间的资源共享和竞争
> 
> ### 8. 错误处理混合变式
> - **多层错误处理**: 不同代码块层次的错误处理
> - **错误传播**: 错误在混合代码结构中的传播
> - **恢复策略**: 错误发生后的恢复和继续执行
> - **资源清理**: 异常情况下的资源清理
> - **状态一致性**: 错误处理中的状态一致性维护
> - **回滚机制**: 复杂操作的事务性回滚
> 
> ### 9. 算法模式混合变式
> - **搜索算法**: 结合线性、条件、迭代的搜索实现
> - **排序算法**: 复杂排序算法的混合代码结构
> - **图算法**: 图遍历和处理的混合代码实现
> - **动态规划**: DP算法的混合代码结构
> - **分治算法**: 分治策略的递归和条件混合
> - **贪心算法**: 贪心选择的条件和迭代混合
> 
> ### 10. 性能与优化混合变式
> - **分支预测**: 条件分支对性能的影响
> - **循环展开**: 循环优化与线性代码的关系
> - **缓存友好**: 数据访问模式的性能考虑
> - **并行化**: 混合代码结构的并行化可能
> - **编译器优化**: 编译器对混合结构的优化
> - **热点路径**: 性能关键路径的识别和优化
> 
> ## 复杂度层次设计
> 
> ### 简单混合 (Easy)
> - 2种代码块类型的基础组合
> - 清晰的执行顺序和数据流
> - 简单的控制流和状态管理
> - 直观的逻辑组合
> 
> ### 中等混合 (Medium)
> - 2-3种代码块类型的中度组合
> - 包含嵌套结构或中等复杂的控制流
> - 涉及状态传递和简单的错误处理
> - 需要仔细分析执行路径
> 
> ### 复杂混合 (Hard)
> - 3种代码块类型的深度融合
> - 复杂的嵌套和控制流结构
> - 多层次的状态管理和错误处理
> - 涉及算法实现或资源管理
> 
> ### 专家级混合 (Expert)
> - 极度复杂的多类型深度嵌套
> - 涉及高级算法和性能优化
> - 复杂的并发和同步处理
> - 需要专业级别的代码理解能力
> 
> ## 生成策略
> 
> ### 种子分析策略
> 1. **识别主导类型**: 分析种子任务的主要代码块类型(A/B/C)
> 2. **提取核心逻辑**: 识别种子中的关键逻辑和计算模式
> 3. **设计融合点**: 确定可以融合其他代码块类型的切入点
> 4. **保持核心复杂度**: 在添加新元素时保持原有难度层次
> 
> ### 变式设计原则
> 1. **渐进式融合**: 从简单混合逐步增加到复杂混合
> 2. **逻辑连贯性**: 确保混合后的代码逻辑清晰且正确
> 3. **现实导向**: 优先设计实际编程中常见的混合模式
> 4. **测试价值**: 每个混合变式都应测试特定的推理能力组合
> 
> ### 质量保证机制
> 1. **执行路径验证**: 验证所有可能执行路径的正确性
> 2. **状态一致性检查**: 确保程序状态的一致性维护
> 3. **边界条件覆盖**: 包含各种边界和异常情况
> 4. **性能考虑**: 确保代码的合理性和可执行性
> 
> ## 输出格式要求
> 
> ```json
> [
>     {
>         "id": "BL-MIX-S00X-V001",
>         "metadata": {
>             "name": "混合代码块变式名称",
>             "category": "Block-Level",
>             "subcategory": "Mixed",
>             "type": "variant",
>             "source": "Generated",
>             "language": "目标语言",
>             "difficulty": "easy/medium/hard/expert",
>             "intervention": 0,
>             "variant_type": "混合模式标签",
>             "mixed_blocks": ["Linear", "Conditional", "Iterative"],
>             "primary_pattern": "主导的代码块模式",
>             "complexity_factors": ["控制流", "状态管理", "错误处理"]
>         },
>         "task": {
>             "description": "混合代码块推理任务描述",
>             "code": "包含多种代码块类型的复合代码",
>             "answer": "执行完成后的最终结果"
>         }
>     },
>     {下一个变式...}
> ]
> 特殊字段说明
> mixed_blocks: 标识该变式包含的代码块类型组合
> primary_pattern: 标识主导的代码块模式
> complexity_factors: 标识增加复杂度的关键因素
> 生成目标
> 总共生成80-100个变式
> 
> 每种难度等级至少包含4-5个变式
> 涵盖至少10-12种不同的混合模式
> 包含2-3个跨语言的混合变式
> 至少包含5-6个三重混合的复杂案例
> 包含不同复杂度因素的变式组合
> 重点测试场景
> 执行路径分析: 在复杂混合结构中正确分析执行路径
> 状态跟踪能力: 跨多种代码块准确跟踪程序状态
> 控制流理解: 对复杂控制流的正确理解和预测
> 边界条件处理: 在混合结构中正确处理边界情况
> 错误传播理解: 理解错误在混合结构中的传播机制
> 性能影响分析: 理解不同混合模式对性能的影响
> 常见混合模式示例
> 初始化+循环+判断: 经典的算法实现模式
> 条件+递归+累积: 树形算法的常见结构
> 循环+嵌套条件+状态更新: 状态机实现模式
> 线性预处理+复杂循环+结果处理: 数据处理管道
> 多层条件+循环+异常处理: 健壮性代码模式
> 递归+条件终止+状态回溯: 回溯算法模式
> 请基于此提示词，为给定的代码块级种子任务生成全面的混合变式集合，输出格式为包含所有变式的JSON数组。
> ```
>
> 

```json
[
    {
        "id": "BL-MIX-S001-V001",
        "metadata": {
            "name": "线性初始化+条件验证混合",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "Linear+Conditional",
            "mixed_blocks": ["Linear", "Conditional"],
            "primary_pattern": "Linear",
            "complexity_factors": ["顺序执行", "条件分支"]
        },
        "task": {
            "description": "给定以下线性初始化后接条件验证的代码块，当input为25时，result的最终值是多少？",
            "code": "int input = 25;\nint result = 0;\nint threshold = 20;\nint multiplier = 3;\n\n// 线性初始化\nresult = input * multiplier;\n\n// 条件验证\nif (result > threshold) {\n    result = result + 10;\n} else {\n    result = result - 5;\n}\n\nprintf(\"Result: %d\\n\", result);",
            "answer": 85
        }
    },
    {
        "id": "BL-MIX-S001-V002",
        "metadata": {
            "name": "条件分支内线性计算",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "Conditional+Linear",
            "mixed_blocks": ["Conditional", "Linear"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["条件判断", "线性计算"]
        },
        "task": {
            "description": "给定以下条件分支内包含线性计算的代码块，当score为88时，final_grade的最终值是多少？",
            "code": "score = 88\nbonus_points = 5\npenalty = 2\n\nif score >= 85:\n    # 线性计算序列\n    adjusted_score = score + bonus_points\n    final_grade = adjusted_score * 1.1\n    final_grade = int(final_grade)\nelse:\n    adjusted_score = score - penalty\n    final_grade = adjusted_score * 0.9\n    final_grade = int(final_grade)\n\nprint(f\"Final grade: {final_grade}\")",
            "answer": 102
        }
    },
    {
        "id": "BL-MIX-S001-V003",
        "metadata": {
            "name": "循环前线性准备+循环处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Linear+Iterative",
            "mixed_blocks": ["Linear", "Iterative"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["线性初始化", "循环累积"]
        },
        "task": {
            "description": "给定以下循环前线性准备后接循环处理的代码块，sum的最终值是多少？",
            "code": "// 线性准备阶段\nint base = 10;\nint increment = 3;\nint limit = 5;\nint sum = base;\n\n// 循环处理阶段\nfor (int i = 1; i <= limit; i++) {\n    sum += i * increment;\n}\n\nprintf(\"Sum: %d\\n\", sum);",
            "answer": 55
        }
    },
    {
        "id": "BL-MIX-S001-V004",
        "metadata": {
            "name": "循环内条件控制",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Iterative+Conditional",
            "mixed_blocks": ["Iterative", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["循环控制", "条件分支"]
        },
        "task": {
            "description": "给定以下循环内包含条件控制的代码块，count的最终值是多少？",
            "code": "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ncount = 0\ntotal = 0\n\nfor num in numbers:\n    if num % 2 == 0:\n        total += num\n        count += 1\n    else:\n        total -= num\n        \nprint(f\"Count: {count}, Total: {total}\")",
            "answer": 5
        }
    },
    {
        "id": "BL-MIX-S001-V005",
        "metadata": {
            "name": "三重混合：初始化+条件+循环",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Linear+Conditional+Iterative",
            "mixed_blocks": ["Linear", "Conditional", "Iterative"],
            "primary_pattern": "Mixed",
            "complexity_factors": ["线性初始化", "条件验证", "循环处理"]
        },
        "task": {
            "description": "给定以下包含线性初始化、条件验证和循环处理的三重混合代码块，当input为7时，result的最终值是多少？",
            "code": "int input = 7;\nint result = 0;\nint base = 5;\nint factor = 2;\n\n// 线性初始化\nresult = input + base;\n\n// 条件验证\nif (result > 10) {\n    // 循环处理\n    for (int i = 1; i <= 3; i++) {\n        result *= factor;\n    }\n} else {\n    result = result * 10;\n}\n\nprintf(\"Result: %d\\n\", result);",
            "answer": 96
        }
    },
    {
        "id": "BL-MIX-S001-V006",
        "metadata": {
            "name": "条件依赖的线性计算链",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Conditional+Linear",
            "mixed_blocks": ["Conditional", "Linear"],
            "primary_pattern": "Linear",
            "complexity_factors": ["条件选择", "线性依赖"]
        },
        "task": {
            "description": "给定以下条件依赖的线性计算链，当x为15时，final_value的最终值是多少？",
            "code": "x = 15\nthreshold = 12\n\n# 条件选择基础值\nif x > threshold:\n    base_value = x * 2\nelse:\n    base_value = x + 10\n\n# 线性计算链\nstep1 = base_value + 5\nstep2 = step1 * 1.5\nfinal_value = int(step2 - 3)\n\nprint(f\"Final value: {final_value}\")",
            "answer": 49
        }
    },
    {
        "id": "BL-MIX-S001-V007",
        "metadata": {
            "name": "嵌套循环与条件过滤",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Iterative+Conditional",
            "mixed_blocks": ["Iterative", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["嵌套循环", "条件过滤"]
        },
        "task": {
            "description": "给定以下嵌套循环与条件过滤的代码块，valid_count的最终值是多少？",
            "code": "int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\nint valid_count = 0;\nint threshold = 5;\n\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 3; j++) {\n        if (matrix[i][j] > threshold) {\n            valid_count++;\n        }\n    }\n}\n\nprintf(\"Valid count: %d\\n\", valid_count);",
            "answer": 4
        }
    },
    {
        "id": "BL-MIX-S001-V008",
        "metadata": {
            "name": "循环累积后线性变换",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Iterative+Linear",
            "mixed_blocks": ["Iterative", "Linear"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["循环累积", "线性变换"]
        },
        "task": {
            "description": "给定以下循环累积后线性变换的代码块，final_result的最终值是多少？",
            "code": "data = [2, 4, 6, 8, 10]\naccumulator = 0\n\n# 循环累积\nfor value in data:\n    accumulator += value * 2\n\n# 线性变换\nintermediate = accumulator / 2\nbonus = 15\nfinal_result = int(intermediate + bonus)\n\nprint(f\"Final result: {final_result}\")",
            "answer": 45
        }
    },
    {
        "id": "BL-MIX-S001-V009",
        "metadata": {
            "name": "多条件分支线性处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Conditional+Linear",
            "mixed_blocks": ["Conditional", "Linear"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["多路分支", "线性处理"]
        },
        "task": {
            "description": "给定以下多条件分支线性处理的代码块，当grade为78时，final_score的最终值是多少？",
            "code": "int grade = 78;\nint final_score = 0;\nint bonus = 0;\nint penalty = 0;\n\nif (grade >= 90) {\n    bonus = 20;\n    penalty = 0;\n    final_score = grade + bonus;\n} else if (grade >= 80) {\n    bonus = 10;\n    penalty = 2;\n    final_score = grade + bonus - penalty;\n} else if (grade >= 70) {\n    bonus = 5;\n    penalty = 5;\n    final_score = grade + bonus - penalty;\n} else {\n    bonus = 0;\n    penalty = 10;\n    final_score = grade - penalty;\n}\n\nprintf(\"Final score: %d\\n\", final_score);",
            "answer": 78
        }
    },
    {
        "id": "BL-MIX-S001-V010",
        "metadata": {
            "name": "条件控制循环终止",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Conditional+Iterative",
            "mixed_blocks": ["Conditional", "Iterative"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["条件终止", "循环控制"]
        },
        "task": {
            "description": "给定以下条件控制循环终止的代码块，iterations的最终值是多少？",
            "code": "int value = 100;\nint iterations = 0;\nint threshold = 10;\n\nwhile (value > threshold) {\n    iterations++;\n    value = value / 2;\n    \n    if (iterations >= 5) {\n        break;\n    }\n}\n\nprintf(\"Iterations: %d, Final value: %d\\n\", iterations, value);",
            "answer": 4
        }
    },
    {
        "id": "BL-MIX-S001-V011",
        "metadata": {
            "name": "线性预处理+复杂循环",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Linear+Iterative",
            "mixed_blocks": ["Linear", "Iterative"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["线性预处理", "复杂循环"]
        },
        "task": {
            "description": "给定以下线性预处理+复杂循环的代码块，processed_count的最终值是多少？",
            "code": "# 线性预处理\nraw_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nfilter_threshold = 5\nmultiplier = 2\nadjustment = 3\n\n# 复杂循环处理\nprocessed_count = 0\nsum_processed = 0\n\nfor item in raw_data:\n    if item > filter_threshold:\n        processed_value = item * multiplier + adjustment\n        sum_processed += processed_value\n        processed_count += 1\n\nprint(f\"Processed count: {processed_count}\")",
            "answer": 5
        }
    },
    {
        "id": "BL-MIX-S001-V012",
        "metadata": {
            "name": "递归调用内条件判断",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Iterative+Conditional",
            "mixed_blocks": ["Iterative", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["递归调用", "条件判断"]
        },
        "task": {
            "description": "给定以下递归调用内条件判断的代码块，fibonacci(6)的返回值是多少？",
            "code": "int fibonacci(int n) {\n    // 基础条件\n    if (n <= 1) {\n        return n;\n    }\n    \n    // 条件优化\n    if (n == 2) {\n        return 1;\n    }\n    \n    // 递归调用\n    return fibonacci(n - 1) + fibonacci(n - 2);\n}\n\nint result = fibonacci(6);\nprintf(\"Fibonacci(6): %d\\n\", result);",
            "answer": 8
        }
    },
    {
        "id": "BL-MIX-S001-V013",
        "metadata": {
            "name": "交替线性与条件处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Linear+Conditional",
            "mixed_blocks": ["Linear", "Conditional"],
            "primary_pattern": "Mixed",
            "complexity_factors": ["交替模式", "状态传递"]
        },
        "task": {
            "description": "给定以下交替线性与条件处理的代码块，当input为12时，result的最终值是多少？",
            "code": "input = 12\nresult = input\n\n# 第一次线性处理\nresult = result * 2\n\n# 第一次条件处理\nif result > 20:\n    result = result - 5\nelse:\n    result = result + 3\n\n# 第二次线性处理\nresult = result + 10\n\n# 第二次条件处理\nif result % 2 == 0:\n    result = result / 2\nelse:\n    result = result * 3\n\nprint(f\"Result: {result}\")",
            "answer": 17.0
        }
    },
    {
        "id": "BL-MIX-S001-V014",
        "metadata": {
            "name": "循环内嵌套条件与线性",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Iterative+Conditional+Linear",
            "mixed_blocks": ["Iterative", "Conditional", "Linear"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["循环嵌套", "条件分支", "线性计算"]
        },
        "task": {
            "description": "给定以下循环内嵌套条件与线性的代码块，final_sum的最终值是多少？",
            "code": "int arr[] = {2, 5, 8, 3, 9, 1, 7, 4};\nint size = 8;\nint final_sum = 0;\nint even_multiplier = 3;\nint odd_multiplier = 2;\n\nfor (int i = 0; i < size; i++) {\n    int current = arr[i];\n    \n    // 条件判断\n    if (current % 2 == 0) {\n        // 线性计算（偶数）\n        current = current * even_multiplier;\n        current = current + 1;\n    } else {\n        // 线性计算（奇数）\n        current = current * odd_multiplier;\n        current = current - 1;\n    }\n    \n    final_sum += current;\n}\n\nprintf(\"Final sum: %d\\n\", final_sum);",
            "answer": 119
        }
    },
    {
        "id": "BL-MIX-S001-V015",
        "metadata": {
            "name": "分支选择不同循环",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Conditional+Iterative",
            "mixed_blocks": ["Conditional", "Iterative"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["分支选择", "不同循环"]
        },
        "task": {
            "description": "给定以下分支选择不同循环的代码块，当mode为'fast'时，result的最终值是多少？",
            "code": "mode = 'fast'\ndata = [1, 2, 3, 4, 5]\nresult = 0\n\nif mode == 'slow':\n    # 慢速处理循环\n    for i in range(len(data)):\n        for j in range(i + 1):\n            result += data[j]\nelif mode == 'fast':\n    # 快速处理循环\n    for item in data:\n        result += item * 2\nelse:\n    # 默认处理循环\n    for item in data:\n        result += item\n\nprint(f\"Result: {result}\")",
            "answer": 30
        }
    },
    {
        "id": "BL-MIX-S001-V016",
        "metadata": {
            "name": "状态机模式混合",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Linear+Conditional+Iterative",
            "mixed_blocks": ["Linear", "Conditional", "Iterative"],
            "primary_pattern": "Mixed",
            "complexity_factors": ["状态机", "状态转换", "循环控制"]
        },
        "task": {
            "description": "给定以下状态机模式混合的代码块，当输入字符串为\"ABBC\"时，final_state的最终值是多少？",
            "code": "typedef enum { IDLE = 0, STATE_A = 1, STATE_B = 2, ERROR = -1 } state_t;\n\nstate_t process_string(const char* input) {\n    state_t current_state = IDLE;\n    int position = 0;\n    \n    // 循环处理每个字符\n    while (input[position] != '\\0') {\n        char ch = input[position];\n        \n        // 状态转换条件\n        switch (current_state) {\n            case IDLE:\n                if (ch == 'A') current_state = STATE_A;\n                else current_state = ERROR;\n                break;\n            case STATE_A:\n                if (ch == 'B') current_state = STATE_B;\n                else current_state = ERROR;\n                break;\n            case STATE_B:\n                if (ch == 'B' || ch == 'C') current_state = STATE_B;\n                else current_state = ERROR;\n                break;\n            default:\n                current_state = ERROR;\n        }\n        \n        // 线性递增\n        position++;\n        \n        // 错误检查\n        if (current_state == ERROR) break;\n    }\n    \n    return current_state;\n}\n\nstate_t final_state = process_string(\"ABBC\");\nprintf(\"Final state: %d\\n\", final_state);",
            "answer": 2
        }
    },
    {
        "id": "BL-MIX-S001-V017",
        "metadata": {
            "name": "数据变换管道",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Linear+Conditional+Iterative",
            "mixed_blocks": ["Linear", "Conditional", "Iterative"],
            "primary_pattern": "Linear",
            "complexity_factors": ["数据管道", "多阶段处理"]
        },
        "task": {
            "description": "给定以下数据变换管道的代码块，processed_data的长度是多少？",
            "code": "raw_data = [10, 25, 8, 33, 15, 42, 7, 28]\n\n# 阶段1: 线性预处理\nscale_factor = 1.2\noffset = 5\nstage1_data = [int(x * scale_factor + offset) for x in raw_data]\n\n# 阶段2: 条件过滤\nthreshold = 20\nstage2_data = []\nfor value in stage1_data:\n    if value >= threshold:\n        stage2_data.append(value)\n\n# 阶段3: 循环变换\nprocessed_data = []\nfor i, value in enumerate(stage2_data):\n    if i % 2 == 0:\n        processed_data.append(value * 2)\n    else:\n        processed_data.append(value + 10)\n\nprint(f\"Processed data length: {len(processed_data)}\")",
            "answer": 6
        }
    },
    {
        "id": "BL-MIX-S001-V018",
        "metadata": {
            "name": "嵌套函数调用混合",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Iterative+Conditional+Linear",
            "mixed_blocks": ["Iterative", "Conditional", "Linear"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["函数嵌套", "递归调用", "多重条件"]
        },
        "task": {
            "description": "给定以下嵌套函数调用混合的代码块，calculate_sum(4, 3)的返回值是多少？",
            "code": "int process_value(int x, int depth) {\n    // 线性基础计算\n    int base = x * 2 + 1;\n    \n    // 条件递归\n    if (depth > 0) {\n        return base + process_value(x - 1, depth - 1);\n    } else {\n        return base;\n    }\n}\n\nint calculate_sum(int n, int depth) {\n    int total = 0;\n    \n    // 循环调用\n    for (int i = 1; i <= n; i++) {\n        int partial = process_value(i, depth);\n        total += partial;\n    }\n    \n    return total;\n}\n\nint result = calculate_sum(4, 3);\nprintf(\"Result: %d\\n\", result);",
            "answer": 80
        }
    },
    {
        "id": "BL-MIX-S001-V019",
        "metadata": {
            "name": "资源管理混合模式",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Linear+Conditional+Iterative",
            "mixed_blocks": ["Linear", "Conditional", "Iterative"],
            "primary_pattern": "Mixed",
            "complexity_factors": ["资源分配", "条件释放", "循环管理"]
        },
        "task": {
            "description": "给定以下资源管理混合模式的代码块，当capacity为5时，allocated_count的最终值是多少？",
            "code": "typedef struct {\n    int* ptr;\n    int size;\n    int allocated;\n} resource_t;\n\nint manage_resources(int capacity) {\n    resource_t resources[10];\n    int allocated_count = 0;\n    \n    // 线性初始化\n    for (int i = 0; i < 10; i++) {\n        resources[i].ptr = NULL;\n        resources[i].size = 0;\n        resources[i].allocated = 0;\n    }\n    \n    // 循环分配\n    for (int i = 0; i < capacity && i < 10; i++) {\n        int size = (i + 1) * 16;\n        \n        // 条件分配\n        if (size <= 64) {\n            resources[i].ptr = malloc(size);\n            if (resources[i].ptr != NULL) {\n                resources[i].size = size;\n                resources[i].allocated = 1;\n                allocated_count++;\n            }\n        }\n    }\n    \n    // 条件释放（模拟，实际不释放）\n    for (int i = 0; i < 10; i++) {\n        if (resources[i].allocated && resources[i].size > 32) {\n            // 这里只是计数，不实际释放\n            // free(resources[i].ptr);\n            // allocated_count--;\n        }\n    }\n    \n    return allocated_count;\n}\n\nint result = manage_resources(5);\nprintf(\"Allocated count: %d\\n\", result);",
            "answer": 4
        }
    },
    {
        "id": "BL-MIX-S001-V020",
        "metadata": {
            "name": "多层跳出控制",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Iterative+Conditional",
            "mixed_blocks": ["Iterative", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["多层循环", "跳出控制"]
        },
        "task": {
            "description": "给定以下多层跳出控制的代码块，found_count的最终值是多少？",
            "code": "matrix = [\n    [1, 2, 3, 15],\n    [4, 5, 6, 16],\n    [7, 8, 9, 17],\n    [10, 11, 12, 18]\n]\n\ntarget = 15\nfound_count = 0\nfound = False\n\nfor i in range(len(matrix)):\n    if found:\n        break\n    for j in range(len(matrix[i])):\n        current = matrix[i][j]\n        if current == target:\n            found = True\n            found_count += 1\n            break\n        elif current > 10:\n            found_count += 1\n            \nprint(f\"Found count: {found_count}\")",
            "answer": 4
        }
    },
    {
        "id": "BL-MIX-S002-V001",
        "metadata": {
            "name": "数组处理条件分支",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "Linear+Conditional",
            "mixed_blocks": ["Linear", "Conditional"],
            "primary_pattern": "Linear",
            "complexity_factors": ["数组操作", "条件处理"]
        },
        "task": {
            "description": "基于BL-LN-S002的数组初始化模式，添加条件验证，当size为3时，initialized_count的值是多少？",
            "code": "int size = 3;\nint arr[5] = {0};\nint initialized_count = 0;\nint default_value = -1;\n\n// 线性初始化\nfor (int i = 0; i < 5; i++) {\n    arr[i] = default_value;\n}\n\n// 条件验证和计数\nif (size > 0 && size <= 5) {\n    for (int i = 0; i < size; i++) {\n        if (arr[i] == default_value) {\n            initialized_count++;\n        }\n    }\n}\n\nprintf(\"Initialized count: %d\\n\", initialized_count);",
            "answer": 3
        }
    },
    {
        "id": "BL-MIX-S002-V002",
        "metadata": {
            "name": "独立配置验证组合",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Linear+Conditional+Iterative",
            "mixed_blocks": ["Linear", "Conditional", "Iterative"],
            "primary_pattern": "Linear",
            "complexity_factors": ["配置管理", "验证循环"]
        },
        "task": {
            "description": "基于BL-LN-S002的独立配置模式，添加循环验证，valid_configs的最终值是多少？",
            "code": "# 线性配置设置（类似原始种子）\nmax_retries = 3\ntimeout_seconds = 30.0\nlog_level = 'INFO'\nis_debug = False\ndefault_encoding = 'utf-8'\n\n# 配置验证循环\nconfigs = {\n    'max_retries': max_retries,\n    'timeout_seconds': timeout_seconds,\n    'log_level': log_level,\n    'is_debug': is_debug,\n    'default_encoding': default_encoding\n}\n\nvalid_configs = 0\nfor key, value in configs.items():\n    # 条件验证每个配置\n    if key == 'max_retries' and isinstance(value, int) and value > 0:\n        valid_configs += 1\n    elif key == 'timeout_seconds' and isinstance(value, float) and value > 0:\n        valid_configs += 1\n    elif key == 'log_level' and value in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:\n        valid_configs += 1\n    elif key == 'is_debug' and isinstance(value, bool):\n        valid_configs += 1\n    elif key == 'default_encoding' and isinstance(value, str) and len(value) > 0:\n        valid_configs += 1\n\nprint(f\"Valid configs: {valid_configs}\")",
            "answer": 5
        }
    },
    {
        "id": "BL-MIX-S003-V001",
        "metadata": {
            "name": "文件处理循环扩展",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Linear+Conditional+Iterative",
            "mixed_blocks": ["Linear", "Conditional", "Iterative"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["文件处理", "循环扩展", "错误处理"]
        },
        "task": {
            "description": "基于BL-LN-S003的文件处理模式，添加批量处理循环，当文件数量为4且2个成功时，success_count的值是多少？",
            "code": "// 模拟文件处理结果\nint file_results[] = {0, -1, 0, -1}; // 0表示成功，-1表示失败\nint file_count = 4;\n\nint process_files_batch(int* results, int count) {\n    int success_count = 0;\n    int total_processed = 0;\n    \n    // 循环处理每个文件\n    for (int i = 0; i < count; i++) {\n        // 线性计数\n        total_processed++;\n        \n        // 条件判断处理结果（基于原始逻辑）\n        int rc = results[i];\n        if (rc == 0) {  // 模拟 blkid_do_safeprobe 返回 0\n            success_count++;\n        }\n        \n        // 可选的错误处理\n        if (rc == -1 && success_count == 0 && i > count/2) {\n            // 如果一半以上失败且没有成功，提前退出\n            break;\n        }\n    }\n    \n    return success_count;\n}\n\nint result = process_files_batch(file_results, file_count);\nprintf(\"Success count: %d\\n\", result);",
            "answer": 2
        }
    },
    {
        "id": "BL-MIX-S004-V001",
        "metadata": {
            "name": "计算链条件优化",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Linear+Conditional",
            "mixed_blocks": ["Linear", "Conditional"],
            "primary_pattern": "Linear",
            "complexity_factors": ["计算链", "条件优化"]
        },
        "task": {
            "description": "基于BL-LN-S004的计算链模式，添加条件优化，当base为15时，optimized_result的最终值是多少？",
            "code": "base = 15\nmultiplier = 3\noffset = 5\n\n# 原始计算链\ntemp = base * multiplier\nresult = temp + offset\n\n# 条件优化\nif result > 40:\n    # 高值优化\n    optimized_result = result * 0.9  # 降低10%\nelif result > 20:\n    # 中值优化\n    optimized_result = result * 1.1  # 增加10%\nelse:\n    # 低值保持\n    optimized_result = result\n\noptimized_result = int(optimized_result)\nprint(f\"Optimized result: {optimized_result}\")",
            "answer": 49
        }
    },
    {
        "id": "BL-MIX-S004-V002",
        "metadata": {
            "name": "多链并行计算",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Linear+Iterative",
            "mixed_blocks": ["Linear", "Iterative"],
            "primary_pattern": "Linear",
            "complexity_factors": ["并行计算", "多链处理"]
        },
        "task": {
            "description": "基于BL-LN-S004的计算链，扩展为多链并行计算，max_result的最终值是多少？",
            "code": "# 多个计算链的基础参数\nchains = [\n    {'base': 10, 'multiplier': 3, 'offset': 5},\n    {'base': 8, 'multiplier': 4, 'offset': 2},\n    {'base': 12, 'multiplier': 2, 'offset': 8},\n    {'base': 6, 'multiplier': 5, 'offset': 3}\n]\n\nresults = []\nmax_result = 0\n\n# 循环处理每个计算链\nfor chain in chains:\n    # 线性计算链（类似原始模式）\n    temp = chain['base'] * chain['multiplier']\n    result = temp + chain['offset']\n    results.append(result)\n    \n    # 跟踪最大值\n    if result > max_result:\n        max_result = result\n\nprint(f\"Max result: {max_result}\")",
            "answer": 35
        }
    },
    {
        "id": "BL-MIX-S005-V001",
        "metadata": {
            "name": "累积计算条件分支",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Linear+Conditional",
            "mixed_blocks": ["Linear", "Conditional"],
            "primary_pattern": "Linear",
            "complexity_factors": ["累积计算", "条件分支"]
        },
        "task": {
            "description": "基于BL-LN-S005的累积模式，添加条件分支，当threshold为50时，final_total的值是多少？",
            "code": "int total = 0;\nint threshold = 50;\nint bonus = 20;\nint penalty = 10;\n\n// 原始累积过程\ntotal += 10;\ntotal += 15;\ntotal += 7;\ntotal *= 2;\n\n// 条件分支处理\nif (total >= threshold) {\n    // 达到阈值，获得奖励\n    int final_total = total + bonus;\n    printf(\"Final total with bonus: %d\\n\", final_total);\n} else {\n    // 未达阈值，扣除惩罚\n    int final_total = total - penalty;\n    printf(\"Final total with penalty: %d\\n\", final_total);\n}",
            "answer": 84
        }
    },
    {
        "id": "BL-MIX-S006-V001",
        "metadata": {
            "name": "屏幕初始化循环验证",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Linear+Iterative+Conditional",
            "mixed_blocks": ["Linear", "Iterative", "Conditional"],
            "primary_pattern": "Linear",
            "complexity_factors": ["初始化循环", "验证检查"]
        },
        "task": {
            "description": "基于BL-LN-S006的屏幕初始化，添加多屏幕循环初始化和验证，当screen_count为3时，valid_screens的值是多少？",
            "code": "typedef struct {\n    void* grid;\n    void* saved_grid;\n    int cstyle;\n    int default_cstyle;\n    int ccolour;\n    int default_ccolour;\n    int initialized;\n} screen_t;\n\nint init_multiple_screens(int screen_count) {\n    screen_t screens[5];\n    int valid_screens = 0;\n    \n    // 循环初始化多个屏幕\n    for (int i = 0; i < screen_count && i < 5; i++) {\n        // 线性初始化（基于原始模式）\n        screens[i].grid = malloc(100); // 模拟 grid_create\n        screens[i].saved_grid = NULL;\n        screens[i].cstyle = 0; // SCREEN_CURSOR_DEFAULT\n        screens[i].default_cstyle = 0;\n        screens[i].ccolour = -1;\n        screens[i].default_ccolour = -1;\n        screens[i].initialized = 1;\n        \n        // 条件验证\n        if (screens[i].grid != NULL && screens[i].ccolour == -1) {\n            valid_screens++;\n        }\n    }\n    \n    return valid_screens;\n}\n\nint result = init_multiple_screens(3);\nprintf(\"Valid screens: %d\\n\", result);",
            "answer": 3
        }
    },
    {
        "id": "BL-MIX-CD001-V001",
        "metadata": {
            "name": "页面大小检查循环扩展",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Conditional+Iterative",
            "mixed_blocks": ["Conditional", "Iterative"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["系统调用", "循环检查"]
        },
        "task": {
            "description": "基于BL-CD-S001的页面大小检查，扩展为多次尝试循环，当尝试3次且第2次成功返回4096时，final_size的值是多少？",
            "code": "#define DEFAULT_MEM_ALIGNMENT 1024\n\nsize_t get_pagesize_with_retry(int max_attempts) {\n    size_t final_size = 0;\n    long results[] = {-1, 4096, 8192}; // 模拟多次 sysconf 调用结果\n    \n    // 循环尝试获取页面大小\n    for (int attempt = 0; attempt < max_attempts; attempt++) {\n        long r = results[attempt];\n        \n        // 原始条件逻辑\n        if (r <= 0) {\n            final_size = DEFAULT_MEM_ALIGNMENT;\n        } else {\n            final_size = (size_t)r;\n            break; // 成功获取，跳出循环\n        }\n    }\n    \n    return final_size;\n}\n\nsize_t result = get_pagesize_with_retry(3);\nprintf(\"Final size: %zu\\n\", result);",
            "answer": 4096
        }
    },
    {
        "id": "BL-MIX-CD002-V001",
        "metadata": {
            "name": "成绩评级批量处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Conditional+Iterative+Linear",
            "mixed_blocks": ["Conditional", "Iterative", "Linear"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["嵌套条件", "批量处理", "统计计算"]
        },
        "task": {
            "description": "基于BL-CD-S002的嵌套条件评级，扩展为批量处理多个学生成绩，A_grade_count的最终值是多少？",
            "code": "scores = [92, 97, 85, 88, 76, 94, 83]\ngrade_counts = {'A+': 0, 'A': 0, 'B': 0, 'C': 0}\nA_grade_count = 0  # A+ 和 A 的总数\n\n# 循环处理每个学生的成绩\nfor score in scores:\n    grade = None\n    \n    # 嵌套条件逻辑（基于原始模式）\n    if score >= 90:\n        if score >= 95:\n            grade = 'A+'\n        else:\n            grade = 'A'\n    else:\n        if score >= 80:\n            grade = 'B'\n        else:\n            grade = 'C'\n    \n    # 线性统计\n    grade_counts[grade] += 1\n    if grade in ['A+', 'A']:\n        A_grade_count += 1\n\nprint(f\"A grade count (A+ and A): {A_grade_count}\")",
            "answer": 4
        }
    },
    {
        "id": "BL-MIX-CD003-V001",
        "metadata": {
            "name": "动态分类系统",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Conditional+Linear+Iterative",
            "mixed_blocks": ["Conditional", "Linear", "Iterative"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["动态阈值", "分类统计"]
        },
        "task": {
            "description": "基于BL-CD-S003的else-if链分类，扩展为动态阈值系统，当values数组有5个元素时，medium_count的值是多少？",
            "code": "int values[] = {5, 15, 25, 35, 8};\nint count = 5;\nint low_threshold = 10;\nint medium_threshold = 20;\nint high_threshold = 30;\n\n// 统计计数器\nint low_count = 0, medium_count = 0, high_count = 0, extreme_count = 0;\n\n// 循环处理每个值\nfor (int i = 0; i < count; i++) {\n    int value = values[i];\n    const char* category;\n    \n    // 原始条件链逻辑\n    if (value < low_threshold) {\n        category = \"low\";\n        low_count++;\n    } else if (value < medium_threshold) {\n        category = \"medium\";\n        medium_count++;\n    } else if (value < high_threshold) {\n        category = \"high\";\n        high_count++;\n    } else {\n        category = \"extreme\";\n        extreme_count++;\n    }\n    \n    // 线性调整阈值（动态特性）\n    if (i == count - 1) {\n        // 最后一次迭代，不调整\n    } else {\n        low_threshold += 1;\n        medium_threshold += 1;\n        high_threshold += 1;\n    }\n}\n\nprintf(\"Medium count: %d\\n\", medium_count);",
            "answer": 2
        }
    },
    {
        "id": "BL-MIX-CD004-V001",
        "metadata": {
            "name": "多语言星期映射",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Conditional+Iterative",
            "mixed_blocks": ["Conditional", "Iterative"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["多语言支持", "循环映射"]
        },
        "task": {
            "description": "基于BL-CD-S004的switch语句，扩展为多语言星期映射，当languages数组有2种语言且day为3时，找到的映射数量是多少？",
            "code": "typedef struct {\n    const char* lang;\n    const char* days[8]; // 0不用，1-7对应周一到周日\n} language_map_t;\n\nlanguage_map_t languages[] = {\n    {\"en\", {\"\", \"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\", \"Friday\", \"Saturday\", \"Sunday\"}},\n    {\"zh\", {\"\", \"星期一\", \"星期二\", \"星期三\", \"星期四\", \"星期五\", \"星期六\", \"星期日\"}}\n};\n\nint day = 3;\nint lang_count = 2;\nint found_mappings = 0;\n\n// 循环遍历每种语言\nfor (int i = 0; i < lang_count; i++) {\n    const char* day_name = NULL;\n    \n    // 原始switch逻辑的等价条件版本\n    if (day >= 1 && day <= 7) {\n        day_name = languages[i].days[day];\n        if (day_name != NULL && strlen(day_name) > 0) {\n            found_mappings++;\n        }\n    }\n}\n\nprintf(\"Found mappings: %d\\n\", found_mappings);",
            "answer": 2
        }
    },
    {
        "id": "BL-MIX-CD005-V001",
        "metadata": {
            "name": "多模式标志处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Conditional+Iterative+Linear",
            "mixed_blocks": ["Conditional", "Iterative", "Linear"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["位操作", "fallthrough", "批量处理"]
        },
        "task": {
            "description": "基于BL-CD-S005的switch fallthrough，扩展为多输入批量处理，当inputs为[1,2,3]时，combined_flags的最终值是多少？",
            "code": "int inputs[] = {1, 2, 3};\nint input_count = 3;\nint combined_flags = 0;\n\n// 循环处理每个输入\nfor (int idx = 0; idx < input_count; idx++) {\n    int input = inputs[idx];\n    int flags = 0;\n    \n    // 原始switch fallthrough逻辑\n    switch (input) {\n        case 1:\n            flags |= 0x01;\n            // fallthrough\n        case 2:\n            flags |= 0x02;\n            // fallthrough\n        case 3:\n            flags |= 0x04;\n            break;\n        default:\n            flags = -1;\n    }\n    \n    // 线性组合标志\n    if (flags >= 0) {\n        combined_flags |= flags;\n    }\n}\n\nprintf(\"Combined flags: 0x%02X\\n\", combined_flags);",
            "answer": 7
        }
    },
    {
        "id": "BL-MIX-CD006-V001",
        "metadata": {
            "name": "三元表达式链式处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Conditional+Iterative",
            "mixed_blocks": ["Conditional", "Iterative"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["三元表达式", "链式处理", "复杂逻辑"]
        },
        "task": {
            "description": "基于BL-CD-S006的三元条件链，扩展为配对处理循环，当pairs数组有3对数据时，max_result的值是多少？",
            "code": "typedef struct {\n    int x;\n    int y;\n} pair_t;\n\npair_t pairs[] = {{7, 5}, {4, 8}, {9, 3}};\nint pair_count = 3;\nint results[3];\nint max_result = 0;\n\n// 循环处理每对数据\nfor (int i = 0; i < pair_count; i++) {\n    int x = pairs[i].x;\n    int y = pairs[i].y;\n    \n    // 原始三元条件链逻辑\n    int result = (x > y) ? ((x % 2 == 0) ? x * 2 : x + 10) : ((y % 2 == 0) ? y * 3 : y - 2);\n    \n    results[i] = result;\n    \n    // 线性更新最大值\n    if (result > max_result) {\n        max_result = result;\n    }\n}\n\nprintf(\"Max result: %d\\n\", max_result);",
            "answer": 24
        }
    },
    {
        "id": "BL-MIX-CD007-V001",
        "metadata": {
            "name": "资源分配批量检查",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Conditional+Iterative+Linear",
            "mixed_blocks": ["Conditional", "Iterative", "Linear"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["内存管理", "批量分配", "错误处理"]
        },
        "task": {
            "description": "基于BL-CD-S007的空指针检查，扩展为批量资源分配，当请求5个资源时，successful_allocations的值是多少？",
            "code": "typedef struct {\n    int fd;\n    short events;\n    int allocated;\n} poll_handle_t;\n\nint allocate_poll_handles(int count) {\n    poll_handle_t* handles[10];\n    int successful_allocations = 0;\n    int sizes[] = {32, 64, 32, 128, 64}; // 模拟不同大小的分配\n    \n    // 循环分配资源\n    for (int i = 0; i < count && i < 10; i++) {\n        // 模拟malloc调用\n        poll_handle_t* p = (poll_handle_t*)malloc(sizes[i % 5]);\n        \n        // 原始空指针检查逻辑\n        if (p == NULL) {\n            handles[i] = NULL;\n        } else {\n            // 线性初始化\n            p->fd = i + 1;\n            p->events = 0x01;\n            p->allocated = 1;\n            handles[i] = p;\n            successful_allocations++;\n        }\n    }\n    \n    return successful_allocations;\n}\n\nint result = allocate_poll_handles(5);\nprintf(\"Successful allocations: %d\\n\", result);",
            "answer": 5
        }
    },
    {
        "id": "BL-MIX-CD008-V001",
        "metadata": {
            "name": "多维度评估系统",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Conditional+Iterative+Linear",
            "mixed_blocks": ["Conditional", "Iterative", "Linear"],
            "primary_pattern": "Conditional",
            "complexity_factors": ["复杂逻辑", "多维度", "批量评估"]
        },
        "task": {
            "description": "基于BL-CD-S008的复杂条件逻辑，扩展为多申请人评估系统，当有3个申请人时，approved_premium_count的值是多少？",
            "code": "applicants = [\n    {'age': 25, 'income': 50000, 'has_degree': True},\n    {'age': 30, 'income': 35000, 'has_degree': False},\n    {'age': 22, 'income': 25000, 'has_degree': True}\n]\n\nstatuses = []\napproved_premium_count = 0\ntotal_approved = 0\n\n# 循环评估每个申请人\nfor applicant in applicants:\n    age = applicant['age']\n    income = applicant['income']\n    has_degree = applicant['has_degree']\n    status = None\n    \n    # 原始复杂条件逻辑\n    if age >= 18 and age <= 65:\n        if income > 30000:\n            if has_degree:\n                status = \"approved_premium\"\n            else:\n                status = \"approved_standard\"\n        else:\n            if age >= 21 and has_degree:\n                status = \"approved_basic\"\n            else:\n                status = \"pending_review\"\n    else:\n        status = \"not_eligible\"\n    \n    statuses.append(status)\n    \n    # 线性统计\n    if status.startswith(\"approved\"):\n        total_approved += 1\n        if status == \"approved_premium\":\n            approved_premium_count += 1\n\nprint(f\"Approved premium count: {approved_premium_count}\")",
            "answer": 1
        }
    },
    {
        "id": "BL-MIX-IT001-V001",
        "metadata": {
            "name": "累加循环条件优化",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "easy",
            "intervention": 0,
            "variant_type": "Iterative+Conditional",
            "mixed_blocks": ["Iterative", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["循环累加", "条件优化"]
        },
        "task": {
            "description": "基于BL-IT-S001的简单for循环，添加条件优化，当threshold为12时，final_sum的值是多少？",
            "code": "int sum = 0;\nint threshold = 12;\nint bonus = 5;\n\n// 原始循环累加\nfor (int i = 1; i <= 5; i++) {\n    sum += i;\n}\n\n// 条件优化\nif (sum >= threshold) {\n    int final_sum = sum + bonus;\n    printf(\"Final sum with bonus: %d\\n\", final_sum);\n} else {\n    int final_sum = sum;\n    printf(\"Final sum: %d\\n\", final_sum);\n}",
            "answer": 20
        }
    },
    {
        "id": "BL-MIX-IT002-V001",
        "metadata": {
            "name": "数组初始化验证循环",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Iterative+Conditional+Linear",
            "mixed_blocks": ["Iterative", "Conditional", "Linear"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["数组初始化", "验证循环", "统计计算"]
        },
        "task": {
            "description": "基于BL-IT-S002的数组初始化，添加验证循环，当GB_SIZE为4时，null_count的值是多少？",
            "code": "#define MAX_SIZE 10\nvoid* pointer_arr[MAX_SIZE];\nint pointer_idx = 0;\nint GB_SIZE = 4;\n\nvoid extended_init_with_validation() {\n    int null_count = 0;\n    int non_null_count = 0;\n    \n    // 线性初始化\n    pointer_idx = 0;\n    \n    // 原始初始化循环\n    for (int i = 0; i < GB_SIZE && i < MAX_SIZE; i++) {\n        pointer_arr[i] = NULL;\n    }\n    \n    // 验证循环\n    for (int i = 0; i < MAX_SIZE; i++) {\n        // 条件检查和统计\n        if (i < GB_SIZE) {\n            if (pointer_arr[i] == NULL) {\n                null_count++;\n            } else {\n                non_null_count++;\n            }\n        }\n    }\n    \n    printf(\"Null count: %d\\n\", null_count);\n}\n\nextended_init_with_validation();",
            "answer": 4
        }
    },
    {
        "id": "BL-MIX-IT003-V001",
        "metadata": {
            "name": "多条件while循环",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Iterative+Conditional",
            "mixed_blocks": ["Iterative", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["多条件", "循环控制"]
        },
        "task": {
            "description": "基于BL-IT-S003的while循环，添加多条件控制，当initial_value为24且max_iterations为6时，final_count的值是多少？",
            "code": "int value = 24;\nint count = 0;\nint max_iterations = 6;\nint min_value = 1;\n\n// 多条件while循环（基于原始逻辑扩展）\nwhile (value > min_value && count < max_iterations) {\n    value = value / 2;\n    count++;\n    \n    // 条件检查：如果值变为奇数且大于1，调整\n    if (value > 1 && value % 2 == 1) {\n        value = value + 1; // 向上舍入到偶数\n    }\n}\n\nint final_count = count;\nprintf(\"Final count: %d\\n\", final_count);",
            "answer": 5
        }
    },
    {
        "id": "BL-MIX-IT004-V001",
        "metadata": {
            "name": "嵌套循环线性处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Iterative+Linear+Conditional",
            "mixed_blocks": ["Iterative", "Linear", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["嵌套循环", "线性处理", "条件过滤"]
        },
        "task": {
            "description": "基于BL-IT-S004的嵌套循环，添加线性处理和条件过滤，filtered_total的最终值是多少？",
            "code": "total = 0\nfiltered_total = 0\nprocessing_factor = 2\nfilter_threshold = 8\n\n# 原始嵌套循环计算\nfor i in range(3):\n    for j in range(2):\n        value = (i + 1) * (j + 1)\n        total += value\n        \n        # 线性处理\n        processed_value = value * processing_factor\n        \n        # 条件过滤\n        if processed_value >= filter_threshold:\n            filtered_total += processed_value\n\nprint(f\"Filtered total: {filtered_total}\")",
            "answer": 28
        }
    },
    {
        "id": "BL-MIX-IT005-V001",
        "metadata": {
            "name": "中断控制统计循环",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "hard",
            "intervention": 2,
            "variant_type": "Iterative+Conditional+Linear",
            "mixed_blocks": ["Iterative", "Conditional", "Linear"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["中断控制", "统计循环", "多重条件"]
        },
        "task": {
            "description": "基于BL-IT-S005的break和continue循环，添加统计功能，当上限为15时，processed_count的值是多少？",
            "code": "int sum = 0;\nint processed_count = 0;\nint skipped_count = 0;\nint early_exit = 0;\nint limit = 15;\n\n// 扩展的循环与统计\nfor (int i = 1; i <= limit; i++) {\n    // 线性计数\n    if (i % 2 == 0) {\n        skipped_count++;\n        continue;\n    }\n    \n    // 条件检查提前退出\n    if (i > 10) {\n        early_exit = 1;\n        break;\n    }\n    \n    // 线性处理\n    sum += i;\n    processed_count++;\n}\n\nprintf(\"Processed count: %d\\n\", processed_count);",
            "answer": 5
        }
    },
    {
        "id": "BL-MIX-IT006-V001",
        "metadata": {
            "name": "do-while条件增强",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "medium",
            "intervention": 1,
            "variant_type": "Iterative+Conditional",
            "mixed_blocks": ["Iterative", "Conditional"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["do-while", "条件增强"]
        },
        "task": {
            "description": "基于BL-IT-S006的do-while循环，添加条件增强，当initial_n为2且target为15时，final_n的值是多少？",
            "code": "int n = 2;\nint target = 15;\nint increment = 3;\nint max_iterations = 8;\nint iterations = 0;\n\n// 增强的do-while循环\ndo {\n    n += increment;\n    iterations++;\n    \n    // 条件调整increment\n    if (n > target && increment > 1) {\n        increment = 1; // 减小增量，精确控制\n    }\n    \n    // 安全检查，避免无限循环\n    if (iterations >= max_iterations) {\n        break;\n    }\n    \n} while (n < target);\n\nint final_n = n;\nprintf(\"Final n: %d\\n\", final_n);",
            "answer": 17
        }
    },
    {
        "id": "BL-MIX-IT007-V001",
        "metadata": {
            "name": "递归函数记忆化",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "c",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Iterative+Conditional+Linear",
            "mixed_blocks": ["Iterative", "Conditional", "Linear"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["递归优化", "记忆化", "缓存管理"]
        },
        "task": {
            "description": "基于BL-IT-S007的递归阶乘，添加记忆化缓存，当计算factorial_cached(5)时，cache_hits的值是多少？",
            "code": "static int cache[20] = {0}; // 缓存数组\nstatic int cache_hits = 0;\nstatic int cache_misses = 0;\n\nint factorial_cached(int n) {\n    // 条件检查缓存\n    if (n < 20 && cache[n] != 0) {\n        cache_hits++;\n        return cache[n];\n    }\n    \n    cache_misses++;\n    \n    // 基础递归条件\n    if (n <= 1) {\n        int result = 1;\n        if (n < 20) cache[n] = result;\n        return result;\n    }\n    \n    // 递归计算\n    int result = n * factorial_cached(n - 1);\n    \n    // 线性缓存存储\n    if (n < 20) {\n        cache[n] = result;\n    }\n    \n    return result;\n}\n\n// 初始化缓存\nfor (int i = 0; i < 20; i++) {\n    cache[i] = 0;\n}\ncache_hits = 0;\ncache_misses = 0;\n\nint result = factorial_cached(5);\nprintf(\"Cache hits: %d\\n\", cache_hits);",
            "answer": 0
        }
    },
    {
        "id": "BL-MIX-IT008-V001",
        "metadata": {
            "name": "复杂累积多路处理",
            "category": "Block-Level",
            "subcategory": "Mixed",
            "type": "variant",
            "source": "Generated",
            "language": "python",
            "difficulty": "expert",
            "intervention": 3,
            "variant_type": "Iterative+Conditional+Linear",
            "mixed_blocks": ["Iterative", "Conditional", "Linear"],
            "primary_pattern": "Iterative",
            "complexity_factors": ["多路处理", "复杂累积", "动态调整"]
        },
        "task": {
            "description": "基于BL-IT-S008的复杂累积，扩展为多路并行处理，当增加分组处理时，group_totals的总和是多少？",
            "code": "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ngroup_size = 3\ngroup_totals = []\ntotal_sum = 0\n\n# 按组处理数字\nfor group_start in range(0, len(numbers), group_size):\n    group = numbers[group_start:group_start + group_size]\n    group_result = 0\n    group_multiplier = 1\n    \n    # 组内处理（基于原始逻辑）\n    for num in group:\n        if num % 2 == 0:\n            group_result += num * group_multiplier\n            group_multiplier += 1\n        else:\n            group_result -= num\n    \n    group_totals.append(group_result)\n    \n    # 线性累加到总和\n    total_sum += group_result\n\nprint(f\"Total sum of group totals: {total_sum}\")",
            "answer": -9
        }
    }
]
```

