import math

def analyze_latency(nodes):
    # Irrelevant function - dead code path
    return sum([len(node['routes']) for node in nodes if node['active']])

def estimate_capacity(loads):
    # Misleading intermediate calculation
    base = sum(loads) / len(loads)
    adjustment = math.sin(len(loads) % 3)
    return int(base * (1 + adjustment))

def simulate_congestion(flow_matrix):
    # Unused complex transformation
    n = len(flow_matrix)
    dummy_result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dummy_result[i][j] = flow_matrix[i][j] * (i + j + 1)
    return dummy_result

def validate_topology(nodes):
    # Distractor: checks structure but not used in final result
    for node in nodes:
        if not isinstance(node, dict) or 'id' not in node:
            return False
    ids = [node['id'] for node in nodes]
    return len(ids) == len(set(ids))

def calculate_efficiency_score(config):
    # Red herring function with complex logic but no impact
    score = 0
    for k, v in config.items():
        if 'bandwidth' in k:
            score += v ** 0.5
        elif 'latency' in k:
            score -= v // 2
    return round(score, 3)

def preprocess_traffic_data(raw_loads):
    # Slicing and filtering - partially relevant preprocessing
    cleaned = [x for x in raw_loads if x > 0]  # List comprehension
    window_avg = [sum(cleaned[i:i+3]) / 3 for i in range(len(cleaned)-2)]
    return [int(x * 1.1) for x in window_avg]

def extract_critical_nodes(network):
    # Complex filtering with slicing distraction
    indices = [i for i, node in enumerate(network) if node.get('priority') == 'high']
    return network[::2] + [network[i] for i in indices]  # Mix of slicing and comprehension

def optimize_bandwidth(nodes, load_profile):
    # Core function with key logic embedded in noise
    
    # Irrelevant preprocessing steps
    _ = analyze_latency(nodes)
    _ = validate_topology(nodes)
    
    # Preprocess load profile - actually used
    processed_load = preprocess_traffic_data(load_profile)
    
    # Extract subsets - some are red herrings
    critical_nodes = extract_critical_nodes(nodes)
    segment_a = nodes[1:-1]  # Slicing - unused
    segment_b = nodes[::-1]   # Reverse slice - unused
    
    # Real computation begins here
    base_capacity = estimate_capacity(processed_load)  # Uses estimated value despite misleading name
    
    # Apply efficiency weighting based on node count
    multiplier = len(critical_nodes) / len(nodes)
    
    # Final bandwidth calculation - depends only on this path
    raw_sum = sum(processed_load)
    adjusted_total = raw_sum * multiplier
    
    # Key rounding behavior
    final_val = int(adjusted_total // 1.7)  # Integer division with non-trivial divisor
    
    # Simulate minor correction factor
    correction = len(processed_load) % 4
    final_val += correction
    
    return final_val

# Main execution block
if __name__ == '__main__':
    # Input data setup
    network_nodes = [
        {'id': 1, 'routes': [2,3], 'active': True, 'priority': 'low', 'latency_ms': 12},
        {'id': 2, 'routes': [1,4], 'active': True, 'priority': 'high', 'latency_ms': 8},
        {'id': 3, 'routes': [4], 'active': False, 'priority': 'medium', 'latency_ms': 15},
        {'id': 4, 'routes': [1,2,3], 'active': True, 'priority': 'high', 'latency_ms': 6}
    ]
    
    traffic_load = [125, -30, 200, 0, 175, 95, -50, 310, 180]
    
    # Dead code - simulation not connected to output
    config_map = {'bandwidth_init': 1000, 'latency_cap': 20}
    _ = calculate_efficiency_score(config_map)
    
    flow_matrix = [[0, 50, 30, 40], [50, 0, 20, 60], [30, 20, 0, 25], [40, 60, 25, 0]]
    _ = simulate_congestion(flow_matrix)
    
    # Actual target computation
    final_bandwidth = optimize_bandwidth(network_nodes, traffic_load)
    
    # Output result as required
    print(f"Target result: {final_bandwidth}")