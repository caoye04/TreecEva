def calculate_final_score(ranks, coeffs):
    # Irrelevant transformation (distractor)
    normalized = [r / sum(ranks) for r in ranks]
    temp_sum = sum(normalized[:2]) * 1.5

    # Actual computation begins
    weighted_values = []
    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        if rank <= 3:
            bonus = 10 // rank  # Higher bonus for top ranks
        else:
            bonus = 0
        # Conditional expression used
        adjusted_weight = weight * 1.1 if bonus > 0 else weight * 0.9
        weighted_values.append((rank + bonus) * adjusted_weight)

    # Secondary distractor: unused sorting and slicing
    sorted_vals = sorted(weighted_values, reverse=True)
    middle_slice = sorted_vals[1:4]  # Not used later
    avg_middle = sum(middle_slice) / len(middle_slice)

    # Real aggregation
    base_total = sum(weighted_values)
    penalty = 0
    for idx, val in enumerate(weighted_values):
        if idx % 2 == 1 and val > avg_middle * 0.8:
            penalty += 2

    # Final score computation
    final = int(base_total - penalty)

    # Dead code path (never executed due to data)
    if any(x < 0 for x in ranks):
        fallback = sum(coeffs) * min(ranks)
        final = fallback  # Not triggered

    return final

# Input setup
rankings = [1, 4, 2, 6, 3]
weights = [5, 3, 8, 2, 7]

# Unused auxiliary variables (distractors)
duplicate_ranks = rankings.copy()
sorted_weights = sorted(weights, reverse=True)
weight_map = {i: w for i, w in enumerate(sorted_weights)}

# Key execution point
final_score = calculate_final_score(rankings, weights)

# Output result
print(f"Result: {final_score}")