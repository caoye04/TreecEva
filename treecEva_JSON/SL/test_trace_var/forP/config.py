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