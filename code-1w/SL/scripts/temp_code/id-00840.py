def calculate_final_score(ranks, coeffs):
    # Irrelevant transformation (dead computation)
    temp_adjustments = [r * 0.95 for r in ranks if r > 2]
    temp_adjustments = [t + 1 for t in temp_adjustments]  # Distractor

    # Core logic: weighted sum with conditional boost
    base_scores = [r * c for r, c in zip(ranks, coeffs)]
    boosted_scores = []
    for i, score in enumerate(base_scores):
        if score >= 10:
            boosted_scores.append(score * 1.2)
        elif score <= 5:
            boosted_scores.append(score * 0.8)
        else:
            boosted_scores.append(score)

    # Additional irrelevant filtering
    filtered_ranks = {i: r for i, r in enumerate(ranks) if r % 2 == 1}  # Not used later

    # Secondary processing: normalize and scale
    total_boosted = sum(boosted_scores)
    avg_boosted = total_boosted / len(boosted_scores)

    # Apply non-linear adjustment based on average
    if avg_boosted > 8:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.95

    # Final aggregation
    adjusted_total = total_boosted * adjustment_factor

    # Simulate ranking penalty for variance
    variance_proxy = max(boosted_scores) - min(boosted_scores)
    penalty = 0
    if variance_proxy > 15:
        penalty = 5
    elif variance_proxy > 10:
        penalty = 3
    else:
        penalty = 1

    final_score = int(adjusted_total - penalty)

    # Dead code branch (never reached in practice)
    if False:
        fallback = sum(ranks) * 2
        final_score = fallback

    return final_score

# Input data
rankings = [4, 7, 12, 5, 9]
weights = [1.0, 1.2, 1.5, 0.8, 1.1]

# Irrelevant auxiliary list comprehension
squared_weights = [w**2 for w in weights]
dropped_calc = [w for w in weights if w < 1.0]

# Key execution point
final_score = calculate_final_score(rankings, weights)

# Output result
print(f"Result: {final_score}")