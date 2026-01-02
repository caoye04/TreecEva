def analyze_sensor_readings():
    raw_readings = [105, 23, 78, 91, 64, 50, 85, 99, 44, 72]
    offset = 10
    adjusted_readings = [x - offset for x in raw_readings]
    processed_data = [x * 1.1 for x in adjusted_readings]
    
    # Irrelevant variable (mild distraction)
    calibration_factor = 0.98
    
    threshold = 80.0
    filtered_sum = sum([x for x in processed_data if x > threshold])
    
    # Additional benign computation
    average_value = sum(processed_data) / len(processed_data)
    
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()