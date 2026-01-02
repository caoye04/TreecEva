def calculate_final_score(data, weight_map):
    base_scores = {}
    for key in data:
        if key in weight_map:
            base_scores[key] = data[key] * weight_map[key]
    
    # Irrelevant transformation (distractor)
    temp_offsets = {k: len(k) * 0.1 for k in data.keys()}
    adjusted_offsets = [v for v in temp_offsets.values() if v > 0.2]
    offset_correction = sum(adjusted_offsets) / len(adjusted_offsets) if adjusted_offsets else 0.0

    # Real computation path
    raw_sum = sum(base_scores.values())
    count_factor = len([v for v in data.values() if v > 5])
    bonus_modifier = 3 if count_factor >= 3 else 1

    # Dead code branch (misleading)
    if offset_correction < 0:
        bonus_modifier *= -1

    intermediate_total = raw_sum + (offset_correction * bonus_modifier)

    # Additional irrelevant list comprehension (distractor)
    redundant_flags = [k.upper() for k in data if data[k] % 2 == 0 and len(k) < 8]
    flag_penalty = len(redundant_flags) * 0.05

    final_normalized = intermediate_total - flag_penalty
    return int(final_normalized)

# Main execution context
rank_data = {
    'alpha': 7,
    'beta': 4,
    'gamma': 9,
    'delta': 6,
    'epsilon': 3
}

weights = {
    'alpha': 2,
    'gamma': 3,
    'delta': 1,
    'beta': 2,
    'zeta': 4  # unused key
}

# Extraneous pre-computations (distraction)
candidate_names = [k for k in rank_data.keys()]
sorted_ranks = sorted(rank_data.values(), reverse=True)
mean_rank = sum(sorted_ranks) / len(sorted_ranks)

# Key statement
final_score = calculate_final_score(rank_data, weights)

# Output result
print(f"Result: {final_score}")