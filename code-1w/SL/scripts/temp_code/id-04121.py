def analyze_sensor_readings():
    raw_readings = [15, 23, 8, 47, 12, 41, 35, 68, 22, 53]
    offset_correction = 7
    corrected_readings = [x - offset_correction for x in raw_readings]
    
    # Extract every second reading starting from first (downsample)
    downsampled = corrected_readings[::2]  # [8, 40, 5, 35, 15]
    
    # Simulate threshold filtering: find indices above 10
    filtered_indices = [i for i, val in enumerate(downsampled) if val > 10]
    
    # Key computation point
    result = processed_data[::2][filtered_indices[1]]
    
    # Irrelevant auxiliary calculation (minor distraction)
    avg_value = sum(corrected_readings) / len(corrected_readings)
    
    # Corrected data flow
    processed_data = [x * 2 for x in corrected_readings]
    
    return result

# Execute and print result
target_result = analyze_sensor_readings()
print(f"Result: {target_result}")