def calculate_final_score(entries, importance_factors):
    # Normalize weights to sum to 1.0
    total_weight = sum(importance_factors)
    normalized_weights = [w / total_weight for w in importance_factors]

    # Extract scores and ranks using enumerate and zip
    raw_scores = []
    for i, entry in enumerate(entries):
        score = entry['score']
        penalty = 0
        if entry['errors'] > 0:
            penalty = entry['errors'] * 5
        adjusted_score = score - penalty
        raw_scores.append(adjusted_score)

    # Misleading intermediate calculation (not used in final logic)
    avg_raw = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    inflated_scores = [s + avg_raw * 0.1 for s in raw_scores]  # Distractor

    # Use lambda to compute dynamic adjustment based on rank position
    rank_boost = list(map(lambda idx: 1 + (0.1 * (len(entries) - idx)), range(len(entries))))

    # Apply correct scoring: weighted sum of raw scores with rank boost
    final_components = []
    for i, (score, weight) in enumerate(zip(raw_scores, normalized_weights)):
        boosted = score * rank_boost[i]
        contribution = boosted * weight
        final_components.append(contribution)

    # Dead code path - never executed due to prior logic
    if False:
        fallback = sum(inflated_scores) * 0.95
        final_components.append(fallback)

    result = sum(final_components)
    return round(result, 4)


# Simulated dataset: model evaluation rankings
rankings = [
    {'name': 'ModelA', 'score': 89, 'errors': 2},
    {'name': 'ModelB', 'score': 92, 'errors': 5},
    {'name': 'ModelC', 'score': 95, 'errors': 1},
    {'name': 'ModelD', 'score': 87, 'errors': 3}
]

# Weighting factors based on evaluation criteria importance
weights = [0.4, 0.3, 0.2, 0.1]

# Extra unused variables to increase cognitive load
baseline_avg = sum(item['score'] for item in rankings) / len(rankings)
decay_factor = 0.98
smoothing_param = 0.05

# Key execution point
final_score = calculate_final_score(rankings, weights)

# Output result as required
print(f"Result: {final_score}")