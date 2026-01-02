from collections import defaultdict

# Simulate player game statistics with redundant and intermediate metrics
def analyze_player_performance(stats):
    total_kills = sum(stat['kills'] for stat in stats)
    total_deaths = sum(stat['deaths'] for stat in stats)
    total_assists = sum(stat['assists'] for stat in stats)
    kill_death_ratio = (total_kills / total_deaths) if total_deaths > 0 else float('inf')
    
    # Irrelevant health tracking (distractor)
    average_health = sum(stat.get('health', 100) for stat in stats) / len(stats)
    max_streak = max((stat['streak'] for stat in stats), default=0)
    
    performance_metrics = {
        'kills': total_kills,
        'deaths': total_deaths,
        'assists': total_assists,
        'kdr': kill_death_ratio,
        'impact': total_assists + total_kills * 0.8
    }
    
    return performance_metrics

# Bonus calculation with red herring logic
def compute_bonus_multiplier(level, rank, streak_bonuses):
    base_multiplier = 1.0
    
    if level > 50:
        base_multiplier += 0.3
    elif level > 30:
        base_multiplier += 0.15
    
    # Misleading rank check that doesn't actually affect final bonus
    temp_bonus = 0.0
    if rank == 'S':
        temp_bonus = 0.25  # Unused variable - distractor
    elif rank == 'A':
        temp_bonus = 0.15  # Also unused
    
    # Actual bonus logic
    streak_sum = sum(streak_bonuses)
    normalized_streak = min(streak_sum / 100, 0.4)
    
    final_multiplier = base_multiplier + 0.1 * (level // 10) + normalized_streak
    
    # Dead code path - never executed under normal conditions (distractor)
    if False and rank == 'Z':
        final_multiplier *= 1.5
    
    return round(final_multiplier, 4)

# Main scoring logic
def calculate_final_score(player_data, bonus_multiplier):
    analysis = analyze_player_performance(player_data['game_sessions'])
    
    base_score = analysis['kills'] * 10 + analysis['assists'] * 5 - analysis['deaths'] * 2
    impact_bonus = analysis['impact'] * 3
    
    # Compute tier modifier using string pattern (python idiom: string method)
    tier_modifier = 1.0
    tier = player_data['tier'].upper()
    if 'PREMIER' in tier:
        tier_modifier = 1.5
    elif 'ELITE' in tier:
        tier_modifier = 1.3
    elif 'PRO' in tier:
        tier_modifier = 1.1
    
    # Aggregate score with multiple factors
    raw_score = (base_score + impact_bonus) * bonus_multiplier * tier_modifier
    
    # Normalization step
    capped_score = min(raw_score, 15000)
    
    # Additional noise variables (semi-relevant)
    session_count = len(player_data['game_sessions'])
    avg_per_session = capped_score / session_count if session_count else 0
    
    # Final adjustment based on consistency (using enumerate)
    consistency_factor = 0
    for i, session in enumerate(player_data['game_sessions']):
        if session['kills'] >= 5:
            consistency_factor += 1 + (i * 0.05)  # Slight positional weight
    
    final_score = int(capped_score + consistency_factor * 10)
    
    # Redundant dictionary counting (collections usage)
    action_counter = defaultdict(int)
    for session in player_data['game_sessions']:
        for action in ['kills', 'deaths', 'assists']:
            action_counter[action] += session[action]
    
    # Unused zip operation (distractor)
    kill_list = [s['kills'] for s in player_data['game_sessions']]
    death_list = [s['deaths'] for s in player_data['game_sessions']]
    for k, d in zip(kill_list, death_list):
        if k > d * 2:
            pass  # No effect
    
    return final_score

# Player data input
player_data = {
    'tier': 'Elite_Champion_2024',
    'level': 42,
    'rank': 'A',
    'game_sessions': [
        {'kills': 7, 'deaths': 3, 'assists': 4, 'streak': 5},
        {'kills': 5, 'deaths': 6, 'assists': 8, 'streak': 3},
        {'kills': 9, 'deaths': 2, 'assists': 3, 'streak': 7},
        {'kills': 6, 'deaths': 4, 'assists': 6, 'streak': 4}
    ]
}

bonus_multiplier = compute_bonus_multiplier(
    player_data['level'], 
    player_data['rank'], 
    [session['streak'] for session in player_data['game_sessions']]
)

final_score = calculate_final_score(player_data, bonus_multiplier)
print(f"Target result: {final_score}")