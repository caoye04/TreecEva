def calculate_final_score(raw_data, limits):
    # Preprocess: filter valid entries based on threshold
    valid_entries = []
    invalid_count = 0
    temp_sum = 0

    for entry in raw_data:
        if 'value' not in entry or 'type' not in entry:
            invalid_count += 1
            continue
        if entry['value'] < limits['min'] or entry['value'] > limits['max']:
            invalid_count += 1
            continue
        valid_entries.append(entry)
        temp_sum += entry['value']

    # Misleading intermediate calculation (not used in final score)
    average_invalid_guess = temp_sum / (len(raw_data) + 1) if len(raw_data) > 0 else 0

    # Categorize entries by type using dictionary operations
    type_counts = {}
    for item in valid_entries:
        item_type = item['type']
        type_counts[item_type] = type_counts.get(item_type, 0) + 1

    # Apply bonus logic for rare types (appearing only once)
    rare_bonus = 0
    for item in valid_entries:
        if type_counts[item['type']] == 1:
            rare_bonus += 5

    # String-based flag processing (red herring)
    flags = ["A", "B", "C"]
    status_log = "Status: " + ", ".join(flags)
    debug_info = status_log.split(", ")
    # This string manipulation has no effect on result

    # Core scoring logic
    base_score = len(valid_entries) * 10
    outlier_penalty = 0
    sorted_values = sorted([item['value'] for item in valid_entries])
    mid = len(sorted_values) // 2
    median_value = sorted_values[mid] if mid % 2 == 1 else (sorted_values[mid-1] + sorted_values[mid]) / 2

    # Bitwise adjustment: use XOR to obscure logic slightly
    adjusted_median = median_value ^ 3  # deterministic but non-obvious

    # Final composition
    if adjusted_median > 50:
        final_score = base_score + rare_bonus - 7
    else:
        final_score = base_score + rare_bonus - 12

    return final_score

# Main execution
raw_dataset = [
    {'value': 25, 'type': 'X'},
    {'value': 45, 'type': 'Y'},
    {'value': 60, 'type': 'Z'},
    {'value': 70, 'type': 'Y'},
    {'value': 30, 'type': 'X'},
    {'extra_field': 'junk'}  # invalid, missing 'value'
]

default_thresholds = {'min': 20, 'max': 100}

# Dummy variables to increase cognitive load
placeholder_list = [i**2 for i in range(10)]
dummy_dict = {k: v for k, v in enumerate('abcdefghij')}
dummy_calc = sum(placeholder_list) / len(dummy_dict)

final_score = calculate_final_score(raw_dataset, default_thresholds)
print(f"Target result: {final_score}")