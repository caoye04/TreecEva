def calculate_final_score(data_map):
    base_value = 0
    adjustment_factor = 1.5
    temp_sum = 0
    outlier_count = 0  # tracking unused metric

    for key, values in data_map.items():
        if len(values) == 0:
            continue
        
        # Irrelevant computation: statistical dispersion (not used)
        mean_val = sum(values) / len(values)
        variance = sum((x - mean_val) ** 2 for x in values) / len(values)
        std_dev = variance ** 0.5
        
        # Semi-relevant normalization (only max matters)
        normalized_peaks = [x / (mean_val + 1) for x in values if x > mean_val]
        
        # Key logic: track maximum value across all lists
        local_max = max(values)
        
        # Conditional expression (required feature)
        base_value += local_max if key.startswith('valid_') else 0
        
        # Dead code path: never affects final result
        if std_dev > 100:
            outlier_count += 1

    # Another red herring variable
    compression_ratio = 0.87
    scaling_offset = adjustment_factor * 2.0  # unused

    # Actual score calculation
    penalty = 3 * (len(data_map) - 2)  # depends on number of entries
    final_score = int(base_value - penalty)

    return final_score

# Main execution
config_flags = {'debug': False, 'log_level': 1}  # irrelevant global
aux_data = [x**2 for x in range(15) if x % 3 != 0]  # distractor list

# Input map with meaningful structure
data_map = {
    'valid_input_a': [12, 18, 23, 7],
    'valid_input_b': [5, 29, 14],
    'invalid_legacy': [99, 101],  # won't contribute due to key name
    'valid_input_c': [8, 41, 30, 22]
}

intermediate_check = sum(aux_data) / len(aux_data)  # distraction

final_score = calculate_final_score(data_map)
print(f"Result: {final_score}")