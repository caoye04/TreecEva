def evaluate_performance(metrics, importance_weights):
    # Preprocessing: Normalize metrics using min-max scaling (irrelevant for binary 0/1)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics)) if max(metrics) != min(metrics) else 0 for m in metrics]

    # Apply weight transformation: only odd-indexed weights are actually used
    adjusted_weights = [w ** 0.5 for w in importance_weights]  # Distractor: not used

    # Key logic: only metrics at even indices contribute, weighted by corresponding importance_weights
    effective_score = 0
    for i in range(len(metrics)):
        if i % 2 == 0:  # Only even indices matter
            contribution = metrics[i] * importance_weights[i]
            effective_score += contribution

    # Secondary scoring path (dead code - never taken unless sum > 10)
    backup_metric = sum([m * 2 for m in metrics if m > 0.5])
    if sum(metrics) > 10:
        return backup_metric  # Not triggered

    # Tertiary distraction: set operations with no impact
    metric_set = set(metrics)
    weight_set = set(importance_weights)
    overlap = metric_set & weight_set  # Unused

    # Final adjustment: add bonus if more than half the weights are above average
    avg_weight = sum(importance_weights) / len(importance_weights)
    high_performers = [w for w in importance_weights if w > avg_weight]
    bonus = len(high_performers) if len(high_performers) > len(importance_weights) / 2 else 0  # Distractor

    # Actual result computation
    final_value = effective_score + bonus  # Bonus is always 0 in this case

    # Irrelevant slicing operation
    tail_metrics = metrics[3:]  # Not used
    reversed_weights = importance_weights[::-1]  # Not used

    # Return final score
    return final_value

# Main execution context
raw_data = [1, 0, 1, 1, 0, 1]
weights = [3, 7, 2, 8, 5, 4]

# Misleading preprocessing
processed = [x * 2 for x in raw_data]
decoy_sum = sum([w * w for w in weights])  # Dead-end calculation

# Core statement
final_score = evaluate_performance(raw_data, weights)

print(f"Result: {final_score}")