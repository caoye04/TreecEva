def calculate_game_points(stats, difficulty):
    base_points = 0
    bonus_multiplier = 1.0
    penalty_points = 0
    achievement_bonus = 0
    
    # Process player statistics to calculate base points
    for stat_name, value in stats.items():
        if stat_name == 'enemies_defeated':
            # Each enemy defeated is worth 5 points
            base_points += value * 5
        elif stat_name == 'treasures_collected':
            # Each treasure is worth 10 points
            base_points += value * 10
        elif stat_name == 'time_played':
            # Time played affects the bonus multiplier (irrelevant calculation)
            bonus_multiplier = min(2.0, value / 100)
        elif stat_name == 'health_remaining':
            # Health remaining affects achievement bonus (misleading)
            if value > 80:
                achievement_bonus += 50
            elif value > 50:
                achievement_bonus += 25
        elif stat_name == 'levels_completed':
            # This is the key stat that matters
            base_points += value * 15
    
    # Apply difficulty multiplier - only even difficulties get a real bonus
    if difficulty % 2 == 0:
        difficulty_bonus = difficulty * 10
    else:
        # Odd difficulties get a different calculation (distraction)
        difficulty_bonus = difficulty * 5
    
    # Calculate penalties based on imaginary conditions
    for threshold in [100, 200, 300, 400]:
        if base_points > threshold:
            penalty_points += 10
    
    # Process special bonuses based on specific combinations
    special_combo = False
    if 'enemies_defeated' in stats and 'treasures_collected' in stats:
        if stats['enemies_defeated'] > 10 and stats['treasures_collected'] > 5:
            special_combo = True
    
    # Secret level bonus (misleading - never used)
    secret_level_bonus = 0
    if 'secret_levels' in stats:
        for level in range(1, stats['secret_levels'] + 1):
            secret_level_bonus += level * 25
    
    # Apply the actual score calculation
    raw_score = base_points + difficulty_bonus
    
    # Misleading calculations that don't affect final result
    adjusted_score = raw_score * bonus_multiplier
    potential_score = adjusted_score - penalty_points + achievement_bonus
    
    # The real calculation that matters
    if 'levels_completed' in stats and stats['levels_completed'] >= 3:
        # The key calculation that determines the final score
        return int(raw_score / 2) + stats['levels_completed'] * difficulty
    else:
        # This branch is never taken with our input
        return int(potential_score * 0.8)

# Player statistics dictionary
player_stats = {
    'enemies_defeated': 15,
    'treasures_collected': 7,
    'time_played': 120,
    'health_remaining': 75,
    'levels_completed': 4,
    'power_ups': 3,  # Irrelevant stat
    'deaths': 2      # Irrelevant stat
}

# Various difficulty levels to confuse
diff_easy = 1
diff_normal = 2
diff_hard = 3
diff_expert = 5

# Misleading calculations with these difficulties
test_easy = calculate_game_points(player_stats, diff_easy)
test_normal = calculate_game_points(player_stats, diff_normal)

# The actual difficulty we care about
difficulty_multiplier = diff_hard

# More misleading variables
potential_final = test_normal * 1.5
adjusted_final = test_easy + 50

# This is the key calculation we're asking about
final_score = calculate_game_points(player_stats, difficulty_multiplier)

# Misleading post-calculation that doesn't affect our answer
if final_score > 100:
    final_score_with_bonus = final_score + 25
else:
    final_score_with_bonus = final_score + 10
    
print(f"Result: {final_score}")