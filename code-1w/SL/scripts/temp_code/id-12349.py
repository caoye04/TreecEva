import math

# Simulated system performance metrics
metrics_log = {
    'response_time_ms': [120, 150, 130, 170, 90],
    'error_rate': [0.02, 0.01, 0.03, 0.025, 0.018],
    'throughput_ops': [80, 75, 85, 70, 90],
    'cpu_utilization': [0.65, 0.72, 0.68, 0.78, 0.60],
    'memory_usage_mb': [450, 470, 460, 480, 440]
}

# Baseline configuration for comparison
baseline_config = {
    'target_response_time': 140,
    'max_error_rate': 0.025,
    'min_throughput': 75,
    'optimal_cpu_range': (0.6, 0.8),
    'scaling_factor': 1.2
}

# Irrelevant auxiliary data (distractor)
dummy_data = {
    'temp_calibrations': [0.1, 0.3, 0.2, 0.4],
    'voltage_stability': {'node_a': 3.3, 'node_b': 3.4},
    'unused_flags': [True, False, True]
}

# Decoy function - looks relevant but unused in final computation
def analyze_health(metrics):
    score = 0
    for val in metrics.get('cpu_utilization', []):
        if val > 0.9:
            score -= 10
        elif val < 0.3:
            score -= 5
    return max(score, -20)

# Helper function with misleading intermediate calculations
def calculate_efficiency_index(data):
    times = data['response_time_ms']
    errors = data['error_rate']
    # Complex but ultimately unused calculation (red herring)
    harmonic_response = len(times) / sum(1/t if t > 0 else 0.001 for t in times)
    penalty = sum(100 * e for e in errors if e > 0.02)
    efficiency = (harmonic_response * 0.7) - penalty
    return efficiency  # Not used in final logic

# Auxiliary transformation with partial relevance
def normalize_series(values, cap=100):
    max_val = max(values) if values else 1
    return [round((v / max_val) * cap) for v in values]

# Secondary metric processor - only one output is actually used
def process_throughput_analysis(raw_data, factor=1.0):
    raw_ops = raw_data['throughput_ops']
    normalized = normalize_series(raw_ops)
    avg_normalized = sum(normalized) / len(normalized)
    peak = max(normalized)
    # Dead-end computation (distractor)
    volatility = sum(abs(normalized[i] - normalized[i-1]) for i in range(1, len(normalized)))
    return {
        'average': avg_normalized,
        'peak': peak,
        'volatility_score': volatility  # Unused downstream
    }

# Core evaluation logic — only this affects final result
config_mode = 'standard'
adjustment_factor = 1.1 if config_mode == 'aggressive' else 1.0

# Conditional expression determining weight scheme
weight_scheme = {
    'time_weight': 0.4 if baseline_config['target_response_time'] >= 130 else 0.3,
    'error_weight': 0.3,
    'throughput_weight': 0.2,
    'stability_weight': 0.1
}

# Linear search for first high-error occurrence (used later)
def find_first_issue(errors, threshold=0.025):
    for i, err in enumerate(errors):
        if err > threshold:
            return i  # Used in final adjustment
    return -1

# Main scoring function with nested logic and distractors
def evaluate_performance(log, config):
    scores = {}
    
    # Response time scoring
    avg_time = sum(log['response_time_ms']) / len(log['response_time_ms'])
    time_deviation = abs(avg_time - config['target_response_time'])
    time_score = max(100 - (time_deviation * 0.5), 0)
    
    # Error rate scoring
    error_exceeds_baseline = [e for e in log['error_rate'] if e > config['max_error_rate']]
    error_count_penalty = len(error_exceeds_baseline) * 8
    error_score = max(90 - error_count_penalty, 0)
    
    # Throughput scoring using processed value
    throughput_result = process_throughput_analysis(log)
    base_throughput_score = throughput_result['average']
    
    # Stability component: CPU within optimal range
    good_cpu_count = sum(1 for u in log['cpu_utilization'] 
                         if config['optimal_cpu_range'][0] <= u <= config['optimal_cpu_range'][1])
    stability_score = (good_cpu_count / len(log['cpu_utilization'])) * 100
    
    # First issue detection (conditional logic dependency)
    first_high_error_idx = find_first_issue(log['error_rate'])
    early_penalty = 15 if first_high_error_idx == 0 else (5 if first_high_error_idx > 0 else 0)
    
    # Bit manipulation red herring (irrelevant but complex-looking)
    magic_flag = 0b1010
    mask = 0b1111
    decoy_metric = (magic_flag ^ mask) << 2  # Computed but unused
    
    # Dictionary-based dynamic weighting
    weights = weight_scheme
    
    # Final weighted aggregation
    weighted_sum = (
        time_score * weights['time_weight'] +
        error_score * weights['error_weight'] +
        base_throughput_score * weights['throughput_weight'] +
        stability_score * weights['stability_weight']
    )
    
    # Apply early penalty and scaling
    final_raw = weighted_sum - early_penalty
    scaled_final = final_raw * config['scaling_factor']
    
    # Integer division and rounding to produce final integer score
    final_integer_score = int(round(scaled_final))
    
    # Critical assignment point
    final_score = final_integer_score
    
    return final_score

# Execute main evaluation
eval_result = evaluate_performance(metrics_log, baseline_config)

# Additional irrelevant transformations (dead code paths)
temp_analysis = calculate_efficiency_index(metrics_log)
health_diag = analyze_health(metrics_log)

# Target result output
Result: eval_result