def analyze_sensor_data():
    raw_readings = [101, 105, 98, 110, 102, 95, 108, 103, 99, 111]
    threshold = 100
    adjustment_factor = 0.9
    
    # Apply calibration adjustment using list comprehension
    calibrated_readings = [int(x * adjustment_factor) for x in raw_readings]
    
    # Identify readings that exceed recalibrated threshold
    filtered_readings = [x for x in calibrated_readings if x > threshold]
    
    # Perform integrity check (irrelevant to final result but adds minor distraction)
    total_readings = len(calibrated_readings)
    valid_percentage = (len(filtered_readings) / total_readings) * 100
    
    # Key computation step
    filtration_score = sum(filtered_readings)
    
    # Debug print (not affecting logic)
    debug_info = f"Valid: {len(filtered_readings)}, Score: {filtration_score}"
    
    print(f"Result: {filtration_score}")

analyze_sensor_data()