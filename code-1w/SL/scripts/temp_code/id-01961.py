def calculate_rating(contribs, penalties):
    base_score = 0
    adjustment_factor = 0.85
    temp_buffer = []
    legacy_multiplier = 1.2  # Unused in current logic
    decay_rate = 0.95

    for key in sorted(contribs.keys()):
        raw_value = contribs[key]
        if raw_value > 50:
            tier_bonus = 10
        elif raw_value > 30:
            tier_bonus = 5
        else:
            tier_bonus = 0

        adjusted_val = raw_value * adjustment_factor + tier_bonus
        if key in penalties:
            adjusted_val -= penalties[key]

        smoothed_val = round(adjusted_val * decay_rate, 2)
        temp_buffer.append(smoothed_val)

    aggregate = sum(temp_buffer)

    outlier_count = 0
    for val in temp_buffer:
        if val < 10:
            outlier_count += 1

    # Irrelevant filtering path
    filtered_results = [v for v in temp_buffer if v > 15]
    ignored_sum = sum(filtered_results)  # Not used later

    final_normalization = 1.0
    if len(temp_buffer) > 3:
        final_normalization = 0.97

    return int(aggregate * final_normalization)

# Main execution context
contributions = {
    'task_alpha': 65,
    'task_beta': 42,
    'task_gamma': 58,
    'task_delta': 33,
    'task_epsilon': 70
}

penalty_map = {
    'task_beta': 3,
    'task_delta': 5,
    'task_gamma': 2
}

intermediate_total = 0
for val in contributions.values():
    intermediate_total += val ** 0.5  # Distractor computation

scaling_constant = 2.1
buffer_memory = [0] * 10  # Simulated pre-allocation, unused

final_score = calculate_rating(contributions, penalty_map)
print(f"Result: {final_score}")