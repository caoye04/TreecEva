def evaluate_performance(metrics, base):
    # Initialize tracking variables
    total_weight = 0.0
    raw_sum = 0.0
    penalty_factor = 1.0
    adjustment_log = []
    
    # Auxiliary calculation with partial relevance
    outlier_count = 0
    smoothed_values = []
    for val in base:
        if abs(val - sum(base) / len(base)) > 2 * (max(base) - min(base)) / 4:
            outlier_count += 1
        smoothed_val = val * 0.9 + (sum(base) / len(base)) * 0.1
        smoothed_values.append(smoothed_val)
    
    # Misleading transformation (not used in final path but looks important)
    transformed_metrics = {x: (x ** 0.5 if x > 0 else 0) for x in metrics}
    temp_result = sum(transformed_metrics.values()) / len(transformed_metrics) * 1.5
    
    # Core logic begins: filter relevant metrics using set operations
    significant_metrics = metrics - {min(metrics), max(metrics)}
    filtered_baseline = [v for v in smoothed_values if v > sum(smoothed_values) / len(smoothed_values)]
    
    # Secondary filtering based on alignment with significant metrics
    aligned_count = 0
    for m in significant_metrics:
        index = m % len(filtered_baseline)
        if filtered_baseline[index] > m * 0.1:
            aligned_count += 1
            adjustment_log.append(m * 0.1)

    # Weighted aggregation with conditional boost
    dynamic_weight = 1.0
    if len(significant_metrics) > 2 and aligned_count >= 2:
        dynamic_weight += 0.25
    
    for metric in significant_metrics:
        contribution = metric * dynamic_weight
        raw_sum += contribution
        total_weight += dynamic_weight
    
    # Final adjustment using historical bias (simulated constant)
    historical_bias = 0.95
    preliminary_score = raw_sum / total_weight if total_weight != 0 else 0
    
    # Distractor block: complex but unused scoring alternative
    alt_score = 0
    if len(metrics) > len(base):
        alt_score = sum(metrics) / len(metrics)
    else:
        temp_arr = [x for x in base if x in metrics]
        alt_score = sum(temp_arr) / len(temp_arr) if temp_arr else 0
    # End of distractor
    
    # Final computation
    final_score = (preliminary_score * historical_bias) + (aligned_count * 0.5)
    
    # Additional red herring variable
    normalized_ratio = (final_score + temp_result) / (outlier_count + 1) if outlier_count else final_score
    
    return final_score

# Main execution
baseline_data = [12, 15, 10, 18, 14, 16, 9]
metric_set = {8, 12, 14, 15, 18, 20}
final_score = evaluate_performance(metric_set, baseline_data)
print(f"Result: {final_score}")