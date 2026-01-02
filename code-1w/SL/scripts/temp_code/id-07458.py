def calculate_final_score(data, weights):
    # Initialize tracking variables
    base_points = 0
    adjustment_factor = 0.0
    temp_buffer = []
    rank_sum = 0
    weight_multiplier = 1.0

    # Irrelevant pre-processing: simulate data validation
    for key in weights:
        if key.startswith('temp'):
            adjustment_factor += weights[key] * 0.1

    # Core logic: process valid ranks and apply weighted bonuses
    valid_entries = {}
    for k, v in data.items():
        if v['rank'] > 0 and v['active']:
            base_points += v['rank']
            rank_sum += v['rank']
            temp_buffer.append(v['rank'] * 0.5)  # unused later
            if 'bonus' in v:
                valid_entries[k] = v['bonus']

    # Apply sorting to emphasize top performers
    sorted_bonuses = sorted(valid_entries.values(), reverse=True)
    bonus_stack = set(sorted_bonuses)  # used only for membership check

    # Compute dynamic multiplier based on bonus diversity
    if len(bonus_stack) >= 3:
        weight_multiplier = 1.25
    else:
        weight_multiplier = 0.9

    # Additional distraction: simulate threshold filtering
    thresholds = [0.8, 1.0, 1.2]
    for t in thresholds:
        if weight_multiplier > t:
            break

    # Final score computation
    bonus_contribution = 0
    for i, b in enumerate(sorted_bonuses):
        if i % 2 == 0:
            bonus_contribution += b * weight_multiplier
        else:
            bonus_contribution += b * 0.8

    final_score = int((base_points + bonus_contribution) * weight_multiplier)

    # Dead code branch (never executed due to data)
    if adjustment_factor > 100:
        final_score *= 2

    return final_score

# Main execution block
rank_data = {
    'player_1': {'rank': 5, 'active': True, 'bonus': 10},
    'player_2': {'rank': 3, 'active': True, 'bonus': 15},
    'player_3': {'rank': 0, 'active': False, 'bonus': 20},  # inactive, skipped
    'player_4': {'rank': 4, 'active': True, 'bonus': 15},
    'player_5': {'rank': 2, 'active': True, 'bonus': 10},
    'temp_player': {'rank': 1, 'active': True, 'bonus': 5}
}

bonus_weights = {
    'w1': 2,
    'w2': 4,
    'temp_debug': 5  # affects adjustment_factor slightly
}

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Target result: {final_score}")