def evaluate_performance(metrics, limits):
    # Irrelevant transformation: character counting in labels
    label_chars = sum(len(key) for key in metrics.keys() if 'name' in key)
    temp_offset = label_chars % 7

    # Semi-relevant pre-processing: normalize metric values
    normalized = {}
    for k, v in metrics.items():
        if isinstance(v, (int, float)):
            normalized[k] = round(v / (max(limits.values()) + 1e-5), 3)
        else:
            normalized[k] = 0.0

    # Distractor: unused conditional expression
    status_flag = 'active' if sum(normalized.values()) > 2 else 'standby'
    mode_weight = 1.2 if status_flag == 'active' else 0.8  # not actually used later

    # Core logic: score based on threshold crossings and set operations
    above_threshold = {k for k, v in metrics.items() if v > limits.get(k, 0)}
    critical_keys = {'response_time', 'error_rate', 'throughput'}
    met_critical = above_threshold.intersection(critical_keys)

    base_score = len(met_critical) * 10

    # Additional logic: conditional expression based on string content
    has_optimized = any('optimized' in k.lower() for k in metrics.keys())
    bonus = 5 if has_optimized else 0

    # Another red herring: complex but unused calculation
    phantom_sum = sum(v ** 0.5 for v in metrics.values() if v > 0) / (temp_offset + 1)
    shadow_factor = int(phantom_sum % 4)  # never used

    # Final computation chain
    adjustment = 0
    if 'latency' in metrics and metrics['latency'] < limits['latency']:
        adjustment += 7
    if len(above_threshold) >= 4:
        adjustment += 3

    final_score = base_score + bonus + adjustment
    return final_score

# Main execution block
metric_data = {
    'response_time': 115,
    'error_rate': 0.03,
    'throughput': 980,
    'latency': 44,
    'bandwidth_utilization': 67,
    'uptime_percentage': 99.97,
    'optimized_caching': True,
    'retry_count': 2
}

thresholds = {
    'response_time': 100,
    'error_rate': 0.05,
    'throughput': 950,
    'latency': 50,
    'bandwidth_utilization': 70,
    'uptime_percentage': 99.9
}

# Key statement
final_score = evaluate_performance(metric_data, thresholds)
print(f"Target result: {final_score}")