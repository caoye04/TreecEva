def calculate_sensor_readings(calibration_values):
    # Initialize sensor data processing
    raw_readings = [45, 78, 92, 33, 67, 84, 29, 51, 76, 88]
    filtered_readings = []
    
    # Process calibration offsets (distractor)
    calibration_sum = sum(calibration_values)
    offset_factor = calibration_sum // len(calibration_values)
    
    # Apply filtering logic
    for reading in raw_readings:
        if reading > 50 and reading < 90:
            filtered_readings.append(reading)
    
    # Calculate average (distractor path)
    if len(filtered_readings) > 0:
        avg_reading = sum(filtered_readings) / len(filtered_readings)
    else:
        avg_reading = 0
    
    # Create primary data set
    primary_set = set(filtered_readings)
    primary_set.add(67)  # Add calibration anchor
    primary_set.discard(33)  # Remove outlier
    
    # Create secondary set with overlapping values
    secondary_set = {78, 84, 92, 45, 51}
    
    # Main computation
    intermediate = len(primary_set.intersection(secondary_set))
    scale_factor = (intermediate * 3) % 7
    
    # Final calculation with string manipulation
    result_str = str(scale_factor * 11)
    numeric_base = int(result_str[:2]) if len(result_str) >= 2 else 0
    
    # Key operation
    final_result = len(primary_set.difference(secondary_set))
    
    # Print result
    print(f"Result: {final_result}")

# Execute with calibration values
calibration_data = [12, 8, 15, 6, 9]
calculate_sensor_readings(calibration_data)