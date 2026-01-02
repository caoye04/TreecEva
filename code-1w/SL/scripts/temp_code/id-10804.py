from collections import defaultdict
from itertools import combinations

# Simulate player action logs in a strategy game
action_log = [
    ('move', 12), ('attack', 8), ('move', 5), ('heal', 20),
    ('attack', 15), ('attack', 7), ('move', 3), ('heal', 10)
]

# Process action frequencies
action_count = defaultdict(int)
for action, value in action_log:
    action_count[action] += 1

# Extract relevant stats
attack_count = action_count['attack']
defense_count = action_count['move']  # moving as evasion proxy
healing_received = sum(val for act, val in action_log if act == 'heal')

# Compute derived metrics with some irrelevant intermediate steps
avg_attack = sum(val for act, val in action_log if act == 'attack') / attack_count if attack_count else 0
attack_efficiency = avg_attack * 0.9 + 2  # arbitrary buff

# Distractor: analyze non-existent 'stealth' actions
stealth_entries = [entry for entry in action_log if entry[0] == 'stealth']
phantom_bonus = len(stealth_entries) * 5  # never used, but looks important

# Modifiers from environment (some are red herrings)
modifiers = {
    'weather_penalty': 0.95,
    'terrain_boost': 1.1,
    'unused_modifier': 3.14159,  # clearly unused
    'crit_factor': 1.2
}

# Secondary distractor computation: all possible attack pairs (no real impact)
damage_pairs = list(combinations([val for act, val in action_log if act == 'attack'], 2))
pair_variance_estimate = len(damage_pairs) * 0.1 if damage_pairs else 0

# Core scoring logic
base_attack_score = attack_count * avg_attack
movement_score = defense_count * 3
healing_score = min(healing_received, 50)  # cap healing contribution

# Final calculation - only some modifiers actually apply
def calculate_final_score(stats, mods):
    score = stats['attack'] + stats['movement'] + stats['healing']
    score *= mods['weather_penalty']  # meaningful penalty
    score *= mods['crit_factor']      # critical hit factor matters
    # Note: terrain_boost and others are not used
    bonus = 5 if stats['attack'] > 20 else 0  # unreachable threshold
    return int(score + bonus)

# Prepare stat bundle
stats = {
    'attack': base_attack_score,
    'movement': movement_score,
    'healing': healing_score
}

# Key execution point
final_score = calculate_final_score(stats, modifiers)

print(f"Result: {final_score}")