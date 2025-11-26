def calculate_player_stats(performance_data):
    raw_scores = [85, 92, 78, 96, 88]
    weight_multipliers = [1.1, 0.9, 1.2, 1.0, 1.05]
    
    # Calculate weighted scores (distractor - not used in final answer)
    weighted_scores = [score * weight for score, weight in zip(raw_scores, weight_multipliers)]
    
    # Filter high performance games and apply adjustments
    high_performance_games = [score for score in raw_scores if score > 80]
    adjustment_factor = 2.5
    adjusted_scores = [score + adjustment_factor for score in high_performance_games]
    
    # Bonus calculation (partially relevant)
    bonus_base = len(adjusted_scores) * 3
    bonus_correction = bonus_base // 2
    
    # Final score calculation
    temp_calc = sum(weighted_scores)  # Distractor calculation
    final_score = adjusted_scores[-1] + bonus_correction
    
    print(f"Target result: {final_score}")
    return final_score

# Execute the function
result = calculate_player_stats([85, 92, 78, 96, 88])