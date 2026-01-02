def process_sensor_readings():
    raw_readings = [105, 202, 105, 308, 202, 410, 308, 515]
    offset = 100
    adjusted_readings = [x - offset for x in raw_readings]
    
    # Filter out values below threshold
    valid_readings = [x for x in adjusted_readings if x > 50]
    
    # Remove duplicates and sort ascending
    compressed_data = sorted(set(valid_readings))
    
    # Final aggregation
    filtered_sum = sum(compressed_data)
    
    # Irrelevant distraction: unused statistic
    peak = max(compressed_data) - min(compressed_data)
    
    print(f"Result: {filtered_sum}")

process_sensor_readings()