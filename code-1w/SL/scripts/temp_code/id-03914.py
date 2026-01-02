def analyze_sensor_data(readings):
    min_signal = 1.5
    max_noise = 100
    normalized = [x / 2.5 for x in readings if x > min_signal]
    smoothed = [normalized[i] for i in range(1, len(normalized)) if abs(normalized[i] - normalized[i-1]) < 10]
    baseline = sum(smoothed) / len(smoothed) if smoothed else 0
    adjusted = [x * 0.9 for x in smoothed]
    filtered_readings = [x for x in adjusted if x > baseline]
    energy_threshold = filtered_readings[-1] if filtered_readings else 0
    return energy_threshold

sensor_input = [3.2, 4.5, 1.8, 10.2, 15.0, 8.7, 12.1, 9.8]
result = analyze_sensor_data(sensor_input)
print(f"Target result: {result}")