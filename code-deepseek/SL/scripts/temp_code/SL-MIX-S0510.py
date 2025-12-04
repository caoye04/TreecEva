def process_data_stream(data_points):
    # Initialize processing variables
    base_multiplier = 17
    offset_correction = 8
    
    # Distractor variables and operations
    temp_buffer = [x * 2 for x in range(5, 12)]
    unused_calibration = sum(temp_buffer) - 45
    misleading_counter = len([x for x in temp_buffer if x > 15])
    
    # Core processing logic with lambda
    transform_func = lambda x: (x ** 2) % 37 + offset_correction
    processed_values = [transform_func(point) for point in data_points]
    
    # Misleading intermediate calculation
    intermediate_sum = sum(processed_values) * 2 - 50
    
    # Dead code path
    if len(data_points) > 10:
        redundant_adjustment = intermediate_sum // 3
    else:
        redundant_adjustment = 0
    
    # Conditional computation with early return
    if len(processed_values) >= 3:
        core_result = (processed_values[0] * processed_values[2]) - processed_values[1]
        if core_result > 100:
            return core_result // base_multiplier
        else:
            return (core_result + offset_correction) * base_multiplier
    
    return -1

def compute_final_value():
    # Setup test data
    sample_points = [4, 7, 11, 3, 9]
    
    # Process main data
    main_result = process_data_stream(sample_points)
    
    # Additional distractor computations
    secondary_calc = sum([x % 5 for x in sample_points]) * 3
    misleading_aggregate = (main_result + secondary_calc) // 2
    
    # Key computation with bitwise operations
    bit_shift_value = (main_result << 2) & 0xFF
    
    # Final computation (answer target)
    final_computation = (bit_shift_value + main_result - secondary_calc) % 73
    
    # Print result for verification
    print(f"Result: {final_computation}")
    return final_computation

result = compute_final_value()