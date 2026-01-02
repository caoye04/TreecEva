def calculate_performance(op_list, overhead):
    base_efficiency = sum(op_list) / len(op_list)
    adjustment_factor = 0.9 if base_efficiency > 50 else 0.7
    return base_efficiency * adjustment_factor - overhead

# System performance metrics
task_load = [45, 60, 55, 70, 50]
overhead_cost = 12.5

# Irrelevant auxiliary variable (minimal distraction)
placeholder_value = "N/A"

# Core computation
average_ops = sum(task_load) / len(task_load)
high_performer_count = len([x for x in task_load if x >= 60])

# Key statement
efficiency_score = calculate_performance(task_load, overhead_cost)

# Output result
print(f"Result: {efficiency_score}")