def calculate_priority(tasks, queue):
    base_score = len(tasks)
    redundancy_check = {x: tasks.count(x) for x in set(tasks)}
    filtered_tasks = [t for t in tasks if 'critical' in t]

    priority_map = {}
    for task in filtered_tasks:
        level = task.split('_')[-1]
        if level.isdigit():
            priority_map[task] = int(level) ** 2

    temp_sum = 0
    for val in priority_map.values():
        temp_sum += val

    # Misleading computation - not used in final result
    phantom_queue = queue.copy()
    phantom_queue.append('placeholder_task')
    shadow_weight = sum([len(t) for t in phantom_queue]) * 0.1

    # Another distraction: unused conditional expression
    fallback = 10 if len(queue) > 100 else 0

    adjustment_factor = len(filtered_tasks) if filtered_tasks else 1

    final_value = temp_sum / adjustment_factor if adjustment_factor != 0 else 0

    return int(final_value)

# Main execution context
all_tasks = ['task_low_1', 'task_critical_3', 'task_medium_2', 'task_critical_5', 'task_critical_3']
backup_queue = ['spare_1', 'spare_2', 'spare_3']

# Irrelevant preprocessing
reversed_names = [t[::-1] for t in all_tasks]
duplicate_count = len(all_tasks) - len(set(all_tasks))

# Key data structure transformation
urgent_tasks = [t for t in all_tasks if 'critical' in t]

# Dead code path (never executed)
if False:
    urgent_tasks = [t.upper() for t in urgent_tasks]

# Core computation point
final_priority = calculate_priority(urgent_tasks, backup_queue)

# Output required format
print(f"Result: {final_priority}")