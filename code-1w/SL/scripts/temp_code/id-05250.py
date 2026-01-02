from collections import defaultdict

# Simulate player action counts in a strategy game
def count_actions(log_entries):
    counts = defaultdict(int)
    for entry in log_entries:
        action = entry.split('_')[0]
        counts[action] += 1
    return counts

# Apply multiplicative modifiers based on game phase
def apply_modifiers(base_counts, mod_map, phase):
    result = {}
    multiplier = mod_map.get(phase, 1)
    for key, value in base_counts.items():
        result[key] = value * multiplier
    return result

# Aggregate total score from modified actions
def calculate_final_score(stats, modifiers):
    base_total = sum(stats.values())
    bonus = 0
    for k, v in stats.items():
        if 'attack' in k and v > 2:
            bonus += v // 2
    return base_total + bonus

# Game event log
event_log = [
    'attack_critical', 'move_north', 'attack_fast', 'defend_heavy',
    'attack_critical', 'move_south', 'defend_light', 'attack_fast'
]

# Count each type of action
action_stats = count_actions(event_log)

# Modifier map for different phases
phase_modifiers = {'midgame': 1.5, 'endgame': 2}

current_phase = 'midgame'

# Apply dynamic phase modifier to stats
modified_stats = apply_modifiers(action_stats, phase_modifiers, current_phase)

# Calculate final score incorporating bonuses
final_score = calculate_final_score(modified_stats, phase_modifiers)

print(f"Result: {final_score}")