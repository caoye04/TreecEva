def process_sensor_readings(readings):
    threshold = 50
    scaled_readings = [x * 1.5 for x in readings]
    valid_readings = set(range(20, 100))
    filtered_data = [int(x) for x in scaled_readings if x in valid_readings]
    outlier_count = len([x for x in readings if x > 80])
    filtered_sum = sum(filtered_data)
    return filtered_sum

sensor_inputs = [30, 45, 55, 60, 85]
result = process_sensor_readings(sensor_inputs)
print(f"Result: {result}")