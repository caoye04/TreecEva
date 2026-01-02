def analyze_sensor_readings(readings):
    scaled_readings = [r * 1.5 for r in readings]
    offset = 10
    adjusted_readings = [r + offset for r in scaled_readings]
    valid_range = (20, 50)
    filtered_readings = [r for r in adjusted_readings if valid_range[0] <= r <= valid_range[1]]
    temp_avg = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0
    threshold = temp_avg - 5
    processed_data = [r for r in filtered_readings if r > 25]
    filtered_sum = sum([x for x in processed_data if x > threshold])
    status_flag = 'normal' if filtered_sum > 30 else 'low'
    extra_calc = len(readings) * 2  # irrelevant to final result
    return filtered_sum

readings_input = [8, 10, 12, 14, 9]
result = analyze_sensor_readings(readings_input)
print(f"Result: {result}")