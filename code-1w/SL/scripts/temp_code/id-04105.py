def calculate_final_score(data, thresholds):
    # Preprocess: filter valid entries based on string pattern
    valid_entries = []
    temp_sum = 0
    outlier_count = 0

    for item in data:
        if not isinstance(item['value'], (int, float)):
            continue
        if item['status'].lower().strip() != 'active':
            continue
        if 'xyz' in item['code'].lower():  # distractor: irrelevant substring check
            temp_sum += item['value'] * 0.1
        valid_entries.append(item)

    # Compute base metrics
    base_total = sum(entry['value'] for entry in valid_entries)
    entry_count = len(valid_entries)
    average_value = base_total / entry_count if entry_count > 0 else 0

    # Threshold filtering with slicing distraction
    sorted_values = sorted([e['value'] for e in valid_entries])
    mid_slice = sorted_values[1:-1]  # Remove min and max (trimming outliers)
    trimmed_average = sum(mid_slice) / len(mid_slice) if mid_slice else 0

    # Dummy dictionary operations for distraction
    stats = {
        'count': entry_count,
        'raw_total': base_total,
        'temp_sum_ignored': temp_sum,
        'outliers_removed': outlier_count
    }
    stats.update({'version': '2.1'})  # red herring update

    # Apply threshold multipliers using conditional logic
    multiplier = 1.0
    if trimmed_average > thresholds['high']:
        multiplier = 1.5
    elif trimmed_average > thresholds['medium']:
        multiplier = 1.2
    elif trimmed_average > thresholds['low']:
        multiplier = 1.1
    else:
        multiplier = 0.9

    # Secondary adjustment based on code prefixes (string method usage)
    prefix_bonus = 0
    for entry in valid_entries:
        if entry['code'].startswith('A') and entry['code'].endswith('Z'):
            prefix_bonus += 5

    # Final score calculation
    preliminary_score = trimmed_average * multiplier
    final_score = preliminary_score + prefix_bonus

    # Dead code path - never executed due to logic above
    if len(valid_entries) == 0 and False:
        final_score = -999

    return final_score

# Input data
input_data = [
    {'value': 100, 'status': 'Active ', 'code': 'ABC123'},
    {'value': 150, 'status': 'inactive', 'code': 'DEF456'},
    {'value': 200, 'status': 'Active', 'code': 'AXYZ789'},
    {'value': 50,  'status': 'Active', 'code': 'AXYZZ'}
]

tuning_thresholds = {
    'low': 80,
    'medium': 120,
    'high': 180
}

# Execution point of interest
final_score = calculate_final_score(input_data, tuning_thresholds)
print(f"Target result: {final_score}")