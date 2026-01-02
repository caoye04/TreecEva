def calculate_final_score(ranks, coeffs):
    # Irrelevant transformation (dead-end computation)
    normalized = [r / sum(ranks) for r in ranks]
    temp_sum = sum([n ** 0.5 for n in normalized])

    # Real computation path: weighted harmonic mean with ranking adjustment
    adjusted_weights = [w + 0.1 for w in coeffs]  # Smoothing
    weighted_inv = [adjusted_weights[i] / (ranks[i] + 1e-9) for i in range(len(ranks))]
    harmonic_base = sum(weighted_inv)

    # Additional distraction: unused sorting and filtering
    filtered_ranks = [r for r in ranks if r < 4]
    sorted_coeffs = sorted(coeffs, reverse=True)
    dummy_aggregate = sum([filtered_ranks[i] * sorted_coeffs[i % len(sorted_coeffs)] for i in range(len(filtered_ranks))])

    # Main result calculation
    scale_factor = 100 / (harmonic_base + 1e-9)
    intermediate_scores = [scale_factor * (coeffs[i] / (ranks[i] + 1e-9)) for i in range(len(ranks))]
    
    # Aggregate final score
    final = sum(intermediate_scores) / len(intermediate_scores)

    # More red herring variables
    outlier_check = [s for s in intermediate_scores if s > 2 * scale_factor]
    correction_term = len(outlier_check) * 0.05

    return final  # Correction term not applied - just a distraction

# Input data
rankings = [1, 3, 4, 2]
weights = [0.4, 0.2, 0.3, 0.5]

# Unused but plausible-looking preprocessing
reversed_weights = [w for w in reversed(weights)]
rank_pairs = [(rankings[i], weights[i]) for i in range(len(rankings))]
sorted_pairs = sorted(rank_pairs, key=lambda x: x[0])

# Key statement
final_score = calculate_final_score(rankings, weights)

print(f"Result: {final_score}")