def calculate_final_score(ranks, coeffs):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    
    # Irrelevant pre-processing: normalization (not used later)
    normalized_ranks = [r / sum(ranks) for r in ranks]
    temp_sum = sum(normalized_ranks)
    dummy_var = temp_sum * 0.01  # Distractor computation
    
    for idx, (rank_val, weight) in enumerate(zip(ranks, coeffs)):
        if rank_val <= 3:
            contribution = (4 - rank_val) * weight
            base_score += contribution
            
            # Bonus logic with side tracking (partially relevant)
            if weight > 1.5:
                bonus_tracker.append(contribution * 0.1)
        else:
            penalty_adjustment += 1  # Minor penalty accumulator
    
    # Secondary loop with enumerate over zipped data
    shift_offset = 0
    for i, (a, b) in enumerate(zip(coeffs, [2, 1, 3, 0, 2])):
        if i % 2 == 0:
            shift_offset += a - b
    
    # Real scoring adjustment
    final_score = base_score - penalty_adjustment + shift_offset
    
    # Dead code path (never executed due to fixed input)
    if len(bonus_tracker) > 10:
        final_score *= 1.1
    
    # Unused variables to increase cognitive load
    max_rank = max(ranks)
    avg_weight = sum(coeffs) / len(coeffs)
    
    return final_score

# Input data
rankings = [1, 4, 2, 5, 3]
weights = [2.0, 0.5, 3.0, 1.0, 2.5]

# Key execution point
final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")