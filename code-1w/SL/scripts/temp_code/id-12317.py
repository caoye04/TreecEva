from collections import defaultdict

# Simulate player action logs in a strategy game
def analyze_player_performance(log_entries):
    action_count = defaultdict(int)
    damage_by_type = defaultdict(float)
    temp_buffer = [0] * 10  # Unused preallocation - red herring

    for entry in log_entries:
        action = entry['action']
        action_count[action] += 1

        if action == 'cast_spell':
            spell_type = entry['subtype']
            damage = entry['damage']
            damage_by_type[spell_type] += damage

        elif action == 'melee_attack':
            bonus_multiplier = entry.get('crit', 1.0)
            base_damage = entry['base']
            total_damage = base_damage * bonus_multiplier
            damage_by_type['melee'] += total_damage

    return dict(action_count), dict(damage_by_type)

# Irrelevant helper - dead code path
def deprecated_scaling(x):
    result = 0
    for i in range(x):
        result += i * 0.5
    return result  # Never called

# Main scoring logic
def calculate_final_score(stats, modifiers):
    base = stats['total_kills'] * 10
    death_penalty = stats['total_deaths'] * 5
    assist_bonus = stats['total_assists'] * 3

    # Dummy computation with misleading name
    phantom_impact = sum([i * 0.1 for i in range(5)])  # Adds 1.0, but irrelevant

    intermediate = base - death_penalty + assist_bonus

    # Apply type-based modifiers
    multiplier = 1.0
    for mtype, val in modifiers.items():
        if mtype == 'aggression':
            multiplier *= (1 + val / 100)
        elif mtype == 'efficiency':
            multiplier *= (1 + val / 100)

    final = int(intermediate * multiplier)
    return final

# Input data
log_data = [
    {'action': 'cast_spell', 'subtype': 'fire', 'damage': 120},
    {'action': 'cast_spell', 'subtype': 'ice', 'damage': 95},
    {'action': 'melee_attack', 'base': 40, 'crit': 2.0},
    {'action': 'cast_spell', 'subtype': 'fire', 'damage': 110},
    {'action': 'melee_attack', 'base': 40, 'crit': 1.0},
]

# Extract high-level stats
actions, damages = analyze_player_performance(log_data)

# Compute derived metrics (some used, some not)
total_fire_damage = damages.get('fire', 0)  # Used indirectly
avg_melee_damage = damages.get('melee', 0) / max(actions.get('melee_attack', 1), 1)  # Distractor

# Build stat profile
player_stats = {
    'total_kills': actions.get('cast_spell', 0),  # Proxy usage
    'total_deaths': 4,  # Fixed penalty
    'total_assists': actions.get('melee_attack', 0),
}

# Modifiers based on playstyle
scaling_mods = {
    'aggression': 20,
    'efficiency': 10,
    'mobility': 15  # Unused modifier - red herring
}

# Critical execution point
final_score = calculate_final_score(player_stats, scaling_mods)

# Output result
print(f"Result: {final_score}")