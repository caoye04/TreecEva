def evaluate_performance(metrics, baseline):
    # Irrelevant transformation
    temp_normalized = [round((x - min(metrics)) / (max(metrics) - min(metrics)) * 100) for x in metrics]
    
    # Distractor: unused weight adjustment
    weights = {key: 1.0 for key in ['a', 'b', 'c']}
    adjustment_factor = sum(weights.values()) * 0.1
    
    # Semi-relevant preprocessing
    adjusted_metrics = []
    for i, val in enumerate(metrics):
        if val > baseline:
            adjusted_metrics.append(val * 0.9)
        else:
            adjusted_metrics.append(val * 1.1)
    
    # Another distractor computation (dead path)
    outlier_count = 0
    for val in metrics:
        if val < baseline * 0.5 or val > baseline * 2.0:
            outlier_count += 1
    
    # Actual logic: count how many adjusted values exceed original baseline
    above_threshold = 0
    for val in adjusted_metrics:
        if val > baseline:
            above_threshold += 1
    
    # Final score based on count and base metric
    final_score = above_threshold * baseline // len(metrics)
    
    # Unused complex structure
    summary_stats = {
        'count': len(metrics),
        'outliers': outlier_count,
        'adjustment': adjustment_factor
    }
    
    return final_score

# Input data
metrics = [85, 90, 78, 92, 88]
baseline = 80

# Key execution point
final_score = evaluate_performance(metrics, baseline)

print(f"Result: {final_score}")