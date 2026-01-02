def analyze_sensor_data(raw_readings):
    scaled_readings = [x * 0.75 for x in raw_readings]
    offset_correction = 10
    corrected_readings = [x + offset_correction for x in scaled_readings]
    valid_range_filter = lambda x: 15 <= x <= 90
    processed_data = [x for x in corrected_readings if valid_range_filter(x)]
    outlier_threshold = 85
    filtered_sum = sum(processed_data)
    return filtered_sum

sensor_input = [20, 30, 40, 50, 60, 70, 80, 90]
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")