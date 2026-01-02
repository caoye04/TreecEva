def calculate_final_score(raw_data, limits):
    # Preprocessing: filter valid entries
    valid_entries = set()
    temp_sum = 0
    outlier_count = 0

    for val in raw_data:
        if val < limits['min'] or val > limits['max']:
            outlier_count += 1
        else:
            valid_entries.add(val)
            temp_sum += val

    # Secondary analysis: detect symmetry pattern (irrelevant to final score)
    max_val = max(valid_entries)
    min_val = min(valid_entries)
    range_center = (max_val + min_val) / 2
    symmetric_matches = 0
    for v in valid_entries:
        if (range_center * 2 - v) in valid_entries:
            symmetric_matches += 1

    # Compute base metrics
    base_average = temp_sum / len(valid_entries) if valid_entries else 0
    variance_proxy = sum((x - base_average) ** 2 for x in valid_entries) / len(valid_entries) if valid_entries else 0

    # Apply weighting factors (only some are used)
    weight_a = 0.85
    weight_b = 1.15
    weight_c = 0.5  # unused distractor

    adjusted_avg = base_average * weight_a if variance_proxy < 200 else base_average * weight_b

    # Bonus logic based on set size and divisibility
    size_bonus = 0
    sorted_vals = sorted(valid_entries)
    for i in range(len(sorted_vals)):
        if sorted_vals[i] % 7 == 0 and sorted_vals[i] != 7:
            size_bonus += 1

    # Final scoring logic
    penalty = 2 * outlier_count
    final_score = int(adjusted_avg + size_bonus * 3 - penalty)

    # Dead code path - never executed under current logic
    if len(valid_entries) > 1000:
        scaling_factor = 1.5
        final_score = int(final_score * scaling_factor)

    return final_score

# Main execution context
data_set = [14, 21, 28, 35, 42, 13, 17, 19, 23, 49, 51, 53]
thresholds = {'min': 10, 'max': 60}

# Extraneous variables (distractors)
dummy_list = [x ** 2 for x in data_set if x % 3 == 0]
placeholder_dict = {k: v for k, v in enumerate(sorted(dummy_list, reverse=True))}
bitwise_flag = 0b1010 ^ 0b1100 & 0b1111  # irrelevant XOR/AND operation

# Key computation
final_score = calculate_final_score(data_set, thresholds)

print(f"Result: {final_score}")