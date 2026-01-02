def calculate_final_score(ranks, weights):
    # Initialize tracking variables
    total_contributions = 0
    max_rank = max(ranks.values())
    min_rank = min(ranks.values())
    rank_range = max_rank - min_rank if max_rank != min_rank else 1

    # Normalization factor (distractor: not directly used in final logic)
    normalization = sum([v ** 0.5 for v in ranks.values()]) or 1

    adjusted_scores = {}
    for key, rank in ranks.items():
        normalized_rank = (max_rank - rank) / rank_range  # higher rank → higher score
        bonus = weights.get(key, 0.1) * normalized_rank
        adjusted_scores[key] = normalized_rank + bonus

    # Secondary processing with set operations (semi-relevant)
    elite_keys = {k for k, v in adjusted_scores.items() if v > 0.7}
    fallback_correction = 0.05 * len(elite_keys)

    # Aggregation with distraction via unused intermediate
    raw_sum = sum(adjusted_scores.values())
    count_factor = len(adjusted_scores)
    average_score = raw_sum / count_factor if count_factor else 0

    # Final computation chain
    volatility_index = sum(
        abs(adjusted_scores[k1] - adjusted_scores[k2])
        for k1 in adjusted_scores for k2 in adjusted_scores if k1 < k2
    ) / (count_factor ** 2) if count_factor > 1 else 0

    stability_modifier = 1 - (volatility_index * 0.8)
    final_contrib = average_score * stability_modifier + fallback_correction

    # Irrelevant dictionary transformation (dead path)
    _ = {k: round(v, 2) for k, v in adjusted_scores.items() if v > 1.5}  # never occurs

    return int(round(final_contrib * 100))


# Main execution context
rank_data = {
    'node_alpha': 3,
    'node_beta': 1,
    'node_gamma': 4,
    'node_delta': 2,
    'node_epsilon': 1
}

bonus_weights = {
    'node_alpha': 0.25,
    'node_gamma': 0.35,
    'node_delta': 0.15
}

# Unused distractor variables
baseline_offset = 12.5
historical_peaks = [3, 1, 4, 1, 5, 9, 2]
duplicate_tracker = set()
for val in historical_peaks:
    duplicate_tracker.add(val)

scaling_factor = 1.0  # unused in final logic

# Key statement
final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Target result: {final_score}")