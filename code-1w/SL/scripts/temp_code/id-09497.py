def analyze_workload(nodes, tasks):
    node_load = {}
    temp_buffer = []
    total_tasks = len(tasks)
    active_nodes = set()

    for idx, task in enumerate(tasks):
        assigned_node = task % len(nodes)
        if assigned_node not in node_load:
            node_load[assigned_node] = 0
        node_load[assigned_node] += (idx + 1) * 3
        active_nodes.add(assigned_node)

    # Distractor: irrelevant temperature simulation
    temp_sum = 0
    for i in range(len(nodes)):
        temp_sum += (i * 1.5) ** 2
    avg_temp = temp_sum / len(nodes) if nodes else 0

    # Real computation begins: normalize loads
    max_load = max(node_load.values()) if node_load else 1
    normalized = {k: v / max_load for k, v in node_load.items()}

    # Use of zip and enumerate together
    efficiency_flags = []
    for i, (node_id, norm_val) in enumerate(zip(node_load.keys(), normalized.values())):
        flag = (i + norm_val) > 1.0
        efficiency_flags.append(flag)

    # Set operations for filtering efficient nodes
    efficient_set = set(i for i, flag in enumerate(efficiency_flags) if flag)
    inefficient_set = set(range(len(nodes))) - efficient_set

    # Secondary distractor: dead code path (never alters final result)
    debug_stats = {}
    if len(efficient_set) == 0:
        debug_stats['warning'] = 'No efficient nodes'
    else:
        debug_stats['redundant_calc'] = sum(efficient_set) * 0.1

    # Core logic: capacity based on load distribution
    high_load_nodes = {k for k, v in node_load.items() if v > max_load * 0.7}
    coverage_ratio = len(high_load_nodes & efficient_set) / len(efficient_set) if efficient_set else 0

    base_capacity = sum(node_load.values())
    adjustment_factor = len(active_nodes) / len(nodes) if nodes else 0
    final_capacity = int(base_capacity * adjustment_factor * (1 + coverage_ratio))

    # This print is required to expose the answer
    print(f"Result: {final_capacity}")
    return final_capacity

# Inputs
compute_nodes = [f'node_{i}' for i in range(7)]
task_queue = [2, 5, 1, 8, 3, 9, 4, 7]

# Execution entry point
final_capacity = analyze_workload(compute_nodes, task_queue)