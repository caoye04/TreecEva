def calculate_game_score():
    player_name = "ALICE_THE_GAMER"
    base_score = 42
    
    # Distractor string operations
    formatted_name = player_name.lower().replace('_', ' ').title()
    name_length = len(formatted_name)
    
    # Actual scoring logic
    level_bonus = 15
    time_penalty = 7
    
    # Distractor calculations
    bonus_check = name_length * 2
    temp_adjustment = (bonus_check + 10) // 3
    
    # Core scoring
    raw_score = base_score + level_bonus
    final_score = raw_score - time_penalty
    
    # Final assignment
    result = final_score
    print(f"Target result: {result}")

calculate_game_score()