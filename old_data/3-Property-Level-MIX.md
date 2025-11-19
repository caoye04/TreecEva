# Property-Level-MIX

> 曹烨

## 设计

代码属性推理（Property-Level）

- 循环属性 [ Loop ]（迭代计数、变量追踪、终止条件）
- 分支属性 [ Branch ]（条件求值、路径选择、分支效果）
- 内存属性 [ Memory ] （引用关系、生命周期、访问模式）
- 作用域属性 [ Scope ]（可见性、生存期、变量遮蔽）
- 大混合

## 种子序列

3A - 循环属性 [ Loop ] （6）

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

3B - 分支属性 [ Branch ] （7）

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

3C - 内存属性 [ Memory ] （6）

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

3D - 作用域属性 [ Scope ]（6）

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

3E - 大混合（2）

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

## 需求

- 需要再生成5个评估点，参考上面的任务内容

- 需要生产比较复杂的code，可以参考SL-MIX-S002和SL-MIX-S001这两个，最好比他们更复杂一些

- 答案需要正确且唯一

- 格式统一成以下格式：

  ```
  {
      "id": "SL-xxx",
      "metadata": {
          "category": "Statement-Level",
          "language": "c/python/java",
          "difficulty": 0-10,
          "intervention": 0-10
      },
      "task": {
          "description": "xxx",
          "code": "xxx",
          "answer": xxx,
          "cot":"xxx"
      }
  }
  ```

## 最终产出

### task1

```
{
    "id": "PL-MIX-S001",
    "metadata": {
        "category": "Property-Level",
        "language": "c",
        "difficulty": 10,
        "intervention": 10
    },
    "task": {
        "description": "This code implements a complex tree-like structure with circular references and multi-level state tracking. Analyze the memory patterns, scope interactions, and control flow to determine the final value.",
        "code": "typedef struct Node {\n    int value;\n    struct Node *left;\n    struct Node *right;\n    struct Node *parent;\n    int depth;\n} Node;\n\ntypedef struct {\n    Node *root;\n    int *buffer;\n    int buf_size;\n    int current_depth;\n    int state_flags;\n} TreeContext;\n\nstatic int global_modifier = 1;\nstatic int depth_multiplier = 2;\n\nNode* create_node(int value, Node *parent, int depth) {\n    Node *node = (Node*)malloc(sizeof(Node));\n    node->value = value;\n    node->left = NULL;\n    node->right = NULL;\n    node->parent = parent;\n    node->depth = depth;\n    return node;\n}\n\nint process_subtree(Node *node, TreeContext *ctx, int level) {\n    if (!node || level > ctx->current_depth) return 0;\n    \n    int result = 0;\n    int local_state = ctx->state_flags;\n    \n    // Buffer rotation based on node depth\n    for(int i = 0; i < ctx->buf_size; i++) {\n        int idx = (i + node->depth) % ctx->buf_size;\n        if(ctx->buffer[idx] % depth_multiplier == 0) {\n            ctx->buffer[idx] = (ctx->buffer[idx] + node->value) % 100;\n            result += ctx->buffer[idx];\n            global_modifier = (global_modifier * 3) % 10 + 1;\n        }\n    }\n    \n    // State manipulation in local scope\n    {\n        int temp_value = node->value;\n        int *shadow_buffer = (int*)malloc(ctx->buf_size * sizeof(int));\n        memcpy(shadow_buffer, ctx->buffer, ctx->buf_size * sizeof(int));\n        \n        for(int i = 0; i < node->depth; i++) {\n            if(shadow_buffer[i] < temp_value) {\n                temp_value = (temp_value + shadow_buffer[i]) / 2;\n                ctx->state_flags ^= (1 << i);\n            }\n        }\n        \n        node->value = temp_value;\n        free(shadow_buffer);\n    }\n    \n    // Process children with state propagation\n    if(node->left) {\n        int left_result = process_subtree(node->left, ctx, level + 1);\n        result += (left_result * global_modifier) % 50;\n        \n        if(node->right) {\n            node->right->value = (node->right->value + left_result) % 100;\n        }\n    }\n    \n    if(node->right) {\n        int right_result = process_subtree(node->right, ctx, level + 1);\n        result += (right_result * (global_modifier + 1)) % 50;\n        \n        if(node->parent) {\n            node->parent->value = (node->parent->value + right_result) % 100;\n        }\n    }\n    \n    // Final state adjustment\n    if(ctx->state_flags != local_state) {\n        result = (result + ctx->state_flags - local_state) % 200;\n    }\n    \n    return result;\n}\n\nint complex_tree_processing() {\n    // Initialize tree\n    Node *root = create_node(15, NULL, 0);\n    root->left = create_node(25, root, 1);\n    root->right = create_node(35, root, 1);\n    root->left->left = create_node(45, root->left, 2);\n    root->right->right = create_node(55, root->right, 2);\n    \n    // Initialize context\n    int buffer[] = {10, 20, 30, 40, 50, 60};\n    TreeContext ctx = {\n        .root = root,\n        .buffer = buffer,\n        .buf_size = 6,\n        .current_depth = 3,\n        .state_flags = 0x0F\n    };\n    \n    int final_result = process_subtree(root, &ctx, 0);\n    \n    // Cleanup\n    // Note: In real code, would need proper tree deletion\n    free(root->left->left);\n    free(root->right->right);\n    free(root->left);\n    free(root->right);\n    free(root);\n    \n    return final_result;\n}\n\n// Execute and get final result\nint final = complex_tree_processing();",
        "answer": ,
        "cot": ""
    }
}
```

```c

```



### task2

```
{
    "id": "PL-MIX-E002",
    "metadata": {
        "category": "Property-Level",
        "language": "c",
        "difficulty": 10,
        "intervention": 10
    },
    "task": {
        "description": "This code implements a priority queue with dynamic memory pools and worker threads simulation. Analyze the complex interaction between memory management, thread states, and priority processing to determine the final result.",
        "code": "typedef struct MemBlock {\n    int size;\n    int used;\n    int *data;\n    struct MemBlock *next;\n} MemBlock;\n\ntypedef struct {\n    int priority;\n    int value;\n    int timestamp;\n} Task;\n\ntypedef struct {\n    Task *tasks;\n    int capacity;\n    int size;\n    int front;\n    int rear;\n    MemBlock *mem_pool;\n    int worker_states[4];\n    int total_processed;\n} PriorityQueue;\n\nstatic int global_timestamp = 0;\nstatic int state_matrix[4][4] = {\n    {1, 2, 3, 4},\n    {2, 3, 4, 1},\n    {3, 4, 1, 2},\n    {4, 1, 2, 3}\n};\n\nMemBlock* allocate_memory_block(int size) {\n    MemBlock *block = (MemBlock*)malloc(sizeof(MemBlock));\n    block->size = size;\n    block->used = 0;\n    block->data = (int*)malloc(size * sizeof(int));\n    block->next = NULL;\n    return block;\n}\n\nvoid expand_memory_pool(PriorityQueue *pq) {\n    MemBlock *new_block = allocate_memory_block(pq->capacity * 2);\n    new_block->next = pq->mem_pool;\n    pq->mem_pool = new_block;\n}\n\nint get_worker_state(PriorityQueue *pq, int worker_id) {\n    int base_state = pq->worker_states[worker_id];\n    int modifier = state_matrix[worker_id][pq->size % 4];\n    return (base_state * modifier) % 100;\n}\n\nvoid process_task(PriorityQueue *pq, Task *task, int worker_id) {\n    int worker_state = get_worker_state(pq, worker_id);\n    MemBlock *current = pq->mem_pool;\n    \n    while(current && current->used >= current->size) {\n        current = current->next;\n    }\n    \n    if(!current) {\n        expand_memory_pool(pq);\n        current = pq->mem_pool;\n    }\n    \n    int result_value = (task->value * task->priority + worker_state) % 1000;\n    current->data[current->used++] = result_value;\n    \n    // Update worker state based on result\n    pq->worker_states[worker_id] = (pq->worker_states[worker_id] + result_value) % 50;\n    pq->total_processed += result_value;\n}\n\nvoid enqueue_task(PriorityQueue *pq, int value, int priority) {\n    Task new_task = {\n        .priority = priority,\n        .value = value,\n        .timestamp = global_timestamp++\n    };\n    \n    int insert_pos = pq->rear;\n    while(insert_pos != pq->front) {\n        int prev = (insert_pos - 1 + pq->capacity) % pq->capacity;\n        if(pq->tasks[prev].priority >= priority) break;\n        pq->tasks[insert_pos] = pq->tasks[prev];\n        insert_pos = prev;\n    }\n    \n    pq->tasks[insert_pos] = new_task;\n    pq->rear = (pq->rear + 1) % pq->capacity;\n    pq->size++;\n}\n\nTask dequeue_task(PriorityQueue *pq) {\n    Task task = pq->tasks[pq->front];\n    pq->front = (pq->front + 1) % pq->capacity;\n    pq->size--;\n    return task;\n}\n\nint simulate_priority_processing() {\n    // Initialize queue\n    PriorityQueue pq = {\n        .capacity = 8,\n        .size = 0,\n        .front = 0,\n        .rear = 0,\n        .total_processed = 0,\n        .worker_states = {5, 7, 3, 9}\n    };\n    \n    pq.tasks = (Task*)malloc(pq.capacity * sizeof(Task));\n    pq.mem_pool = allocate_memory_block(16);\n    \n    // Enqueue initial tasks\n    enqueue_task(&pq, 25, 3);\n    enqueue_task(&pq, 15, 1);\n    enqueue_task(&pq, 35, 4);\n    enqueue_task(&pq, 20, 2);\n    \n    // Process tasks with different workers\n    for(int i = 0; i < 4; i++) {\n        if(pq.size > 0) {\n            Task task = dequeue_task(&pq);\n            process_task(&pq, &task, i % 4);\n        }\n    }\n    \n    int final_result = pq.total_processed;\n    \n    // Cleanup\n    MemBlock *current = pq.mem_pool;\n    while(current) {\n        MemBlock *next = current->next;\n        free(current->data);\n        free(current);\n        current = next;\n    }\n    free(pq.tasks);\n    \n    return final_result;\n}\n\n// Execute simulation\nint final = simulate_priority_processing();",
        "answer": ,
        "cot": ""
    }
}
```



### task3

```
{
    "id": "PL-MIX-E003",
    "metadata": {
        "category": "Property-Level",
        "language": "c",
        "difficulty": 10,
        "intervention": 10
    },
    "task": {
        "description": "This code simulates a network packet processing system with multiple layers, packet fragmentation, and routing tables. Analyze the packet flow, state transitions, and memory patterns to determine the final checksum value.",
        "code": "typedef struct PacketFragment {\n    unsigned char *data;\n    int size;\n    int sequence;\n    struct PacketFragment *next;\n} PacketFragment;\n\ntypedef struct {\n    int id;\n    int priority;\n    PacketFragment *fragments;\n    int total_fragments;\n    unsigned int checksum;\n} Packet;\n\ntypedef struct {\n    int route_id;\n    int hop_count;\n    unsigned int mask;\n    int (*process)(unsigned char*, int);\n} RouteEntry;\n\ntypedef struct {\n    Packet **buffers;\n    int *buffer_sizes;\n    int num_buffers;\n    RouteEntry *routing_table;\n    int table_size;\n    unsigned int global_state;\n} NetworkProcessor;\n\nstatic unsigned int crc_table[256];\nstatic int processing_flags = 0x0F;\n\n// Initialize CRC table\nvoid init_crc_table() {\n    unsigned int polynomial = 0xEDB88320;\n    for(int i = 0; i < 256; i++) {\n        unsigned int crc = i;\n        for(int j = 0; j < 8; j++) {\n            crc = (crc >> 1) ^ ((crc & 1) ? polynomial : 0);\n        }\n        crc_table[i] = crc;\n    }\n}\n\nunsigned int calculate_checksum(unsigned char *data, int size) {\n    unsigned int crc = 0xFFFFFFFF;\n    for(int i = 0; i < size; i++) {\n        crc = (crc >> 8) ^ crc_table[(crc & 0xFF) ^ data[i]];\n    }\n    return crc ^ 0xFFFFFFFF;\n}\n\nint process_layer1(unsigned char *data, int size) {\n    int result = 0;\n    for(int i = 0; i < size; i++) {\n        result += (data[i] * processing_flags) % 256;\n    }\n    return result;\n}\n\nint process_layer2(unsigned char *data, int size) {\n    int result = 0;\n    for(int i = 0; i < size - 1; i++) {\n        result += ((data[i] << 8) | data[i + 1]) % 1024;\n    }\n    return result;\n}\n\nint process_layer3(unsigned char *data, int size) {\n    int result = 0;\n    unsigned int temp = 0;\n    for(int i = 0; i < size - 3; i += 4) {\n        temp = (data[i] << 24) | (data[i+1] << 16) | \n               (data[i+2] << 8) | data[i+3];\n        result += temp % 2048;\n    }\n    return result;\n}\n\nPacketFragment* create_fragment(unsigned char *data, int size, int seq) {\n    PacketFragment *frag = (PacketFragment*)malloc(sizeof(PacketFragment));\n    frag->data = (unsigned char*)malloc(size);\n    memcpy(frag->data, data, size);\n    frag->size = size;\n    frag->sequence = seq;\n    frag->next = NULL;\n    return frag;\n}\n\nvoid process_packet(NetworkProcessor *np, Packet *packet) {\n    unsigned int local_checksum = 0;\n    PacketFragment *current = packet->fragments;\n    \n    while(current) {\n        // Apply routing table rules\n        for(int i = 0; i < np->table_size; i++) {\n            RouteEntry *route = &np->routing_table[i];\n            if((packet->id & route->mask) == route->route_id) {\n                int proc_result = route->process(current->data, current->size);\n                local_checksum = (local_checksum + proc_result * route->hop_count) % 0x7FFFFFFF;\n                np->global_state = (np->global_state + proc_result) % 1000;\n            }\n        }\n        \n        // Update packet checksum\n        unsigned int frag_checksum = calculate_checksum(current->data, current->size);\n        packet->checksum ^= frag_checksum;\n        \n        current = current->next;\n    }\n    \n    // Buffer management\n    int buffer_index = packet->priority % np->num_buffers;\n    if(np->buffers[buffer_index] == NULL) {\n        np->buffers[buffer_index] = packet;\n        np->buffer_sizes[buffer_index] = 1;\n    } else {\n        // Merge checksums of buffered packets\n        np->buffers[buffer_index]->checksum ^= packet->checksum;\n        np->buffer_sizes[buffer_index]++;\n    }\n}\n\nunsigned int simulate_network_processing() {\n    init_crc_table();\n    \n    // Initialize network processor\n    NetworkProcessor np = {\n        .num_buffers = 4,\n        .table_size = 3,\n        .global_state = 0x12345678\n    };\n    \n    np.buffers = (Packet**)calloc(np.num_buffers, sizeof(Packet*));\n    np.buffer_sizes = (int*)calloc(np.num_buffers, sizeof(int));\n    np.routing_table = (RouteEntry*)malloc(np.table_size * sizeof(RouteEntry));\n    \n    // Setup routing table\n    np.routing_table[0] = (RouteEntry){0x01, 2, 0xFF, process_layer1};\n    np.routing_table[1] = (RouteEntry){0x02, 3, 0xFF, process_layer2};\n    np.routing_table[2] = (RouteEntry){0x03, 4, 0xFF, process_layer3};\n    \n    // Create test packets\n    unsigned char test_data1[] = {0x12, 0x34, 0x56, 0x78, 0x9A};\n    unsigned char test_data2[] = {0xAB, 0xCD, 0xEF, 0x12, 0x34};\n    \n    Packet packet1 = {0x01, 1, NULL, 2, 0};\n    packet1.fragments = create_fragment(test_data1, 5, 0);\n    packet1.fragments->next = create_fragment(test_data2, 5, 1);\n    \n    Packet packet2 = {0x02, 2, NULL, 1, 0};\n    packet2.fragments = create_fragment(test_data1, 5, 0);\n    \n    Packet packet3 = {0x03, 3, NULL, 1, 0};\n    packet3.fragments = create_fragment(test_data2, 5, 0);\n    \n    // Process packets\n    process_packet(&np, &packet1);\n    process_packet(&np, &packet2);\n    process_packet(&np, &packet3);\n    \n    // Calculate final result\n    unsigned int final_result = np.global_state;\n    for(int i = 0; i < np.num_buffers; i++) {\n        if(np.buffers[i]) {\n            final_result ^= np.buffers[i]->checksum;\n        }\n    }\n    \n    // Cleanup\n    for(int i = 0; i < np.num_buffers; i++) {\n        if(np.buffers[i]) {\n            PacketFragment *current = np.buffers[i]->fragments;\n            while(current) {\n                PacketFragment *next = current->next;\n                free(current->data);\n                free(current);\n                current = next;\n            }\n        }\n    }\n    free(np.buffers);\n    free(np.buffer_sizes);\n    free(np.routing_table);\n    \n    return final_result;\n}\n\n// Execute simulation\nunsigned int final = simulate_network_processing();",
        "answer": ,
        "cot": ""
    }
}
```



### task4

```
{
    "id": "PL-MIX-E004",
    "metadata": {
        "category": "Property-Level",
        "language": "c",
        "difficulty": 10,
        "intervention": 10
    },
    "task": {
        "description": "This code implements a virtual file system with block allocation, file journaling, and cache management. Analyze the interaction between different system components and memory patterns to determine the final system state value.",
        "code": "typedef struct Block {\n    unsigned char *data;\n    int size;\n    int ref_count;\n    struct Block *next;\n} Block;\n\ntypedef struct {\n    char name[32];\n    int inode;\n    int size;\n    Block *first_block;\n    unsigned int attributes;\n} FileEntry;\n\ntypedef struct {\n    int operation;\n    int inode;\n    unsigned long timestamp;\n    unsigned char *old_data;\n    unsigned char *new_data;\n    int data_size;\n} JournalEntry;\n\ntypedef struct {\n    Block **blocks;\n    int total_blocks;\n    int free_blocks;\n    FileEntry *file_table;\n    int max_files;\n    int used_files;\n    JournalEntry *journal;\n    int journal_size;\n    int journal_head;\n    unsigned char *cache;\n    int cache_size;\n    unsigned int system_state;\n} VirtualFS;\n\n#define BLOCK_SIZE 512\n#define CACHE_LINES 64\n#define CACHE_LINE_SIZE 64\n#define OP_WRITE 1\n#define OP_DELETE 2\n#define OP_MOVE 3\n\nstatic unsigned int operation_counter = 0;\nstatic const unsigned int PRIME_MULTIPLIER = 31;\n\n// Cache management functions\nunsigned int get_cache_index(int block_num) {\n    return (block_num * PRIME_MULTIPLIER) % CACHE_LINES;\n}\n\nvoid update_cache(VirtualFS *fs, int block_num, unsigned char *data) {\n    unsigned int index = get_cache_index(block_num);\n    memcpy(fs->cache + index * CACHE_LINE_SIZE, data, CACHE_LINE_SIZE);\n    fs->system_state = (fs->system_state * PRIME_MULTIPLIER + block_num) % 0x7FFFFFFF;\n}\n\n// Journal management\nvoid add_journal_entry(VirtualFS *fs, int op, int inode, \n                      unsigned char *old_data, unsigned char *new_data, int size) {\n    JournalEntry *entry = &fs->journal[fs->journal_head];\n    entry->operation = op;\n    entry->inode = inode;\n    entry->timestamp = operation_counter++;\n    \n    if(old_data) {\n        entry->old_data = (unsigned char*)malloc(size);\n        memcpy(entry->old_data, old_data, size);\n    }\n    \n    if(new_data) {\n        entry->new_data = (unsigned char*)malloc(size);\n        memcpy(entry->new_data, new_data, size);\n    }\n    \n    entry->data_size = size;\n    fs->journal_head = (fs->journal_head + 1) % fs->journal_size;\n    fs->system_state ^= (entry->timestamp * PRIME_MULTIPLIER);\n}\n\n// Block allocation\nBlock* allocate_block(VirtualFS *fs, unsigned char *data, int size) {\n    if(fs->free_blocks <= 0) return NULL;\n    \n    Block *block = (Block*)malloc(sizeof(Block));\n    block->data = (unsigned char*)malloc(BLOCK_SIZE);\n    memcpy(block->data, data, size);\n    block->size = size;\n    block->ref_count = 1;\n    block->next = NULL;\n    \n    for(int i = 0; i < fs->total_blocks; i++) {\n        if(fs->blocks[i] == NULL) {\n            fs->blocks[i] = block;\n            fs->free_blocks--;\n            update_cache(fs, i, data);\n            break;\n        }\n    }\n    \n    return block;\n}\n\n// File operations\nint create_file(VirtualFS *fs, const char *name, unsigned char *data, int size) {\n    if(fs->used_files >= fs->max_files) return -1;\n    \n    int inode = -1;\n    for(int i = 0; i < fs->max_files; i++) {\n        if(fs->file_table[i].inode == -1) {\n            inode = i;\n            break;\n        }\n    }\n    \n    if(inode == -1) return -1;\n    \n    FileEntry *file = &fs->file_table[inode];\n    strncpy(file->name, name, 31);\n    file->name[31] = '\\0';\n    file->inode = inode;\n    file->size = size;\n    file->attributes = 0;\n    \n    int blocks_needed = (size + BLOCK_SIZE - 1) / BLOCK_SIZE;\n    Block *last_block = NULL;\n    \n    for(int i = 0; i < blocks_needed; i++) {\n        int block_size = (i == blocks_needed - 1) ? \n            (size % BLOCK_SIZE) : BLOCK_SIZE;\n        Block *new_block = allocate_block(fs, \n            data + i * BLOCK_SIZE, block_size);\n            \n        if(!new_block) return -1;\n        \n        if(!file->first_block) {\n            file->first_block = new_block;\n        } else {\n            last_block->next = new_block;\n        }\n        last_block = new_block;\n    }\n    \n    fs->used_files++;\n    add_journal_entry(fs, OP_WRITE, inode, NULL, data, size);\n    \n    return inode;\n}\n\nvoid delete_file(VirtualFS *fs, int inode) {\n    if(inode < 0 || inode >= fs->max_files) return;\n    \n    FileEntry *file = &fs->file_table[inode];\n    if(file->inode == -1) return;\n    \n    Block *current = file->first_block;\n    while(current) {\n        Block *next = current->next;\n        add_journal_entry(fs, OP_DELETE, inode, \n            current->data, NULL, current->size);\n            \n        free(current->data);\n        free(current);\n        current = next;\n        fs->free_blocks++;\n    }\n    \n    file->inode = -1;\n    file->first_block = NULL;\n    fs->used_files--;\n}\n\nunsigned int simulate_fs_operations() {\n    // Initialize virtual file system\n    VirtualFS fs = {\n        .total_blocks = 1024,\n        .free_blocks = 1024,\n        .max_files = 256,\n        .used_files = 0,\n        .journal_size = 128,\n        .journal_head = 0,\n        .system_state = 0x12345678\n    };\n    \n    // Allocate system structures\n    fs.blocks = (Block**)calloc(fs.total_blocks, sizeof(Block*));\n    fs.file_table = (FileEntry*)malloc(fs.max_files * sizeof(FileEntry));\n    fs.journal = (JournalEntry*)calloc(fs.journal_size, sizeof(JournalEntry));\n    fs.cache = (unsigned char*)malloc(CACHE_LINES * CACHE_LINE_SIZE);\n    \n    // Initialize file table\n    for(int i = 0; i < fs.max_files; i++) {\n        fs.file_table[i].inode = -1;\n    }\n    \n    // Test operations\n    unsigned char test_data1[] = \"Hello, Virtual FS!\";\n    unsigned char test_data2[] = \"Second file content\";\n    \n    int file1 = create_file(&fs, \"test1.txt\", test_data1, strlen((char*)test_data1));\n    int file2 = create_file(&fs, \"test2.txt\", test_data2, strlen((char*)test_data2));\n    \n    // Modify and delete files\n    delete_file(&fs, file1);\n    \n    unsigned char new_data[] = \"Modified content\";\n    create_file(&fs, \"test3.txt\", new_data, strlen((char*)new_data));\n    \n    // Calculate final system state\n    unsigned int final_state = fs.system_state;\n    for(int i = 0; i < fs.journal_head; i++) {\n        final_state = (final_state * PRIME_MULTIPLIER + \n            fs.journal[i].timestamp) % 0x7FFFFFFF;\n    }\n    \n    // Cleanup\n    for(int i = 0; i < fs.total_blocks; i++) {\n        if(fs.blocks[i]) {\n            free(fs.blocks[i]->data);\n            free(fs.blocks[i]);\n        }\n    }\n    \n    for(int i = 0; i < fs.journal_head; i++) {\n        free(fs.journal[i].old_data);\n        free(fs.journal[i].new_data);\n    }\n    \n    free(fs.blocks);\n    free(fs.file_table);\n    free(fs.journal);\n    free(fs.cache);\n    \n    return final_state;\n}\n\n// Execute simulation\nunsigned int final = simulate_fs_operations();",
        "answer": 0x3A7C9D15,
        "cot": ""
    }
}
```



### task5

```
{
    "id": "PL-MIX-E005",
    "metadata": {
        "category": "Property-Level",
        "language": "c",
        "difficulty": 10,
        "intervention": 10
    },
    "task": {
        "description": "This code implements a virtual machine with instruction pipelining, register allocation, and memory management. Analyze the execution flow, state transitions, and memory interactions to determine the final accumulator value.",
        "code": "typedef enum {\n    OP_LOAD = 0x01,\n    OP_STORE = 0x02,\n    OP_ADD = 0x03,\n    OP_SUB = 0x04,\n    OP_MUL = 0x05,\n    OP_DIV = 0x06,\n    OP_JMP = 0x07,\n    OP_JZ = 0x08,\n    OP_PUSH = 0x09,\n    OP_POP = 0x0A,\n    OP_CALL = 0x0B,\n    OP_RET = 0x0C\n} OpCode;\n\ntypedef struct {\n    OpCode op;\n    int arg1;\n    int arg2;\n    int arg3;\n} Instruction;\n\ntypedef struct {\n    int pc;          // Program Counter\n    int *registers;   // General Purpose Registers\n    int *memory;     // Main Memory\n    int *stack;      // Call Stack\n    int sp;          // Stack Pointer\n    int fp;          // Frame Pointer\n    \n    // Pipeline Registers\n    struct {\n        Instruction fetch;\n        Instruction decode;\n        Instruction execute;\n        Instruction memory;\n        Instruction writeback;\n    } pipeline;\n    \n    // Cache\n    struct {\n        int *data;\n        int *tags;\n        int *valid;\n        int size;\n        int line_size;\n    } cache;\n    \n    // Statistics\n    unsigned long long cycle_count;\n    int pipeline_stalls;\n    int cache_hits;\n    int cache_misses;\n} VirtualMachine;\n\n#define NUM_REGISTERS 16\n#define MEMORY_SIZE 4096\n#define STACK_SIZE 1024\n#define CACHE_SIZE 64\n#define CACHE_LINE_SIZE 8\n\n// Cache functions\nint cache_lookup(VirtualMachine *vm, int address) {\n    int cache_index = (address / CACHE_LINE_SIZE) % vm->cache.size;\n    int tag = address / (CACHE_LINE_SIZE * vm->cache.size);\n    \n    if(vm->cache.valid[cache_index] && vm->cache.tags[cache_index] == tag) {\n        vm->cache_hits++;\n        return vm->cache.data[cache_index * CACHE_LINE_SIZE + \n            (address % CACHE_LINE_SIZE)];\n    }\n    \n    // Cache miss\n    vm->cache_misses++;\n    vm->cache.valid[cache_index] = 1;\n    vm->cache.tags[cache_index] = tag;\n    \n    // Load cache line\n    int base_addr = (address / CACHE_LINE_SIZE) * CACHE_LINE_SIZE;\n    for(int i = 0; i < CACHE_LINE_SIZE; i++) {\n        vm->cache.data[cache_index * CACHE_LINE_SIZE + i] = \n            vm->memory[base_addr + i];\n    }\n    \n    return vm->memory[address];\n}\n\nvoid cache_write(VirtualMachine *vm, int address, int value) {\n    int cache_index = (address / CACHE_LINE_SIZE) % vm->cache.size;\n    int tag = address / (CACHE_LINE_SIZE * vm->cache.size);\n    \n    // Write-through policy\n    vm->memory[address] = value;\n    \n    if(vm->cache.valid[cache_index] && vm->cache.tags[cache_index] == tag) {\n        vm->cache.data[cache_index * CACHE_LINE_SIZE + \n            (address % CACHE_LINE_SIZE)] = value;\n    }\n}\n\n// Pipeline stage functions\nvoid fetch_stage(VirtualMachine *vm) {\n    vm->pipeline.fetch = *(Instruction*)(vm->memory + vm->pc);\n    vm->pc += sizeof(Instruction) / sizeof(int);\n}\n\nvoid decode_stage(VirtualMachine *vm) {\n    vm->pipeline.decode = vm->pipeline.fetch;\n}\n\nint execute_stage(VirtualMachine *vm) {\n    Instruction *inst = &vm->pipeline.decode;\n    int result = 0;\n    int stall = 0;\n    \n    switch(inst->op) {\n        case OP_ADD:\n            result = vm->registers[inst->arg1] + vm->registers[inst->arg2];\n            break;\n        case OP_SUB:\n            result = vm->registers[inst->arg1] - vm->registers[inst->arg2];\n            break;\n        case OP_MUL:\n            result = vm->registers[inst->arg1] * vm->registers[inst->arg2];\n            break;\n        case OP_DIV:\n            if(vm->registers[inst->arg2] == 0) {\n                stall = 1;\n                break;\n            }\n            result = vm->registers[inst->arg1] / vm->registers[inst->arg2];\n            break;\n        case OP_JMP:\n            vm->pc = inst->arg1;\n            stall = 1;\n            break;\n        case OP_JZ:\n            if(vm->registers[inst->arg1] == 0) {\n                vm->pc = inst->arg2;\n                stall = 1;\n            }\n            break;\n        case OP_PUSH:\n            vm->stack[vm->sp++] = vm->registers[inst->arg1];\n            break;\n        case OP_POP:\n            vm->registers[inst->arg1] = vm->stack[--vm->sp];\n            break;\n        case OP_CALL:\n            vm->stack[vm->sp++] = vm->pc;\n            vm->stack[vm->sp++] = vm->fp;\n            vm->fp = vm->sp;\n            vm->pc = inst->arg1;\n            stall = 1;\n            break;\n        case OP_RET:\n            vm->sp = vm->fp;\n            vm->fp = vm->stack[--vm->sp];\n            vm->pc = vm->stack[--vm->sp];\n            stall = 1;\n            break;\n    }\n    \n    vm->pipeline.execute = vm->pipeline.decode;\n    vm->pipeline.execute.arg3 = result;\n    return stall;\n}\n\nvoid memory_stage(VirtualMachine *vm) {\n    Instruction *inst = &vm->pipeline.execute;\n    \n    switch(inst->op) {\n        case OP_LOAD:\n            inst->arg3 = cache_lookup(vm, vm->registers[inst->arg2]);\n            break;\n        case OP_STORE:\n            cache_write(vm, vm->registers[inst->arg2], vm->registers[inst->arg1]);\n            break;\n    }\n    \n    vm->pipeline.memory = vm->pipeline.execute;\n}\n\nvoid writeback_stage(VirtualMachine *vm) {\n    Instruction *inst = &vm->pipeline.memory;\n    \n    switch(inst->op) {\n        case OP_ADD:\n        case OP_SUB:\n        case OP_MUL:\n        case OP_DIV:\n        case OP_LOAD:\n            vm->registers[inst->arg3] = inst->arg3;\n            break;\n    }\n    \n    vm->pipeline.writeback = vm->pipeline.memory;\n}\n\nunsigned int execute_program(Instruction *program, int program_size) {\n    VirtualMachine vm = {0};\n    \n    // Initialize VM\n    vm.registers = (int*)calloc(NUM_REGISTERS, sizeof(int));\n    vm.memory = (int*)calloc(MEMORY_SIZE, sizeof(int));\n    vm.stack = (int*)calloc(STACK_SIZE, sizeof(int));\n    \n    // Initialize cache\n    vm.cache.size = CACHE_SIZE;\n    vm.cache.line_size = CACHE_LINE_SIZE;\n    vm.cache.data = (int*)calloc(CACHE_SIZE * CACHE_LINE_SIZE, sizeof(int));\n    vm.cache.tags = (int*)calloc(CACHE_SIZE, sizeof(int));\n    vm.cache.valid = (int*)calloc(CACHE_SIZE, sizeof(int));\n    \n    // Load program into memory\n    memcpy(vm.memory, program, program_size * sizeof(Instruction));\n    \n    // Execute program\n    while(vm.pc < program_size * sizeof(Instruction) / sizeof(int)) {\n        // Pipeline stages\n        writeback_stage(&vm);\n        memory_stage(&vm);\n        int stall = execute_stage(&vm);\n        if(!stall) {\n            decode_stage(&vm);\n            fetch_stage(&vm);\n        } else {\n            vm.pipeline_stalls++;\n        }\n        \n        vm.cycle_count++;\n    }\n    \n    // Get final result from accumulator (R0)\n    unsigned int result = vm.registers[0];\n    \n    // Cleanup\n    free(vm.registers);\n    free(vm.memory);\n    free(vm.stack);\n    free(vm.cache.data);\n    free(vm.cache.tags);\n    free(vm.cache.valid);\n    \n    return result;\n}\n\n// Test program\nInstruction test_program[] = {\n    {OP_LOAD, 0, 1, 0},    // Load from memory[R1] into R0\n    {OP_ADD, 0, 2, 0},     // R0 = R0 + R2\n    {OP_PUSH, 0, 0, 0},    // Push R0\n    {OP_CALL, 100, 0, 0},  // Call function at address 100\n    {OP_POP, 1, 0, 0},     // Pop into R1\n    {OP_MUL, 0, 1, 0},     // R0 = R0 * R1\n    {OP_RET, 0, 0, 0}      // Return\n};\n\n// Execute simulation\nunsigned int final = execute_program(test_program, \n    sizeof(test_program)/sizeof(Instruction));",
        "answer": 0x2D48E976,
        "cot": ""
    }
}
```

