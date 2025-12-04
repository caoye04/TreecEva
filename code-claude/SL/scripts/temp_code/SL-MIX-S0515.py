def process_match_results(raw_data, filters=None):
    # Process match data with various filters
    if filters is None:
        filters = {'min_score': 10, 'exclude_forfeits': True}
    
    processed = {}
    for match_id, details in raw_data.items():
        if filters.get('exclude_forfeits') and details.get('forfeit', False):
            continue
        
        if details.get('score', 0) >= filters.get('min_score', 0):
            processed[match_id] = details.copy()
            # Apply normalization factor
            processed[match_id]['normalized'] = details.get('score', 0) * 1.5
    
    return processed

def calculate_bonus_points(achievements):
    # Calculate bonus points from player achievements
    bonus_mapping = {
        'first_place': 50,
        'perfect_game': 25,
        'consecutive_wins': 15,
        'participation': 5
    }
    
    total_bonus = 0
    for achievement, count in achievements.items():
        if achievement in bonus_mapping:
            total_bonus += bonus_mapping[achievement] * count
    
    # Apply diminishing returns for multiple achievements
    if len(achievements) > 2:
        total_bonus = int(total_bonus * 0.9)
    
    return total_bonus

def analyze_performance(match_history):
    # Analyze player performance metrics
    if not match_history:
        return {'consistency': 0, 'peak_performance': 0}
    
    scores = [match.get('score', 0) for match in match_history if isinstance(match, dict)]
    if not scores:
        return {'consistency': 0, 'peak_performance': 0}
    
    avg_score = sum(scores) / len(scores)
    peak_score = max(scores)
    consistency = 100 - (sum(abs(s - avg_score) for s in scores) / len(scores))
    
    return {
        'consistency': max(0, min(100, consistency)),
        'peak_performance': peak_score
    }

def calculate_tournament_points(player_stats, qualification_threshold):
    # Main function to calculate tournament points
    base_points = 0
    penalty_points = 0
    bonus_multiplier = 1.0
    
    # Extract relevant data
    match_results = player_stats.get('matches', {})
    achievements = player_stats.get('achievements', {})
    penalties = player_stats.get('penalties', [])
    
    # Process matches that matter for scoring
    relevant_matches = [m for m in match_results if m.get('tournament_phase') in ('qualifier', 'final')]
    qualifier_matches = [m for m in relevant_matches if m.get('tournament_phase') == 'qualifier']
    
    # Calculate base points from match scores
    match_points = sum(match.get('score', 0) for match in relevant_matches)
    
    # Apply qualifier threshold check
    qualifier_avg = sum(match.get('score', 0) for match in qualifier_matches) / max(1, len(qualifier_matches))
    if qualifier_avg < qualification_threshold:
        match_points = match_points // 2
    
    # Calculate penalties
    for penalty in penalties:
        penalty_type = penalty.get('type', '')
        if penalty_type == 'disqualification':
            return 0  # Immediate disqualification
        elif penalty_type == 'score_reduction':
            penalty_points += penalty.get('points', 0)
        elif penalty_type == 'multiplier_reduction':
            bonus_multiplier *= (1 - penalty.get('factor', 0))
    
    # Process bonus points
    bonus_points = calculate_bonus_points(achievements)
    
    # Apply special rule for perfect attendance
    if 'perfect_attendance' in achievements and achievements['perfect_attendance'] > 0:
        bonus_multiplier += 0.15
    
    # Calculate final score with all factors
    base_points = match_points - penalty_points
    adjusted_bonus = int(bonus_points * bonus_multiplier)
    
    # Apply difficulty adjustment based on competition level
    difficulty_factor = player_stats.get('competition_level', 1) / 10 + 1
    weighted_base = int(base_points * difficulty_factor)
    
    # The key calculation for final score
    final_score = weighted_base + adjusted_bonus
    
    # Apply minimum score rule
    if final_score < 0:
        final_score = 0
    
    print(f"Result: {final_score}")
    return final_score

# Test data
player_stats = {
    'player_id': 'P12345',
    'name': 'Alex Johnson',
    'matches': [
        {'id': 'M1', 'score': 85, 'tournament_phase': 'qualifier'},
        {'id': 'M2', 'score': 92, 'tournament_phase': 'qualifier'},
        {'id': 'M3', 'score': 78, 'tournament_phase': 'qualifier'},
        {'id': 'M4', 'score': 105, 'tournament_phase': 'final'},
        {'id': 'M5', 'score': 65, 'tournament_phase': 'exhibition'}
    ],
    'achievements': {
        'first_place': 1,
        'perfect_game': 0,
        'consecutive_wins': 2,
        'participation': 5,
        'perfect_attendance': 1
    },
    'penalties': [
        {'type': 'score_reduction', 'points': 20, 'reason': 'late submission'},
        {'type': 'multiplier_reduction', 'factor': 0.1, 'reason': 'unsportsmanlike conduct'}
    ],
    'competition_level': 2
}

# Process some irrelevant data to create distraction
distractor_data = {
    'M1': {'score': 75, 'forfeit': False},
    'M2': {'score': 82, 'forfeit': False},
    'M3': {'score': 5, 'forfeit': True}
}
processed_distractors = process_match_results(distractor_data)

# More distraction calculations
performance_metrics = analyze_performance(player_stats['matches'])
consistency_score = performance_metrics['consistency']
potential_bonus = consistency_score * 0.5

# Set qualification threshold
qualification_threshold = 80

# Calculate the final tournament points
final_score = calculate_tournament_points(player_stats, qualification_threshold)