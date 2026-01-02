def analyze_sensor_data():
    raw_readings = [105, 203, 98, 110, 150, 88, 92, 210, 101, 97]
    threshold = 100
    scaling_factor = 0.75
    
    # Extract recent stable readings (middle 6 values)
    mid_readings = raw_readings[2:8]
    
    # Filter out any spikes above threshold
    filtered_data = [x for x in mid_readings if x <= threshold]
    
    # Calculate final adjusted reading
    result = sum(filtered_data) * scaling_factor
    
    # Irrelevant diagnostic variable (minimal interference)
    avg_raw = sum(raw_readings) / len(raw_readings)
    
    print(f"Result: {result}")

analyze_sensor_data()