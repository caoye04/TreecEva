def calculate_performance_rating():
    base_metrics = [85, 90, 78, 92]
    adjustment_factors = {'inflation': 1.02, 'bonus': 1.1, 'penalty': 0.9}
    
    # Irrelevant string processing (distractor)
    status_labels = ['pass', 'fail', 'exceeds']
    label_map = {label: idx for idx, label in enumerate(status_labels)}
    processed_label = ','.join(status_labels).upper().replace('FAIL', 'REVIEW')

    # Semi-relevant data transformation (some distraction)
    adjusted_metrics = []
    for val in base_metrics:
        temp_val = val * adjustment_factors['inflation']
        if temp_val > 85:
            temp_val *= adjustment_factors['bonus']
        else:
            temp_val *= adjustment_factors['penalty']
        adjusted_metrics.append(round(temp_val))

    # Dead code path (misleading branch)
    if len(base_metrics) > 10:
        fallback_value = sum(adjusted_metrics) / len(adjusted_metrics)
        return int(fallback_value)

    # Core logic embedded within noise
    outlier_threshold = 88
    filtered_metrics = [m for m in adjusted_metrics if m >= outlier_threshold]
    
    # Additional distraction with dictionary operations
    metric_stats = {
        'count': len(adjusted_metrics),
        'max': max(adjusted_metrics),
        'min': min(adjusted_metrics)
    }
    metric_stats['range'] = metric_stats['max'] - metric_stats['min']

    # Conditional expression with actual impact
    scaling_factor = 1.5 if metric_stats['range'] > 20 else 1.2
    
    # Final computation chain
    raw_sum = sum(filtered_metrics)
    penalty_deduction = 0
    for i in range(len(filtered_metrics)):
        if i % 2 == 1:
            penalty_deduction += 3
    
    intermediate_result = raw_sum - penalty_deduction
    final_score = int(intermediate_result * scaling_factor)

    # Misleading print (not affecting result)
    debug_info = f"Final internal state: {metric_stats}, labels: {processed_label}"
    
    return final_score

# Key execution point
final_score = calculate_performance_rating()
print(f"Result: {final_score}")