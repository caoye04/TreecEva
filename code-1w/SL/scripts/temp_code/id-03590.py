def process_results(data, limit):
    # Irrelevant tracking variables (distractors)
    total_entries = len(data)
    temp_sum = sum([v['value'] for v in data])
    avg_value = temp_sum / total_entries if total_entries else 0

    # Misleading pre-processing with slicing that isn't used later
    sorted_values = sorted([item['value'] for item in data], reverse=True)
    top_half_slice = sorted_values[:len(sorted_values)//2]
    filtered_names = [item['name'] for item in data if item['active']]

    # Actual logic begins: count how many exceed limit and have valid status
    valid_count = 0
    penalty_adjustment = 0

    status_map = {k: idx for idx, k in enumerate(['active', 'pending', 'suspended'])}

    for record in data:
        value = record['value']
        status = record['status']
        active_flag = record['active']

        # Conditional expression with modular arithmetic side check
        if value > limit and status in status_map and status != 'suspended':
            valid_count += 1
            # Extra computation that may or may not affect final result
            mod_adjust = value % 7
            if mod_adjust > 4:
                penalty_adjustment -= 1
            else:
                penalty_adjustment += 1

    # Linear search through names for a rare condition (mostly irrelevant)
    rare_names = []
    for entry in data:
        if 'x' in entry['name'].lower() or 'z' in entry['name'].lower():
            rare_names.append(entry['name'])

    # Final score calculation — only valid_count and penalty_adjustment matter
    base_score = valid_count * 13
    final_score = base_score + penalty_adjustment

    # Dead code path: never executed due to logic above
    if len(rare_names) > 100:
        final_score *= 2

    return final_score

# Input data setup
assessment_data = [
    {'name': 'alpha', 'value': 23, 'status': 'active', 'active': True},
    {'name': 'beta', 'value': 15, 'status': 'pending', 'active': True},
    {'name': 'gamma', 'value': 8, 'status': 'suspended', 'active': False},
    {'name': 'delta', 'value': 31, 'status': 'active', 'active': True},
    {'name': 'epsilon', 'value': 12, 'status': 'active', 'active': True},
    {'name': 'zeta', 'value': 45, 'status': 'pending', 'active': True},
    {'name': 'eta', 'value': 38, 'status': 'active', 'active': True}
]

threshold = 20
final_score = process_results(assessment_data, threshold)
print(f"Result: {final_score}")