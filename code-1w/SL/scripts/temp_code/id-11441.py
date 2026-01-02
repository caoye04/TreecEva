def analyze_sensor_data(raw_readings, base_offset):
    scaled_readings = [r * 1.5 + base_offset for r in raw_readings]
    adjusted_readings = [int(x) for x in scaled_readings if x > 0]
    processed_values = [val ** 2 for val in adjusted_readings]
    outlier = 9999  # Irrelevant variable (distractor)
    temp_cache = [x for x in processed_values if x < 5000]  # Unused intermediate list
    threshold = 1000
    filtered_sum = sum([x for x in processed_values if x > threshold])
    debug_mode = False  # Distractor flag
    return filtered_sum

raw_sensor_inputs = [3, -1, 4, 0, 5]
base_correction = 10
result = analyze_sensor_data(raw_sensor_inputs, base_correction)
print(f"Result: {result}")