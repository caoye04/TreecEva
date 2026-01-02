import math

# Irrelevant utility function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

def parse_log_entry(entry):
    parts = entry.strip().split('|')
    if len(parts) < 3:
        return None
    timestamp, level, msg = parts[0], parts[1], '|'.join(parts[2:])
    return {
        'time': timestamp,
        'level': level.strip(),
        'message': msg.strip().lower()
    }

# Decoy data processing that looks important but isn't used in final result
test_logs = [
    '2023-08-01|ERROR|System failure in module X',
    '2023-08-02|INFO |Data pipeline completed',
    '2023-08-03|WARN |High memory usage detected'
]

parsed_entries = [parse_log_entry(log) for log in test_logs if log]
error_count = sum(1 for e in parsed_entries if e and e['level'] == 'error')

# Real computation begins: system performance evaluator
def compute_weighted_average(values, weights):
    if not values or not weights or len(values) != len(weights):
        return 0.0
    total = sum(v * w for v, w in zip(values, weights))
    return total / sum(weights)

def bitwise_diagnostic(value):
    # Bit manipulation red herring
    shifted = (value << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return (toggled >> 2) & 0x3F

def analyze_stability_factor(raw_metric):
    base = abs(raw_metric - 50)
    adjusted = base * 1.75
    if adjusted > 100:
        adjusted = 100 - (adjusted - 100)
    return round(math.cos(math.radians(adjusted)) * 50 + 50, 4)

def validate_thresholds(config):
    # String method distraction
    valid_keys = [k for k in config.keys() if k.startswith('thresh_')]
    levels = [str(config[k]).upper().strip() for k in valid_keys]
    critical_found = any('CRITICAL' in lvl for lvl in levels)
    # Unused but plausible-looking logic
    if critical_found:
        fallback_mode = config.get('fallback', False)
        return fallback_mode
    return False

def evaluate_performance(metrics, config):
    # Extract relevant metrics
    response_time = metrics.get('response_time_ms', 0)
    throughput = metrics.get('req_per_sec', 0)
    error_rate = metrics.get('error_rate', 0)
    
    # Distractor: complex unused transformation
    transformed_metrics = {
        'rt_zscore': (response_time - 250) / 100 if response_time else 0,
        'tp_rank': int(math.log(throughput + 1, 2)) if throughput > 0 else 0,
        'err_binary': 'HIGH' if error_rate > 0.05 else 'OK'
    }
    
    # Real scoring logic
    time_score = max(0, 100 - (response_time / 5))
    throughput_score = min(100, throughput / 10)
    error_score = 100 - (error_rate * 1000)
    
    # Weighted combination
    raw_values = [time_score, throughput_score, error_score]
    weights = [0.4, 0.3, 0.3]
    composite = compute_weighted_average(raw_values, weights)
    
    # Stability adjustment using trigonometric logic
    stability = analyze_stability_factor(composite)
    adjusted_composite = (composite * 0.7) + (stability * 0.3)
    
    # Final nonlinear boost based on config flag (actual key decision)
    boost_enabled = config.get('enable_performance_boost', False)
    if boost_enabled and adjusted_composite >= 60:
        adjusted_composite = min(100, adjusted_composite * 1.15)
    
    # Irrelevant bit manipulation on final score (no effect)
    temp_val = int(adjusted_composite)
    masked = bitwise_diagnostic(temp_val)
    _ = masked  # unused
    
    # Final assignment
    final_value = round(adjusted_composite, 2)
    
    return final_value

# Input data
metric_data = {
    'response_time_ms': 120,
    'req_per_sec': 280,
    'error_rate': 0.012,
    'timeout_count': 3  # unused field
}

user_config = {
    'thresh_low': 'warning',
    'thresh_high': 'critical',
    'enable_performance_boost': True,
    'fallback': False,
    'debug_mode': 'verbose'  # irrelevant
}

# Dead code: looks important but unused
baseline_metrics = [95.0, 87.5, 92.0]
baseline_avg = sum(baseline_metrics) / len(baseline_metrics)

diag_code = bitwise_diagnostic(42)

# Key execution point
final_score = evaluate_performance(metric_data, user_config)

print(f"Result: {final_score}")