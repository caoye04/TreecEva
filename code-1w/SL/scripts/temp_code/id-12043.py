def process_sensor_readings(readings):
    threshold = 50
    scaling_factor = 1.5
    adjusted_readings = [int(x * scaling_factor) for x in readings]
    valid_range = set(range(20, 100))
    filtered_data = list(filter(lambda val: val in valid_range, adjusted_readings))
    outlier_count = len(readings) - len([v for v in adjusted_readings if v in valid_range])
    filtered_sum = sum(filtered_data)
    return filtered_sum

sensor_inputs = [30, 45, 60, 70, 25]
result = process_sensor_readings(sensor_inputs)
print(f"Result: {result}")