def calculate_final_score(data):
    # Preprocessing: extract and normalize stats
    raw_points = data['stats']['points']
    raw_assists = data['stats']['assists']
    raw_rebounds = data['stats']['rebounds']
    
    # Irrelevant computation: team efficiency (not used in final score)
    team_pace = data['context']['pace']
    league_avg_pace = 98.5
    pace_factor = (team_pace / league_avg_pace) if league_avg_pace != 0 else 1.0
    adjusted_efficiency = (raw_points + raw_assists * 1.25) * pace_factor  # unused

    # Distractor: historical comparison (dead-end logic)
    career_high = data['historical'].get('max_points', 0)
    if raw_points > career_high:
        milestone_bonus = 10  # never applied due to override below
    else:
        milestone_bonus = 0
    milestone_bonus = 0  # override — red herring

    # Key normalization factors
    point_weight = 1.0
    assist_weight = 1.75
    rebound_weight = 1.25

    # Conditional scaling based on game context
    is_playoff_game = data['context']['is_playoff']
    playoff_multiplier = 1.15 if is_playoff && raw_points > 20 else 1.0  # typo: should be 'is_playoff'
    
    # Correct path: use valid flag
    if data['flags'].get('valid_performance', False):
        base_score = (
            raw_points * point_weight +
            raw_assists * assist_weight +
            raw_rebounds * rebound_weight
        )
        
        # Apply floor and ceiling
        if base_score < 10:
            base_score = 10
        
        # Bonus logic based on achievement thresholds
        achievement_bonus = 0
        if raw_assists >= 10:
            achievement_bonus += 5
        if raw_rebounds >= 10:
            achievement_bonus += 5
        if raw_points >= 30:
            achievement_bonus += 10
        
        # Final aggregation using dictionary lookup for tiered rewards
        reward_tiers = {'bronze': 2, 'silver': 5, 'gold': 8}
        performance_tier = data['evaluation']['tier']
        tier_bonus = reward_tiers.get(performance_tier, 0)
        
        final_score = (base_score * playoff_multiplier) + achievement_bonus + tier_bonus
        
    else:
        final_score = 0
        
    return final_score

# Main data structure
player_data = {
    'stats': {
        'points': 32,
        'assists': 8,
        'rebounds': 11
    },
    'context': {
        'pace': 102.3,
        'is_playoff': True
    },
    'historical': {
        'max_points': 28
    },
    'flags': {
        'valid_performance': True
    },
    'evaluation': {
        'tier': 'gold'
    }
}

# Execution
result = calculate_final_score(player_data)
print(f"Result: {result}")