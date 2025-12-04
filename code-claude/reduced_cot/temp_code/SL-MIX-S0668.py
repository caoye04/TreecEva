import itertools

def calculate_game_score(player_stats, opponent_stats):
    # Calculate base score from player statistics
    base_score = player_stats['points'] * 2 - opponent_stats['points']
    
    # Apply bonus for consecutive wins
    streak_bonus = 0
    if player_stats['streak'] >= 3:
        streak_bonus = player_stats['streak'] * 5
    
    # Calculate efficiency ratio (not used in final calculation)
    efficiency = player_stats['points'] / (player_stats['attempts'] or 1)
    performance_index = efficiency * 100 if efficiency > 0.5 else efficiency * 50
    
    # Apply team bonuses based on player positions
    positions = {'forward', 'center', 'guard'}
    player_positions = set(player_stats['positions'])
    position_bonus = len(player_positions & positions) * 15
    
    # Calculate opponent difficulty modifier
    difficulty_tiers = {'easy': 0.8, 'medium': 1.0, 'hard': 1.2, 'expert': 1.5}
    difficulty = difficulty_tiers.get(opponent_stats['tier'], 1.0)
    
    # Generate potential multipliers (only one will be used)
    potential_multipliers = list(itertools.product([0.9, 1.0, 1.1], [1, 2, 3]))
    selected_multiplier = potential_multipliers[player_stats['rank'] % len(potential_multipliers)]
    multiplier = selected_multiplier[0] * (selected_multiplier[1] // 2)
    
    # Calculate defensive adjustment (not used in final calculation)
    defense_adjustment = opponent_stats['defense'] & player_stats['defense']
    
    # Apply final calculation with bit manipulation for special bonus
    special_bonus = (player_stats['special'] | 4) ^ 2 if player_stats['special'] > 0 else 0
    
    # Calculate final score using relevant components
    raw_score = base_score + streak_bonus + position_bonus + special_bonus
    adjusted_score = int(raw_score * difficulty * multiplier)
    
    return adjusted_score

# Player and opponent statistics
player_stats = {
    'points': 28,
    'attempts': 20,
    'streak': 4,
    'positions': ['forward', 'guard'],
    'rank': 7,
    'defense': 13,
    'special': 3
}

opponent_stats = {
    'points': 22,
    'tier': 'hard',
    'defense': 9
}

# Calculate the game score
final_score = calculate_game_score(player_stats, opponent_stats)
print(f"Result: {final_score}")