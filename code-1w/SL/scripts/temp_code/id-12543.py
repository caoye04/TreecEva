def analyze_component_health(sensor_data, thresholds):
    status_flags = {}
    for key, readings in sensor_data.items():
        avg = sum(readings) / len(readings)
        status_flags[key] = avg <= thresholds.get(key, 100)
    return status_flags

sensor_data = {
    'temp': [78, 85, 88, 91, 83],
    'voltage': [115, 118, 120, 117, 119],
    'rpm': [3400, 3600, 3550, 3650, 3580]
}
thresholds = {'temp': 90, 'voltage': 125, 'rpm': 4000}

# Irrelevant health analysis (distraction)
health_status = analyze_component_health(sensor_data, thresholds)

# Dummy transformation chain (red herring)
def transform_metrics(raw):
    scaled = {k: v * 1.05 for k, v in raw.items()}
    adjusted = {k: v + 2 if 'temp' in k else v + 1 for k, v in scaled.items()}
    return adjusted

# Unused function — dead code path
def deprecated_normalization(data):
    max_val = max(data.values())
    return {k: round(v / max_val, 3) for k, v in data.items()}

# Simulated performance log parser (distractor with string manipulation)
def parse_logs(log_entries):
    parsed = []
    for entry in log_entries:
        parts = entry.split('|')
        if len(parts) < 3:
            continue
        timestamp, level, msg = parts[0], parts[1].strip(), parts[2].strip()
        severity = 1 if 'WARN' in level else (2 if 'ERR' in level else 0)
        parsed.append({'time': timestamp, 'severity': severity, 'msg': msg})
    # Extract error count (misleading metric)
    error_count = sum(1 for p in parsed if p['severity'] == 2)
    return error_count

log_data = [
    "2023-08-01T10:01| INFO | System initialized",
    "2023-08-01T10:05| WARN | High latency detected",
    "2023-08-01T10:07| ERR  | Connection timeout"
]

error_count = parse_logs(log_data)

# Core logic buried among distractions
base_metrics = {
    'latency': 45.6,
    'throughput': 892,
    'consistency': 0.91,
    'availability': 0.99
}

# Complex conditional expression used in weighting (required feature)
benchmark_weights = {
    'latency': 0.3 if base_metrics['latency'] < 50 else 0.25,
    'throughput': 0.25,
    'consistency': 0.2 + (0.05 if base_metrics['availability'] > 0.98 else 0),
    'availability': 0.15
}

# Data structure mix: dictionary and list operations
weight_sum = sum(benchmark_weights.values())
if abs(weight_sum - 1.0) > 1e-6:
    benchmark_weights = {k: v / weight_sum for k, v in benchmark_weights.items()}

# Multi-step transformation with distractors
adjusted_metrics = {}
for k, v in base_metrics.items():
    if k == 'latency':
        adjusted_metrics[k] = 100 * (1 - min(v / 100, 1))
    elif k == 'throughput':
        adjusted_metrics[k] = min(v / 10, 100)
    else:
        adjusted_metrics[k] = v * 100

# Redundant sorting (irrelevant to final result)
sorted_keys = sorted(adjusted_metrics.keys(), key=lambda x: len(x), reverse=True)
backup_copy = {k: adjusted_metrics[k] for k in sorted_keys}

# Conditional expression embedded in calculation (required feature)
def evaluate_reliability(value, threshold):
    return 90 if value >= threshold else (50 if value >= threshold * 0.8 else 30)

# Fake reliability check (unused)
reliability_scores = {
    'latency': evaluate_reliability(base_metrics['latency'], 40),
    'throughput': evaluate_reliability(base_metrics['throughput'], 800)
}

# Critical function containing answer derivation
metrics = [adjusted_metrics[k] for k in ['latency', 'throughput', 'consistency', 'availability']]
def evaluate_performance(m_list, weights_dict):
    weighted_sum = 0
    keys_in_order = ['latency', 'throughput', 'consistency', 'availability']
    for i, key in enumerate(keys_in_order):
        norm_val = m_list[i] / 100.0  # Normalize to 0-1
        weight = weights_dict[key]
        contribution = norm_val * weight * 100
        weighted_sum += contribution
    # Additional adjustment based on system health (false dependency)
    health_bonus = 5 if health_status.get('voltage', True) and health_status.get('rpm', True) else 0
    return int(weighted_sum + health_bonus)  # Final score as integer

# Key assignment statement
final_score = evaluate_performance(metrics, benchmark_weights)
print(f"Result: {final_score}")