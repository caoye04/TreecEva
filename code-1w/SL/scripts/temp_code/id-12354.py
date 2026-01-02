def calculate_performance(op_list, overhead):
    base_effort = sum(op_list) // len(op_list)
    adjusted = list(map(lambda x: (x + base_effort) // 2, op_list))
    total_adjusted = sum(adjusted[:len(adjusted)//2])
    return round(total_adjusted / (overhead + 1), 3)

# System performance metrics
operations = [84, 92, 78, 65, 96, 88]
overhead = 12
temp_buffer = operations[::-1]  # Irrelevant: reversed list not used in calculation
efficiency_ratio = calculate_performance(operations, overhead)
Result: efficiency_ratio