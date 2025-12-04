def calculate_bonus(achievements, level):
    bonus_points = sum(len(a) for a in achievements)
    level_multiplier = level * 0.5
    return int(bonus_points * level_multiplier)

def calculate_final_score(stats, history):
    # Base score calculation
    base_score = stats['kills'] * 10 - stats['deaths'] * 5
    
    # Weapon usage analysis (not directly affecting score)
    weapon_usage = {}
    for weapon in history['weapons_used']:
        weapon_usage[weapon] = weapon_usage.get(weapon, 0) + 1
    
    # Most used weapon gives small bonus
    if weapon_usage:
        most_used = max(weapon_usage.items(), key=lambda x: x[1])[0]
        weapon_bonus = len(most_used) # Just a small bonus based on weapon name length
    else:
        weapon_bonus = 0
    
    # Team contribution factor
    team_factor = 1.0
    if stats['team_assists'] > 10:
        team_factor = 1.2
    elif stats['team_assists'] > 5:
        team_factor = 1.1
    
    # Calculate streaks (this is tracked but not used in final calculation)
    max_streak = 0
    current_streak = 0
    for event in history['events']:
        if event == 'kill':
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        elif event == 'death':
            current_streak = 0
    
    # Bonus from achievements
    achievement_bonus = calculate_bonus(stats['achievements'], stats['level'])
    
    # Special event points that don't affect the total
    special_points = history['special_events'] * 25
    
    # Calculate final score
    adjusted_score = (base_score + weapon_bonus) * team_factor
    final_score = adjusted_score + achievement_bonus
    
    return int(final_score)

# Player statistics
player_stats = {
    'kills': 24,
    'deaths': 8,
    'team_assists': 7,
    'level': 4,
    'achievements': ['FirstBlood', 'DoubleKill', 'Survivor']
}

# Game history data
game_history = {
    'weapons_used': ['Rifle', 'Pistol', 'Rifle', 'Sniper', 'Rifle', 'Knife'],
    'events': ['kill', 'kill', 'death', 'kill', 'kill', 'death', 'kill'],
    'special_events': 3
}

# Calculate the player's final score
total_score = calculate_final_score(player_stats, game_history)
print(f"Result: {total_score}")