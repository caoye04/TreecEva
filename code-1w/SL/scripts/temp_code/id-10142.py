def analyze_sensor_readings():
    raw_readings = [105, 230, 98, 412, 376, 89, 114, 295, 401, 76]
    offset = 50
    adjusted_readings = [x - offset for x in raw_readings]
    processed_data = [x * 1.1 for x in adjusted_readings if x > 100]
    
    # Irrelevant auxiliary variable (minor distraction)
    diagnostic_flag = len(processed_data) > 5
    
    threshold = 150
    filtered_sum = sum([x for x in processed_data if x > threshold])
    
    # Additional benign operation
    normalized_value = round(filtered_sum / 100, 2)
    
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()