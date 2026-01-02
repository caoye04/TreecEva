def analyze_readings(sensor_data):
    scaled_data = [x * 0.75 for x in sensor_data]
    offset_correction = 10
    corrected_data = [x + offset_correction for x in scaled_data]
    
    # Apply filter to retain only values within normal operating range
    filtered_data = [x for x in corrected_data if 15 <= x <= 25]
    
    # Unrelated diagnostic variable (minor distraction)
    diagnostic_flag = len(corrected_data) > len(filtered_data)
    
    processed_data = list(map(lambda x: round(x - 10, 2), filtered_data))
    filtered_sum = sum(processed_data)
    
    # Additional unrelated computation (low-level interference)
    average_raw = sum(sensor_data) / len(sensor_data) if sensor_data else 0
    
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Input data
readings = [20, 22, 28, 30, 18, 15]
analyze_readings(readings)