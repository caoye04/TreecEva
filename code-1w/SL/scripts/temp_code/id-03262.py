def calculate_final_score(ranks, coeffs):
    base_score = 0
    penalty_adjustment = 0
    temp_multiplier = 1.0
    
    # Irrelevant normalization (distractor)
    total_rank = sum(ranks)
    normalized_ranks = [r / total_rank for r in ranks]
    
    # Real computation begins
    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        if rank <= 3:
            base_score += 10 * weight
        else:
            base_score += max(0, 5 - rank) * weight
        
        # Distractor: unused conditional logic
        if i % 2 == 0:
            temp_multiplier *= 1.05

    # Additional distraction: dead code path
    overflow_flag = False
    if base_score > 1000:
        overflow_flag = True
        correction_factor = 0.9
    
    # Another red herring: irrelevant sorting
    sorted_weights = sorted(coeffs, reverse=True)
    weighted_sum = sum(w ** 2 for w in sorted_weights)
    
    # Actual penalty logic (semi-relevant)
    for idx, r in enumerate(ranks):
        if r == 1:
            penalty_adjustment -= 5
        elif r > 10:
            penalty_adjustment -= 2

    # Final score depends only on base_score and penalty_adjustment
    final_result = base_score + penalty_adjustment
    
    # Key assignment
    final_score = int(final_result)
    return final_score

# Input data
contestant_ranks = [1, 4, 2, 7, 3, 12]
importance_weights = [1.2, 0.8, 1.5, 0.6, 1.0, 0.4]

# Execution point
final_score = calculate_final_score(contestant_ranks, importance_weights)
print(f"Target result: {final_score}")