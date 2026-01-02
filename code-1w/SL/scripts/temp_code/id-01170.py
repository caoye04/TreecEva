def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    normalized = {}
    for k, v in metrics.items():
        if v > 0:
            normalized[k] = (v - 1) / (10 - 1) * 9 + 1
        else:
            normalized[k] = 0

    # Calculate weighted harmonic mean with threshold filtering
    filtered_metrics = {k: v for k, v in metrics.items() if v >= 5}  # Only consider passing metrics

    # Auxiliary computation: count how many metrics are above average (distractor)
    avg_metric = sum(metrics.values()) / len(metrics)
    above_avg_count = sum(1 for v in metrics.values() if v > avg_metric)

    # Bitwise interference: encode metric keys into flags (dead code path)
    flag_register = 0
    for i, k in enumerate(metrics.keys()):
        if 'response' in k:
            flag_register |= (1 << i)
        elif 'latency' in k:
            flag_register ^= (3 << i)

    # Core logic: weighted harmonic mean
    weighted_inv_sum = 0.0
    weight_sum = 0.0
    temp_debug_log = []

    for name, weight in weights.items():
        if name in filtered_metrics:
            value = filtered_metrics[name]
            weighted_inv_sum += weight / value
            weight_sum += weight
            temp_debug_log.append(f'{name}: {value}')

    if weight_sum == 0:
        return 0.0

    harmonic_mean = weight_sum / weighted_inv_sum

    # Additional transformation: apply sigmoid-like dampening (not used)
    fake_dampened = 1 / (1 + 2 ** (-harmonic_mean / 10))

    # Final adjustment based on completeness
    completeness_ratio = len(filtered_metrics) / len(metrics)
    final_score = harmonic_mean * (0.8 + 0.2 * completeness_ratio)

    # Dead code: simulate fallback mechanism
    if completeness_ratio < 0.5:
        backup_scores = [v for k, v in metrics.items() if 'error' not in k]
        final_score = sum(backup_scores) / len(backup_scores)

    return int(round(final_score))

# Main execution
metrics = {
    'throughput': 8,
    'latency': 4,  # below threshold, excluded from harmonic mean
    'accuracy': 9,
    'memory_usage': 6,
    'response_time': 3  # below threshold
}
weights = {
    'throughput': 0.3,
    'accuracy': 0.4,
    'memory_usage': 0.2,
    'response_time': 0.1
}

intermediate_total = sum(metrics.values())  # distractor variable
reference_baseline = max(metrics.values())  # irrelevant reference

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")