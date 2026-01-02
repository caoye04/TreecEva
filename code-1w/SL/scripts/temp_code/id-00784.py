def calculate_remaining_capacity(nodes, utilization):
    total_nodes = len(nodes)
    active_nodes = [node for node in nodes if node['status'] == 'active']
    inactive_count = total_nodes - len(active_nodes)

    # Misleading computation: average_load has no effect on final result
    average_load = sum(node['load'] for node in nodes) / total_nodes if total_nodes else 0
    threshold_exceeded = any(node['load'] > 80 for node in active_nodes)

    # Real logic begins: extract indices and map to capacity
    active_indices = {i for i, node in enumerate(nodes) if node['status'] == 'active'}
    capacity_map = {i: node['capacity'] for i, node in enumerate(nodes)}

    # Distractor: unused transformation of data
    scaled_utilization = [(util * 1.1) for util in utilization]
    filtered_util = [u for u in scaled_utilization if u < 95]

    # Core calculation using set operations and zip
    relevant_indices = active_indices.intersection(set(range(len(utilization))))
    paired_data = list(zip(relevant_indices, [utilization[i] for i in sorted(relevant_indices)]))

    # Compute base remaining capacity
    base_remaining = 0
    for idx, used in paired_data:
        allocated = capacity_map[idx]
        consumed = int(allocated * (used / 100))
        recovered = consumed * 0.1  # Simulate partial recovery
        net_usage = consumed - recovered
        base_remaining += allocated - net_usage

    # Secondary distractor: complex but unused structure
    backup_plan = {f'node_{i}': {'priority': (i*3)%7, 'fallback': False} for i in range(total_nodes)}
    for k, v in backup_plan.items():  
        v['fallback'] = v['priority'] > 5

    # Final adjustment based on redundancy factor
    redundancy_factor = 1.0 if len(active_nodes) > 2 else 0.9
    adjusted_capacity = base_remaining * redundancy_factor

    # Red herring: dead code path
    emergency_override = False
    if threshold_exceeded and inactive_count > 3:
        adjusted_capacity *= 0.8  # Never executed due to conditions

    final_capacity = int(adjusted_capacity)
    return final_capacity

# Setup input data
nodes = [
    {'status': 'active', 'load': 65, 'capacity': 100},
    {'status': 'inactive', 'load': 0, 'capacity': 80},
    {'status': 'active', 'load': 75, 'capacity': 120},
    {'status': 'active', 'load': 55, 'capacity': 90},
    {'status': 'maintenance', 'load': 10, 'capacity': 110}
]
utilization = [60, 70, 85, 50, 40]  # Percent usage corresponding to each node

# Execute main logic
capacity_snapshot = [node['capacity'] for node in nodes]
baseline_total = sum(capacity_snapshot)

# Key execution point
final_capacity = calculate_remaining_capacity(nodes, utilization)
print(f"Result: {final_capacity}")