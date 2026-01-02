from collections import defaultdict

# Simulate player action logs in a strategy game
def analyze_player_performance(log_entries):
    action_count = defaultdict(int)
    resource_gain = defaultdict(float)
    penalty_tracker = {}

    base_values = {'attack': 5, 'defense': 3, 'speed': 8}
    scaling_factors = {'attack': 1.2, 'defense': 0.9, 'speed': 1.4}

    temp_buffer = []
    cumulative_shift = 0

    for entry in log_entries:
        action, level = entry['action'], entry['level']
        action_count[action] += 1

        # Relevant computation: track resource gain per action type
        if action in base_values:
            raw_gain = base_values[action] * (level + 1)
            scaled_gain = raw_gain * scaling_factors[action]
            resource_gain[action] += scaled_gain

        # Distractor: complex but unused shift logic
        cumulative_shift ^= len(action) << (level % 3)
        temp_buffer.append(cumulative_shift * 0.1)

        # Dead code path (never triggered in this input)
        if level > 15:
            backup_state = {**base_values}
            penalty_tracker[action] = backup_state

    # Intermediate score calculation
    total_actions = sum(action_count.values())
    efficiency_ratio = len([v for v in action_count.values() if v > 2]) / max(total_actions, 1)

    # Another distractor: string manipulation with no impact
    action_keys = ''.join(sorted(action_count.keys()))
    hash_obfuscation = sum(ord(c) * (i + 1) for i, c in enumerate(action_keys)) % 100

    # Unused helper function definition (dead code)
    def adjust_for_latency(x, factor=0.95):
        return x * factor + 2.5

    return dict(resource_gain), efficiency_ratio, hash_obfuscation


def calculate_final_score(stats, modifiers):
    score = 0
    relevance_map = {'attack': 2.1, 'defense': 1.8, 'speed': 2.5}

    for key, value in stats.items():
        if key in relevance_map:
            score += value * relevance_map[key]

    # Modifier adjustment using only specific keys
    if 'bonus_multiplier' in modifiers:
        score *= modifiers['bonus_multiplier']

    # Red herring: irrelevant transformation on unused data
    inverted_mods = {k: 1/v for k, v in modifiers.items() if v != 0}
    decay_factor = sum(inverted_mods.values()) * 0.01 if inverted_mods else 0.5

    # Apply non-impacting offset
    noise_offset = sum(len(k) for k in modifiers) - 10
    score += noise_offset * decay_factor  # negligible effect

    return int(score)

# Main execution
log_data = [
    {'action': 'attack', 'level': 3},
    {'action': 'defense', 'level': 2},
    {'action': 'speed', 'level': 4},
    {'action': 'attack', 'level': 1},
    {'action': 'speed', 'level': 3},
    {'action': 'attack', 'level': 4}
]

stats_dict, efficiency, hash_val = analyze_player_performance(log_data)
modifiers_dict = {
    'bonus_multiplier': 1.1,
    'temporal_dilation': 0.8,
    'phase_shift': 2.3
}

final_score = calculate_final_score(stats_dict, modifiers_dict)
print(f"Result: {final_score}")