def calculate_final_score(ranks, coeffs):
    # Initialize variables
    base_points = 0
    bonus_adjustment = 0
    penalty_tracker = []
    intermediate_values = []
    
    # Misleading pre-computation (not used in final logic)
    for i, rank in enumerate(ranks):
        if rank < 5:
            bonus_adjustment += i * 0.1  # Distractor: never applied

    # Actual scoring logic with zip and enumerate
    for idx, (rank, weight) in enumerate(zip(ranks, coeffs)):
        contribution = (10 - rank) * weight
        intermediate_values.append(contribution)
        
        # Apply conditional scaling based on position
        if idx % 2 == 0:
            contribution *= 1.1
        else:
            contribution *= 0.95
            
        base_points += contribution
    
    # Secondary adjustment using min/max pattern
    max_intermediate = max(intermediate_values)
    min_intermediate = min(intermediate_values)
    stability_bonus = (max_intermediate - min_intermediate) / 2
    
    # Dead code branch (never executed due to data)
    if len(penalty_tracker) > 100:
        base_points -= sum(penalty_tracker)
    
    # Final computation
    final_score = int(base_points + stability_bonus)
    return final_score

# Input data
rankings = [3, 7, 2, 9, 4]
weights = [1.2, 0.8, 1.5, 0.6, 1.1]

# Execute calculation
final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")