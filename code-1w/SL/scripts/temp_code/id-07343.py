def analyze_sensor_data(raw_readings):
    offset = 1
    shifted_data = [x + offset for x in raw_readings]
    
    # Extract critical phase window using slicing
    phase_window = shifted_data[3:9]
    
    # Apply threshold filtering and transform
    filtered_readings = [val for val in phase_window if val > 5]
    processed_segments = tuple(x ** 2 for x in filtered_readings)
    
    # Secondary buffer (irrelevant to final result, adds minimal interference)
    buffer_cache = {i: shifted_data[i] * 2 for i in range(0, len(shifted_data), 3)}
    
    # Key computation point
    filtration_yield = sum(processed_segments) // len(processed_segments)
    
    return filtration_yield

# Simulated sensor input
sensor_input = [0, 1, 2, 3, 4, 5, 6, 7]
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")