def analyze_sensor_readings():
    raw_readings = [105, 92, 110, 88, 95, 120, 76, 83, 98, 101]
    threshold = 90
    
    # Normalize readings by subtracting baseline offset
    baseline_corrected = [x - 5 for x in raw_readings]
    
    # Identify valid readings above threshold after correction
    valid_readings = [x for x in baseline_corrected if x > threshold]
    
    # Apply calibration factor conditionally using conditional expression
    calibrated_readings = [val * 1.1 if val > 100 else val for val in valid_readings]
    
    # Slice to exclude potential outlier (last reading)
    processed_data = calibrated_readings[:-1] if len(calibrated_readings) > 3 else calibrated_readings
    
    # Filter again based on secondary criterion
    filtered_data = [x for x in processed_data if x % 2 == 0]
    
    # Final aggregation
    filtered_sum = sum(filtered_data)
    
    # Irrelevant distraction: unused variable
    peak_value = max(raw_readings) if raw_readings else 0
    
    return filtered_sum

result = analyze_sensor_readings()
print(f"Result: {result}")