def calculate_final_score(records, importance):
    base = 0
    bonus_tracker = {key: 0 for key in importance}
    penalty_offset = len(records) * 0.1
    temp_result = []

    for record in records:
        raw_value = record['value']
        category = record['category']
        normalized = raw_value / (sum(importance.values()) + 1)

        if category in importance:
            weighted = normalized * importance[category]
            base += weighted

            # Irrelevant accumulation (distractor)
            bonus_tracker[category] += raw_value % 7

        # Dead code path (conditional never met in input)
        if raw_value < 0:
            temp_result.append(-raw_value)

    # Lambda used for dynamic threshold (semi-relevant)
    adjust = lambda x: x * 1.5 if x > 5 else x * 0.8
    adjusted_base = adjust(base)

    # Complex but non-impacting computation
    outlier_check = [v for v in bonus_tracker.values() if v > 10]
    stability_factor = 1.0
    if len(outlier_check) == 0:
        stability_factor = 1.1

    # Final score calculation with distraction variables
    inflation_rate = 0.05
    final_score = int(adjusted_base * stability_factor - penalty_offset)

    return final_score

# Input data
weights = {'alpha': 3, 'beta': 2, 'gamma': 4}
data = [
    {'value': 14, 'category': 'alpha'},
    {'value': 21, 'category': 'beta'},
    {'value': 8, 'category': 'gamma'},
    {'value': 17, 'category': 'alpha'},
    {'value': 12, 'category': 'gamma'}
]

# Execution
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")