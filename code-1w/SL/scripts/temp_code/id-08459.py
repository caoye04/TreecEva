def calculate_final_score(data, weights):
    base_points = 0
    adjustment_factor = 0.0
    temp_sum = 0  # distractor: used in irrelevant computation
    offset_cache = {}  # semi-relevant: tracks offsets but not all are used

    for key, value in data.items():
        if value < 5:
            temp_sum += value ** 2  # dead computation branch
            continue
        base_points += value * 10

        # Irrelevant transformation
        transformed = (value + 3) * 2
        if transformed > 20:
            offset_cache[key] = transformed - 20

    # Distractor loop: computes unused metric
    outlier_count = 0
    for v in data.values():
        if v > 8:
            outlier_count += 1
    scale_hint = outlier_count * 1.5  # never used

    # Actual scoring logic
    weighted_bonus = 0
    for i, (k, w) in enumerate(weights.items()):
        if k in data and data[k] >= 5:
            weighted_bonus += w * (data[k] // 5)

    final_adjustment = 0
    for val in offset_cache.values():
        final_adjustment += val

    final_score = base_points + weighted_bonus * 2 + int(final_adjustment)

    return final_score

# Main execution
rank_data = {'player_A': 7, 'player_B': 4, 'player_C': 9, 'player_D': 6}
bonus_weights = {'player_A': 3, 'player_C': 5, 'player_D': 2, 'player_E': 4}  # player_E not in data

# Misleading preliminary calculations
aggregate = sum(rank_data.values()) * 2 - 5  # irrelevant
interim_metric = len(bonus_weights.keys()) * max(rank_data.values())  # unused

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Target result: {final_score}")