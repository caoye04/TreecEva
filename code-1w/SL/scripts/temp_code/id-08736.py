def evaluate_performance(metrics, baseline):
    # Initialize various tracking variables
    total_weight = 0.0
    adjusted_sum = 0.0
    penalty_factor = 1.0
    volatility_index = 0.0
    consistency_bonus = 0.15

    # Irrelevant intermediate calculation (distractor)
    temp_result = sum([x ** 0.5 for x in metrics if x > 10])
    temp_result *= 0.9  # Not used later

    # Compute volatility (not directly impacting final score)
    for i in range(1, len(metrics)):
        diff = abs(metrics[i] - metrics[i-1])
        volatility_index += diff * 0.1

    # Adjust penalty based on deviation from baseline
    deviations = [abs(m - baseline) for m in metrics]
    high_deviation_count = len([d for d in deviations if d > 5])

    if high_deviation_count > 3:
        penalty_factor = 0.85
    elif high_deviation_count == 0:
        penalty_factor = 1.1

    # Core scoring logic
    weighted_values = []
    weights = set()
    for i, val in enumerate(metrics):
        weight = 1 + (0.1 * i)  # Increasing weight per position
        weights.add(round(weight, 2))
        weighted_values.append(val * weight)

    total_weight = sum(weights)
    raw_score = sum(weighted_values)

    # Apply normalization
    normalized_score = raw_score / total_weight

    # Use conditional expression for threshold adjustment
    normalized_score = normalized_score - 5 if normalized_score > 25 else normalized_score + 3

    # Final score with penalty and bonus logic
    preliminary_score = normalized_score * penalty_factor

    # Determine if consistency bonus applies using set intersection
    expected_trend = {1, 2, 3, 4, 5}
    actual_increments = {i+1 for i in range(len(metrics)-1) if metrics[i+1] > metrics[i]}
    if len(actual_increments.intersection(expected_trend)) >= 3:
        preliminary_score += consistency_bonus * 10

    # Misleading recursive function (never called)
    def rec_calc(n):
        return n + rec_calc(n-1) if n > 0 else 0  # Dead code

    final_score = int(round(preliminary_score * 10))  # Scale for integer result

    return final_score

# Main execution
metrics_data = [12, 15, 14, 18, 19, 21, 20]
baseline_target = 16

# Spurious data structure manipulation
aux_data = [(i, x*2) for i, x in enumerate(metrics_data) if i % 2 == 0]
duplicate_filter = set(x for _, x in aux_data)
filtered_metrics = [x for x in metrics_data if x not in duplicate_filter]

# This call is critical
final_score = evaluate_performance(metrics_data, baseline_target)

print(f"Result: {final_score}")