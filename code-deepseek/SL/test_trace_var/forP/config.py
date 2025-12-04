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