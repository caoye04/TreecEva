def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    normalized = {}
    for k, v in metrics.items():
        normalized[k] = (v - 50) / 50 if v > 50 else (v + 50) / 50

    # Apply weights and compute weighted sum
    weighted_sum = 0.0
    for metric, weight in weights.items():
        if metric in metrics:
            weighted_sum += metrics[metric] * weight

    # Secondary scoring based on thresholds (distractor logic)
    bonus = 0
    if metrics['accuracy'] > 85:
        bonus += 10
    if metrics['latency'] < 30:
        bonus += 5

    # Bitwise interference: manipulate bonus with irrelevant XOR pattern
    temp_flag = bonus ^ 15
    temp_flag = temp_flag & 7  # Masking bits (dead code)

    # Set operations: determine which metrics meet high standard
    high_performers = {k for k, v in metrics.items() if v >= 90}
    target_metrics = {'accuracy', 'throughput', 'stability'}
    overlap_count = len(high_performers & target_metrics)  # Only this affects final score

    # Final score computation (core logic)
    base_score = int(weighted_sum)
    final_score = base_score + (overlap_count * 5)

    # Dead code path: never reached due to prior logic
    if temp_flag < 0:
        final_score *= 2

    return final_score


# Main execution
base_weights = {
    'accuracy': 0.4,
    'throughput': 0.3,
    'latency': 0.2,
    'stability': 0.1
}

metric_set = {
    'accuracy': 92,
    'throughput': 88,
    'latency': 35,
    'stability': 91
}

# Extraneous data structures (distraction)
data_logs = [
    {'timestamp': 1678886400, 'value': 92},
    {'timestamp': 1678886500, 'value': 88},
    {'timestamp': 1678886600, 'value': 91}
]

summary_stats = {
    'max': max(metric_set.values()),
    'min': min(metric_set.values()),
    'range': max(metric_set.values()) - min(metric_set.values())
}

# Key statement
final_score = evaluate_performance(metric_set, base_weights)
print(f"Result: {final_score}")