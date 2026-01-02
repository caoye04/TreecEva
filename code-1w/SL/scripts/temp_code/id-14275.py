def evaluate_performance(metrics, weights):
    # Normalize metrics to z-scores (irrelevant for final result but adds cognitive load)
    mean_metric = sum(metrics) / len(metrics)
    variance = sum((x - mean_metric) ** 2 for x in metrics) / len(metrics)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_metric) / std_dev for x in metrics] if std_dev != 0 else [0] * len(metrics)

    # Weighted harmonic mean calculation (actual relevant logic)
    weighted_inv_sum = sum(weights[i] / metrics[i] for i in range(len(metrics)) if metrics[i] != 0)
    harmonic_baseline = 1 / weighted_inv_sum if weighted_inv_sum != 0 else 0

    # Simulate threshold adjustments (some dead code paths)
    adjustment_factor = 0
    if harmonic_baseline > 50:
        adjustment_factor = 1.2
    elif harmonic_baseline < 30:
        adjustment_factor = 0.8  # Never reached due to data
    else:
        adjustment_factor = 1.0

    # Apply non-linear transformation (distractor)
    transformed = [x ** 0.5 for x in z_scores]
    avg_transformed = sum(transformed) / len(transformed) if transformed else 0

    # Actual key computation path
    weight_sum = sum(weights)
    normalized_weights = [w / weight_sum for w in weights]
    weighted_metrics = sum(metrics[i] * normalized_weights[i] for i in range(len(metrics)))

    # Final scoring with conditional boost
    base_final = weighted_metrics * harmonic_baseline / 100
    if all(m > 20 for m in metrics):
        base_final += 5  # Small deterministic bonus

    # Red herring: unused helper function
    calculate_entropy = lambda lst: -sum(p * (p).log() for p in lst if p > 0)

    # Another distraction: character counting in metric names (never used)
    metric_labels = ['latency', 'throughput', 'accuracy', 'stability']
    char_count = sum(len(label) for label in metric_labels)
    dummy_offset = char_count % 7

    # Final assignment
    final_score = int(base_final + dummy_offset * 0.1)  # dummy_offset effect negligible

    return final_score

# Input data
dataset_metrics = [45, 60, 55, 50]
importance_weights = [0.1, 0.3, 0.4, 0.2]

# Execution point
final_score = evaluate_performance(dataset_metrics, importance_weights)
print(f"Result: {final_score}")