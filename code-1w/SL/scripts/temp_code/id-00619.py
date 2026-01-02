def evaluate_performance(metrics, weights):
    # Initialize score and auxiliary tracking variables
    base_score = 0
    adjustment_factor = 1.0
    temp_sum = 0
    decay_rate = 0.95  # Unused in final logic, red herring
    outlier_count = 0  # Distractor: counts values above threshold but not used

    # Irrelevant preprocessing: normalize keys (has no effect on result)
    normalized_metrics = {k.strip().lower(): v for k, v in metrics.items()}

    # Semi-relevant transformation: scale metric values by weight
    scaled_values = {}
    for key in weights:
        if key in normalized_metrics:
            scaled_values[key] = normalized_metrics[key] * weights[key]
            temp_sum += normalized_metrics[key]

    # Linear aggregation of scaled values (core logic)
    for key in scaled_values:
        base_score += scaled_values[key]

    # Additional logic: apply condition-based bonus
    bonus_applied = False
    if base_score > 75 and len(scaled_values) >= 3:
        base_score += 10
        bonus_applied = True

    # Fake complexity: simulate decay over iterations (not actually applied)
    simulated_history = []
    for i in range(3):
        simulated_history.append(base_score * (decay_rate ** i))

    # Final decision tree with early exit
    if bonus_applied:
        final_score = int(base_score)
        return final_score

    # Fallback (not reached in this case)
    final_score = int(base_score * adjustment_factor)
    return final_score


# Main execution
metrics = {
    'accuracy': 88,
    'latency': 45,
    'throughput': 60,
    'reliability': 90,
    'usability': 70
}

weights = {
    'accuracy': 0.3,
    'throughput': 0.25,
    'reliability': 0.2,
    'usability': 0.15,
    'efficiency': 0.1  # Not present in metrics, so contributes nothing
}

# Intermediate distractor calculations
aggregate = sum(metrics.values()) // len(metrics)  # Irrelevant average
threshold_filter = [v for v in metrics.values() if v > 50]  # Unused list

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")