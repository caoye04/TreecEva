def analyze_sensor_data():
    raw_readings = [105, 231, 98, 412, 305, 229, 56, 88, 192]
    
    # Normalize readings to baseline range
    normalized = [x / 10 for x in raw_readings]
    
    # Identify stable metrics using threshold logic
    stable_threshold = 25.0
    high_metrics = [val for val in normalized if val > stable_threshold]
    low_metrics = [val for val in normalized if val < 100.0]
    
    # Compute overlap via set intersection
    valid_set = set(high_metrics) & set(low_metrics)
    sorted_metrics = sorted(valid_set)
    
    # Apply corrective filter based on parity
    filtered_metrics = [val for val in sorted_metrics if int(val) % 2 == 0]
    
    # Critical statement
    filtration_score = sum(filtered_metrics)
    
    # Irrelevant auxiliary variable (minor distraction)
    dummy_counter = len(raw_readings) - len(normalized)
    
    print(f"Result: {filtration_score}")

analyze_sensor_data()