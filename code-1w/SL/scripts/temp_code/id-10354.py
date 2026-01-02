def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for binary flags)
    normalized = {k: (v - 0) / (100 - 0) for k, v in metrics.items() if v != 'N/A'}

    # Flag thresholds for performance categories (distractor structure)
    performance_levels = {
        'entry': 40, 'mid': 60, 'senior': 80, 'expert': 90
    }

    # Compute weighted harmonic mean for numeric metrics only
    numeric_metrics = {k: v for k, v in metrics.items() if isinstance(v, (int, float))}
    weighted_values = []
    total_weight = 0

    for metric_name, raw_value in numeric_metrics.items():
        weight = weights.get(metric_name, 1.0)
        if raw_value > 0:  # Avoid division by zero
            weighted_values.append(weight / raw_value)
            total_weight += weight

    # Use harmonic aggregation only if valid values exist
    if weighted_values and total_weight > 0:
        harmonic_base = total_weight / sum(weighted_values)
    else:
        harmonic_base = 0

    # Boolean logic block: assess achievement of goals (semi-relevant)
    goal_achieved = all(
        metrics.get(goal, 0) >= threshold 
        for goal, threshold in [('accuracy', 75), ('efficiency', 65)]
    )

    # Apply bonus logic via lambda (key python feature)
    performance_bonus = (lambda x, g: x * 1.2 if g else x * 0.8)(harmonic_base, goal_achieved)

    # Set operation to detect redundant metrics (another python feature)
    expected_metrics = {'accuracy', 'efficiency', 'latency', 'memory_use'}
    provided_metrics = set(metrics.keys())
    missing = expected_metrics - provided_metrics
    redundancy_penalty = -5 * len(provided_metrics - expected_metrics)

    # Final adjustment based on completeness
    completeness_factor = 1.0 if not missing else 0.9

    # Intermediate distractor calculation (unused final computation)
    avg_metric = sum(v for v in metrics.values() if isinstance(v, int)) / len(numeric_metrics) if numeric_metrics else 0
    temp_debug_score = avg_metric * completeness_factor  # Dead code path

    # Core result computation
    base_score = performance_bonus * completeness_factor
    final_score = int(round(base_score + redundancy_penalty))  # Final answer assignment

    return final_score

# Main execution context
benchmark_weights = {
    'accuracy': 3.0,
    'efficiency': 2.5,
    'latency': 1.5,
    'memory_use': 1.0
}

metric_set = {
    'accuracy': 88,
    'efficiency': 70,
    'latency': 45,
    'memory_use': 60,
    'throughput': 120,  # Extra (redundant) metric
    'cache_hit_rate': 85  # Another redundant metric
}

# Trigger point: final_score assignment inside function
final_score = evaluate_performance(metric_set, benchmark_weights)
print(f"Result: {final_score}")