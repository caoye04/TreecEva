def evaluate_performance(metrics, weights):
    # Initialize various tracking variables (some are distractions)
    baseline = 100
    adjustment_factor = 0.95
    temp_result = 0
    cumulative = 0
    
    # Irrelevant scaling of weights (not used in final logic)
    scaled_weights = list(map(lambda w: w * adjustment_factor, weights))
    
    # Secondary metric analysis (partially relevant)
    adjusted_metrics = []
    for i, metric in enumerate(metrics):
        if metric < 50:
            adjusted_value = metric * 1.1
        elif metric > 80:
            adjusted_value = metric * 1.2
        else:
            adjusted_value = metric
        adjusted_metrics.append(adjusted_value)
    
    # Dummy loop to calculate unused trend indicator
    trend = 0
    for j in range(len(adjusted_metrics) - 1):
        if adjusted_metrics[j+1] > adjusted_metrics[j]:
            trend += 1
    trend_indicator = trend / len(adjusted_metrics) if adjusted_metrics else 0

    # Core scoring logic (depends on original metrics and weights)
    weighted_sum = 0
    max_possible = 0
    for idx in range(len(metrics)):
        weighted_sum += metrics[idx] * weights[idx]
        max_possible += 100 * weights[idx]
    
    # Normalize score
    normalized_score = (weighted_sum / max_possible) * baseline
    
    # Apply conditional bonus based on consistency
    variation = max(metrics) - min(metrics)
    consistency_bonus = 0
    if variation <= 10:
        consistency_bonus = 5
    elif variation <= 20:
        consistency_bonus = 2
    
    # Final computation
    raw_score = normalized_score + consistency_bonus
    penalty = 0
    if sum(1 for m in metrics if m < 60) >= 2:
        penalty = 10
    
    final_score = raw_score - penalty
    
    # Dead code branch (never executed under current logic)
    if False:
        fallback = sum(adjusted_metrics) / len(adjusted_metrics)
        final_score = max(final_score, fallback)

    return final_score

# Main execution
metrics = [78, 85, 63, 91, 77]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")