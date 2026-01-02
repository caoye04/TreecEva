def evaluate_performance(metrics, base):
    # Irrelevant transformation (distractor)
    normalized = [round(x / sum(metrics) * 100, 2) for x in metrics]
    
    # Semi-relevant preprocessing
    filtered = [x for x in metrics if x > base * 0.75]
    
    # Dead code path - never executed due to data
    if len(metrics) > 100:
        return -1
    
    # Core logic begins here
    high_performers = set()
    for i, val in enumerate(metrics):
        if val > base:
            high_performers.add(i)
    
    # Additional distraction: unused set operation
    indices = set(range(len(metrics)))
    low_performers = indices.difference(high_performers)
    suspicious_indices = {i for i in low_performers if metrics[i] < base * 0.5}
    
    # Conditional expression with side-effect-free computation
    adjustment = 1.2 if len(high_performers) >= 3 else 0.9
    
    # Key computation chain
    raw_score = sum(metrics) / len(metrics)
    bonus = len(high_performers) * 5
    penalty = len(suspicious_indices) * 3
    temp_result = (raw_score * adjustment) + bonus - penalty
    
    # Early return red herring (never triggered)
    if temp_result < 0:
        return 0
    
    # Final score calculation
    final_score = int(temp_result // 1)  # Floor to integer
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Baseline configuration
baseline = 20
metric_set = [25, 18, 30, 22, 15, 35]

# Trigger execution
final_score = evaluate_performance(metric_set, baseline)