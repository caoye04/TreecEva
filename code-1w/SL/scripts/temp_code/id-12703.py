def evaluate_performance(data, importance):
    # Normalize data using min-max scaling (irrelevant for final result but adds distraction)
    normalized = [(x - min(data)) / (max(data) - min(data)) if max(data) != min(data) else 0 for x in data]
    
    # Auxiliary computation: calculate entropy (not used in final score)
    import math
    entropy = sum(-x * math.log(x + 1e-9) for x in normalized)
    entropy_adjusted = entropy * 0.1

    # Key transformation: apply weight-based scoring
    weighted_values = map(lambda val, w: val * w, data, importance)
    raw_score = sum(weighted_values)

    # Secondary adjustment based on pattern detection
    trend_bias = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_bias += 0.5
        elif data[i] < data[i-1]:
            trend_bias -= 0.3

    # Simulate experience bonus (distractor with slicing)
    experience_window = data[:3]
    if len(experience_window) == 3 and sum(experience_window) > 60:
        experience_bonus = 10
    else:
        experience_bonus = 0

    # Final aggregation logic
    base_performance = raw_score * 1.2
    stability_penalty = 0
    for val in data:
        if abs(val - 50) > 40:  # High deviation from norm
            stability_penalty += 2

    # Actual answer depends only on base_performance - stability_penalty
    final_score = base_performance - stability_penalty

    # Dead code path: never executed due to condition
    if False:
        final_score *= 0.9
        final_score += 5

    return final_score

# Main execution
metrics = [85, 72, 90, 45, 68]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Preprocessing side calculations (distraction)
reversed_metrics = metrics[::-1]
midpoint_slice = reversed_metrics[1:4]
avg_mid = sum(midpoint_slice) / len(midpoint_slice)

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")