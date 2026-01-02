def calculate_final_score():
    # Student quiz scores (out of 10)
    scores = [7, 9, 8, 10, 6]
    
    # Calculate average score
    avg_score = sum(scores) / len(scores)
    
    # Bonus points for perfect scores
    perfect_count = scores.count(10)
    bonus_points = perfect_count * 1.5
    
    # Apply modular arithmetic to cap bonus at 3 points
    capped_bonus = bonus_points % 4
    
    # Use set operations to find unique scores
    unique_scores = set(scores)
    diversity_penalty = 0.5 if len(unique_scores) < 3 else 0
    
    # Final score calculation
    final_score = avg_score + capped_bonus - diversity_penalty
    
    return final_score

# Execute function and print result
target_result = calculate_final_score()
print(f"Result: {target_result}")