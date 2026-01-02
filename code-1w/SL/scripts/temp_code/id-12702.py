def calculate_performance(data):
    base_points = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0
    temp_result = 0
    intermediate_values = []

    for entry in data:
        raw_score = entry['value'] * entry['weight']
        if entry['type'] == 'critical':
            base_points += raw_score * 1.5
        elif entry['type'] == 'standard':
            base_points += raw_score
        else:
            base_points += raw_score * 0.8

        # Irrelevant string processing (distractor)
        status_msg = f"Processing {entry['name']}..."
        status_flag = 'OK' if 'high' in status_msg.lower() else 'INFO'
        _ = len(status_flag)  # Dead computation

        # Collect intermediate but not directly used values
        intermediate_values.append(raw_score ** 0.5)

    # Sorting has no effect on final result (distractor)
    sorted_intermediates = sorted(intermediate_values, reverse=True)
    trimmed = sorted_intermediates[1:-1]  # Remove outliers (unused)

    # Conditional expression for bonus (used)
    bonus_multiplier = 1.2 if base_points > 200 else (1.1 if base_points > 150 else 1.0)

    # Additional red herring: unused penalty logic
    for val in intermediate_values:
        if val > 20:
            penalty_adjustment -= 5
        elif val < 5:
            penalty_adjustment += 2

    # Final score calculation (key line)
    final_score = base_points * bonus_multiplier

    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Input data
benchmark_data = [
    {'name': 'TaskA', 'value': 40, 'weight': 2.0, 'type': 'critical'},
    {'name': 'TaskB', 'value': 30, 'weight': 3.0, 'type': 'standard'},
    {'name': 'TaskC', 'value': 25, 'weight': 2.5, 'type': 'standard'},
    {'name': 'TaskD', 'value': 50, 'weight': 1.8, 'type': 'critical'},
    {'name': 'TaskE', 'value': 20, 'weight': 1.5, 'type': 'optional'}
]

# Execution point
final_score = calculate_performance(benchmark_data)