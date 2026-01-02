from collections import defaultdict
import math

# Simulate sensor network data processing with interference

def generate_noise(length):
    return [math.sin(i * 0.5) + math.cos(i * 0.3) for i in range(length)]

def parse_sensor_data(raw):
    # Irrelevant parsing logic (dead path)
    parsed = {}
    for k, v in raw.items():
        if isinstance(v, list):
            parsed[k] = sum(x ** 0.5 for x in v if x > 0)
    return parsed

def analyze_pattern(seq):
    # Misleading pattern analyzer (unused)
    count = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            count += 1
    return count

def filter_outliers(data_list):
    mean_val = sum(data_list) / len(data_list)
    std_dev = (sum((x - mean_val) ** 2 for x in data_list) / len(data_list)) ** 0.5
    return [x for x in data_list if abs(x - mean_val) <= 2 * std_dev]

def transform_node_weights(nodes):
    weighted_map = defaultdict(float)
    total_power = 0
    
    for node_id, attrs in nodes.items():
        signal = attrs['signal']
        hops = attrs['hops']
        age = attrs['age']
        
        # Core calculation: relevance score
        base_score = (signal ** 2) / (hops + 1)
        decay_factor = 0.95 ** age
        weighted_map[node_id] = base_score * decay_factor
        
        # Distractor: accumulate total power (not used later)
        total_power += signal * (hops % 3)
    
    # Another distractor: normalize using unused total
    if total_power > 0:
        for k in weighted_map:
            weighted_map[k] /= (total_power * 0.01)

    return dict(weighted_map)

def compute_entropy(values):
    # Unused advanced metric
    prob_dist = [v / sum(values) for v in values]
    return -sum(p * math.log(p) for p in prob_dist if p > 0)

def aggregate_performance(nodes):
    # Transform to weighted scores
    weights = transform_node_weights(nodes)
    
    # Extract scores and apply filtering (core path)
    raw_scores = list(weights.values())
    filtered_scores = filter_outliers(raw_scores)
    
    # Add noise to simulate environmental interference (but not really affecting outcome)
    noise = generate_noise(len(filtered_scores))
    adjusted = [s + n*0.01 for s, n in zip(filtered_scores, noise)]
    
    # Final aggregation
    avg_adjusted = sum(adjusted) / len(adjusted) if adjusted else 0
    peak = max(adjusted) if adjusted else 0
    
    # Critical result computation
    final_score = int(avg_adjusted * 1000) + int(peak * 100)
    
    # Red herring: entropy of noise
    _ = compute_entropy(noise)
    
    return final_score

# Setup realistic network node data
network_nodes = {
    'node_01': {'signal': 8.7, 'hops': 2, 'age': 3},
    'node_02': {'signal': 9.1, 'hops': 1, 'age': 5},
    'node_03': {'signal': 7.4, 'hops': 3, 'age': 2},
    'node_04': {'signal': 6.8, 'hops': 1, 'age': 4},
    'node_05': {'signal': 10.2, 'hops': 2, 'age': 1},
    'node_06': {'signal': 5.9, 'hops': 4, 'age': 6},
    'node_07': {'signal': 8.0, 'hops': 1, 'age': 3}
}

# Dead code path: full system diagnostic (never called)
full_diagnostic_run = False
if full_diagnostic_run:
    raw_input = {k: [v['signal']*2] for k, v in network_nodes.items()}
    parsed_data = parse_sensor_data(raw_input)
    pattern_trend = analyze_pattern([v[0] for v in parsed_data.values()])

# Execute main logic
final_score = aggregate_performance(network_nodes)
print(f"Result: {final_score}")