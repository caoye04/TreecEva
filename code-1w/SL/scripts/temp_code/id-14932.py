def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final logic but adds distraction)
    normalized = {k: (v - 50) / 50 if v > 50 else 0 for k, v in metrics.items()}

    # Compute weighted sum using only specific keys
    relevant_keys = ['accuracy', 'latency', 'throughput']
    weighted_sum = sum(metrics[key] * weights[key] for key in relevant_keys if key in metrics)

    # Secondary computation on normalized values (distractor)
    efficiency_ratio = len([v for v in normalized.values() if v > 0.5])
    saturation_level = sum(1 for m in metrics.values() if m >= 75)

    # Complex conditional update based on thresholds (semi-relevant)
    bonus = 0
    if metrics.get('accuracy', 0) > 85 and metrics.get('throughput', 0) > 90:
        bonus += 10
    if metrics.get('error_rate', 100) < 5:
        bonus += 5

    # Dummy list comprehension with lambda (set operation mimicry via filtering)
    critical_metrics = list(filter(lambda x: x[1] > 80, metrics.items()))
    penalty = len(set(metrics.keys()) & {'overhead', 'jitter'}) * 3

    # Final score calculation - this is the key line
    final_score = weighted_sum + bonus - penalty

    # Dead code path (never executed under current inputs)
    if False:
        fallback = sum(normalized.values()) * 10
        final_score = max(final_score, fallback)

    return final_score

# Input data
metrics = {
    'accuracy': 92,
    'latency': 88,
    'throughput': 95,
    'error_rate': 3,
    'overhead': 40,
    'jitter': 60,
    'reliability': 70
}

weights = {
    'accuracy': 1.2,
    'latency': 0.8,
    'throughput': 1.0
}

# Execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")