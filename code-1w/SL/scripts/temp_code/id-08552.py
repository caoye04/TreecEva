def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation: reverse and slice (distractor)
    reversed_metrics = metrics[::-1]
    temp_adjustment = sum(reversed_metrics[:3]) * 0.1

    # Semi-relevant preprocessing: normalize within range
    normalized = [max(0.0, min(m, 100.0)) for m in metrics]

    # Key slicing operation: focus on core performance indicators
    core_metrics = normalized[1:-1]  # Exclude first and last

    # Misleading statistical computation (not used in final logic)
    avg_metric = sum(normalized) / len(normalized)
    stdev_guess = (max(normalized) - min(normalized)) / 4  # Rough estimate

    # Threshold comparison with state tracking
    passed_count = 0
    margin_buffer = 0.0
    for i, val in enumerate(core_metrics):
        threshold = thresholds.get(i + 1, 75)
        if val >= threshold:
            passed_count += 1
        else:
            margin_buffer += (threshold - val)

    # Conditional branching based on performance pattern
    if passed_count >= 3:
        base_score = 90.0
    elif passed_count >= 2:
        base_score = 65.0
    else:
        base_score = 40.0

    # Bonus logic: perfect scores in middle triggers uplift (uses tuple unpacking)
    mid_index = len(core_metrics) // 2
    if len(core_metrics) % 2 == 0:
        left_mid, right_mid = core_metrics[mid_index-1], core_metrics[mid_index]
        if left_mid == 100 and right_mid == 100:
            bonus = 10.0
        else:
            bonus = 5.0
    else:
        center_val = core_metrics[mid_index]
        bonus = 15.0 if center_val == 100 else 2.5

    # Final adjustment using buffer (but only if certain conditions met)
    final_multiplier = 1.0
    if margin_buffer > 0:
        final_multiplier = 0.95

    # Critical answer-determining line
    final_score = (base_score + bonus) * final_multiplier

    # Dead code path: never executed due to logic above (distractor)
    if temp_adjustment < 0:
        final_score *= 1.1

    return final_score

# Main execution
metrics_data = [85.0, 92.0, 100.0, 88.0, 76.0, 95.0]
thresholds_config = {1: 80, 2: 90, 3: 85, 4: 70, 5: 90}

# Extraneous variable (distractor)
baseline_avg = sum(metrics_data) / len(metrics_data)
dropped_segment = metrics_data[3:4]

# Key statement
final_score = evaluate_performance(metrics_data, thresholds_config)

print(f"Result: {final_score}")