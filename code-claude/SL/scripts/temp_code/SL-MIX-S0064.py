def calculate_game_statistics(player_data):
    # Extract player scores from raw data
    raw_scores = [int(score.strip()) for score in player_data.split(',')]
    
    # Track bonus multipliers (not used in final calculation)
    bonus_multipliers = [1.5 if score > 85 else 1.0 for score in raw_scores]
    
    # Filter invalid scores (negative or above 100)
    valid_scores = []
    invalid_count = 0
    
    for score in raw_scores:
        if 0 <= score <= 100:
            valid_scores.append(score)
        else:
            invalid_count += 1
    
    # Calculate average (not used in final result)
    average_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0
    
    # Apply threshold filtering (relevant for final calculation)
    threshold = 30
    valid_scores = [s for s in valid_scores if s >= threshold]
    
    # Calculate potential team bonus (not used)
    team_bonus = 50 if len(valid_scores) >= 5 and average_score > 70 else 0
    
    # Final calculation
    total_points = sum(valid_scores)
    
    # Check if we need score normalization (we don't)
    if invalid_count > 3 and average_score < 50:
        normalization_factor = 1.2
    else:
        normalization_factor = 1.0
    
    print(f"Result: {total_points}")
    return total_points

# Sample player data
player_data = "75, 92, 86, -5, 65, 110, 42, 10, 29, 44"
result = calculate_game_statistics(player_data)