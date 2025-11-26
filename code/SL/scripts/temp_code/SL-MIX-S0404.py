def analyze_sensor_data(sensor_readings):
    # Process multiple sensor readings using zip and enumerate
    processed_values = []
    adjustment_factors = [0.8, 1.2, 0.9, 1.1, 1.0]
    
    # Main processing loop with zip
    for index, (reading, factor) in enumerate(zip(sensor_readings, adjustment_factors)):
        adjusted_value = reading * factor
        processed_values.append(adjusted_value)
    
    # Calculate statistics (some are distractors)
    max_reading = max(sensor_readings)
    min_reading = min(sensor_readings)
    total_sum = sum(sensor_readings)
    
    # Calculate weighted average using processed values
    weighted_avg = sum(processed_values) / len(processed_values)
    
    # Intermediate calculations (distractors)
    range_difference = max_reading - min_reading
    normalization_factor = total_sum / 100
    
    # Key calculation with processing
    base_value = weighted_avg * 2.5
    adjustment_offset = base_value % 10
    processing_result = int(weighted_avg) + len(processed_values)
    
    # Final statement
    final_calculation = processing_result + adjustment_offset
    
    print(f"Target result: {processing_result}")
    return processing_result

# Sensor readings from environmental monitoring system
sensor_data = [45, 38, 52, 41, 49]
result = analyze_sensor_data(sensor_data)