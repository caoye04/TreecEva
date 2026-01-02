def analyze_readings(sensor_readings, base_offset):
    adjusted_readings = [r + base_offset for r in sensor_readings]
    valid_readings = [r for r in adjusted_readings if r > 0]
    processed_data = list(map(lambda x: x * 1.5, valid_readings))
    threshold = 10.0
    filtered_sum = sum([x for x in processed_data if x > threshold])
    status_flag = True  # Irrelevant flag (minimal distraction)
    return filtered_sum

sensor_inputs = [1, -2, 3, 4, -5, 6]
base = 2
result = analyze_readings(sensor_inputs, base)
print(f"Result: {result}")