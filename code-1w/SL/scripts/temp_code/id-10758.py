from collections import defaultdict

# Simulate player performance metrics in a strategy game
def analyze_player_performance():
    base_values = [12, 15, 8, 20, 14]
    weights = [0.1, 0.3, 0.2, 0.3, 0.1]
    
    # Irrelevant intermediate calculation (distractor)
    avg_base = sum(base_values) / len(base_values)
    weighted_sum = sum(b * w for b, w in zip(base_values, weights))
    
    # Track action frequencies using defaultdict (relevant)
    actions = ['move', 'attack', 'move', 'defend', 'attack', 'move', 'cast']
    action_count = defaultdict(int)
    for action in actions:
        action_count[action] += 1
    
    # Misleading normalization (not used later)
    total_actions = len(actions)
    normalized = {k: v / total_actions for k, v in action_count.items()}
    
    # Build stats dictionary (used in final calculation)
    stats = {
        'efficiency': weighted_sum,
        'moves_made': action_count['move'],
        'attacks_landed': action_count['attack'],
        'defensive_moves': action_count['defend'] + action_count['cast']
    }
    
    # Extra unused stats (distractors)
    stats['unused_metric_1'] = avg_base * 0.5
    stats['placeholder_flag'] = False
    
    # Modifiers based on achievement unlocks (semi-relevant)
    achievements = ['first_blood', 'tactical', 'unstoppable']
    modifiers = defaultdict(float)
    if 'tactical' in achievements:
        modifiers['efficiency_boost'] = 1.2
    if 'unstoppable' in achievements:
        modifiers['combo_multiplier'] = 1.5
    modifiers['base_penalty'] = -2.0  # Applied regardless
    
    # Dead code path (distractor)
    temp_result = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                temp_result += i * 2
    # This loop doesn't affect final outcome

    def calculate_final_score(player_stats, buffs):
        score = player_stats['efficiency']
        score *= buffs['efficiency_boost']
        if player_stats['attacks_landed'] > 1:
            score += buffs.get('combo_multiplier', 1.0) * 5
        score += player_stats['defensive_moves'] * 2
        score += buffs['base_penalty']
        return int(score)

    final_score = calculate_final_score(stats, modifiers)
    
    # Red herring variable with similar name
    final_tally = final_score + 10  # Not used
    
    # Output the correct result
    print(f"Result: {final_score}")

analyze_player_performance()