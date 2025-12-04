def process_data_points():
    # Initialize data points with tuples
    sensor_readings = [(12, 5), (8, 3), (15, 7), (6, 2)]
    calibration_offsets = [1, -2, 0, 3]
    
    # Process readings using list comprehension with conditional expression
    processed_readings = [
        (x + offset if x > 10 else x - offset) 
        for (x, y), offset in zip(sensor_readings, calibration_offsets)
    ]
    
    # Distractor computation (not used in final result)
    temp_sum = sum(x + y for x, y in sensor_readings)
    
    # Apply bitwise XOR operations
    xor_result = 0
    for val in processed_readings:
        xor_result ^= val
    
    # Final computation with additional distractor
    scaling_factor = 2.5
    intermediate = xor_result * scaling_factor
    
    # Unnecessary transformation (distractor)
    transformed = [(x & 0xF) | (x >> 4) for x in processed_readings]
    
    # The actual result computation
    final_result = int(intermediate % 100)
    
    return final_result

def result_computation():
    result = process_data_points()
    print(f"Target result: {result}")
    return result

# Execute the computation
result_computation()