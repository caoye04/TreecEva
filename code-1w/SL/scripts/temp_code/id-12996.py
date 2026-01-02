def analyze_sensor_readings():
    raw_readings = [105, 92, 97, 110, 88, 95, 103, 98, 100, 107, 94, 102]
    calibration_offset = 5
    adjusted_readings = [x + calibration_offset for x in raw_readings]
    
    # Misleading computation: temperature conversion (not used)
    celsius_readings = [(x - 32) * 5/9 for x in raw_readings]
    average_celsius = sum(celsius_readings) / len(celsius_readings)
    
    # Simulate noise detection with slicing
    early_window = adjusted_readings[:5]
    late_window = adjusted_readings[-5:]
    noise_candidates = set(early_window).symmetric_difference(set(late_window))
    
    # Actual processing path
    valid_range = set(range(95, 110))
    cleaned_data = [x for x in adjusted_readings if x in valid_range]
    
    # Red herring: sorting and reversing (doesn't affect sum)
    sorted_cleaned = sorted(cleaned_data)
    reversed_cleaned = sorted_cleaned[::-1]
    
    # Key operation
    filtered_data = [x for x in reversed_cleaned if x % 2 == 0]
    filtered_sum = sum(filtered_data)
    
    # Dead code branch (never executed)
    if False:
        outlier_count = len(raw_readings) - len(cleaned_data)
        filtered_sum += outlier_count
    
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()