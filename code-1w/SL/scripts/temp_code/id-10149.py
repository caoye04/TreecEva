def analyze_sensor_data(readings, min_level=50):
    baseline_energy = 23.7
    processed = [r ** 0.5 for r in readings if r > min_level]
    smoothed = list(map(lambda x: round(x, 2), processed))
    valid_peak = any(s > 9.0 for s in smoothed)
    filtered_readings = [s for s in smoothed if s > 7.5]
    energy_threshold = filtered_readings[-1] if len(filtered_readings) > 0 else baseline_energy
    return energy_threshold

sensor_input = [100, 144, 64, 81, 121, 49]
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")