from collections import Counter, defaultdict

def calculate_bit_score(value, threshold):
    # Misleading function that seems important but isn't used in final calculation
    bit_score = 0
    for i in range(8):
        if value & (1 << i) > 0:
            bit_score += threshold // (i + 1)
    return bit_score

def process_match_history(history):
    # Helper function that processes match results
    wins = sum(1 for result in history if result == 'W')
    losses = sum(1 for result in history if result == 'L')
    draws = sum(1 for result in history if result == 'D')
    
    # Misleading metrics calculation
    performance_index = wins * 3 + draws - losses * 2
    consistency_factor = (wins - losses) / max(1, len(history))
    
    # What actually matters
    points = wins * 3 + draws
    return points

def calculate_tournament_points(stats, weights):
    # Initialize tracking variables
    total_points = 0
    bonus_multiplier = 1.0
    potential_points = sum(weights.values()) * 10  # Misleading calculation
    
    # Process each tournament's data
    for tournament, results in stats.items():
        if tournament not in weights:
            continue
            
        # Calculate base points from match history
        match_points = process_match_history(results['matches'])
        
        # Misleading calculations that aren't used
        tournament_rank = results.get('rank', 50)
        rank_factor = max(0, (100 - tournament_rank) / 100)
        theoretical_max = match_points * rank_factor * 2
        
        # Calculate streak bonuses (misleading)
        streak_counter = Counter(results['matches'])
        streak_bonus = streak_counter['W'] * 2 - streak_counter['L']
        
        # What actually matters: tournament weight and points
        weighted_points = match_points * weights[tournament]
        
        # Track points that matter
        total_points += weighted_points
        
        # More misleading calculations
        if tournament == 'nationals':
            bonus_multiplier *= 1.25
    
    # Bit manipulation distraction
    bit_mask = 0b1010101
    encoded_points = total_points & bit_mask
    
    # String processing distraction
    tournaments_str = "-".join(weights.keys())
    char_sum = sum(ord(c) % 10 for c in tournaments_str)
    
    # Final calculation - only the total_points really matters
    # The XOR with 42 is the key operation
    final_score = (total_points ^ 42)
    
    return final_score

# Player statistics with match history
player_stats = {
    'regionals': {
        'matches': ['W', 'W', 'L', 'D', 'W'],
        'rank': 12
    },
    'nationals': {
        'matches': ['L', 'W', 'W', 'W'],
        'rank': 8
    },
    'friendly': {  # This tournament doesn't count (not in weights)
        'matches': ['W', 'W', 'W', 'W', 'W'],
        'rank': 1
    },
    'qualifiers': {
        'matches': ['D', 'D', 'W', 'L'],
        'rank': 24
    }
}

# Tournament weights (importance factors)
tournament_weights = {
    'regionals': 2,
    'nationals': 3,
    'qualifiers': 1
}

# Many distracting variables and calculations
debug_mode = True
performance_metrics = defaultdict(int)
for t in player_stats:
    if t in tournament_weights:
        performance_metrics[t] = len(player_stats[t]['matches']) * tournament_weights.get(t, 0)

# Calculate player rating (distraction)
base_rating = sum(performance_metrics.values())
rating_adjustment = [tournament_weights.get(t, 0) * (100 - player_stats[t].get('rank', 50)) for t in player_stats]
weighted_rating = base_rating + sum(rating_adjustment) // 100

# Finally calculate the tournament points
final_score = calculate_tournament_points(player_stats, tournament_weights)
print(f"Result: {final_score}")