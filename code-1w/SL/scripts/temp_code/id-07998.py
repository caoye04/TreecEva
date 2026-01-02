def evaluate_performance(metrics, weights):
    # Normalize metrics (irrelevant for final logic but adds distraction)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics) + 1e-8) for m in metrics]
    
    # Weighted sum calculation - core logic
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    
    # Distractor: complex transformation on a copy of data
    transformed = [x ** 2 for x in metrics if x > 0.5]
    temp_result = sum(transformed) / (len(transformed) + 1)
    adjustment = temp_result * 0.1 if temp_result > 1 else 0
    
    # Secondary distractor: unused conditional branch
    if len(metrics) > 10:
        outlier_count = len([x for x in metrics if x < 0.1])
        weighted_sum -= outlier_count * 0.05

    # Simulate confidence interval (not used)
    mean_val = sum(metrics) / len(metrics)
    variance = sum((x - mean_val) ** 2 for x in metrics) / len(metrics)
    std_dev = variance ** 0.5
    ci_lower = mean_val - 1.96 * std_dev
    ci_upper = mean_val + 1.96 * std_dev

    # Actual key computation path
    base_score = weighted_sum * 100
    penalty = 0
    for i, m in enumerate(metrics):
        if m < 0.3 and weights[i] >= 0.2:
            penalty += 5
    
    final_score = base_score - penalty
    
    return final_score

# Input data
metrics = [0.85, 0.72, 0.93, 0.68, 0.41, 0.88, 0.29, 0.76]
weights = [0.15, 0.20, 0.10, 0.25, 0.05, 0.12, 0.18, 0.08]

# Execution point of interest
temp_var = sum(w ** 2 for w in weights)  # red herring
baseline_check = any(m > 0.9 for m in metrics)  # side check
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")