def evaluate_performance(data, importance):
    base = sum([x * 0.85 for x in data if x > 5])
    bonus = 0
    penalty = 0
    
    temp_values = [data[i] + data[-(i+1)] for i in range(len(data))]
    mirror_sum = sum(temp_values[:len(temp_values)//2])
    
    for idx, val in enumerate(data):
        if val >= 8 and idx % 2 == 0:
            bonus += 3
        elif val < 4 and idx % 3 == 0:
            penalty += 2

    # Irrelevant intermediate calculation (distractor)
    avg_temp = mirror_sum / len(temp_values) if temp_values else 0
    adjusted_avg = avg_temp * 1.1 if avg_temp > 6 else avg_temp * 0.9

    # Actual score computation
    raw_score = base + bonus - penalty
    
    weighted_sum = sum(d * w for d, w in zip(data, importance))
    normalization_factor = sum(importance) or 1
    
    # Final score depends on both raw logic and weights
    final_score = (raw_score * 0.6) + (weighted_sum / normalization_factor * 0.4)
    
    # Dead code path (never executed but looks relevant)
    if False:
        correction = len(data) - len(importance)
        final_score += correction

    return final_score

# Main execution
metrics = [7, 9, 3, 8, 6, 2, 7]
weights = [0.5, 1.0, 0.3, 1.2, 0.7, 0.4, 0.9]

# Unused variables (distractors)
candidate_level = 'senior'
evaluation_date = '2023-11-15'
threshold_pass = 25.0
min_requirement = any(x >= 9 for x in metrics)

intermediate_snapshot = metrics[1:5:2]
summary_stats = {"high": len([x for x in metrics if x >= 7]), "low": len([x for x in metrics if x < 5])}

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")