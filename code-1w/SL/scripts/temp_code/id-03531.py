def process_sensor_data():
    raw_readings = [23.5, 17.2, 45.8, 12.1, 9.0, 36.3, 41.7, 8.5]
    offset = 5.0
    adjusted_readings = [x + offset for x in raw_readings]
    
    # Apply nonlinear calibration using a lambda function
    calibrated_map = lambda val: round(val ** 0.5 * 2, 2)
    mapped_values = list(map(calibrated_map, adjusted_readings))
    
    # Threshold for significant activity
    threshold = 10.0
    inactive_count = len([x for x in mapped_values if x <= threshold])  # distractor
    
    # Key computation step
    filtered_sum = sum(filter(lambda x: x > threshold, mapped_values))
    
    # Additional unrelated tracking
    status_flags = {"low": 0, "medium": 1, "high": 2}
    mode = "high"
    
    # Output the target result
    print(f"Result: {filtered_sum}")

process_sensor_data()