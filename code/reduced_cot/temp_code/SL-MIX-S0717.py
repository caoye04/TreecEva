def analyze_sensor_data(readings):
    # Initialize counters
    valid_count = 0
    temp_total = 0
    calibration_factor = 1.25
    debug_sum = 0
    
    # Process sensor readings
    for reading in readings:
        # Filter valid readings (within operational range)
        if 10 <= reading <= 90:
            valid_count += 1
            temp_total += reading
            debug_sum += reading * 2  # Distractor calculation
        
        # Redundant check for debugging
        if reading > 100:
            calibration_factor *= 1.1
    
    # Calculate average and apply processing
    if valid_count > 0:
        average_temp = temp_total / valid_count
        processed_data = average_temp * calibration_factor
        
        # Additional processing steps
        rounded_data = round(processed_data, 2)
        final_adjustment = rounded_data - (debug_sum % 5)  # Distractor operation
        
        return int(final_adjustment * 10)
    
    return 0

# Sensor data processing
sensor_readings = [25, 45, 67, 89, 12, 34, 78, 95, 102, 8, 56]
calibration_offset = 3.7  # Unused variable
backup_readings = [x for x in sensor_readings if x < 50]  # Unused list

result = analyze_sensor_data(sensor_readings)
final_count = result
print(f"Result: {final_count}")