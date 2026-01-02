def calculate_final_score(ranks, coeffs):
    normalized = []
    total_weight = sum(coeffs)
    temp_vals = [0] * len(ranks)
    
    # Irrelevant pre-processing (distractor)
    offset = min(ranks) if ranks else 0
    adjusted_ranks = [r - offset + 1 for r in ranks]
    
    # Actual computation begins
    for i, (rank, weight) in enumerate(zip(adjusted_ranks, coeffs)):
        inv_rank = 1 / rank
        weighted_inv = inv_rank * weight
        temp_vals[i] = weighted_inv
    
    # Additional distraction: unused intermediate calculation
    avg_rank = sum(adjusted_ranks) / len(adjusted_ranks) if adjusted_ranks else 0
    penalty = 0
    for r in adjusted_ranks:
        if r > avg_rank * 1.5:
            penalty += 0.1  # Minor red herring

    # Core logic: sum of weighted inverse ranks
    raw_score = sum(temp_vals)
    normalized_score = raw_score / total_weight
    
    # Secondary adjustment based on ranking spread (actual relevant step)
    rank_range = max(adjusted_ranks) - min(adjusted_ranks)
    if rank_range > 5:
        normalized_score *= 0.9
    
    return round(normalized_score * 100, 2)

# Main execution
rankings = [3, 1, 4, 1, 5, 9, 2]
weights = [1, 2, 1, 2, 1, 2, 1]

# Dummy data for distraction
aux_data = [(i, x*2) for i, x in enumerate(rankings)]
duplicate_check = {x: rankings.count(x) for x in set(rankings)}

# Unused helper function (dead code path)
def validate_input(data):
    return all(isinstance(x, int) and x > 0 for x in data)

# Key statement
final_score = calculate_final_score(rankings, weights)

print(f"Result: {final_score}")