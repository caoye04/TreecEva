def evaluate_performance(metrics, threshold):
    # Initialize relevant and irrelevant variables
    score = 0
    penalty = 0
    temp_sum = 0
    outlier_count = 0

    # Secondary helper logic (some steps are distractions)
    adjustment_factor = len(metrics) / (threshold + 1)
    scaling_constant = 0.85  # Not actually used

    for key in metrics:
        value = metrics[key]
        temp_sum += value

        if value > threshold * 2:
            outlier_count += 1
            penalty += 1
        elif value > threshold:
            score += int(value // 1.5)
        else:
            score += max(0, value - 5)

    # Distractor block: dead computation with unused variables
    hypothetical_gain = outlier_count * 3.7
    buffer_zone = [i * 2 for i in range(outlier_count)]
    cumulative_shift = sum(buffer_zone) / (outlier_count + 1) if outlier_count > 0 else 0

    # Relevant final calculation
    if score > penalty * 5:
        final_score = score - penalty * 2
    else:
        final_score = score - penalty * 4

    return final_score


# Main execution
base_threshold = 12
metric_data = {
    'throughput': 23,
    'latency': 8,
    'accuracy': 15,
    'reliability': 45,
    'consistency': 9,
    'response_time': 6
}

auxiliary_data = {k: v * 1.1 for k, v in metric_data.items()}  # Unused but plausible
processed_flags = [k.upper() for k in metric_data.keys() if len(k) > 8]  # Dead code path

final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")