def evaluate_performance(metrics, threshold):
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100) for x in metrics]
    
    # Semi-relevant filtering
    filtered_metrics = [x for x in metrics if x > threshold * 0.5]

    # Dummy statistical calculation (not used in final result)
    avg_filtered = sum(filtered_metrics) / len(filtered_metrics) if filtered_metrics else 0
    variance_proxy = sum((x - avg_filtered) ** 2 for x in filtered_metrics) / len(filtered_metrics) if filtered_metrics else 0

    # Core logic: count how many metrics exceed the threshold
    above_threshold = 0
    for val in metrics:
        if val >= threshold:
            above_threshold += 1

    # Secondary condition based on bitwise pattern (hidden rule)
    bit_condition_met = 0
    for val in metrics:
        # Only values with odd XOR even pattern contribute
        if (val ^ threshold) & 1:  # XOR parity check
            bit_condition_met += 1

    # Decision logic with short-circuit behavior
    if above_threshold > 2 and bit_condition_met >= 3:
        base_score = 85
    elif above_threshold > 1:
        base_score = 60 + above_threshold * 5
    else:
        base_score = 40

    # Adjustment based on list comprehension side-effect (subtle but relevant)
    adjustments = [1 if i % 2 == 0 and v > threshold else -1 for i, v in enumerate(metrics)]
    net_adjustment = sum(adjustments) * 3

    # Final score computation
    final_score = base_score + net_adjustment

    # Dead code branch (never executed due to logic above)
    if len(metrics) < 0:  # Impossible condition
        final_score = -999

    return final_score

# Main execution
metrics_data = [78, 82, 85, 90, 76]
threshold_level = 80

# Unused variables (distractors)
correlation_matrix = [[1.0 for _ in range(len(metrics_data))] for _ in range(len(metrics_data))]
baseline_projection = sum(metrics_data) / len(metrics_data) + 10
reference_ranks = {i+1: val for i, val in enumerate(sorted(metrics_data, reverse=True))}

final_score = evaluate_performance(metrics_data, threshold_level)
print(f"Target result: {final_score}")