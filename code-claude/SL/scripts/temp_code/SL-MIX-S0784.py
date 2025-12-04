def calculate_engagement_metric(views, likes, comments):
    # Calculate user engagement score based on platform metrics
    engagement_base = views * 0.01 + likes * 0.5 + comments * 2
    return min(100, engagement_base)

def apply_bitwise_bonus(score, achievements):
    # Apply bonuses based on achievement bit flags
    bonus_multiplier = 1.0
    if achievements & 0x1:  # First achievement
        bonus_multiplier += 0.05
    if achievements & 0x2:  # Second achievement
        bonus_multiplier += 0.08
    if achievements & 0x4:  # Third achievement
        bonus_multiplier += 0.12
    if achievements & 0x8:  # Fourth achievement
        bonus_multiplier += 0.15
    return score * bonus_multiplier

def normalize_ratings(ratings):
    # Normalize a list of ratings to sum to 100
    total = sum(ratings)
    if total == 0:
        return [0] * len(ratings)
    return [round((r / total) * 100, 2) for r in ratings]

def calculate_player_rating(stats):
    # Extract player statistics
    games_played = stats.get('games', 0)
    wins = stats.get('wins', 0)
    losses = stats.get('losses', 0)
    achievements = stats.get('achievements', 0)
    
    # Calculate base metrics
    potential_metrics = {
        'accuracy': stats.get('accuracy', 0) * 2.5,
        'speed': stats.get('speed', 0) * 1.8,
        'strategy': stats.get('strategy', 0) * 3.2
    }
    
    # Track unused metrics for future features
    unused_metrics = {
        'stamina': stats.get('stamina', 0) * 1.3,
        'teamwork': stats.get('teamwork', 0) * 2.7
    }
    
    # Calculate win rate
    total_games = wins + losses
    win_rate = (wins / total_games) * 100 if total_games > 0 else 0
    
    # Apply difficulty adjustment (higher difficulties earn more points)
    difficulty_levels = {'easy': 0.8, 'medium': 1.0, 'hard': 1.2, 'expert': 1.5}
    difficulty = stats.get('difficulty', 'medium')
    difficulty_multiplier = difficulty_levels.get(difficulty, 1.0)
    
    # Calculate engagement score (not used in final calculation)
    engagement = calculate_engagement_metric(
        stats.get('profile_views', 0),
        stats.get('likes', 0),
        stats.get('comments', 0)
    )
    
    # Process achievements
    achievement_names = [
        'first_win', 'ten_wins', 'perfect_game', 'no_losses'
    ]
    achievement_counts = sum(1 for i, name in enumerate(achievement_names) 
                           if achievements & (1 << i))
    
    # Calculate preliminary score
    skill_score = sum(potential_metrics.values()) / len(potential_metrics)
    preliminary_score = (skill_score * 0.6) + (win_rate * 0.4)
    
    # This normalization step is actually not used
    normalized_scores = normalize_ratings([preliminary_score, engagement, achievement_counts * 10])
    
    # Apply difficulty multiplier
    adjusted_score = preliminary_score * difficulty_multiplier
    
    # Apply achievement bonuses
    final_score = apply_bitwise_bonus(adjusted_score, achievements)
    
    # Cap at 100 points
    return min(100, final_score)

# Player statistics
player_stats = {
    'games': 50,
    'wins': 35,
    'losses': 15,
    'accuracy': 8.2,  # Out of 10
    'speed': 7.5,     # Out of 10
    'strategy': 6.8,  # Out of 10
    'stamina': 9.1,   # Out of 10 (not used)
    'teamwork': 6.5,  # Out of 10 (not used)
    'difficulty': 'hard',
    'profile_views': 1240,
    'likes': 85,
    'comments': 17,
    'achievements': 0x7  # Binary: 0111 (first three achievements)
}

# Calculate player rating
final_score = calculate_player_rating(player_stats)
print(f"Result: {final_score}")