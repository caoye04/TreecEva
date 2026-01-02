from itertools import combinations

def preprocess_records(raw_entries):
    # Irrelevant transformation: convert timestamps to offsets (not used in final logic)
    time_offsets = [entry['ts'] - 1000 for entry in raw_entries if 'ts' in entry]
    filtered_names = [e['name'].upper() for e in raw_entries if len(e['name']) > 2]
    return filtered_names  # Distractor return, not used later

def calculate_baseline(samples, factor=1.5):
    base = sum([s['value'] for s in samples]) / len(samples)
    adjustment = factor * 0.1
    return base + adjustment  # Semi-relevant, but only base matters

def analyze_trends(data_stream):
    trends = {}
    for i in range(1, len(data_stream)):
        delta = data_stream[i] - data_stream[i-1]
        trend_key = 'up' if delta > 0 else 'down'
        trends[i] = {'delta': delta, 'trend': trend_key}
    
    # Complex but irrelevant aggregation
    counts = {k: 0 for k in ['up', 'down']}
    for record in trends.values():
        counts[record['trend']] += 1
    
    # Dead code path (never accessed in control flow)
    if False:
        return max(trends.keys())
    
    return trends  # Not actually used

def normalize_readings(raw_seq, ceiling=100):
    normalized = []
    for val in raw_seq:
        capped = min(val, ceiling)
        scaled = round(capped / ceiling, 3)
        normalized.append(scaled)
    return normalized

def compute_entropy(weights):
    import math
    entropy = 0
    for w in weights:
        if w > 0:
            entropy -= w * math.log(w)
    return round(entropy, 4)  # Computed but unused in final score

def evaluate_performance(weight_map, data_list):
    total = 0
    metric_weights = [weight_map[k] for k in ['accuracy', 'latency', 'throughput'] if k in weight_map]
    
    # Use itertools to generate all possible 2-item combinations of data points
    pairs = list(combinations(data_list, 2))
    pair_contributions = []
    
    for a, b in pairs:
        diff = abs(a - b)
        if diff > 0.1:
            pair_contributions.append(diff * 0.5)
    
    # Real computation starts here
    base_value = sum(data_list) * 10
    weight_sum = sum(metric_weights)
    adjusted = base_value * weight_sum
    
    # Additional red herring: complex conditional that doesn't affect outcome
    if len(pair_contributions) > 5:
        adjusted *= 0.95
    elif len(pair_contributions) == 0:
        adjusted += 10
    else:
        adjusted += 5  # This branch triggers
    
    # Final deterministic step
    final_component = adjusted + (metric_weights[0] * 100)
    return int(final_component)

# Main execution block
if __name__ == '__main__':
    # Input data
    records = [
        {'name': 'sensor1', 'value': 45, 'ts': 1005},
        {'name': 'x', 'value': 60, 'ts': 1010},
        {'name': 'zeta', 'value': 55, 'ts': 1015}
    ]

    readings = [88, 92, 76, 81, 96]

    # Distractor function calls
    _ = preprocess_records(records)
    _ = calculate_baseline(records, factor=2.0)
    _ = analyze_trends(readings)

    # Relevant processing
    normalized_data = normalize_readings(readings)
    
    # Entropy computed but not used in evaluation_performance
    weights = [0.4, 0.35, 0.25]
    _ = compute_entropy(weights)
    
    metric_weights = {
        'accuracy': 0.4,
        'latency': 0.35,
        'throughput': 0.25,
        'reliability': 0.1  # Unused key
    }
    
    # Key execution point
    final_score = evaluate_performance(metric_weights, normalized_data)
    
    print(f"Result: {final_score}")