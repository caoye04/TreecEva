from collections import defaultdict

# Simulate player action logs in a strategy game
action_log = [
    ('move', 'north', 15),
    ('attack', 'dragon', 40),
    ('move', 'east', 10),
    ('collect', 'gold', 25),
    ('attack', 'goblin', 12),
    ('cast', 'heal', 33),
    ('attack', 'dragon', 45)
]

# Track action frequencies and cumulative effects
total_actions = len(action_log)
action_count = defaultdict(int)
cumulative_damage = 0
damage_records = []
idle_time = 0
phantom_counter = 0  # Distractor: not used in final logic

for action_type, target, value in action_log:
    action_count[action_type] += 1
    if action_type == 'attack':
        cumulative_damage += value
        damage_records.append(value)
    elif action_type == 'move':
        idle_time += value % 3  # Minor side computation
    elif action_type == 'cast':
        phantom_counter += value * 0.1  # Red herring

# Compute derived stats
avg_damage = cumulative_damage / len(damage_records) if damage_records else 0
max_single_damage = max(damage_records)
action_efficiency = total_actions / (cumulative_damage + 1)  # Avoid div by zero

# Modifiers based on behavior patterns
modifiers = {
    'aggression': action_count['attack'] * 1.5,
    'mobility': action_count['move'] * 2,
    'utility': action_count['cast'] + action_count['collect']
}

# Player stats summary
stats = {
    'total_actions': total_actions,
    'cumulative_damage': cumulative_damage,
    'avg_damage': avg_damage,
    'max_hit': max_single_damage,
    'efficiency': action_efficiency
}

# Irrelevant intermediate calculation (distractor)
theoretical_throughput = (total_actions * avg_damage) / (action_count['move'] + 0.5)
scaled_effort = theoretical_throughput * 0.75 + idle_time

# Core scoring logic
def calculate_final_score(player_stats, mods):
    base = player_stats['cumulative_damage']
    aggression_bonus = mods['aggression'] * player_stats['avg_damage']
    mobility_penalty = mods['mobility'] * 1.2  # High mobility reduces focus
    utility_bonus = mods['utility'] * 5
    
    # Apply non-linear adjustment for max hit
    spike_factor = (player_stats['max_hit'] ** 1.1) // 10
    
    # Final composition
    score = base + aggression_bonus - mobility_penalty + utility_bonus + spike_factor
    
    # Dead code branch (never executed, adds interference)
    if False:
        score = score * 0.9 + 100  # This does nothing
    
    return int(score)

# Execution point of interest
final_score = calculate_final_score(stats, modifiers)
print(f"Result: {final_score}")