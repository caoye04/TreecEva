def analyze_pattern_sequence(data_points):
    temp_sum = sum(data_points)
    pattern_index = len(data_points) // 2
    return temp_sum * pattern_index

def filter_valid_patterns(sequence):
    threshold = 15
    filtered = [x for x in sequence if x % 2 == 0 and x > threshold]
    misleading_count = len(filtered) * 3  # Distractor computation
    return filtered, misleading_count

def process_sequence_patterns(main_data, aux_data):
    primary_sum = sum(main_data)
    aux_sum = sum(aux_data)
    
    # Irrelevant intermediate calculations
    temp_product = primary_sum * aux_sum
    offset_adjustment = temp_product % 7  # Never used
    
    filtered_main, dummy = filter_valid_patterns(main_data)
    filtered_aux, another_dummy = filter_valid_patterns(aux_data)
    
    # Distractor operations that don't affect final result
    combined_length = len(filtered_main) + len(filtered_aux)
    pattern_multiplier = combined_length * 2  # Misleading calculation
    
    # Key logic chain
    processed_main = analyze_pattern_sequence(filtered_main)
    processed_aux = analyze_pattern_sequence(filtered_aux)
    
    final_count = processed_main + processed_aux
    return final_count

# Main execution
primary_data = [8, 12, 16, 20, 24, 28, 32]
secondary_data = [10, 14, 18, 22, 26, 30]

# Irrelevant computations that don't affect the answer
preliminary_check = len(primary_data) == len(secondary_data)  # False but unused
backup_calculation = (sum(primary_data) + sum(secondary_data)) // 5  # Dead code path

result = process_sequence_patterns(primary_data, secondary_data)
final_sequence_count = result

print(f"Target result: {final_sequence_count}")