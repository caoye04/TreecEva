def calculate_final_score(ranks, weights):
    # Simulate a ranking aggregation system with normalization and weighting
    normalized = {}
    temp_values = []
    total_weight = sum(weights)
    weight_map = {i: w / total_weight for i, w in enumerate(weights)}

    # Irrelevant scaling factor (distractor)
    scale_factor = 1.0
    adjusted_ranks = [max(10 - r, 0) for r in ranks]  # Misleading transformation

    # Real computation happens here using zip and dictionary lookup
    for idx, (rank, adj_rank) in enumerate(zip(ranks, adjusted_ranks)):
        norm_val = (11 - rank) / 10  # Normalize rank to 0-1 scale (higher is better)
        weighted_norm = norm_val * weight_map[idx]
        normalized[idx] = weighted_norm
        temp_values.append(adj_rank * 0.1)  # Dead computation path

    # Secondary distraction: unused smoothing
    smoothed = []
    for i in range(len(temp_values)):
        if i == 0:
            smoothed.append(temp_values[i])
        else:
            smoothed.append((temp_values[i] + temp_values[i-1]) / 2)

    # Final score is sum of normalized weighted scores
    aggregate = sum(normalized.values())
    penalty = 0
    for k, v in normalized.items():
        if v < 0.05:
            penalty += 0.01  # Minor penalty for low contributions

    final_result = aggregate - penalty
    return round(final_result, 4)

# Main execution
rankings = [3, 1, 4, 2, 5]
weights = [10, 25, 20, 30, 15]

# Dummy variables for distraction
baseline_scores = [75, 88, 92, 80, 70]
decay_factor = 0.95
rolling_avg = sum(baseline_scores) / len(baseline_scores)

# Key statement
final_score = calculate_final_score(rankings, weights)

print(f"Result: {final_score}")