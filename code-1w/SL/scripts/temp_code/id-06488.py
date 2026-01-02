import math

def analyze_components(input_list, threshold):
    # Irrelevant helper function – dead code path
    return [x for x in input_list if x > threshold]

def preprocess_signal(signal_data):
    # Distractor: signal processing that isn't used in final result
    normalized = [(x - min(signal_data)) / (max(signal_data) - min(signal_data)) for x in signal_data]
    return [round(x * 100) for x in normalized]

def calculate_entropy(values):
    # Unused advanced calculation – misleading intermediate concept
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_outliers(data, factor=1.5):
    # Red herring function – looks important but not used
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def build_lookup(keys, values):
    # Creates a decoy dictionary structure – never accessed
    lookup = {}
    for k, v in zip(keys, values):
        lookup[k] = v * 2 if v % 2 == 0 else v * 3
    return lookup

def evaluate_performance(metrics, baseline):
    # Core logic embedded within distractions
    temp_results = []
    adjustment_factor = 0.92
    
    # Real computation begins
    for metric in metrics:
        if len(metric) == 3:
            a, b, c = metric
            # Meaningful check
            if (a + b) % 2 == 0 and c > 50:
                # Valid transformation
                transformed = (a * a) + (b // 2) - (c % 7)
                temp_results.append(transformed)
    
    # Decoy aggregation
    fake_aggregate = sum([x ** 0.5 for x in temp_results if x > 0])
    
    # Actual key computation
    base_total = sum(temp_results)
    multiplier = len(metrics) if base_total > 100 else len(metrics) * 2
    
    # Apply adjustment using dictionary-based weight lookup
    weights = {'level1': 1.1, 'level2': 1.3, 'critical': 1.6}
    level_keys = set(weights.keys())  # Use of set operation
    active_levels = set(['level1', 'level2'])
    applied_levels = level_keys & active_levels  # Set intersection – actual use
    
    enhancement = 1.0
    if 'level1' in applied_levels:
        enhancement *= weights['level1']
    
    # Linear search through list to find first qualifying condition
    thresholds = [50, 75, 100, 120]
    ceiling = 100
    for t in thresholds:
        if base_total > t:
            ceiling = t + 50
            break
    
    # Final computation chain
    raw_score = base_total * multiplier * enhancement
    if raw_score > ceiling:
        raw_score = ceiling + (raw_score - ceiling) * 0.3
    
    # Final answer derived after multiple steps
    final_score = int(raw_score - 18)  # Key deterministic offset
    
    # Output required format
    print(f"Result: {final_score}")
    return final_score

# Main execution block with realistic scenario: system diagnostics
metric_set = [
    (4, 6, 55),   # triggers condition
    (3, 5, 40),   # skipped (c <= 50)
    (2, 8, 76),   # triggers condition
    (5, 3, 90),   # skipped ((a+b) odd)
    (6, 4, 88)    # triggers condition
]

benchmark_data = {
    'version': '3.7.1',
    'calibration': [0.1, 0.4, 0.8, 0.9],
    'nodes_active': 12,
    'peak_load': 98765
}

# Unused variables – red herrings
baseline_metrics = [95, 87, 91, 89]
calibration_phase = preprocess_signal(benchmark_data['calibration'])
entropy_value = calculate_entropy(calibration_phase)
lookup_table = build_lookup(['A','B','C'], [10,20,30])

# Critical call
final_score = evaluate_performance(metric_set, benchmark_data)