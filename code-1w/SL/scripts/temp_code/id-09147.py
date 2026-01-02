def evaluate_performance(data, importance):
    base = sum(x * y for x, y in zip(data, importance))
    adjustment = 0
    temp_factor = 0
    
    # Irrelevant computation chain (distractor)
    temp_vals = [x ** 2 for x in data]
    temp_sum = sum(temp_vals)
    if temp_sum > 100:
        adjustment += 5
        outlier_count = len([x for x in data if x > 10])
        scaling = outlier_count / len(data) if data else 0
        temp_factor = scaling * 2
    
    # Real logic: apply conditional weight boost for high engagement
    engagement_index = data[2] if len(data) > 2 else 0
    boost = 1.2 if engagement_index > 7 else 1.0
    
    # Secondary distractor: unused loop over zipped data
    cumulative = 0
    for i, (val, w) in enumerate(zip(data, importance)):
        cumulative += val + w
        intermediate = cumulative * 0.1  # Dead computation

    # Actual contribution: only base and boost matter
    adjusted_base = base * boost
    
    # More red herring variables
    normalized = adjusted_base / (sum(importance) or 1)
    penalty = 0
    if sum(data) < 20:
        penalty = 2
    
    final_score = int(adjusted_base - penalty)  # Only this line matters for output
    
    # Additional misleading post-processing
    if final_score % 2 == 0:
        final_score += temp_factor  # temp_factor is float but won't affect int cast earlier
    
    return final_score

# Main execution
metrics = [8, 6, 9, 4]
weights = [0.3, 0.2, 0.4, 0.1]
final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")