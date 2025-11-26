def analyze_sensor_data(readings):
    # Distractor: Initialize irrelevant tracking variables
    temp_sum = 0
    max_reading = -999
    calibration_factor = 1.25
    debug_flag = False
    
    # Distractor: Perform some unnecessary calculations
    for i in range(len(readings)):
        temp_sum += readings[i] * 2  # Misleading operation
        if readings[i] > max_reading:
            max_reading = readings[i]
    
    # Main logic: Process the actual data
    valid_readings = [r for r in readings if r % 3 == 0]
    processed_data = {}
    
    for idx, val in enumerate(valid_readings):
        # Distractor: Some dead code paths
        if idx > 10 and debug_flag:
            print(f"Debug: {val}")  # Never executes
        
        # Actual processing
        if val > 15:
            processed_data[val] = (val & 0x0F) | ((val >> 4) & 0x0F)
        else:
            processed_data[val] = val ^ 0b101010
    
    # More distractor operations
    avg_temp = temp_sum / len(readings) if readings else 0
    sensor_offset = max_reading * calibration_factor
    
    # Key computation: Calculate the actual result
    bit_operations = [v for k, v in processed_data.items() if k % 2 == 0]
    if bit_operations:
        final_result = sum(bit_operations) - (len(bit_operations) * 7)
    else:
        final_result = sensor_offset  # Dead code path
    
    # Final adjustments
    final_result = (final_result % 256) if final_result > 100 else final_result
    
    # Distractor: Unused conditional
    if avg_temp > 50:
        unused_var = avg_temp * 3  # Never used
    
    return final_result

# Test data
sensor_data = [12, 18, 24, 9, 15, 21, 6, 27, 33, 30, 3, 36]
result = analyze_sensor_data(sensor_data)
print(f"Result: {result}")