def calculate_network_flow(nodes, edges):
    base_flow = 0
    flow_map = {node: idx * 2 for idx, node in enumerate(nodes)}
    
    temp_val = 0
    for i, (src, dst) in enumerate(zip(nodes[:-1], nodes[1:])):
        edge_key = f'{src}-{dst}'
        if edge_key in edges:
            increment = (flow_map[src] + flow_map[dst]) // (i + 1)
            base_flow += increment
    
    adjustment_factor = 1.0
    flags = [True, False, True]
    if all(flags) or len(nodes) > 5:
        adjustment_factor = 0.5
    elif not any(flags):
        adjustment_factor = 2.0

    final_penalty = 0
    for k, v in flow_map.items():
        if v % 4 == 0:
            final_penalty += 1

    result = base_flow * adjustment_factor - final_penalty
    return int(result)

# Irrelevant helper (distractor)
def log_status(code):
    status_msg = "Operation completed" if code == 200 else "Error"
    return status_msg

# Setup data
nodes = ['router_a', 'switch_b', 'bridge_c', 'hub_d']
edges = {'router_a-switch_b': 10, 'switch_b-bridge_c': 5, 'bridge_c-hub_d': 3}

# Computation
flow_capacity = calculate_network_flow(nodes, edges)

# Output
print(f"Result: {flow_capacity}")