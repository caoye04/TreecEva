def calculate_final_score(ranks, coeffs):
    base_score = 0
    bonus_offset = 0
    temp_sum = 0
    
    # Distractor: Initialize irrelevant tracking variables
    max_rank_seen = -1
    rank_count = len(ranks)
    cumulative_product = 1
    
    for i, (rank, weight) in enumerate(zip(ranks, coeffs)):
        # Relevant scoring logic
        base_score += (10 - rank) * weight
        
        # Distractor: Irrelevant computations
        if rank > 5:
            bonus_offset += 2
        else:
            bonus_offset -= 1
        
        temp_sum += rank
        cumulative_product *= (rank % 3 + 1)  # Unused later
        
        # Semi-relevant adjustment
        if i % 2 == 0:
            base_score -= 1

    # More distractors: unused intermediate calculations
    average_rank = temp_sum / rank_count if rank_count else 0
    penalty_factor = 0
    for idx in range(len(ranks)):
        if ranks[idx] < 3 and coeffs[idx] > 2:
            penalty_factor += 0.5  # Never actually applied

    # Final score with only partial use of above work
    final_raw = base_score + bonus_offset
    
    # Key statement
    final_score = int(final_raw // 1)  # Integer division, no change
    
    print(f"Target result: {final_score}")
    return final_score

# Input data
player_ranks = [1, 4, 2, 6, 3]
importance_weights = [3, 2, 4, 1, 3]

# Execution point
final_score = calculate_final_score(player_ranks, importance_weights)