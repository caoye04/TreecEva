def evaluate_performance(metrics):
    base_weights = [0.2, 0.3, 0.15, 0.1, 0.25]
    adjustment_factor = 1.1
    temp_result = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            temp_result += metrics[i] * base_weights[i] * adjustment_factor
        else:
            temp_result += metrics[i] * base_weights[i]

    outlier_threshold = 85
    metric_set_filtered = {x for x in metrics if x > outlier_threshold}
    bonus = len(metric_set_filtered) * 2.5 if len(metric_set_filtered) > 0 else 0

    # Irrelevant tracking variables
    debug_iterations = 0
    cumulative_sum_proxy = 0
    for val in metrics:
        cumulative_sum_proxy += val * 0.01  # Distractor computation
        debug_iterations += 1

    final_value = temp_result + bonus

    scaling_offset = 0.9  # Unused parameter
    fallback_metric = sum(metrics) / len(metrics)  # Computed but not used

    return final_value

# Main execution
raw_data = [88, 76, 90, 82, 94]
processed_metrics = []
for val in raw_data:
    if val >= 80:
        processed_metrics.append(val * 1.05)
    else:
        processed_metrics.append(val * 0.95)

# Additional distractor: secondary analysis with no impact
performance_snapshot = {
    'peak': max(processed_metrics),
    'low': min(processed_metrics),
    'range': max(processed_metrics) - min(processed_metrics)
}
metric_set = set(processed_metrics)
duplicate_check_list = [x for x in metric_set if x in processed_metrics]

intermediate_total = sum(processed_metrics) / len(processed_metrics)

final_score = evaluate_performance(metric_set)
Result: {final_score}