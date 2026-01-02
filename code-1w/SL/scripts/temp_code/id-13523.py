def process_sensor_readings(readings):
    scaled_readings = [x * 0.75 + 2 for x in readings]
    valid_mask = [bool((i + 1) % 2) for i in range(len(scaled_readings))]
    masked_readings = [v for i, v in enumerate(scaled_readings) if valid_mask[i]]
    outlier_threshold = 10.0
    filtered_data = list(filter(lambda x: abs(x) < outlier_threshold, masked_readings))
    adjustment_factor = len(filtered_data) % 4
    adjusted_values = [x + adjustment_factor for x in filtered_data]
    filtered_sum = sum(adjusted_values)
    temp_var_ignored = [x ** 2 for x in readings[:3]]
    unused_tuple = (15, 25, 35)
    return filtered_sum

sensor_inputs = [8, -6, 12, 4, -9, 7]
result = process_sensor_readings(sensor_inputs)
filtered_sum = result
print(f"Result: {filtered_sum}")