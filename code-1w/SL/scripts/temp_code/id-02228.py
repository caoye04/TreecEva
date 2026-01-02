def analyze_sensor_readings():
    raw_readings = [15, 23, 37, 41, 52, 68, 73, 84, 91]
    offset = 5
    adjusted_readings = [x - offset for x in raw_readings]
    threshold = 60
    filtered_readings = [x for x in adjusted_readings if x > threshold]
    reversed_data = filtered_readings[::-1]
    filtered_sum = sum(reversed_data[1::2])
    auxiliary_total = sum(adjusted_readings)
    correction_factor = 1.0
    return filtered_sum

result = analyze_sensor_readings()
print(f"Result: {result}")