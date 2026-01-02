def analyze_sensor_readings(readings):
    threshold = 25
    scaled_readings = [x * 1.2 for x in readings]
    normalized = [int(x) for x in scaled_readings]
    filtered_data = [x for x in normalized if x > threshold]
    temp_offset = 5  # Irrelevant variable (minimal distraction)
    result = sum(filtered_data)
    return result

sensor_inputs = [18, 22, 30, 40, 15]
output = analyze_sensor_readings(sensor_inputs)
print(f"Result: {output}")