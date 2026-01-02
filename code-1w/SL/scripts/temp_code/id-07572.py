from itertools import cycle

def balance_workload(nodes, tasks):
    base_capacity = 3
    node_pool = [base_capacity * (i + 1) for i in range(nodes)]
    temp_shadow = [n * 2 for n in node_pool]  # Irrelevant transformation
    
    task_distribution = []
    load_tracker = {i: 0 for i in range(nodes)}
    
    # Simulate uneven task assignment
    for task_size in tasks:
        assigned = False
        for idx in range(nodes):
            if load_tracker[idx] + task_size <= node_pool[idx]:
                load_tracker[idx] += task_size
                task_distribution.append(idx)
                assigned = True
                break
        if not assigned:
            load_tracker[0] += task_size // 2  # Fallback with partial load

    # Dead code branch - never taken under current logic
    if len(task_distribution) > 100:
        scale_factor = sum(temp_shadow) / len(temp_shadow)
        for k in load_tracker:
            load_tracker[k] = int(load_tracker[k] * scale_factor)

    # Secondary processing: find max utilization relative to base
    normalized_loads = []
    for i in range(nodes):
        ratio = load_tracker[i] / node_pool[i]
        normalized_loads.append(round(ratio, 4))
    
    avg_normalized = sum(normalized_loads) / nodes
    peak_load = max(load_tracker.values())
    final_load = int(peak_load * avg_normalized)  # Key result computation
    
    return final_load

# Simulation parameters
tasks = [2, 3, 1, 4, 2, 3, 5, 1, 2, 4]
nodes = 4

# Misleading pre-computations
shadow_nodes = [n * 2 for n in [3, 6, 9, 12]]
dummy_calc = sum([x ** 2 for x in shadow_nodes]) // 2  # Unused value

final_load = balance_workload(nodes, tasks)
print(f"Result: {final_load}")