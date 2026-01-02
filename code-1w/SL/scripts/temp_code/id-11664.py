def calculate_final_score(ranks, coeffs):
    # Initialize variables
    base_score = 0
    penalty = 0
    bonus_tracker = []
    temp_result = 0

    # Irrelevant pre-processing (distractor)
    normalized_ranks = [r / sum(ranks) for r in ranks]
    scaled_coeffs = [c * 10 for c in coeffs]

    # Real computation begins
    weighted_sum = 0
    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        if rank < 5:
            contribution = rank * weight
            weighted_sum += contribution
            
            # Track bonuses for top performers (only top 3)
            if i < 3:
                bonus_tracker.append(contribution * 0.1)
        else:
            penalty += 1

    # Secondary adjustment based on ranking distribution
    distinct_ranks = len(set(ranks))
    diversity_bonus = 0.5 if distinct_ranks > 4 else 0.2

    # Dummy loop with no impact (dead code path - distractor)
    cumulative_shift = 0
    for shift in range(len(coeffs)):
        cumulative_shift += shift * 0.01  # negligible effect, ignored

    # Another irrelevant transformation
    reversed_weights = coeffs[::-1]
    for j, val in enumerate(reversed_weights):
        temp_result += val % (j + 1) if j + 1 != 0 else 0

    # Final score calculation - only weighted_sum, penalty, and diversity_bonus matter
    base_score = weighted_sum - penalty + diversity_bonus

    final_score = int(base_score + sum(bonus_tracker))  # actual answer depends on this

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
rankings = [1, 3, 4, 6, 2, 8, 5]
weights = [2, 4, 3, 1, 5, 2, 4]

# Call function
final_score = calculate_final_score(rankings, weights)