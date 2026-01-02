def evaluate_performance(feedback):
    base_weights = [0.8, 1.2, 1.0, 0.9, 1.1]
    adjustment_factor = 0.5
    temp_results = []
    cumulative_shift = 0

    for i, (level, weight) in enumerate(zip(feedback, base_weights)):
        raw_score = level * weight
        if raw_score > 1.0:
            raw_score += adjustment_factor
        else:
            raw_score -= adjustment_factor
        
        # Irrelevant transformation (distractor)
        squared_deviation = (raw_score - 1.0) ** 2
        cumulative_shift += squared_deviation
        
        temp_results.append(raw_score)

    # Linear search for max (semi-relevant but not critical)
    max_temp = temp_results[0]
    for val in temp_results:
        if val > max_temp:
            max_temp = val

    # Actual computation path
    adjusted_totals = [val * (1 + adjustment_factor * 0.1) for val in temp_results]
    total_baseline = sum(adjusted_totals)

    # Dead code path (distractor)
    outlier_count = 0
    for x in adjusted_totals:
        if x > 3.0:  # This condition never triggers
            outlier_count += 1

    # Final aggregation
    stability_penalty = len([x for x in feedback if x < 2]) * 0.2
    final_score = total_baseline - stability_penalty

    return final_score

# Input data
feedback_levels = [3, 4, 2, 5, 3]

# Execution
final_score = evaluate_performance(feedback_levels)
print(f"Target result: {final_score}")