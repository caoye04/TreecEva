def calculate_final_score(entries, limits):
    base_points = 0
    bonus_tally = 0
    penalty_counter = 0
    temp_aggregate = 0  # distractor: used in dead logic

    # Dead code path (distractor)
    if len(entries) > 100:
        temp_aggregate += sum([x * 0.1 for x in range(10)])

    for entry in entries:
        magnitude = entry.get('value', 0)
        category = entry.get('type')
        isActive = entry.get('active', True)

        # Irrelevant filtering (distractor)
        if magnitude < 0:
            penalty_counter += 1
            continue

        # Core scoring logic
        if isActive:
            if category == 'A':
                base_points += magnitude * 2
                if magnitude > limits['A']:
                    bonus_tally += 5
            elif category == 'B':
                base_points += magnitude
                if magnitude > limits['B']:
                    bonus_tally += 3
            else:
                base_points += max(magnitude - 10, 0)

        # Semi-relevant but non-impacting computation
        adjustment = (magnitude // 5) if category != 'X' else 0
        temp_aggregate += adjustment  # distractor accumulation

    # Another distraction: unused helper expression
    outlier_flag = any([e.get('value', 0) > 200 for e in entries])

    # Final score calculation — only base_points and bonus_tally matter
    final_computation = base_points + bonus_tally

    return final_computation


# Main execution
config_thresholds = {'A': 50, 'B': 75}
data_entries = [
    {'value': 60, 'type': 'A', 'active': True},
    {'value': 80, 'type': 'B', 'active': True},
    {'value': 40, 'type': 'A', 'active': True},
    {'value': 90, 'type': 'C', 'active': True},
    {'value': 55, 'type': 'B', 'active': False},  # inactive, won't contribute
    {'value': 70, 'type': 'A', 'active': True},
]

intermediate_sum = sum([item['value'] for item in data_entries if item['type'] != 'B'])  # distractor
scaling_factor = 1.0 if intermediate_sum > 100 else 0.9  # irrelevant to final result

final_score = calculate_final_score(data_entries, config_thresholds)
print(f"Result: {final_score}")