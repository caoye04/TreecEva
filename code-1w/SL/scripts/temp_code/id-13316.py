def analyze_sensor_data(readings):
    base_offset = 0.5
    adjusted_readings = [r * 1.2 + base_offset for r in readings]
    valid_range_readings = [r for r in adjusted_readings if 1.0 <= r <= 10.0]
    smoothed_readings = [r - 0.1 for r in valid_range_readings]
    filtered_readings = [r for r in smoothed_readings if r > 0.5]
    energy_threshold = max(filtered_readings)
    return energy_threshold

sensor_input = [0.8, 2.1, 9.5, 0.3, 4.7, 12.0, 6.8]
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")