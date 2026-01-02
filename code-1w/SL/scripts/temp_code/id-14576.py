def evaluate_performance(data, importance):
    # Initialize various tracking variables (some are distractions)
    total = 0
    bonus = 0
    penalty = 0
    temp_sum = 0  # used in intermediate calc
    adjustment_factor = 0.95
    
    # Irrelevant data structure - distractor
    historical_bonuses = {2019: 5, 2020: 3, 2021: 7, 2022: 2}
    recent_trends = [0.8, 0.9, 1.0, 1.1]
    trend_multiplier = sum(recent_trends) / len(recent_trends)  # not actually used
    
    # Real computation begins
    weighted_sum = sum(x * y for x, y in zip(data, importance))
    
    # Conditional bonus logic (partially relevant)
    if weighted_sum > 80:
        bonus = 10
        extra_incentive = 5  # dead variable
    elif weighted_sum > 60:
        bonus = 5
    else:
        penalty = 8
        
    # Another distraction: unused helper lambda
    calculate_risk = lambda x: x * 0.1 if x < 50 else x * 0.05
    risk_adjusted = calculate_risk(weighted_sum)  # computed but unused
    
    # More irrelevant computation
    normalized_data = [x / max(data) for x in data if x > 0]
    avg_normalized = sum(normalized_data) / len(normalized_data)
    efficiency_ratio = avg_normalized * 100  # semi-relevant, never used
    
    # Key state tracking with set operations (relevant)
    critical_metrics = set(range(len(data)))
    dropped_indices = set()
    for i, val in enumerate(data):
        if val < 50:
            dropped_indices.add(i)
    retained_metrics = critical_metrics - dropped_indices
    retention_rate = len(retained_metrics) / len(critical_metrics)
    
    # Apply retention adjustment
    if retention_rate >= 0.7:
        total = weighted_sum * adjustment_factor + bonus
    else:
        total = weighted_sum - penalty
    
    # Final score assignment
    final_score = int(total)  # answer is deterministic integer
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
metrics = [85, 90, 75, 88, 92]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Execute function
final_score = evaluate_performance(metrics, weights)