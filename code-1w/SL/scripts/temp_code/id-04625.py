def process_sensor_data():
    raw_readings = [102, 107, 98, 110, 103, 95, 108, 112, 99, 105]
    threshold = 100
    scaling_factor = 0.75
    
    # Extract recent high-value readings above threshold
    high_readings = [x for x in raw_readings if x > threshold]
    
    # Apply correction offset (irrelevant to final result)
    correction_offset = 2
    adjusted_readings = [x - correction_offset for x in high_readings]
    
    # Filter every second element from corrected data (distraction)
    subsampled_data = adjusted_readings[::2]
    
    # Focus on original high readings: take last 4 values
    filtered_data = high_readings[-4:]
    
    # Compute final weighted result
    result = sum(filtered_data) * scaling_factor
    
    # Print result as required
    print(f"Result: {result}")
    
    return result

process_sensor_data()