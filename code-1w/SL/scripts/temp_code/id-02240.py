def analyze_sensor_data(readings):
    min_signal = 1.5
    max_signal = 9.8
    sample_rate = 100
    scaling_factor = 2.1

    # Normalize readings using slicing and conditional logic
    normalized = [round((x - min_signal) / (max_signal - min_signal) * scaling_factor, 2) for x in readings]

    # Filter valid energy levels above threshold
    valid_range = [val for val in normalized if 0.5 <= val <= scaling_factor]
    
    # Simulate window-based processing
    window_size = 3
    filtered_readings = valid_range[:len(valid_range) - (len(valid_range) % window_size)] if len(valid_range) % window_size != 0 else valid_range
    
    # Critical assignment point
    energy_threshold = filtered_readings[-1] if filtered_readings else 0
    
    return energy_threshold

# Input data
sensor_inputs = [3.2, 7.1, 9.5, 2.8, 5.6, 8.9, 1.0, 4.4]
result = analyze_sensor_data(sensor_inputs)
print(f"Result: {result}")