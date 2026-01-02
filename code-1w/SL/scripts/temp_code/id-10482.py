def analyze_sensor_data():
    raw_readings = [105, 92, -5, 117, 99, 100, -1, 94]
    calibration_offset = 3
    adjusted_readings = [x + calibration_offset for x in raw_readings]
    
    # Define valid range and collect valid entries
    min_threshold = 95
    max_threshold = 115
    valid_entries = []
    for val in adjusted_readings:
        if min_threshold <= val <= max_threshold:
            valid_entries.append(val)
    
    # Irrelevant distraction: unused set operation
    outlier_set = {x for x in adjusted_readings if x < min_threshold or x > max_threshold}
    
    filtered_sum = sum(valid_entries)
    return filtered_sum

result = analyze_sensor_data()
print(f"Result: {result}")