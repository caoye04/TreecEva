def calculate_final_score(ranks, multiplier):
    base_points = 0
    penalty = 0
    temp_adjustment = 0
    
    # Accumulate points based on rank positions
    for i, rank in enumerate(ranks):
        if rank <= 3:
            base_points += 10
        elif rank <= 6:
            base_points += 5
        else:
            base_points += 1
            
        # Irrelevant temperature-like adjustment (distractor)
        temp_adjustment += (i + 1) * 0.1

    # Simulate conditional logic with red herring computation
    scaling_factor = 1.5 if len(ranks) > 5 else 1.2
    unused_metric = sum(ranks) / len(ranks)  # Dead computation
    
    # Apply multiplier only if top performer exists
    has_top_performer = any(rank == 1 for rank in ranks)
    effective_multiplier = multiplier if has_top_performer else 1.0
    
    # Bonus accumulation with distractor condition
    extra_bonus = 0
    for point in range(base_points):
        if point % 7 == 0 and point > 0:
            extra_bonus += 2
    
    # Final score calculation — key line
    final_score = base_points * effective_multiplier + extra_bonus
    
    # Unused noise variables
    debug_trace = [base_points, effective_multiplier, extra_bonus]
    validation_checksum = hash(tuple(debug_trace)) % 1000
    
    return final_score

# Main execution
rank_data = [1, 4, 7, 2, 8, 3, 5]
bonus_multiplier = 1.8
tolerance_threshold = 0.001  # Unused parameter
reference_baseline = [x * 2 for x in rank_data]  # Distractor list comprehension

final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")