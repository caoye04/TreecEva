def analyze_sensor_readings(readings):
    thresholds = [15, 25, 35]
    adjusted = [x - 5 for x in readings if x > 10]
    filtered_data = []
    for i, val in enumerate(adjusted):
        if val > thresholds[i % len(thresholds)]:
            filtered_data.append(val)
    result = sum(filtered_data)
    return result

sensor_input = [22, 18, 40, 31, 9]
output = analyze_sensor_readings(sensor_input)
print(f"Target result: {output}")