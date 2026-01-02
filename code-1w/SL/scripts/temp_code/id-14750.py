def analyze_sensor_data(readings):
    adjusted_readings = [x * 1.05 for x in readings]
    valid_range = [x for x in adjusted_readings if 20 <= x <= 100]
    outliers = [x for x in adjusted_readings if x < 20 or x > 100]
    filtered_readings = [x for x in valid_range if x > 50]
    energy_threshold = 0
    if filtered_readings:
        energy_threshold = max(filtered_readings)
    return energy_threshold

sensor_inputs = [45, 60, 80, 15, 95, 110, 70]
result = analyze_sensor_data(sensor_inputs)
print(f"Target result: {result}")