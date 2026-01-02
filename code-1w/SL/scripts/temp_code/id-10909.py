import itertools

def analyze_utilization(usage_log, threshold=0.75):
    high_load = []
    for entry in usage_log:
        avg_load = sum(entry['history']) / len(entry['history'])
        peak_load = max(entry['history'])
        if avg_load > threshold and peak_load > 0.9:
            high_load.append(entry['node_id'])
    return high_load

def calculate_redundancy(nodes, mode='hot'):
    redundancy_factor = 1
    if mode == 'hot':
        redundancy_factor = 2
    elif mode == 'warm':
        redundancy_factor = 1.5
    else:
        redundancy_factor = 1.2
    total_redundant_nodes = len(nodes) * redundancy_factor
    return int(total_redundant_nodes)

def generate_flow_paths(sources, destinations):
    paths = []
    for src, dst in itertools.product(sources, destinations):
        if src != dst:
            paths.append(f'{src}->{dst}')
    return paths[:10]

def optimize_allocation(resources, traffic):
    base_capacity = 0
    adjustment_factor = 1.0
    
    # Real computation steps
    for node, capacity in resources.items():
        base_capacity += capacity
        temp_adj = 0
        for load in traffic.get(node, []):
            if load > 0.8:
                temp_adj += 0.1
        adjustment_factor += temp_adj
    
    # Distractor: complex but unused calculation
    shadow_capacity = 0
    for k in resources:
        for t in range(3):
            shadow_capacity += (hash(k) % 100) * 0.01
    shadow_capacity = round(shadow_capacity, 2)
    
    # Another distractor: dead logic with early exit that isn't triggered
    emergency_mode = False
    fallback_capacities = []
    if len(resources) > 20:
        for val in resources.values():
            fallback_capacities.append(val * 0.5)
        return sum(fallback_capacities)
    
    # Actual answer computation
    final_bandwidth = int(base_capacity * adjustment_factor)
    
    # Irrelevant logging
    log_entry = {'stage': 'optimization', 'result': final_bandwidth, 'mode': 'standard'}
    return final_bandwidth

# Main execution
resource_map = {
    'server_alpha': 120,
    'server_beta': 95,
    'server_gamma': 140,
    'server_delta': 80
}

target_thresholds = [0.6, 0.7, 0.8]
current_mode = 'hot'

traffic_matrix = {
    'server_alpha': [0.7, 0.85, 0.92],
    'server_beta': [0.65, 0.71],
    'server_gamma': [0.5, 0.81, 0.83, 0.93],
    'server_delta': [0.79, 0.82]
}

# Unused but plausible-looking data structures
historical_trends = [
    {'week': 1, 'avg_load': 0.62},
    {'week': 2, 'avg_load': 0.68},
    {'week': 3, 'avg_load': 0.71}
]

redundant_count = calculate_redundancy(list(resource_map.keys()), current_mode)
utilized_nodes = analyze_utilization([
    {'node_id': 'server_alpha', 'history': [0.7, 0.8, 0.9]},
    {'node_id': 'server_beta', 'history': [0.6, 0.7, 0.65]}
])

path_list = generate_flow_paths(['A', 'B'], ['X', 'Y', 'Z'])

# Key statement
final_bandwidth = optimize_allocation(resource_map, traffic_matrix)

print(f"Result: {final_bandwidth}")