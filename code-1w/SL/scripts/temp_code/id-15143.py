def calculate_final_score(items, importance_weights):
    # Initialize tracking variables
    total_contributions = 0
    penalty_adjustments = 0
    temp_buffer = []

    # Irrelevant pre-processing: normalize weights (not actually used in final logic)
    normalized_weights = [w / sum(importance_weights) for w in importance_weights]

    # Main processing loop with nested conditions
    for i, item in enumerate(items):
        base_value = item.get('value', 0)
        category = item.get('category', 'unknown')
        multiplier = importance_weights[i % len(importance_weights)]

        # Compute contribution with conditional modifiers
        if category == 'critical':
            raw_contribution = base_value * multiplier * 1.2
        elif category == 'optional':
            raw_contribution = base_value * multiplier * 0.8
        else:
            raw_contribution = base_value * multiplier

        # Accumulate only non-zero contributions
        if raw_contribution > 0:
            total_contributions += raw_contribution
            temp_buffer.append(raw_contribution)

        # Simulate stateful adjustment (distractor logic)
        if i % 3 == 0:
            penalty_adjustments -= 0.5  # Minor irrelevant decrement

    # Secondary analysis on buffer (semi-relevant)
    filtered_peaks = [x for x in temp_buffer if x > sum(temp_buffer) / len(temp_buffer)]
    peak_bonus = len(filtered_peaks) * 1.5

    # Dummy statistic collection (dead code path - never used)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    outlier_count = sum(1 for x in temp_buffer if x > avg_temp * 2)

    # Final score computation - only total_contributions and peak_bonus matter
    final_result = total_contributions + peak_bonus + penalty_adjustments
    return int(final_result)

# Input data setup
input_data = [
    {'value': 10, 'category': 'standard'},
    {'value': 15, 'category': 'critical'},
    {'value': 5, 'category': 'optional'},
    {'value': 20, 'category': 'standard'},
    {'value': 8, 'category': 'critical'},
    {'value': 12, 'category': 'standard'}
]

weights = [2, 3, 1]

# Execution point of interest
final_score = calculate_final_score(input_data, weights)
print(f"Target result: {final_score}")