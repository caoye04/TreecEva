"""
配置文件和COT模板定义 - 增强版行内注释
"""

# 行内注释模板 - 增强版
INLINE_COT_TEMPLATES = {
    'assign_constant': {
        'template': "  # 赋值: {var} = {value}",
    },
    
    'assign_expr': {
        'template': "  # 计算: {expr_detail} = {result}",
    },
    
    'aug_assign': {
        'template': "  # 更新: {var} 从第{def_line}行的 {old_val} 变为 {old_val}{op}{operand} = {result}",
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

# COT输出配置
COT_CONFIG = {
    'show_line_numbers': True,
    'show_variable_state': False,
    'compact_mode': True,
    'track_variable_source': True,  # 追踪变量来源
}