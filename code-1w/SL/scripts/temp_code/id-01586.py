def optimize_routing(flow_matrix, node_capacity):
    max_load = 0
    temp_buffer = []
    for row in flow_matrix:
        row_sum = sum(row)
        if row_sum > max_load:
            max_load = row_sum
        temp_buffer.append(row_sum * 0.1)  # Irrelevant computation

    adjustment_factor = 1.0
    if max_load > node_capacity * 0.75:
        adjustment_factor = 0.9
    elif max_load < node_capacity * 0.3:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 1.0

    # Simulate diagnostic check (dead code path for some cases)
    diagnostics = {}
    diagnostics['peak_flow'] = max_load
    diagnostics['capacity_util'] = max_load / node_capacity if node_capacity else 0
    diagnostics['status'] = 'optimal' if diagnostics['capacity_util'] < 0.8 else 'overloaded'

    # Dummy set operation with no impact
    unused_nodes = {i for i, row in enumerate(flow_matrix) if sum(row) == 0}
    backup_route_count = len(unused_nodes) * 2 if len(unused_nodes) > 2 else 0

    base_bandwidth = node_capacity * 1.5
    penalty = 0
    if max_load > node_capacity:
        penalty = (max_load - node_capacity) * 0.5

    final_bandwidth = (base_bandwidth - penalty) * adjustment_factor

    # Additional irrelevant transformation
    scaled_diagnostics = {k: round(v * 1.05, 2) for k, v in diagnostics.items() if isinstance(v, float)}

    return final_bandwidth

# Input data
flow_data = [
    [10, 20, 30],
    [5,  0,  15],
    [25, 10, 5]
]
node_limit = 45

# Execute
final_bandwidth = optimize_routing(flow_data, node_limit)
print(f"Result: {final_bandwidth}")