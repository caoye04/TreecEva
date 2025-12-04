def calculate_final_score(scores, penalties):
    base_score = sum(scores)
    penalty_points = sum(penalties.values())
    
    # Apply score multiplier based on highest score
    max_score = max(scores) if scores else 0
    multiplier = 1.5 if max_score > 100 else 1.0
    
    # Calculate bonus points (not used in final calculation)
    bonus_factors = [0.1, 0.2, 0.3]
    bonus_points = sum(s * f for s, f in zip(scores, bonus_factors)) if len(scores) > 0 else 0
    
    # Track intermediate results (not used in final calculation)
    intermediate_results = {
        "raw_score": base_score,
        "bonus": bonus_points,
        "penalties": penalty_points
    }
    
    # Calculate adjusted score with conditional expression
    adjusted_score = base_score * multiplier - penalty_points
    return adjusted_score if adjusted_score > 0 else 0

# Game data
game_scores = [75, 120, 45]
penalties = {"time": 15, "fouls": 30, "warnings": 5}

# Calculate potential alternative scores (not used in final calculation)
alt_calculation = sum(s for s in game_scores if s > 50)
bonus_threshold = 200
time_bonus = 25 if sum(game_scores) > bonus_threshold else 0

# Final calculation
total_points = calculate_final_score(game_scores, penalties)

# Display results
print(f"Alternative points: {alt_calculation}")
print(f"Time bonus: {time_bonus}")
print(f"Result: {total_points}")