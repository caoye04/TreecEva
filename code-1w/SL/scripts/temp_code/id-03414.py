def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result)
    normalized = {k: (v - 50) / 50 if v > 50 else 0 for k, v in metrics.items()}

    # Irrelevant transformation: map categories to abstract levels
    level_map = {'accuracy': 'high', 'speed': 'medium', 'consistency': 'low'}
    performance_levels = {k: level_map.get(k, 'unknown') for k in metrics.keys()}

    # Distractor: calculate harmonic mean (not used)
    try:
        harmonic_mean = len(metrics) / sum(1/v for v in metrics.values())
    except ZeroDivisionError:
        harmonic_mean = 0

    # Only 'accuracy' and 'speed' contribute to final score
    weighted_sum = 0
    total_weight = 0
    for metric, value in metrics.items():
        if metric in ['accuracy', 'speed']:
            weight = weights.get(metric, 1)
            weighted_sum += value * weight
            total_weight += weight

    # Apply non-linear bonus if accuracy > 80
    if metrics.get('accuracy', 0) > 80:
        weighted_sum *= 1.1

    # Dead code path: never executed due to data
    if 'debug' in metrics and metrics['debug'] < 0:
        return -1

    base_score = weighted_sum / total_weight if total_weight else 0

    # Final adjustment based on consistency threshold
    if metrics.get('consistency', 100) >= 75:
        base_score += 5

    return int(base_score)


# Main execution
raw_data = [85, 72, 60]
labels = ['accuracy', 'speed', 'consistency']
metrics = dict(zip(labels, raw_data))
weights = {'accuracy': 3, 'speed': 2, 'consistency': 1}  # Consistency weight not used

# Irrelevant set operations (distractor)
unique_metrics = set(metrics.keys())
expected_metrics = {'accuracy', 'speed', 'consistency'}
missing = expected_metrics - unique_metrics

# Auxiliary dictionary processing (semi-relevant)
diagnostic_log = {
    'timestamp': 1234567890,
    'status': 'completed',
    'values': [metrics[k] for k in labels]
}

# Key computation
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")