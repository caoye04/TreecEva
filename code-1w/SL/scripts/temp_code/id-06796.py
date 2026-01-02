def calculate_rating(metrics, weights):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = {}

    # Distractor: Initialize irrelevant tracking variables
    max_metric = float('-inf')
    min_metric = float('inf')
    metric_count = 0

    for i, (key, value) in enumerate(metrics.items()):
        if i % 2 == 0:
            base += value * weights[i % len(weights)]
            temp_result[key] = value * 1.1  # Unused transformation
        else:
            # Irrelevant computation
            adjusted = value * 0.95 + 2
            if adjusted > 50:
                bonus += 3
            else:
                bonus += 1

        # Tracking distractors (not used in final result)
        if value > max_metric:
            max_metric = value
        if value < min_metric:
            min_metric = value
        metric_count += 1

    # Real logic continues: apply weight scaling based on index parity
    for j in range(len(weights)):
        if j % 3 == 0:
            penalty += weights[j] * 0.5

    # Core calculation
    intermediate = base - penalty + bonus

    # Additional distraction: zipping unrelated sequences
    indices = list(range(len(metrics)))
    statuses = ['active', 'inactive', 'unknown', 'pending']
    metadata_pairs = list(zip(indices, statuses))  # Not used

    # Final rating with fixed offset
    final_rating = int(intermediate + 7.3)

    return final_rating

# Main execution
quality_metrics = {
    'reliability': 85,
    'latency': 45,
    'throughput': 92,
    'accuracy': 78,
    'consistency': 88
}

efficiency_weights = [0.8, 0.6, 1.1, 0.9, 1.3]

# Misleading pre-computations
avg_metric = sum(quality_metrics.values()) / len(quality_metrics)
decay_factor = avg_metric * 0.01
projected_loss = decay_factor * 12  # Dead code path

final_score = calculate_rating(quality_metrics, efficiency_weights)
print(f"Target result: {final_score}")