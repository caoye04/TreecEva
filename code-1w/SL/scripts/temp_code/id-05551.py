def analyze_sensor_readings():
    raw_readings = [102, 95, 110, 87, 98, 103, 91, 115, 89, 107]
    offset = 5
    adjusted_readings = [x - offset for x in raw_readings]
    
    calibration_factor = 1.1
    calibrated_readings = [round(x * calibration_factor) for x in adjusted_readings]
    
    outlier_limit = 100
    cleaned_data = [x for x in calibrated_readings if x < outlier_limit]
    
    base_threshold = 95
    adjustment_ratio = 0.9
    dynamic_threshold = base_threshold * adjustment_ratio
    
    processed_data = [x + 1 for x in cleaned_data]
    threshold = int(dynamic_threshold)
    filtered_sum = sum([x for x in processed_data if x > threshold])
    
    # Irrelevant tracking variables (minimal distraction)
    reading_count = len(raw_readings)
    avg_value = sum(processed_data) / len(processed_data) if processed_data else 0
    
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()