def analyze_sensor_data(raw_readings):
    offset = 10
    scaling_factor = 2
    threshold = 25
    adjusted_readings = [r + offset for r in raw_readings]
    processed_values = [v * scaling_factor for v in adjusted_readings]
    temp_buffer = [val for val in processed_values if val < 50]  # distraction
    filtered_sum = sum([x for x in processed_values if x > threshold])
    correction = len(temp_buffer) * 2
    final_result = filtered_sum - correction
    return final_result

sensor_inputs = [3, 7, 12, 18, 22]
result = analyze_sensor_data(sensor_inputs)
filtered_sum_intermediate = sum([x * 2 + 20 for x in sensor_inputs if (x * 2 + 20) > 25])
print(f"Result: {result}")