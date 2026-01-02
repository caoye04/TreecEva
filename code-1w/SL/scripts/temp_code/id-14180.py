def evaluate_performance(metrics, threshold):
    # Irrelevant preprocessing: normalize unrelated fields
    normalized = [max(0, min(100, m + 5)) for m in metrics]
    adjusted = [m * 1.1 for m in normalized if m > 10]  # Distractor list comprehension

    # Core logic: count how many metrics exceed threshold with modular penalty
    count_above = 0
    penalty_points = 0
    temp_result = []

    for i, metric in enumerate(metrics):
        if metric > threshold:
            count_above += 1
            if i % 3 == 0:  # Apply penalty on every 3rd index
                penalty_points += (metric % 7)  # Modular arithmetic used
        else:
            temp_result.append(metric * 2)  # Dead path: not used later

    # Secondary distractor computation (unused)
    outlier_count = sum(1 for x in metrics if x < 10 or x > 90)
    stability_factor = len(metrics) // (outlier_count + 1)

    # Final score calculation: depends only on count_above and penalty_points
    base_score = count_above * 25
    final_score = base_score - penalty_points

    # Extra distraction: unused conditional mutation
    if final_score > 100:
        final_score = 99
    elif final_score < 0:
        final_score = 0

    return final_score

# Main execution
metrics = [85, 72, 90, 45, 68, 93, 50]
threshold = 70
final_score = evaluate_performance(metrics, threshold)
print(f"Result: {final_score}")