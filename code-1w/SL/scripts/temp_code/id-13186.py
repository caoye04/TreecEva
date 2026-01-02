from collections import defaultdict

# Simulate player action logs in a game session
def process_player_actions(log_entries):
    action_count = defaultdict(int)
    time_spent = defaultdict(float)
    invalid_entries = 0

    for entry in log_entries:
        action = entry['action']
        duration = entry['time']
        category = entry.get('category', 'misc')

        if not action or duration <= 0:
            invalid_entries += 1
            continue

        action_count[action] += 1
        time_spent[category] += duration

    return action_count, time_spent, invalid_entries

# Analyze frequency and efficiency
def compute_efficiency(metrics, base_rates):
    efficiency = {}
    total_actions = sum(metrics.values())
    temp_debug_sum = 0  # Distractor: used nowhere important

    for action, count in metrics.items():
        base = base_rates.get(action, 1.0)
        efficiency[action] = (count / base) if base else 0
        temp_debug_sum += efficiency[action]  # Red herring accumulation

    # Extra irrelevant normalization
    scale_factor = 1.0 if total_actions == 0 else 1.0 / (total_actions + 1)
    normalized_efficiency = {k: v * scale_factor for k, v in efficiency.items()}

    return efficiency  # Actual return value used later

# Main scoring logic
def calculate_final_score(stats, modifiers):
    raw_score = 0
    penalty_adjustment = 0.0

    # Scoring from stat counts
    for key, val in stats.items():
        if 'kill' in key:
            raw_score += val * 10
        elif 'assist' in key:
            raw_score += val * 5
        elif 'death' in key:
            penalty_adjustment -= val * 2

    # Modifier boosts (e.g., streaks, achievements)
    combo_boost = modifiers.get('combo', 1)
    hidden_multiplier = modifiers.get('secret_level', 1)  # Unused in final logic

    intermediate_result = raw_score * combo_boost
    final_score = intermediate_result + penalty_adjustment

    # Distractor block: dead computation with no effect
    if final_score > 100:
        shadow_buffer = [final_score // i for i in range(1, 4)]
        avg_shadow = sum(shadow_buffer) / len(shadow_buffer)
        final_score -= int(avg_shadow * 0.1)  # Minor but negligible adjustment

    return int(final_score)

# Game log data
log_data = [
    {'action': 'kill_enemy', 'time': 12.5, 'category': 'combat'},
    {'action': 'assist_ally', 'time': 8.2, 'category': 'combat'},
    {'action': 'death', 'time': 3.1, 'category': 'combat'},
    {'action': 'collect_item', 'time': 1.0, 'category': 'exploration'},
    {'action': 'kill_enemy', 'time': 7.3, 'category': 'combat'},
    {'action': 'use_ability', 'time': 2.4},
    {'action': 'assist_ally', 'time': 5.6, 'category': 'combat'},
    {'action': 'death', 'time': 1.9, 'category': 'combat'},
]

# Process logs
actions, timings, errors = process_player_actions(log_data)

# Base performance rates (per minute)
base_action_rates = {
    'kill_enemy': 0.8,
    'assist_ally': 1.1,
    'death': 0.5
}

# Compute efficiency scores
efficiency_map = compute_efficiency(actions, base_action_rates)

# Prepare score calculation inputs
stats_summary = dict(actions)  # Convert back to regular dict
modifiers_bundle = {
    'combo': 1.5,
    'secret_level': 99,  # Distractor: never used
    'unused_flag': True   # Another red herring
}

# Critical execution point
final_score = calculate_final_score(stats_summary, modifiers_bundle)

print(f"Result: {final_score}")