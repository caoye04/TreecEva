def evaluate_performance(weights, scores):
    # Normalize scores using min-max scaling (irrelevant for final result)
    min_score, max_score = min(scores), max(scores)
    normalized = [(s - min_score) / (max_score - min_score + 1e-8) for s in scores]

    # Apply weight masking based on performance tier (distractor logic)
    tiers = ['low', 'medium', 'high']
    performance_tier = tiers[len(scores) % 3]
    mask = [1 if i % 2 == 0 else 0.5 for i in range(len(weights))]  # Semi-relevant masking

    # Core computation: weighted sum with slicing and conditional adjustment
    relevant_weights = weights[1:-1]  # Slice to exclude first and last weight
    trimmed_scores = scores[1:-1]
    weighted_sum = sum(w * s for w, s in zip(relevant_weights, trimmed_scores))

    # Dead code path - never executed due to fixed condition (distractor)
    if performance_tier == 'ultra':
        bonus = 100
    else:
        bonus = 0

    # Conditional logic affecting final score
    adjustment = 0.0
    if weighted_sum > 40:
        adjustment = 5.0
    elif weighted_sum > 30:
        adjustment = 2.5
    else:
        adjustment = 0.0

    # Dictionary-based multiplier lookup (semi-relevant)
    multipliers = {'low': 1.0, 'medium': 1.1, 'high': 1.2}
    multiplier = multipliers[performance_tier]

    # Final score calculation (this is the key line)
    final_score = (weighted_sum + adjustment) * multiplier

    # Irrelevant post-processing (distractor)
    outlier_count = sum(1 for s in scores if s > 90)
    penalty = outlier_count * 0.1

    return final_score

# Main execution
metric_weights = [0.5, 1.2, 0.8, 1.5, 0.7]
raw_scores = [85, 76, 88, 92, 74]

# Intermediate distractor variables
average_raw = sum(raw_scores) / len(raw_scores)
sorted_pairs = sorted(zip(metric_weights, raw_scores), key=lambda x: x[0])
duplicate_calc = sum(s**2 for s in raw_scores[:3])  # Unused computation

final_score = evaluate_performance(metric_weights, raw_scores)
print(f"Target result: {final_score}")