import itertools

# Simulated system performance metrics (some are red herrings)
def collect_diagnostics():
    return {
        'latency_ms': 120,
        'cpu_load': 75,
        'mem_util': 82,
        'disk_io': 45,
        'net_packets': 91,
        'cache_hit_ratio': 0.68,
        'queue_depth': 15,
        'error_rate': 0.03
    }

def normalize(value, min_val, max_val):
    # Normalize to 0-100 scale
    return 100 * (value - min_val) / (max_val - min_val) if max_val > min_val else 50

def apply_weight(val, weight):
    # Apply arbitrary weighting (used in final calculation)
    return val * weight

# Irrelevant transformation chain (distractor)
def transform_signal(data):
    result = 0
    for x in data:
        result ^= int(x * 17) & 255  # Bit manipulation red herring
    return result

def analyze_redundancy(pattern):
    counter = 0
    for a, b in itertools.pairwise(pattern):
        if a == b:
            counter += 1
    return counter > 5  # Dead logic path

def compute_entropy(seq):
    from math import log2
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy  # Unused metric

def filter_outliers(data_list, threshold=2):
    mean_val = sum(data_list) / len(data_list)
    std_dev = (sum((x - mean_val)**2 for x in data_list) / len(data_list))**0.5
    return [x for x in data_list if abs(x - mean_val) <= threshold * std_dev]

# Core evaluation logic
def evaluate_performance(metrics, weights):
    score_components = []
    
    # Relevant metrics with real impact
    relevant_keys = ['latency_ms', 'cpu_load', 'mem_util', 'error_rate']
    
    # Misleading pre-processing (looks important but some parts unused)
    normalized = {}
    for key, val in metrics.items():
        if key == 'latency_ms':
            normalized[key] = 100 - normalize(val, 10, 200)  # Inverted: lower latency = better
        elif key == 'error_rate':
            normalized[key] = 100 - normalize(val, 0.01, 0.1)
        elif key in ['cpu_load', 'mem_util']:
            normalized[key] = 100 - normalize(val, 50, 100)
        else:
            normalized[key] = 50  # Neutral for irrelevant metrics
    
    # Weighted aggregation
    total_weight = 0
    for key in relevant_keys:
        weight = weights.get(key, 0)
        if weight > 0:
            raw_contrib = apply_weight(normalized[key], weight)
            score_components.append(raw_contrib)
            total_weight += weight
    
    if total_weight == 0:
        return 0
    
    final_raw = sum(score_components) / total_weight
    
    # Final adjustment based on fake redundancy check (dead branch)
    pattern = [int(metrics[k]) for k in ['cpu_load', 'mem_util', 'disk_io'] if k in metrics]
    if analyze_redundancy(pattern * 2):  # Always false due to data
        final_raw = max(final_raw - 10, 0)
    
    return round(final_raw, 4)

# --- Entry Point ---
if __name__ == '__main__':
    # Collect real data
    system_metrics = collect_diagnostics()
    
    # Define actual weights (only some keys matter)
    importance_weights = {
        'latency_ms': 0.3,
        'cpu_load': 0.25,
        'mem_util': 0.25,
        'error_rate': 0.2
    }
    
    # Distractor: signal processing on unrelated data
    diagnostic_keys = list(system_metrics.keys())
    key_hash = transform_signal([ord(diagnostic_keys[i][0]) for i in range(len(diagnostic_keys))])
    
    # Fake entropy analysis (unused)
    dummy_sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    diversity_metric = compute_entropy(dummy_sequence)
    
    # Filtering outlier attempt (no effect)
    cleaned_vals = filter_outliers(list(system_metrics.values()), threshold=1.5)
    
    # Critical execution point
    final_score = evaluate_performance(system_metrics, importance_weights)
    
    # Print required output
    print(f"Result: {final_score}")