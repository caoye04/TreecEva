import itertools
from collections import defaultdict

def calculate_player_score(player_data, modifiers):
    # Track player performance metrics
    base_points = sum(player_data['achievements'])
    penalty_points = player_data.get('penalties', 0) * 5
    
    # Process bonus multipliers (unused calculation path)
    bonus_factors = [1.5, 2.0, 0.75]
    potential_bonus = max(bonus_factors) * min(player_data['achievements'])
    
    # Calculate team synergy (distractor)
    team_synergy = defaultdict(int)
    for player_id, teammate_id in itertools.combinations(range(1, 6), 2):
        synergy_score = (player_id * teammate_id) % 7
        team_synergy[player_id] += synergy_score
    
    # Apply special modifiers
    active_modifier_value = 0
    for modifier_name, modifier_value in modifiers.items():
        if modifier_name.startswith('power'):
            # Power modifiers apply to base points
            active_modifier_value += modifier_value
        elif modifier_name.startswith('team'):
            # Team modifiers are tracked but not used in final calculation
            team_factor = modifier_value * 2
    
    # Process achievement strings for hidden bonuses
    achievement_names = player_data.get('achievement_names', [])
    name_bonus = 0
    for name in achievement_names:
        if 'legend' in name.lower():
            name_bonus += 15
        elif 'master' in name.lower():
            name_bonus += 10
        # This condition is never met in our data
        elif 'impossible' in name.lower():
            name_bonus += 50
    
    # Calculate experience multiplier
    experience_years = player_data['experience']
    exp_multiplier = 1.0
    if experience_years > 5:
        exp_multiplier = 1.2
    elif experience_years > 3:
        exp_multiplier = 1.1
    
    # Apply score modifiers based on player level
    level_bonus = 0
    player_level = player_data['level']
    if player_level >= 10:
        level_chars = str(player_level)
        # Sum of digits in player level
        level_bonus = sum(int(digit) for digit in level_chars)
    
    # Calculate final score
    raw_score = (base_points - penalty_points + name_bonus) * exp_multiplier
    adjusted_score = raw_score + level_bonus + active_modifier_value
    
    # Apply position-specific adjustments (distractor)
    position = player_data.get('position', 'unknown')
    position_modifiers = {'striker': 1.1, 'defender': 0.9, 'midfielder': 1.0}
    position_factor = position_modifiers.get(position, 1.0)
    
    # Return integer score
    return int(adjusted_score)

# Player data
player_data = {
    'id': 42,
    'name': 'Alex Johnson',
    'achievements': [25, 30, 15, 20],
    'penalties': 2,
    'experience': 4,
    'level': 12,
    'position': 'midfielder',
    'achievement_names': ['Season Master', 'Goal Legend', 'Team Player']
}

# Available modifiers
all_modifiers = {
    'power_up': 25,
    'power_down': -10,
    'team_synergy': 3,
    'special_event': 5,
    'seasonal_bonus': 7
}

# Select active modifiers
active_modifiers = {k: v for k, v in all_modifiers.items() if k.startswith('power')}

# Calculate intermediary values (distractors)
team_metrics = {'synergy': 0.85, 'coordination': 0.92, 'morale': 0.78}
season_stats = [89, 92, 76, 85, 91]
sliced_stats = season_stats[1:4]  # Slice operation
recent_performance = sum(sliced_stats) / len(sliced_stats)

# Calculate player's final score
final_score = calculate_player_score(player_data, active_modifiers)
print(f"Result: {final_score}")