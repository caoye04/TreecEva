def analyze_sensor_data(raw_readings):
    threshold = 50
    adjusted_readings = [x - 10 for x in raw_readings if x > 30]
    processed_data = adjusted_readings[1::2]  # Take every second element starting from index 1
    temp_log = {f'sample_{i}': v for i, v in enumerate(adjusted_readings)}
    filtered_sum = sum(processed_data)
    status_flag = True if filtered_sum > threshold else False
    return filtered_sum

readings = [25, 45, 60, 20, 55, 70, 10, 80]
result = analyze_sensor_data(readings)
print(f"Result: {result}")