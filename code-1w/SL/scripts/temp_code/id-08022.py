def analyze_sensor_data():
    raw_readings = [104, -52, 98, 110, -67, 43, 120, -29, 88, 102]
    threshold = 90
    
    # Extract significant positive readings above threshold
    high_readings = [x for x in raw_readings if x > threshold]
    low_readings = [x for x in raw_readings if x < threshold]  # unused, minor distraction
    
    # Apply correction: exclude maximum outlier
    corrected_data = sorted(high_readings)[:-1]  # Remove highest value (outlier)
    
    # Slice to use only the first three values
    filtered_data = corrected_data[:3]
    
    scaling_factor = 0.5
    result = sum(filtered_data) * scaling_factor
    
    # Irrelevant transformation (not used)
    reversed_data = raw_readings[::-1]  # slicing but not affecting result
    
    return result

output = analyze_sensor_data()
print(f"Result: {output}")