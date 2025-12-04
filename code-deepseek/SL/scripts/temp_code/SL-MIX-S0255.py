def validate_data_entries():
    data_stream = {'A': 15, 'B': 8, 'C': 22, 'D': 17, 'E': 9}
    validation_rules = {'min_threshold': 10, 'max_threshold': 20}
    
    # Primary validation processing
    valid_count = 0
    temp_sum = 0
    
    for key, value in data_stream.items():
        if value >= validation_rules['min_threshold'] and value <= validation_rules['max_threshold']:
            valid_count += 1
            temp_sum += value
        
        # Distractor calculation - doesn't affect final result
        redundant_check = value * 3 // 2
    
    # Intermediate processing with some distraction
    average_valid = temp_sum // valid_count if valid_count > 0 else 0
    deviation_calc = (temp_sum - average_valid * valid_count) ** 2
    
    # Main logic chain
    base_score = valid_count * 7
    adjustment_factor = (base_score % 13) + 3
    
    # Final computation
    total_validation = base_score + adjustment_factor
    
    # Final statement
    final_result = total_validation * 2 - 10
    
    print(f"Result: {total_validation}")
    return total_validation

validate_data_entries()