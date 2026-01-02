def evaluate_performance(metrics, threshold):
    # Initialize various tracking variables (some are distractions)
    temp_accum = 0
    outlier_count = 0
    normalized_sum = 0.0
    adjustment_factor = 1.5
    
    # Irrelevant statistical tracking (distractor)
    mean_deviation = 0
    deviation_samples = []
    
    for val in metrics:
        if val > threshold * 2:
            outlier_count += 1
        if val < threshold:
            temp_accum += val * 0.5
        else:
            temp_accum += val * 1.1
    
    # Semi-relevant transformation
    raw_total = sum(metrics)
    penalty = outlier_count * 3
    
    # Complex normalization with red herring logic
    if len(metrics) > 5:
        scaling_factor = 0.9
    else:
        scaling_factor = 1.0
    
    # Dead code path - never executed due to data, but looks relevant
    consistency_check = True
    for i in range(len(metrics) - 1):
        if abs(metrics[i] - metrics[i+1]) > 20:
            consistency_check = False
            break

    # Unused helper computation (distraction)
    avg_metric = raw_total / len(metrics) if metrics else 0
    variance_proxy = sum((x - avg_metric) ** 2 for x in metrics) / len(metrics) if metrics else 0

    # Core logic hidden among distractions
    valid_metrics = {x for x in metrics if x >= threshold}  # Set operation (required feature)
    filtered_sum = sum(valid_metrics)
    bonus = len(valid_metrics) * 2
    
    # Final calculation using key variables
    final_score = int((filtered_sum + bonus - penalty) * scaling_factor)
    
    return final_score

# Main execution
base_threshold = 8
metric_data = [5, 12, 9, 3, 14, 7, 11]
data_variance = sum((x - 8.5) ** 2 for x in metric_data)  # Unused
max_value = max(metric_data)  # Slight distraction
min_value = min(metric_data)  # Slight distraction

count_above_avg = len([x for x in metric_data if x > 8])  # Computed but unused

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)
print(f"Result: {final_score}")