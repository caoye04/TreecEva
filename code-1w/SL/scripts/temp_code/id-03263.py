def calculate_final_score(ranks, coeffs):
    base_scores = [1 / (rank + 1) for rank in ranks]
    weighted_scores = [score * coeff for score, coeff in zip(base_scores, coeffs)]
    adjustment_factor = sum(weighted_scores) / len(weighted_scores)
    
    # Distractor: Irrelevant computation on derived stats
    temp_stats = [x ** 2 for x in weighted_scores if x > 0.5]
    avg_temp = sum(temp_stats) / len(temp_stats) if temp_stats else 0.0
    decay_correction = avg_temp * 0.1  # Unused correction term
    
    # Real logic continues
    raw_total = sum(weighted_scores)
    penalty = 0
    for i, rank in enumerate(ranks):
        if rank == 0:
            penalty += coeffs[i] * 0.2
    
    # Secondary distractor: complex but unused formula
    hypothetical_max = sum([coeffs[i] for i in range(len(coeffs)) if ranks[i] == 0])
    efficiency_ratio = hypothetical_max / (raw_total + 1e-9) if hypothetical_max > 0 else 0
    
    # Final calculation
    final_normalized = raw_total - penalty
    return round(final_normalized, 4)

# Main execution
contestant_ranks = [2, 0, 1, 3, 0]
importance_weights = [0.8, 1.2, 1.0, 0.5, 1.5]

# Intermediate distractor variables
rank_data = contestant_ranks.copy()
weights = importance_weights[:]
duplicate_check = {r: contestant_ranks.count(r) for r in set(contestant_ranks)}
relevance_map = {i: w for i, w in enumerate(importance_weights) if w >= 1.0}

# Key computational step
final_score = calculate_final_score(rank_data, weights)

# Output result
print(f"Target result: {final_score}")