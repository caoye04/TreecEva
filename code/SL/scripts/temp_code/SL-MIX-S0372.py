def compute_final_score(participants):
    # Initialize base scores and temporary calculations
    base_points = [25, 40, 35, 30]
    adjustment_factor = 1.5
    preliminary_sum = sum(base_points) * adjustment_factor
    
    # Process participant data with list comprehension
    valid_scores = [score for score in participants if score >= 60]
    invalid_count = len(participants) - len(valid_scores)
    
    # Calculate bonus points (distractor - not used in final calculation)
    bonus_calc = (invalid_count * 5) + adjustment_factor
    
    # Compute weighted average of valid scores
    if valid_scores:
        weighted_avg = sum(score * 0.8 for score in valid_scores) / len(valid_scores)
        # Apply modular arithmetic for final calculation
        final_score = int(weighted_avg) % 100
    else:
        final_score = preliminary_sum % 50  # This branch won't be taken
    
    # Intermediate step that doesn't affect final result
    unused_calc = bonus_calc + preliminary_sum
    
    return final_score

# Participant data with mixed valid and invalid scores
participants_data = [72, 58, 85, 91, 45, 78, 62, 95]

# Execute the main computation
final_score = compute_final_score(participants_data)
print(f"Target result: {final_score}")