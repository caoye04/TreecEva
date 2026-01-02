def calculate_final_score(performances, importance_weights):
    base_adjustment = 0.0
    bonus_multiplier = 1.2
    penalty_factor = 0.8
    intermediate_results = []
    temp_aggregate = 0

    for idx, (perf, weight) in enumerate(zip(performances, importance_weights)):
        weighted_perf = perf * weight
        if idx % 2 == 0:
            adjusted_perf = weighted_perf * bonus_multiplier
        else:
            adjusted_perf = weighted_perf * penalty_factor

        # Distractor: unused computation
        squared_deviation = (perf - 5) ** 2
        temp_aggregate += squared_deviation  # Irrelevant to final result

        intermediate_results.append(adjusted_perf)

    # Real computation path
    raw_total = sum(intermediate_results)
    scaling_offset = len(intermediate_results) * 0.1
    final_score = raw_total + scaling_offset

    # More distractions: dead code and red herring variables
    outlier_count = 0
    for val in performances:
        if val > 10:
            outlier_count += 1
    # This logic is never used

    auxiliary_sum = 0
    for w in importance_weights:
        auxiliary_sum += w ** 0.5
    # Unused helper sum

    return int(final_score)

# Input data
rankings = [4, 7, 6, 3, 8]
weights = [0.5, 1.0, 0.8, 0.6, 1.2]

# Execute main logic
final_score = calculate_final_score(rankings, weights)

# Print result
print(f"Result: {final_score}")