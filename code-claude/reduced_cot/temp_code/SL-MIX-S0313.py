import itertools

def calculate_player_score(stats, bonus):
    # Base points from player statistics
    base_points = stats['hits'] * 1.0 + stats['runs'] * 1.5 + stats['home_runs'] * 4.0
    
    # Defensive points calculation (not used in final calculation)
    defensive_rating = stats['fielding'] * 0.8 + stats['assists'] * 0.5
    
    # Experience factor affects multiplier
    experience_factor = min(stats['years'], 10) / 10.0
    
    # Calculate consistency bonus (not directly used)
    consistency = stats['games_played'] / 162.0 if stats['games_played'] > 0 else 0
    
    # Apply team performance modifier
    team_modifier = bonus['team_performance'] if stats['team_wins'] > 80 else 1.0
    
    # Calculate streak multiplier
    streak_bonus = 1.0
    if stats['current_streak'] > 0:
        streak_bonus = 1.0 + (stats['current_streak'] * 0.01)
    elif stats['current_streak'] < 0:
        # Negative streaks reduce score slightly
        streak_bonus = 1.0 / (1.0 - stats['current_streak'] * 0.005)
    
    # Position-specific bonus (catcher and pitcher get extra points)
    position_bonus = 1.2 if stats['position'] in ['catcher', 'pitcher'] else 1.0
    
    # League adjustment factor (not used in final calculation)
    league_factor = 1.1 if stats['league'] == 'major' else 1.0
    
    # Calculate injury risk (not directly used)
    injury_risk = 0.05 * stats['previous_injuries']
    
    # Apply all relevant multipliers
    multiplier = team_modifier * streak_bonus * position_bonus * (1.0 + experience_factor)
    
    # Calculate the weighted performance score
    performance_score = base_points * multiplier
    
    # Apply seasonal adjustment
    seasonal_games = [g for g in range(stats['games_played']) if g % 20 == 0]
    seasonal_factor = len(seasonal_games) / 10.0 if seasonal_games else 0.1
    
    # Final score calculation (rounded to 2 decimal places)
    return round(performance_score * seasonal_factor, 2)

# Player statistics
player_stats = {
    'hits': 156,
    'runs': 89,
    'home_runs': 32,
    'fielding': 0.985,
    'assists': 45,
    'years': 7,
    'games_played': 152,
    'team_wins': 92,
    'current_streak': 5,
    'position': 'catcher',
    'league': 'major',
    'previous_injuries': 2
}

# Performance bonus factors
bonus_factors = {
    'team_performance': 1.15,
    'fan_popularity': 1.2,  # Not used in calculation
    'media_coverage': 0.95  # Not used in calculation
}

# Calculate the player's final score
final_score = calculate_player_score(player_stats, bonus_factors)
print(f"Target result: {final_score}")