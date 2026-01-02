def evaluate_performance(metrics, threshold):
    # Irrelevant transformation
    temp_data = [x * 1.05 for x in metrics if x > 0]
    adjusted_metrics = [max(0, x - 2) for x in metrics]
    
    # Distractor: unused helper calculation
    outlier_count = 0
    for val in adjusted_metrics:
        if val > 20:
            outlier_count += 1

    # Real computation begins
    above_threshold = [val for val in adjusted_metrics if val >= threshold]
    if len(above_threshold) == 0:
        return -1
    
    avg_above = sum(above_threshold) / len(above_threshold)
    stability_factor = 1.0
    
    # Additional distraction: complex but unused logic
    rolling_avg_diffs = []
    for i in range(1, len(adjusted_metrics)):
        rolling_avg_diffs.append(abs(adjusted_metrics[i] - adjusted_metrics[i-1]))
    
    # Actual decision path
    if avg_above >= 15:
        stability_factor = 1.2
    elif avg_above >= 10:
        stability_factor = 1.1
    else:
        stability_factor = 0.9

    base_score = sum(adjusted_metrics) / len(adjusted_metrics)
    final_score = base_score * stability_factor
    
    # Red herring: modifying unrelated state
    debug_log = {'processed': len(metrics), 'filtered': len(above_threshold)}
    debug_log['version'] = '2.1'

    return int(final_score)

# Input data
metrics = [18, 12, 25, 3, 7, 16, 14]
threshold = 10

# Execution point
final_score = evaluate_performance(metrics, threshold)
print(f"Result: {final_score}")