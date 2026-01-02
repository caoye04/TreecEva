import itertools

def analyze_signal(data, threshold=0.75):
    # Irrelevant signal processing function (dead path)
    filtered = [x for x in data if abs(x) > threshold]
    return sum(filtered) / len(filtered) if filtered else 0

def compute_entropy(sequence):
    # Distractor: computes entropy but not used in final result
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 6)

def transform_dataset(records, key_map):
    # Complex red herring: transforms data but result unused
    mapped = {}
    for k, v in records.items():
        if k in key_map:
            mapped[key_map[k]] = v * 1.5 if v % 2 == 0 else v * 0.8
    return mapped

def detect_anomalies(time_series):
    # Dead logic path with misleading intermediate calculations
    anomalies = []
    baseline = sum(time_series) / len(time_series)
    for i, val in enumerate(time_series):
        if abs(val - baseline) > 0.5 * baseline and val > 10:
            anomalies.append(i)
    return anomalies

def merge_configs(*configs):
    # Unused utility with complex dictionary operations
    result = {}
    for config in configs:
        for k, v in config.items():
            if k in result:
                if isinstance(v, dict) and isinstance(result[k], dict):
                    result[k].update(v)
                else:
                    result[k] += v
            else:
                result[k] = v
    return result

def evaluate_performance(weights, results):
    # CORE LOGIC: This is where the actual answer is computed
    weighted_sum = 0.0
    normalization = 0
    
    # Real computation begins here — deeply nested and mixed with distractors
    for metric, weight in weights.items():
        if metric.startswith('perf_'):
            raw = results.get(metric.replace('perf_', ''), 0)
            cap = 100 if 'throughput' in metric else 90
            adjusted = min(raw, cap)
            contribution = adjusted * weight
            weighted_sum += contribution
            normalization += weight
    
    # Additional relevant logic buried in noise
    throughput_val = results.get('throughput', 0)
    latency_penalty = 0
    if throughput_val > 75:
        latency_ref = results.get('latency', 0)
        if latency_ref > 0:
            penalty_factor = 1.2 - (100 / (latency_ref + 25))
            latency_penalty = throughput_val * penalty_factor * 0.05
    
    # Final calculation
    base_score = weighted_sum / normalization if normalization else 0
    final_adjustment = base_score - latency_penalty
    
    # Decoy operation: looks important but doesn't affect anything
    _ = [x**2 for x in range(8) if x % 2 == 0]
    
    return int(round(final_adjustment))

# --- MAIN EXECUTION BLOCK ---

# Irrelevant dataset (distractor)
signal_data = [0.1, 0.8, -1.2, 0.9, 0.76, 1.5]
entropy_sequence = ['A', 'B', 'B', 'C', 'A', 'A', 'D']
time_series_data = [12, 15, 9, 40, 8, 11, 52]

# Unused configurations
config_a = {'debug': True, 'level': 2, 'flags': {'opt': 1}}
config_b = {'level': 3, 'flags': {'secure': False}, 'timeout': 30}

# Real input data
metric_weights = {
    'perf_throughput': 0.4,
    'perf_latency': 0.3,
    'perf_accuracy': 0.2,
    'perf_memory': 0.1
}

raw_results = {
    'throughput': 88,
    'latency': 50,
    'accuracy': 96,
    'memory': 70,
    'cache_hit': 82  # unused metric
}

# Call irrelevant functions to create distraction
_ = analyze_signal(signal_data)
_ = compute_entropy(entropy_sequence)
_ = detect_anomalies(time_series_data)
_ = transform_dataset({'X1': 4, 'X2': 6}, {'X1': 'Y1', 'X2': 'Y2'})
_ = merge_configs(config_a, config_b)

# Key execution point
final_score = evaluate_performance(metric_weights, raw_results)

# Output result as required
print(f"Target result: {final_score}")