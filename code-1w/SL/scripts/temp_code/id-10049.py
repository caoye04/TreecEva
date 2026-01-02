def analyze_readings(sensor_data):
    threshold = 50
    scaled_data = [x * 1.5 for x in sensor_data]
    processed_data = list(map(lambda x: int(x) if x > threshold else 0, scaled_data))
    invalid_count = len([x for x in sensor_data if x < 0])
    filtered_sum = sum(processed_data)
    status_flag = True if filtered_sum > 200 else False
    result_log = {'entries': len(sensor_data), 'adjusted_total': filtered_sum, 'valid': status_flag}
    print(f"Target result: {filtered_sum}")
    return filtered_sum

readings = [30, 55, 40, 70, 25]
analyze_readings(readings)