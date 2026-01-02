def analyze_sensor_data(raw_readings):
    scaled_readings = [x * 0.75 for x in raw_readings]
    offset_correction = 1.25
    corrected_readings = [x + offset_correction for x in scaled_readings]
    
    # Apply threshold filter using lambda and slicing
    valid_range_filter = lambda x: 2.0 <= x <= 8.0
    filtered_readings = [x for x in corrected_readings if valid_range_filter(x)]
    
    # Process every other element starting from index 1 (slicing)
    processed_data = filtered_readings[1::2] if len(filtered_readings) > 1 else []
    
    filtered_sum = sum(processed_data)
    return filtered_sum

# Simulated sensor input
data_stream = [3, 6, 9, 4, 2, 8, 7]
result = analyze_sensor_data(data_stream)
filtered_sum = result
print(f"Result: {filtered_sum}")