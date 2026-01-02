def analyze_sensor_data():
    raw_readings = [105, 23, 78, 91, 47, 150, 64, 88, 120]
    offset_adjustment = 5
    adjusted_readings = [x - offset_adjustment for x in raw_readings]
    
    # Irrelevant diagnostic flag (distractor)
    system_diagnostic_pass = len(adjusted_readings) > 5
    
    outlier_threshold = 110
    valid_range_min = 30
    
    # Filter readings within normal operating range
    filtered_measurements = [val for val in adjusted_readings if valid_range_min <= val <= outlier_threshold]
    
    # Use lambda to compute adjustment factor (real computation path)
    adjustment_factor = (lambda x: 0.95 if x > 100 else 1.0)(len(filtered_measurements))
    
    # Final score before scaling
    filtration_score = sum(filtered_measurements)
    
    # Apply scaling (not affecting the target variable)
    scaled_result = filtration_score * adjustment_factor
    
    # Another irrelevant set operation (distractor)
    unique_values = set(filtered_measurements)
    stability_index = len(unique_values) // 2
    
    print(f"Result: {filtration_score}")

analyze_sensor_data()