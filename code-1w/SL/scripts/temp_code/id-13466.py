def balance_workload(nodes, tasks):
    base_capacity = 10
    overflow_threshold = 8
    node_loads = [0] * len(nodes)
    temp_buffer = []

    # Preprocess: categorize tasks by type (distraction: not all types affect logic)
    task_categories = ['critical', 'standard', 'low_priority']
    categorized_tasks = {t: [] for t in task_categories}
    for i, task in enumerate(tasks):
        category = task_categories[i % 3]
        categorized_tasks[category].append(task * (i + 1))  # Irrelevant scaling

    # Real workload assignment
    for idx, node_id in enumerate(nodes):
        assigned = len(tasks) // len(nodes) + (1 if idx < len(tasks) % len(nodes) else 0)
        raw_load = assigned * base_capacity * 0.9

        # Simulate dynamic adjustment with lambda helper
        adjust_load = lambda load, mod: load * 1.1 if mod > overflow_threshold else load * 0.95
        modulation_factor = (idx + 1) * 0.7
        adjusted = adjust_load(raw_load, modulation_factor)

        # Conditional expression for resilience boost (semi-relevant)
        resilience_boost = 2.5 if modulation_factor < 1.0 else 0
        node_loads[idx] = round(adjusted + resilience_boost, 2)

        # Dead code path: buffer accumulation with no downstream use
        if idx % 2 == 0:
            temp_buffer.extend([raw_load] * 2)

    # Secondary distraction: unused structure manipulation
    status_map = {i: 'active' if load > 6 else 'idle' for i, load in enumerate(node_loads)}
    avg_load = sum(node_loads) / len(node_loads)

    # Final computation using list comprehension (core step)
    normalized_loads = [max(load, avg_load) for load in node_loads]
    final_load = int(sum(normalized_loads) // 1.5)  # Key result derivation

    # Unused intermediate
    peak_deviation = max(abs(load - avg_load) for load in node_loads)

    return final_load

# Input setup
processing_nodes = ['n1', 'n2', 'n3', 'n4']
incoming_tasks = [3, 7, 2, 5, 8, 4, 6]

# Execution point
final_load = balance_workload(processing_nodes, incoming_tasks)
print(f"Result: {final_load}")