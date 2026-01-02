def analyze_sensor_data(raw_readings):
    scaled_data = [int(x * 1.5) for x in raw_readings]
    adjusted_data = [x + 1 for x in scaled_data]
    valid_range = [x for x in adjusted_data if 10 <= x <= 50]
    processed_data = [x ^ 3 for x in valid_range]
    filtered_sum = sum([x for x in processed_data if x & 1])
    return filtered_sum

sensor_readings = [5, 8, 10, 12, 7, 3, 9]
result = analyze_sensor_data(sensor_readings)
print(f"Result: {result}")