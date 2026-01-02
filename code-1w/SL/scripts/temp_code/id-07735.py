import itertools

# Simulated system performance metrics (some relevant, some red herrings)
def collect_diagnostics():
    return {
        'latency_ms': 120,
        'throughput_ops': 850,
        'error_rate': 0.03,
        'cpu_load': 78.5,
        'memory_mb': 4200,
        'disk_io': 140,
        'queue_depth': 6,
        'timeout_count': 2,
        'retry_attempts': 5,
        'cache_hit_ratio': 0.88
    }

def normalize(value, min_val, max_val):
    # Normalize to 0-1 scale
    return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))

def analyze_trends(data_points):
    # Irrelevant trend analysis (dead-end function)
    if len(data_points) < 3:
        return 0
    trends = [b - a for a, b in zip(data_points, data_points[1:])]
    return sum(1 for t in trends if t > 0) - sum(1 for t in trends if t < 0)

def filter_outliers(values, threshold=2.0):
    # Unused outlier removal (distractor)
    mean = sum(values) / len(values)
    std = (sum((x - mean)**2 for x in values) / len(values))**0.5
    return [v for v in values if abs(v - mean) <= threshold * std]

def calculate_entropy(data):
    # Red herring: entropy calculation not used in final score
    from math import log2
    total = sum(data.values())
    probabilities = [count / total for count in data.values()]
    return -sum(p * log2(p) for p in probabilities if p > 0)

def extract_key_signals(metrics):
    # Extract and transform only the relevant metrics
    signals = {}
    
    # Relevant transformations
    signals['response_time'] = normalize(metrics['latency_ms'], 50, 200)
    signals['success_rate'] = 1 - metrics['error_rate']
    signals['system_load'] = 1 - normalize(metrics['cpu_load'], 50, 100)
    signals['resource_efficiency'] = normalize(10000 - metrics['memory_mb'], 5000, 10000)
    
    # Generate distractor derived metrics
    signals['theoretical_bandwidth'] = metrics['throughput_ops'] * 0.75 / metrics['disk_io']
    signals['queue_pressure'] = metrics['queue_depth'] * metrics['timeout_count']
    
    return signals

def apply_weighting(factors, importance_map):
    # Apply weighted sum using list comprehension and zip
    return sum(factors[f] * importance_map[f] for f in factors if f in importance_map)

def generate_combinations(items):
    # Distractor: unused combinatorial explosion
    return list(itertools.combinations(items, 2))

def validate_integrity(checksums):
    # Fake validation chain
    base = 0
    for c in checksums:
        base ^= hash(str(c))
    return base % 1000

def evaluate_performance(raw_metrics, weight_profile):
    # Core logic buried in noise
    clean_signals = extract_key_signals(raw_metrics)
    
    # Define actual weights (only subset used)
    effective_weights = {
        'response_time': 0.35,
        'success_rate': 0.40,
        'system_load': 0.15,
        'resource_efficiency': 0.10
        # Note: other keys in clean_signals are ignored
    }
    
    # Use list comprehension to filter valid factor keys
    valid_factors = {k: v for k, v in clean_signals.items() if k in effective_weights}
    
    # Compute final weighted score
    raw_score = apply_weighting(valid_factors, effective_weights)
    
    # Final scaling to 0-100 range
    scaled_score = round(raw_score * 100, 4)
    
    # Introduce decoy transformation
    adjusted_score = scaled_score * (1 + 0.01 * raw_metrics.get('retry_attempts', 0))
    
    # The real answer is scaled_score, not adjusted_score
    return scaled_score

# Irrelevant data structures
telemetry_log = [
    {'timestamp': 1001, 'event': 'start', 'pid': 101},
    {'timestamp': 1005, 'event': 'read', 'pid': 102},
    {'timestamp': 1010, 'event': 'write', 'pid': 101}
]

feature_flags = {
    'enable_cache': True,
    'debug_mode': False,
    'experimental_parser': None
}

# Simulated historical data (unused)
historical_throughput = [780, 820, 850, 830, 810, 860, 890]

# Key execution begins here
current_metrics = collect_diagnostics()

# Weight configuration (only partially applied)
weights_config = {
    'response_time': 0.35,
    'success_rate': 0.40,
    'system_load': 0.15,
    'resource_efficiency': 0.10,
    'throughput_impact': 0.05  # Unused weight
}

# Dead code path invocation (does nothing useful)
diagnostic_pairs = generate_combinations(list(current_metrics.keys())[:6])
entropy_value = calculate_entropy({
    'errors': int(current_metrics['error_rate'] * 100),
    'timeouts': current_metrics['timeout_count'],
    'retries': current_metrics['retry_attempts']
})

# THIS IS THE KEY STATEMENT
final_score = evaluate_performance(current_metrics, weights_config)

# Print result as required
print(f"Result: {final_score}")