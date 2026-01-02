def calculate_final_score(ranks, coeffs):
    # Normalize ranks using min-max scaling (irrelevant for final logic but looks important)
    min_rank = min(ranks)
    max_rank = max(ranks)
    normalized = [(r - min_rank) / (max_rank - min_rank + 1e-9) for r in ranks]

    # Apply weights using lambda (actual relevant step)
    weighted_sum = sum(map(lambda x, w: x * w, ranks, coeffs))

    # Dummy transformation on coefficients (distractor)
    transformed_coeffs = [c ** 2 for c in coeffs]
    temp_correction = sum(transformed_coeffs) / len(transformed_coeffs)

    # Redundant set operation to track unique contributions (semi-relevant but not used directly)
    unique_contributions = set()
    for i, (r, w) in enumerate(zip(ranks, coeffs)):
        contribution = r * w
        if contribution > 0.5 * weighted_sum / len(ranks):
            unique_contributions.add(i)

    # Secondary scoring using enumerate (distractor with partial relevance)
    secondary_score = 0
    for idx, val in enumerate(ranks):
        if idx % 2 == 0:
            secondary_score += val * 0.1

    # Actual core logic: weighted harmonic mean (key computation)
    weighted_harmonic_components = []
    for r, w in zip(ranks, coeffs):
        if r != 0:
            weighted_harmonic_components.append(w / r)
    if sum(weighted_harmonic_components) != 0:
        harmonic_base = sum(coeffs) / sum(weighted_harmonic_components)
    else:
        harmonic_base = 0

    # Final score combines harmonic base and weighted sum with adjustment
    # Despite distractions, this is where the answer comes from
    final_component = weighted_sum * 0.6 + harmonic_base * 0.4

    # Dead code path (never executed but adds confusion)
    if temp_correction < 0:
        final_component *= 1.1

    return int(round(final_component))


# Input data
rankings = [10, 5, 8, 3, 12]
weights = [0.1, 0.3, 0.2, 0.25, 0.15]

# Additional irrelevant variables (distraction)
data_log = []
for i, r in enumerate(rankings):
    data_log.append({'index': i, 'value': r, 'flagged': r > 7})

# Semi-useful tuple unpacking (adds complexity)
total_weight = sum(weights)
count_high_rank = len([r for r in rankings if r > 7])
diagnostic_tuple = (total_weight, count_high_rank)

# Key execution point
final_score = calculate_final_score(rankings, weights)

# Print result
print(f"Result: {final_score}")