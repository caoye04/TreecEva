def evaluate_performance(feedback):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []

    # Irrelevant list for distraction
    irrelevant_logs = [f'log_{i}' for i in range(10)]

    # Misleading computation that doesn't affect final result
    temp_aggregate = sum([len(log) for log in irrelevant_logs]) % 7

    for category, entries in feedback.items():
        category_total = 0
        category_bonus = 0

        for entry in entries:
            raw_value = entry['rating']
            multiplier = entry.get('multiplier', 1)
            weighted = raw_value * multiplier
            category_total += weighted

            if raw_value >= 4:
                category_bonus += 1

            # Dead code path — never executed due to logic, but looks relevant
            if raw_value < 0:
                raise ValueError("Ratings cannot be negative")  # unreachable

        base_score += category_total

        if category_bonus >= 2:
            bonus_tracker.append(category_bonus * 1.5)

    # Another misleading intermediate calculation
    phantom_offset = len(irrelevant_logs) - temp_aggregate  # unused later

    adjustment_factor = 0
    for i in range(len(bonus_tracker)):
        adjustment_factor += bonus_tracker[i]

    # Actual key computation
    final_score = int(base_score + adjustment_factor)

    # Distractor: unused normalization attempt
    if base_score > 0:
        normalized = (final_score / base_score) * 100  # not used

    return final_score


# Data setup
feedback_map = {
    'usability': [
        {'rating': 5, 'multiplier': 1.2},
        {'rating': 4, 'multiplier': 1.0},
        {'rating': 3, 'multiplier': 0.8}
    ],
    'performance': [
        {'rating': 4, 'multiplier': 1.1},
        {'rating': 5, 'multiplier': 1.3},
        {'rating': 2, 'multiplier': 0.9}
    ],
    'design': [
        {'rating': 3, 'multiplier': 1.0},
        {'rating': 4, 'multiplier': 1.0},
        {'rating': 4, 'multiplier': 1.0}
    ]
}

# Execution point of interest
final_score = evaluate_performance(feedback_map)

print(f"Result: {final_score}")