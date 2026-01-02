def evaluate_performance(metrics, baseline):
    # Irrelevant transformation: normalize unrelated metric
    normalized_load = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100, 2) for x in metrics]
    
    # Distractor: complex set operation with no impact on result
    outlier_set = {i for i, val in enumerate(metrics) if val > 1.5 * sum(metrics) / len(metrics)}
    adjusted_metrics = [val for i, val in enumerate(metrics) if i not in outlier_set]

    # Real computation begins: calculate trend deviation
    trend_deviation = sum(abs(metrics[i] - metrics[i-1]) for i in range(1, len(metrics)))
    
    # Conditional logic with early exit red herring
    if len(adjusted_metrics) < 3:
        return -1  # Dead code path due to input size
    
    # Core logic: weighted combination of volatility and efficiency
    volatility = sum((a - b) ** 2 for a, b in zip(metrics, metrics[1:]))
    efficiency_ratio = len([e for e in metrics if e >= baseline]) / len(metrics)
    
    # Secondary distractor: unused helper calculation
    peak_duration = 0
    current_streak = 0
    for val in metrics:
        if val > baseline * 1.1:
            current_streak += 1
        else:
            peak_duration = max(peak_duration, current_streak)
            current_streak = 0
    avg_peak = peak_duration / len(metrics) if metrics else 0  # Not used

    # Final score computation - this is what matters
    base_score = 100 - volatility * 0.5
    bonus = 25 if efficiency_ratio > 0.6 else 10
    penalty = 15 if trend_deviation > 40 else 0
    final_score = base_score + bonus - penalty

    return final_score

# Input data
metrics_data = [85, 90, 87, 92, 88, 84, 91]
baseline_target = 86

# Key execution point
final_score = evaluate_performance(metrics_data, baseline_target)
print(f"Result: {final_score}")