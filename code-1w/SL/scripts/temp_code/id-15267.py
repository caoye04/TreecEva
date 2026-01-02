import itertools

# Simulated system performance metrics (some are red herrings)
def collect_diagnostics():
    return {
        'latency_ms': 45,
        'throughput_ops': 980,
        'cpu_load': 78,
        'mem_usage_mb': 1024,
        'disk_iops': 230,
        'error_rate': 0.002,
        'queue_depth': 15,
        'cache_hit_ratio': 0.88
    }

def preprocess_data(raw):
    # Irrelevant transformation chain (distractor)
    processed = {k: v * 1.05 for k, v in raw.items()}
    processed['latency_ms'] = max(processed['latency_ms'], 10)
    processed['norm_throughput'] = processed['throughput_ops'] / 100
    return processed

def compute_health_flags(data):
    # Misleading health indicators (partially irrelevant)
    flags = {}
    for key in data:
        if 'error' in key or 'load' in key:
            flags[key] = data[key] > 50
        else:
            flags[key] = data[key] < 500
    return flags

def analyze_pattern_sequence():
    # Dead-end function: generates unused sequence patterns
    seq = [i ** 2 for i in range(1, 20) if i % 3 != 0]
    rolling_avg = [sum(seq[i:i+3]) / 3 for i in range(len(seq) - 2)]
    filtered_pairs = list(itertools.combinations([x for x in rolling_avg if x > 100], 2))
    return len(filtered_pairs)  # Never used

def calculate_derived_metrics(data):
    # Mix of relevant and irrelevant derived values
    derived = {
        'efficiency_index': (data['throughput_ops'] * data['cache_hit_ratio']) / data['latency_ms'],
        'saturation_level': (data['cpu_load'] + data['mem_usage_mb'] / 100) / 2,
        'risk_factor': data['error_rate'] * data['queue_depth'],
        'bandwidth_estimate': data['throughput_ops'] * data['latency_ms']  # Not used later
    }
    return derived

def filter_outliers(values):
    # Unused utility (red herring)
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean) <= 2 * std_dev]

def validate_consistency(metrics):
    # Distractor logic with side computations
    keys_of_interest = ['latency_ms', 'throughput_ops', 'error_rate']
    baseline_ref = {k: v * 0.95 for k, v in metrics.items() if k in keys_of_interest}
    drifts = {k: abs(metrics[k] - baseline_ref[k]) for k in baseline_ref}
    total_drift = sum(drifts.values())
    consistency_flag = total_drift < 10
    return consistency_flag  # Used but doesn't affect final score

def normalize_metric(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def evaluate_performance(metrics, weights):
    # Core logic buried among noise
    base_keys = ['latency_ms', 'throughput_ops', 'error_rate', 'cache_hit_ratio']
    ranges = {
        'latency_ms': (10, 100),
        'throughput_ops': (500, 1500),
        'error_rate': (0.0001, 0.01),
        'cache_hit_ratio': (0.7, 1.0)
    }
    
    # Normalize relevant metrics
    normalized = {}
    for key in base_keys:
        reverse = key in ['latency_ms', 'error_rate']  # Lower is better
        val = metrics[key]
        norm = normalize_metric(val, *ranges[key])
        normalized[key] = 1 - norm if reverse else norm
    
    # Weighted aggregation
    score = sum(normalized[k] * weights[k] for k in base_keys)
    return int(score * 100)  # Final integer score

# --- Main Execution ---
if __name__ == '__main__':
    raw_metrics = collect_diagnostics()
    cleaned = preprocess_data(raw_metrics)
    
    # Irrelevant intermediate steps
    health_flags = compute_health_flags(cleaned)
    derived = calculate_derived_metrics(cleaned)
    _ = analyze_pattern_sequence()  # Dead call
    _ = filter_outliers(list(cleaned.values()))  # Dead call
    
    # Validation that doesn't alter flow
    is_consistent = validate_consistency(cleaned)
    
    # Critical weighting scheme (only these matter)
    weights = {
        'latency_ms': 0.3,
        'throughput_ops': 0.4,
        'error_rate': 0.2,
        'cache_hit_ratio': 0.1
    }
    
    # Key statement
    final_score = evaluate_performance(cleaned, weights)
    
    # Output result
    print(f"Result: {final_score}")