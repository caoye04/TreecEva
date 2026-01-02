from collections import defaultdict

# Simulate player action logs in a strategy game
def analyze_player_performance(log_entries):
    action_count = defaultdict(int)
    damage_by_type = defaultdict(float)
    wasted_actions = 0
    total_cooldown_time = 0.0

    for entry in log_entries:
        action = entry['action']
        action_count[action] += 1

        if action == 'ability_x':
            damage_by_type['burst'] += entry['damage']
            if entry['overkill']:
                wasted_actions += 1
        elif action == 'ability_y':
            damage_by_type['sustained'] += entry['damage']
            total_cooldown_time += entry['cooldown']
        elif action == 'defend':
            # Track defensive efficiency
            if entry['blocked'] < entry['incoming']:
                action_count['inefficient_defense'] += 1

    return action_count, damage_by_type, wasted_actions, total_cooldown_time

# Calculate composite score with weighting
def calculate_damage_efficiency(damage_dict):
    burst = damage_dict.get('burst', 0)
    sustained = damage_dict.get('sustained', 0)
    total = burst + sustained
    
    if total == 0:
        return 0.0
    
    efficiency = (burst * 1.5 + sustained) / total  # Weighted contribution
    return round(efficiency, 4)

# Secondary metric: assess resource conservation
def evaluate_resource_usage(log_entries):
    energy_spent = 0
    max_energy_capacity = 100
    recoveries = 0

    for entry in log_entries:
        if 'energy_cost' in entry:
            energy_spent += entry['energy_cost']
            if entry.get('energy_recovered', 0) > 0:
                recoveries += 1

    consumption_rate = energy_spent / max_energy_capacity
    return consumption_rate, recoveries

# Main scoring function
def calculate_final_score(stats, modifiers):
    base_efficiency = stats['efficiency']
    usage_ratio = stats['usage_ratio']
    raw_damage = stats['total_damage']

    # Modifier effects
    terrain_boost = modifiers.get('terrain_advantage', False)
    morale_bonus = modifiers.get('morale', 1.0)
    penalty_factor = modifiers.get('penalties', 0)

    adjusted_efficiency = base_efficiency * (1 + morale_bonus)

    # Complex scoring formula
    score_component_1 = adjusted_efficiency * 100
    score_component_2 = raw_damage / 10
    score_component_3 = usage_ratio * 50

    preliminary_score = score_component_1 + score_component_2 + score_component_3

    if terrain_boost:
        preliminary_score *= 1.2

    final_score = int(preliminary_score - (penalty_factor * 15))

    # Irrelevant intermediate calculation (distractor)
    theoretical_max = 100 * (1 + 1.5) + 500 + 50
    unused_buffer = theoretical_max - preliminary_score

    return final_score

# Simulation data
log_data = [
    {'action': 'ability_x', 'damage': 120, 'overkill': False, 'energy_cost': 25},
    {'action': 'ability_y', 'damage': 85, 'cooldown': 3.5, 'energy_cost': 20},
    {'action': 'ability_x', 'damage': 150, 'overkill': True, 'energy_cost': 25},
    {'action': 'defend', 'blocked': 40, 'incoming': 60, 'energy_cost': 10},
    {'action': 'ability_y', 'damage': 90, 'cooldown': 3.5, 'energy_cost': 20},
    {'action': 'ability_x', 'damage': 130, 'overkill': False, 'energy_cost': 25},
    {'action': 'defend', 'blocked': 50, 'incoming': 50, 'energy_cost': 10},
]

# Extract performance metrics
counts, damage_breakdown, waste, cooldown = analyze_player_performance(log_data)
conservation_rate, refills = evaluate_resource_usage(log_data)

# Compute derived statistics
total_actions = sum(counts.values())
efficiency_metric = calculate_damage_efficiency(damage_breakdown)
usage_ratio = (total_actions - waste) / total_actions if total_actions else 0
overall_damage = sum(damage_breakdown.values())

# Compile stats
performance_stats = {
    'efficiency': efficiency_metric,
    'usage_ratio': usage_ratio,
    'total_damage': overall_damage
}

# Environment modifiers
game_modifiers = {
    'terrain_advantage': True,
    'morale': 0.25,
    'penalties': 2
}

# Critical statement
final_score = calculate_final_score(performance_stats, game_modifiers)

print(f"Result: {final_score}")