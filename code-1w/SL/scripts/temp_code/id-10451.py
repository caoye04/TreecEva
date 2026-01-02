def evaluate_performance(weights, scores):
    # Normalize scores using min-max scaling (irrelevant for final result)
    min_score, max_score = min(scores), max(scores)
    normalized = [(s - min_score) / (max_score - min_score + 1e-8) for s in scores]

    # Apply weight transformation via lambda (only some weights are actually used)
    transformed_weights = list(map(lambda w: w ** 2 + 0.1, weights))

    # Misleading entropy-like computation (not used in final score)
    import math
    shannon_entropy = -sum(w * math.log(w + 1e-9) for w in weights)

    # Core logic: only first three scores and weights matter
    relevant_scores = scores[:3]
    effective_weights = weights[:3]

    # Weighted sum on relevant dimensions
    weighted_sum = sum(score * weight for score, weight in zip(relevant_scores, effective_weights))

    # Secondary adjustment based on conditional logic
    bonus = 0
    if weighted_sum > 75:
        bonus = 10
    elif weighted_sum > 60:
        bonus = 5

    # Final aggregation with red herring variables
    base_result = weighted_sum + bonus
    scaling_factor = 1.0  # unused distraction
    offset_correction = "N/A"  # irrelevant string

    # Final score calculation
    final_score = base_result + shannon_entropy * 0  # entropy not actually applied

    return final_result

# Input data
evaluation_metric_weights = [0.4, 0.3, 0.3, 0.5, 0.2]
eraw_performance_scores = [80, 70, 90, 45, 60]

# Execution point of interest
final_score = evaluate_performance(evaluation_metric_weights, eraw_performance_scores)
print(f"Result: {final_score}")