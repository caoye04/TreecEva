def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    temp_normalized = {k: v / (sum(metrics.values()) + 1e-5) for k, v in metrics.items()}
    
    # Semi-relevant pre-processing
    adjusted_metrics = {}
    for key, value in metrics.items():
        if key in ['latency', 'error_rate']:
            adjusted_metrics[key] = max(0, 100 - value)
        else:
            adjusted_metrics[key] = min(value, 90)
    
    # Dead code path (misleading)
    outlier_flags = []
    for val in metrics.values():
        if val > 200:
            outlier_flags.append(True)
    
    # Core logic begins here — real computation
    score = 0
    for name, val in adjusted_metrics.items():
        if name in thresholds:
            if val >= thresholds[name]:
                score += 25
            elif val >= thresholds[name] * 0.7:
                score += 15
            else:
                score += 5
    
    # Additional distraction: unused helper calculation
    avg_threshold_gap = sum(abs(val - thresholds.get(name, 0)) for name, val in metrics.items()) / len(metrics)
    
    # Real final adjustment
    if 'throughput' in adjusted_metrics and adjusted_metrics['throughput'] > 80:
        score += 10
    
    return int(score)

# Main execution context
raw_data = {
    'latency': 45,
    'throughput': 85,
    'error_rate': 30,
    'jitter': 60
}

threshold_map = {
    'latency': 50,
    'throughput': 75,
    'error_rate': 40,
    'jitter': 55
}

# Distractor variables (not used in final logic)
calibration_factor = 1.05
baseline_metrics = set(raw_data.keys())
deprecated_keys = set(['retries', 'timeout'])
overlap_check = baseline_metrics & deprecated_keys  # Useless intersection

# Simulated preprocessing step (semi-relevant but non-critical)
filtered_data = {k: v for k, v in raw_data.items() if v > 0}

# Actual pipeline
metric_data = {}
for k, v in filtered_data.items():
    metric_data[k] = v * 1.1 if k == 'throughput' else v

# Key statement
final_score = evaluate_performance(metric_data, threshold_map)

print(f"Result: {final_score}")