def analyze_sensor_data(sensor_readings):
    processed_samples = len(sensor_readings)
    calibration_offset = 2.5
    threshold = 15.0
    
    valid_count = 0
    temp_sum = 0
    max_reading = float('-inf')
    
    for i, reading in enumerate(sensor_readings):
        # Apply calibration offset (distractor - not used in final result)
        calibrated_reading = reading + calibration_offset
        temp_sum += calibrated_reading
        
        # Check if reading exceeds threshold
        if reading > threshold:
            valid_count += 1
        
        # Track maximum reading (distractor - not used in final result)
        if reading > max_reading:
            max_reading = reading
    
    # Calculate average (distractor - not used in final result)
    average_reading = temp_sum / processed_samples if processed_samples > 0 else 0
    
    # Calculate ratio of valid samples using conditional expression
    final_ratio = valid_count / processed_samples if processed_samples > 0 else 0
    
    # Slicing operations to analyze first and last segments (distractors)
    first_quarter = sensor_readings[:len(sensor_readings)//4]
    last_quarter = sensor_readings[3*len(sensor_readings)//4:]
    
    print(f"Result: {final_ratio}")
    return final_ratio

# Test data
sensor_data = [12.8, 18.2, 9.5, 22.1, 16.7, 25.3, 8.9, 19.6, 14.2, 27.8]
result = analyze_sensor_data(sensor_data)