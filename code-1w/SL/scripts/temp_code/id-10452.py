def calculate_final_score(ranks, coeffs):
    # Preprocessing: Normalize rankings using a lambda transformation
    normalized = [(lambda x: (x - min(ranks)) / (max(ranks) - min(ranks) + 1e-8))(rank) for rank in ranks]

    # Irrelevant distraction: Compute entropy-like metric (not used in final result)
    import math
    entropy = 0.0
    for r in ranks:
        prob = r / sum(ranks)
        entropy -= prob * math.log(prob + 1e-8)

    # Distractor list comprehension: compute squared deviations (unused)
    deviations = [((i + 1) - r) ** 2 for i, r in enumerate(ranks)]

    # Actual weighting logic: apply coefficients with offset correction
    adjusted_weights = []
    for i, w in enumerate(coeffs):
        if i % 2 == 0:
            adjusted_weights.append(w * 1.1)
        else:
            adjusted_weights.append(w * 0.9)

    # Core calculation: dot product of normalized ranks and adjusted weights
    weighted_sum = sum(normalized[i] * adjusted_weights[i] for i in range(len(normalized)))

    # Final nonlinear scaling (deterministic)
    final_score = int(weighted_sum * 1000 + 0.5)  # Round to nearest integer

    return final_score


# Input data
rankings = [10, 5, 8, 3, 12]
weights = [0.2, 0.4, 0.1, 0.25, 0.05]

# Additional red herring: unused helper function
find_median = lambda lst: sorted(lst)[len(lst)//2]
median_rank = find_median(rankings)

# Unused transformation
inverted_ranks = list(map(lambda x: 1 / (x + 1), rankings))

# Key execution point
final_score = calculate_final_score(rankings, weights)

# Output result
print(f"Target result: {final_score}")