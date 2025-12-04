def calculate_game_score():
    player_levels = [3, 5, 2, 7, 4]
    bonus_multipliers = [2, 1, 3, 1, 2]
    
    # Calculate base scores with enumerate
    enumerated_levels = []
    for idx, level in enumerate(player_levels):
        enumerated_levels.append(idx * level)
    
    # Apply bonus multipliers with zip
    enhanced_scores = []
    for base, multiplier in zip(enumerated_levels, bonus_multipliers):
        enhanced_scores.append(base * multiplier)
    
    # Calculate final score
    enumerate_data = enhanced_scores[1:4]  # Take middle three elements
    final_score = sum(enumerate_data)
    
    print(f"Target result: {final_score}")

calculate_game_score()