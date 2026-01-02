from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
def collect_sensor_data(nodes):
    readings = defaultdict(list)
    for node_id, values in nodes.items():
        if len(values) > 2:
            smoothed = sum(values) / len(values)
            readings['stable'].append(smoothed)
        else:
            readings['unstable'].append(sum(values))
    return readings

def compute_baseline(readings):
    base = 0
    temp_offsets = [1.2, 0.8, 1.5, 0.9]
    for val in temp_offsets:
        base += val * 0.5
    return int(base)

def filter_outliers(data_list, threshold=1.5):
    if not data_list:
        return []
    median_val = sorted(data_list)[len(data_list) // 2]
    return [x for x in data_list if abs(x - median_val) < threshold]

def evaluate_performance(weights, results):
    # Irrelevant helper computation (distractor)
    aux_sum = sum([i * i for i in range(4)])  # Unused later
    
    total_weight = sum(weights.values())
    normalized = {k: v / total_weight for k, v in weights.items()}
    
    # Simulated transformation chain
    transformed = []
    for val in results['stable']:
        transformed.append((val * 1.1) + 0.5)
    
    # Filtering step with red herring condition
    valid_results = filter_outliers(transformed)
    if len(valid_results) == 0:
        fallback = compute_baseline(results)
        return fallback * 2
    
    # Core logic contribution
    aggregate = sum(valid_results)
    
    # Multiple assignment distraction
    alpha, beta, gamma = 10, 20, 30
    beta = alpha + gamma  # Dead computation
    
    # Final weighted combination
    score = aggregate * normalized['efficiency']
    bonus = len(results['stable']) * 1.5
    final_score = int(score + bonus)
    
    # Extraneous bit manipulation (semi-relevant but doesn't alter flow)
    flag_mask = 0b1010
    debug_flag = flag_mask & 0b1111
    
    return final_score

# Main execution block
sensor_nodes = {
    'node_01': [23, 25, 24, 26],
    'node_02': [19, 20],
    'node_03': [31, 33, 30, 32],
    'node_04': [17],
    'node_05': [44, 46, 45]
}

raw_data = collect_sensor_data(sensor_nodes)
metric_weights = {
    'efficiency': 0.6,
    'latency': 0.2,
    'throughput': 0.15,
    'reliability': 0.05
}
# Misleading variable initialization
placeholder_result = [0] * len(sensor_nodes)

final_score = evaluate_performance(metric_weights, raw_data)
print(f"Result: {final_score}")