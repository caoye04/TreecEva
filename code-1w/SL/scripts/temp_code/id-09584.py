def evaluate_performance(metrics, base):
    # Irrelevant transformation (distractor)
    normalized = [round(x / 1.5, 2) for x in metrics]
    
    # Semi-relevant filtering
    filtered_metrics = {x for x in metrics if x > base * 0.8}

    # Misleading cumulative sum that isn't used
    temp_sum = 0
    for val in normalized:
        temp_sum += val * 0.1
    
    # Core logic: count how many metrics exceed 110% of baseline
    threshold = base * 1.1
    above_threshold = {x for x in metrics if x > threshold}
    
    # Additional state tracking (some distraction)
    status_flags = []
    for m in metrics:
        if m < base * 0.5:
            status_flags.append('LOW')
        elif m > base * 1.2:
            status_flags.append('HIGH')
    
    # Actual score computation
    bonus = len(above_threshold) * 5
    penalty = len(status_flags)  # counts all flagged entries, but only HIGH matters
    high_count = len([f for f in status_flags if f == 'HIGH'])
    adjustment = high_count * 2
    
    # Final decision logic with nested conditionals
    if len(filtered_metrics) >= 3:
        base_score = 70
        if bonus > 10:
            base_score += 15
        else:
            base_score += 5
    else:
        base_score = 50
    
    # Critical assignment point
    final_score = base_score + bonus - penalty + adjustment
    
    # Dead code path (irrelevant print)
    if False:
        print(f'Debug: {temp_sum}, {normalized}')
        
    return final_score

# Input setup
metric_data = [85, 92, 103, 76, 115]
baseline_reference = 90

# Execute and print result
result = evaluate_performance(metric_data, baseline_reference)
print(f"Target result: {result}")