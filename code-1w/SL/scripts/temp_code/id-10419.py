def evaluate_performance(data, limit):
    temp_result = 0
    backup_cache = [0] * len(data)
    cumulative = 0
    adjustment_factor = 0.85

    for i in range(len(data)):
        if data[i] < 0:
            cumulative -= data[i]  # Irrelevant for final logic
            backup_cache[i] = -1
            continue

        sliced_window = data[max(0, i-2):i+1]
        window_avg = sum(sliced_window) / len(sliced_window)

        if window_avg > limit:
            temp_result += 2
        elif window_avg == limit:
            temp_result += 1
        else:
            temp_result -= 1

        if temp_result > 5:  # Early saturation check (distractor)
            temp_result = 5

    # Secondary path that doesn't affect outcome
    post_analysis = 0
    for x in backup_cache:
        post_analysis += x

    scaling_multiplier = 3.5
    final_value = temp_result * scaling_multiplier

    # Dead code - never executed due to logic above
    if post_analysis == 100:
        final_value *= 2

    return int(final_value)

# Main execution
raw_metrics = [3, 7, 2, 8, 4, 6]
threshold = 5
offset_correction = sum(raw_metrics) // len(raw_metrics)
intermediate_calc = [x - offset_correction for x in raw_metrics]

# Only this call matters
final_score = evaluate_performance(intermediate_calc, threshold)
print(f"Result: {final_score}")