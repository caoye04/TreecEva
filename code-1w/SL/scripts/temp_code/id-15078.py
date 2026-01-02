from collections import defaultdict

# Simulate player action logs in a strategy game
def analyze_player_performance(logs):
    action_count = defaultdict(int)
    damage_dealt = 0
    healing_received = 0
    tactical_points = 0

    # Core processing loop
    for entry in logs:
        action = entry['action']
        value = entry['value']
        action_count[action] += 1
        
        if action == 'attack':
            damage_dealt += value
            tactical_points += value // 10
        elif action == 'heal':
            healing_received += value
            tactical_points += value // 25
        elif action == 'defend':
            tactical_points += value // 5

    # Irrelevant intermediate calculation (distractor)
    avg_action_value = sum(e['value'] for e in logs) / len(logs) if logs else 0
    action_efficiency = {act: cnt / len(logs) for act, cnt in action_count.items()}

    # Unused helper function (dead code - distractor)
    compute_ratio = lambda x, y: (x + 1) / (y + 1)

    return {
        'damage': damage_dealt,
        'healing': healing_received,
        'tactical': tactical_points,
        'count': dict(action_count)
    }

# Modifier system based on equipment and status
def apply_modifiers(base_stats, mod_list):
    temp_bonus = 0
    penalty_reduction = 0

    for mod in mod_list:
        if mod['type'] == 'amplify':
            temp_bonus += mod['strength']
        elif mod['type'] == 'resist':
            penalty_reduction += mod['strength']

    # Apply only tactical point multiplier
    base_stats['tactical'] = int(base_stats['tactical'] * (1 + temp_bonus * 0.1))
    
    # Red herring: calculate but do not use these
    total_mods = len(mod_list)
    net_effect = temp_bonus - penalty_reduction
    efficiency_ratio = (base_stats['damage'] + 1) / (sum(base_stats['count'].values()) + 1)

    return base_stats

# Final scoring with weighted formula
def calculate_final_score(stats, modifiers):
    base_tactical = stats['tactical']
    raw_damage = stats['damage']
    
    # Scoring weights
    dmg_weight = 0.3
    tac_weight = 0.7

    # Compute score components
    damage_score = raw_damage * dmg_weight
    tactical_score = base_tactical * tac_weight
    
    # Misleading alternate calculation (not used)
    max_possible = max(stats['damage'], stats['healing'], stats['tactical'])
    normalized = base_tactical / (max_possible + 1e-8)
    
    final_score = int(damage_score + tactical_score)
    
    # Additional unused diagnostics
    consistency_check = len(stats['count']) >= 3
    action_diversity = len([v for v in stats['count'].values() if v > 2])

    return final_score

# Input data
player_log = [
    {'action': 'attack', 'value': 45},
    {'action': 'defend', 'value': 20},
    {'action': 'attack', 'value': 32},
    {'action': 'heal', 'value': 50},
    {'action': 'attack', 'value': 67},
    {'action': 'defend', 'value': 15},
    {'action': 'attack', 'value': 38},
    {'action': 'heal', 'value': 25}
]

modifiers = [
    {'type': 'amplify', 'strength': 3},
    {'type': 'resist', 'strength': 1},
    {'type': 'amplify', 'strength': 2}
]

# Execute pipeline
stats = analyze_player_performance(player_log)
stats_with_mods = apply_modifiers(stats, modifiers)
final_score = calculate_final_score(stats_with_mods, modifiers)

print(f"Result: {final_score}")