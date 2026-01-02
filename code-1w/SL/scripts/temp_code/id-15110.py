def evaluate_performance(metrics, weights):
    base_score = 0
    penalty_adjustment = 0
    temp_factor = 0.0
    final_score = 0
    
    # Irrelevant temperature-like computation (distractor)
    for i in range(len(metrics)):
        temp_factor += metrics[i] * 0.1
    
    # Real scoring logic with conditional weighting
    weighted_sum = 0.0
    total_weight = 0.0
    
    for idx, (metric, weight) in enumerate(zip(metrics, weights)):
        if metric < 0:
            penalty_adjustment -= 1
            continue
        if weight <= 0:
            continue
        weighted_sum += metric * weight
        total_weight += weight
        
        # Additional distraction: tracking unused intermediate
        debug_info = f"Step {idx}: added {metric}*{weight}"
    
    if total_weight > 0:
        base_score = weighted_sum / total_weight
    else:
        base_score = 0
    
    # Apply artificial cap and bonus (complexity + distractor)
    capped_base = min(base_score, 95.0)
    bonus = 5 if penalty_adjustment == 0 and base_score > 90 else 0
    
    # Final computation
    final_score = capped_base + bonus
    
    # Dead code path - never executed under normal inputs
    if False:
        final_score *= 1.1  # Would inflate, but unreachable
    
    return final_score

# Input data
metrics = [88, 92, -1, 94, 87]
weights = [0.2, 0.3, 0.0, 0.4, 0.1]

# Extra irrelevant variables (distractors)
baseline_ref = 85.5
temp_cache = []
iteration_log = {}

# Key execution point
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")