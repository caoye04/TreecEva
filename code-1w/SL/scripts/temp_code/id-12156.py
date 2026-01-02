def analyze_sensor_data(readings):
    scaled_readings = [x * 0.75 for x in readings]
    adjusted_readings = list(map(lambda x: x + 1.5, scaled_readings))
    valid_range = [x for x in adjusted_readings if 3.0 <= x <= 10.0]
    filtered_readings = [x for x in valid_range if x > 5.0]
    energy_threshold = max(filtered_readings)
    return energy_threshold

sensor_inputs = [8, 12, 4, 9, 15, 6, 10]
result = analyze_sensor_data(sensor_inputs)
print(f"Target result: {result}")