def calculate_final_score(ranks, coeffs):
    # Initialize variables
    base_points = 0
    bonus_adjustment = 0
    penalty_tracker = []
    intermediate_results = []

    # Irrelevant tracking (distractor)
    debug_log = []
    for i in range(len(ranks)):
        if ranks[i] < 0:
            debug_log.append(f"Invalid rank at index {i}")

    # Real computation begins
    weighted_sum = sum(ranks[i] * coeffs[i] for i in range(len(ranks)))

    # Simulate performance bands (semi-relevant)
    performance_bands = {1: 'A', 2: 'B', 3: 'C'}
    band_counts = {k: 0 for k in performance_bands}

    for val in ranks:
        band_index = min(val // 10 + 1, 3) if val > 0 else 1
        if band_index in band_counts:
            band_counts[band_index] += 1

    # Bonus logic based on distribution (distraction with partial relevance)
    if band_counts[1] == 0 and len(ranks) >= 3:
        bonus_adjustment += 5
    elif len(ranks) > 4:
        bonus_adjustment += 2

    # Core transformation
    transformed = [abs(x - 5) for x in ranks]
    filtered = [t for t in transformed if t % 2 == 0]

    # More distractions: unused helper list
    temp_aggregates = []
    for x in filtered:
        temp_aggregates.append(x ** 0.5)

    # Actual score contribution from filtered even deviations
    diversity_factor = len(set(filtered))
    base_points += sum(filtered) + diversity_factor

    # Apply modular adjustment based on coefficient symmetry
    coeff_symmetric = coeffs == coeffs[::-1]
    if coeff_symmetric:
        base_points += 10

    # Final composition
    raw_score = base_points + bonus_adjustment
    scaling_factor = 1.5 if len(ranks) > 3 else 1.0
    final_score = int(raw_score * scaling_factor)

    # Dead code path (irrelevant print)
    if False:
        print(f"Temp aggregates: {temp_aggregates}")

    return final_score

# Input data
rankings = [8, 3, 12, 7, 9]
weights = [2, 1, 3, 1, 2]

# Execution
final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")