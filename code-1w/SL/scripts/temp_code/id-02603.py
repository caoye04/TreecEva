def calculate_player_score(levels, base_score):
    total_score = base_score
    bonuses = [5, -2, 8, 0, 3]
    penalties = {2: 4, 4: 1}
    level_multiplier = 1
    
    for index, (level, completed) in enumerate(zip(levels, [True, False, True, True, False])):
        if completed:
            adjustment = bonuses[index]
            if index in penalties:
                adjustment -= penalties[index]
            total_score += adjustment * level_multiplier
            level_multiplier += 1
    
    Result: total_score