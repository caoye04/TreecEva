def analyze_readings(sensor_readings):
    base_offset = 10
    adjusted_readings = [r + base_offset for r in sensor_readings]
    
    squared_values = [x**2 for x in adjusted_readings]
    mean_value = sum(squared_values) / len(squared_values)
    threshold = mean_value ** 0.5

    processed_data = [int(y // 1.5) for y in squared_values]
    filtered_sum = sum([x for x in processed_data if x > threshold])
    
    dummy_var = "analysis_complete"
    status_log = [dummy_var]
    return filtered_sum

sensor_inputs = [3, 7, 2, 8, 5]
result = analyze_readings(sensor_inputs)
print(f"Result: {result}")