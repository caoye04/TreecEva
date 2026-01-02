def calculate_final_score(log, config):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = 0

    for entry in log:
        if entry['type'] == 'success':
            base_score += entry['value'] * config['weight_success']
            bonus_tracker.append(entry['value'] // 10)
        elif entry['type'] == 'warning':
            penalty_adjustment -= entry['value'] * config['weight_warning']
        elif entry['type'] == 'error':
            penalty_adjustment -= entry['value'] * config['weight_error']

    # Irrelevant intermediate calculation (distractor)
    avg_bonus = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0
    temp_result = avg_bonus * 2.5

    # Secondary processing with dictionary lookup
    multiplier_key = 'multiplier_level_{}' .format(min(len(log), 3))
    scaling_factors = {
        'multiplier_level_1': 1.0,
        'multiplier_level_2': 1.2,
        'multiplier_level_3': 1.5
    }
    scaling_multiplier = scaling_factors.get(multiplier_key, 1.0)

    # Another irrelevant computation (dead code path)
    debug_value = 0
    if len(log) > 100:
        debug_value = sum(b ** 2 for b in bonus_tracker)

    # Final score computation (depends only on base_score, penalty, and scaling)
    raw_score = (base_score + penalty_adjustment) * scaling_multiplier
    final_score = int(round(raw_score))

    return final_score

# Simulation data
weights = {
    'weight_success': 1.1,
    'weight_warning': 0.8,
    'weight_error': 1.5
}

data_log = [
    {'type': 'success', 'value': 40},
    {'type': 'success', 'value': 60},
    {'type': 'warning', 'value': 10},
    {'type': 'error', 'value': 5},
    {'type': 'success', 'value': 25}
]

# Key execution point
final_score = calculate_final_score(data_log, weights)
print(f"Target result: {final_score}")