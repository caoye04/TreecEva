def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = {k: v / max(metrics.values()) for k, v in metrics.items()}
    excess = {k: v - thresholds.get(k, 0) for k, v in normalized.items()}

    # Semi-relevant filtering (some values used later)
    above_threshold = {k: v for k, v in normalized.items() if v > thresholds.get(k, 0.5)}

    # Key logic: compute weighted score
    weights = {'latency': 0.4, 'throughput': 0.3, 'accuracy': 0.2, 'memory': 0.1}
    base_score = sum(metrics.get(key, 0) * weight for key, weight in weights.items())

    # Bonus calculation based on completeness
    completeness_bonus = 10 if len(above_threshold) == len(thresholds) else 5

    # Penalty for missing metrics (not all metrics affect final score)
    missing_penalty = 0
    for metric in thresholds:
        if metric not in metrics:
            missing_penalty += 3

    # Red herring: unused complex structure
    stats_summary = {
        'count': len(metrics),
        'avg': sum(metrics.values()) / len(metrics),
        'peak': max(metrics.values()),
        'unused_diagnostic': set(metrics.keys()) - set(thresholds.keys())
    }

    # Conditional adjustment (uses intermediate values)
    adjustment_factor = 1.1 if base_score > 80 and completeness_bonus == 10 else 0.9

    # Final computation
    adjusted_score = base_score * adjustment_factor - missing_penalty + completeness_bonus

    # Dead code path (never executed under normal inputs)
    if False:
        adjusted_score = max(adjusted_score, 50)  # unreachable

    return int(adjusted_score)


def calculate_final_score(system_data):
    # Extract subsystem metrics (some irrelevant)
    primary_metrics = system_data['performance']['primary']
    secondary_metrics = system_data['performance']['secondary']  # unused

    # Thresholds for evaluation
    safety_thresholds = {'latency': 0.1, 'throughput': 500, 'accuracy': 0.9, 'memory': 200}

    # Compute score using main function
    score = evaluate_performance(primary_metrics, safety_thresholds)

    # Additional distractor logic
    outliers = [v for v in primary_metrics.values() if v > 2 * safety_thresholds.get('throughput', 1)]
    correction_term = len(outliers) * 2

    # Final aggregation (correction_term has no effect due to conditional)
    if score < 70:
        final_score = score - correction_term
    else:
        final_score = score  # correction_term ignored

    return final_score

# Input data
system_report = {
    'performance': {
        'primary': {
            'latency': 85,
            'throughput': 600,
            'accuracy': 95,
            'memory': 180
        },
        'secondary': {
            'cpu': 75,
            'disk': 40
        }
    },
    'version': '2.1.0'
}

# Execute and print result
result = calculate_final_score(system_report)
print(f"Result: {result}")