def evaluate_performance(data, importance):
    temp_result = 0
    adjustment_factor = 0.85
    scaling_constant = 1.2  # unused in final logic, distraction
    baseline_offset = 10  # used only in irrelevant path

    cumulative = [0] * len(data)
    for i in range(len(data)):
        if data[i] > 75:
            temp_result += importance[i] * 1.5
        elif data[i] > 50:
            temp_result += importance[i] * 1.0
        else:
            temp_result += importance[i] * 0.3

        cumulative[i] = temp_result  # tracking but not used

    # Simulate data smoothing (distractor section)
    smoothed = cumulative[:]
    for j in range(2):
        for i in range(1, len(smoothed) - 1):
            smoothed[i] = (smoothed[i-1] + smoothed[i] + smoothed[i+1]) / 3

    # Dead code path - never executed due to fixed condition
    correction_term = 0
    if False:  # clearly unreachable
        correction_term = sum(cumulative) * 0.05
        baseline_offset += correction_term

    # Core logic reuses temp_result with final adjustment
    final_value = temp_result * adjustment_factor

    outlier_check = [x for x in data if x < 40]  # computed but unused
    if len(outlier_check) > 2:
        final_value *= 0.9

    return int(final_value)

# Main execution
metrics = [88, 76, 91, 52, 67]
weights = [0.2, 0.3, 0.25, 0.15, 0.1]

intermediate_total = sum(m * w for m, w in zip(metrics, weights))  # distraction calc

# Unrelated list processing (slice-based, adds cognitive load)
reversed_metrics = metrics[::-1]
subset = reversed_metrics[1:4]
subset_sum = sum(subset)

scaling_sequence = [1.1, 1.2, 1.3, 1.4, 1.5]
drift_adjustment = 0
for idx, val in enumerate(scaling_sequence):
    drift_adjustment += val * 0.01  # minor accumulation, irrelevant

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")