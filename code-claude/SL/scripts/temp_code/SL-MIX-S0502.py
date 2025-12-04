def calculate_weighted_score(stats, weights):
    # Extract relevant statistics
    points = stats.get('points', 0)
    assists = stats.get('assists', 0)
    rebounds = stats.get('rebounds', 0)
    
    # Extract weights for calculation
    points_weight = weights.get('points', 1.0)
    assists_weight = weights.get('assists', 0.7)
    rebounds_weight = weights.get('rebounds', 0.5)
    
    # Calculate defensive impact (not used in final calculation)
    steals = stats.get('steals', 0)
    blocks = stats.get('blocks', 0)
    defensive_impact = steals * 1.2 + blocks * 1.5
    
    # Calculate shooting efficiency
    attempts = stats.get('field_goal_attempts', 0)
    made = stats.get('field_goals_made', 0)
    shooting_efficiency = made / attempts if attempts > 0 else 0
    
    # Calculate raw score
    raw_score = points * points_weight + assists * assists_weight + rebounds * rebounds_weight
    
    # Apply efficiency bonus
    efficiency_bonus = raw_score * shooting_efficiency * 0.2
    
    # Unnecessary calculations for games played analysis
    games_played = stats.get('games', 82)
    per_game_average = raw_score / games_played if games_played > 0 else 0
    career_projection = per_game_average * 820  # Projected over 10 seasons
    
    # Calculate final weighted score
    return raw_score + efficiency_bonus

# Player statistics dictionary
player_stats = {
    'name': 'Michael Jordan',
    'points': 32,
    'assists': 6,
    'rebounds': 8,
    'steals': 2.3,
    'blocks': 1.1,
    'field_goals_made': 12,
    'field_goal_attempts': 25,
    'games': 75
}

# Define importance weights
weights = {
    'points': 1.2,
    'assists': 0.8,
    'rebounds': 0.6
}

# Unnecessary scoring system variations
alt_weights = lambda pts, ast, reb: {'points': pts * 1.1, 'assists': ast * 0.9, 'rebounds': reb * 0.7}

# Calculate fantasy points (not used in final result)
fantasy_points = player_stats['points'] + (player_stats['assists'] * 1.5) + (player_stats['rebounds'] * 1.2)

# Calculate the player's final score
final_score = calculate_weighted_score(player_stats, weights)

# Output comparison dictionary (not affecting final result)
comparison = {'raw_stats': sum(player_stats[k] for k in ['points', 'assists', 'rebounds']),
              'weighted': final_score}

print(f"Result: {final_score}")