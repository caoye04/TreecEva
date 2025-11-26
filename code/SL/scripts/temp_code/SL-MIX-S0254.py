def process_data_values(data_input):
    # Distractor: complex but irrelevant string operations
    temp_str = 'computation_result_placeholder'
    processed_str = temp_str.upper().replace('_', '-').strip()
    str_length = len(processed_str)
    
    # Main logic path - data processing with multiple steps
    initial_sum = sum(data_input)
    processed_data = [x * 2 if x > 10 else x // 2 for x in data_input]
    
    # Misleading intermediate computation (unused)
    fake_metric = len([x for x in processed_data if x % 3 == 0]) * 7
    
    # Distractor: complex set operations that don't affect result
    value_set = set(processed_data)
    unique_count = len(value_set)
    overlapping = value_set.intersection({5, 10, 15})
    
    # Actual relevant computation
    filtered_values = [x for x in processed_data if x > 5]
    weighted_sum = sum(filtered_values) * 1.5
    
    # Dead code path with misleading calculations
    if str_length > 20:
        fake_adjustment = weighted_sum * 0.8
    else:
        fake_adjustment = weighted_sum * 1.2
    
    # Final result calculation
    final_result = int(weighted_sum) - unique_count
    return final_result

# Main execution
original_data = [8, 15, 22, 7, 18, 12, 9]
composite_score = process_data_values(original_data)

# Distractor: more irrelevant computations
sample_dict = {'a': 5, 'b': 10, 'c': 15}
dict_sum = sum(sample_dict.values())
string_slice = 'intervention_test'[3:11]

print(f"Target result: {composite_score}")