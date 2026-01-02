def calculate_performance(data_map):
    base_multiplier = 3
    temp_offset = 0
    cumulative_weight = 0
    adjustment_factor = 1.5  # unused red herring
    outlier_count = 0

    scores = [entry['value'] for entry in data_map if entry['active']]
    weights = []
    for i, val in enumerate(scores):
        if i % 3 == 0:
            weights.append(base_multiplier * 2)
        elif i % 3 == 1:
            weights.append(base_multiplier)
        else:
            weights.append(base_multiplier // 2)

    weighted_sum = 0
    total_influence = 0

    for idx, (score, weight) in enumerate(zip(scores, weights)):
        if score < 0:
            temp_offset += 1  # irrelevant tracking
            continue
        if score > 90:
            outlier_count += 1  # distractor: not used later
        contribution = score * weight * (1 + idx * 0.05)
        weighted_sum += contribution
        total_influence += weight * (1 + idx * 0.05)

    average_contribution = weighted_sum / total_influence if total_influence else 0

    # Secondary processing with redundant logic
    modifiers = [0.9, 1.1, 1.0, 0.95]
    trend_adjusted = average_contribution
    for mod in modifiers:
        trend_adjusted *= mod  # cyclic neutral adjustment

    # Final threshold logic
    if average_contribution > 75:
        final_rating = int(trend_adjusted * 1.2)
    else:
        final_rating = int(trend_adjusted)

    return final_rating

# Simulated benchmark dataset
dataset = [
    {'value': 85, 'active': True},
    {'value': 92, 'active': True},
    {'value': 76, 'active': True},
    {'value': 58, 'active': True},
    {'value': -5, 'active': True},  # invalid due to negative
    {'value': 88, 'active': True},
    {'value': 95, 'active': False}, # inactive, should be skipped
    {'value': 73, 'active': True}
]

intermediate_stats = {'count': len(dataset), 'peak': max(d['value'] for d in dataset)}
summary_flag = intermediate_stats['peak'] > 90

final_score = calculate_performance(dataset)
print(f"Result: {final_score}")