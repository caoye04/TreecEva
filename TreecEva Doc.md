# TreecEva

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

## 种子任务构建

### 1 - 语句级推理 [ Statement-Level ]

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

### 2 -  代码块级推理 [ Block-Level ]

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

### 3 - 代码属性推理 [ Property-Level ] 

#### 3A - 循环属性 [ Loop ]

> （迭代计数、变量追踪、终止条件）

#### 3B - 分支属性 [ Branch ]

> （条件求值、路径选择、分支效果）

#### 3C - 内存属性 [ Memory ] 

> （引用关系、生命周期、访问模式）

#### 3D - 作用域属性 [ Scope ]

> （可见性、生存期、变量遮蔽）

#### 3E - 大混合





# insight

- 粗粒度要求带来：自由发挥、真实案例

- 造代码之外还有：让AI去生成一些hint，描述代码情况
- case和case之间散一点

