def analyze_sensor_readings():
    raw_readings = [105, 92, 98, 110, 88, 103, 95, 108, 97, 100]
    threshold = 95
    
    # Extract recent high-precision samples (last 6 readings)
    recent_samples = raw_readings[-6:]
    
    # Filter out noise below threshold
    filtered_data = [x for x in recent_samples if x >= threshold]
    
    # Compute average of valid high-quality readings
    result = sum(filtered_data) // len(filtered_data)
    
    # Auxiliary variable for potential expansion (not used in main logic)
    outlier_count = len(recent_samples) - len(filtered_data)
    
    print(f"Result: {result}")

analyze_sensor_readings()