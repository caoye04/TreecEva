def evaluate_performance(data, importance):
    temp_results = []
    adjusted_values = []
    outlier_threshold = sum(data) / len(data)
    scaling_factor = 1.5  # unused distractor
    offset_correction = -0.2  # red herring variable

    for i, val in enumerate(data):
        if val > outlier_threshold:
            temp_results.append(val * 0.9)
        else:
            temp_results.append(val)

    # Apply weight adjustment using slicing and tuple unpacking
    weighted_sum = 0
    norm_importance = [w / sum(importance) for w in importance]
    for j in range(len(temp_results)):
        weighted_sum += temp_results[j] * norm_importance[j]

    # Simulate correction pass (irrelevant to final logic)
    corrected_sum = weighted_sum * 1.0  # no real effect
    dummy_check = corrected_sum < 0  # dead computation

    # Secondary processing with slicing and conditional filtering
    segment_a = temp_results[:3]
    segment_b = temp_results[3:]
    bonus_award = 0
    if len(segment_b) > 0 and max(segment_b) > 80:
        bonus_award = 5

    # Final aggregation with distraction variables
    base_performance = sum(segment_a) * 0.3 + sum(segment_b) * 0.7
    volatility_penalty = 0
    for k in range(1, len(temp_results)):
        diff = abs(temp_results[k] - temp_results[k-1])
        if diff > 15:
            volatility_penalty += 1  # tracked but not used

    final_score = int(base_performance + bonus_award)
    return final_score

# Main execution context
metrics = [85, 72, 90, 45, 88]
weights = [0.1, 0.1, 0.2, 0.3, 0.3]
initial_avg = sum(metrics) / len(metrics)  # irrelevant pre-calculation
placeholder_flag = False  # unused boolean flag
dummy_list = [x ** 0.5 for x in metrics if x > 50]  # dead code path

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")