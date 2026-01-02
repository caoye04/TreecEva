from collections import defaultdict
import itertools

# Simulate player action logs in a strategy game
actions = [
    ('move', 'north', 15), ('attack', 'goblin', 8), ('collect', 'ore', 3),
    ('attack', 'troll', 12), ('cast', 'heal', 25), ('collect', 'wood', 7),
    ('attack', 'goblin', 9), ('move', 'east', 22), ('collect', 'ore', 5)
]

# Track resource yields and combat effectiveness
total_resources = defaultdict(int)
combat_log = []
dummy_counter = 0

for action_type, target, value in actions:
    if action_type == 'collect':
        total_resources[target] += value
        dummy_counter += 1  # Distractor: not used later
    elif action_type == 'attack':
        combat_log.append((target, value))

# Calculate base efficiency score
base_efficiency = sum(total_resources.values()) * 1.5

# Analyze combat patterns
encounters = {}
for enemy, damage in combat_log:
    if enemy not in encounters:
        encounters[enemy] = []
    encounters[enemy].append(damage)

average_damage = {
    enemy: sum(dmg_list) / len(dmg_list)
    for enemy, dmg_list in encounters.items()
}

# High-damage threshold flag (distractor logic)
high_damage_burst = any(d >= 20 for d in itertools.chain.from_iterable(encounters.values()))

# Prepare stats and modifiers
stats = {
    'resources': sum(total_resources.values()),
    'unique_enemies': len(encounters),
    'total_attacks': len(combat_log)
}

modifiers = [1.2, 0.9, 1.0, 1.1]

# Irrelevant transformation on modifiers (adds noise)
transformed_mods = list(map(lambda x: x ** 2 if x < 1.0 else x, modifiers))
dummy_result = sum(x for x in transformed_mods if x > 1.05)  # Unused

# Core scoring function
def calculate_final_score(player_stats, mod_weights):
    base = player_stats['resources'] * 2.5
    enemy_bonus = player_stats['unique_enemies'] * 10
    attack_penalty = player_stats['total_attacks'] * 0.5
    
    # Apply weighted modifier effect (only last three matter)
    effective_weight = sum(mod_weights[1:]) / len(mod_weights[1:])
    
    intermediate = (base + enemy_bonus - attack_penalty) * effective_weight
    
    # Dummy safety check (never triggers in this case)
    if intermediate < 0:
        return 0
    
    return int(intermediate)

final_score = calculate_final_score(stats, modifiers)
print(f"Target result: {final_score}")