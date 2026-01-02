def analyze_sensor_data():
    raw_readings = [105, -200, 350, 415, -100, 220, 95, 500]
    threshold = 100
    scaling_factor = 0.85
    
    # Normalize readings: shift all values by base_offset
    base_offset = 100
    normalized = [x + base_offset for x in raw_readings]
    
    # Filter out values below threshold (using original scale)
    valid_mask = [abs(x) > threshold for x in raw_readings]
    filtered_data = [normalized[i] for i in range(len(normalized)) if valid_mask[i]]
    
    # Apply conditional adjustment using slicing and set logic
    if len(filtered_data) > 4:
        mid_segment = filtered_data[1:-1]
        unique_mid = list(set(mid_segment))
        adjusted_mid = [x * 0.95 for x in unique_mid]
        filtered_data = [filtered_data[0]] + adjusted_mid + [filtered_data[-1]]
    
    result = sum(filtered_data) * scaling_factor
    print(f"Result: {result}")
    return result

analyze_sensor_data()