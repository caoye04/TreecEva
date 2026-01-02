def analyze_sensor_data(raw_readings):
    scaled_readings = [x * 0.75 for x in raw_readings]
    offset_correction = 10
    corrected_readings = [x + offset_correction for x in scaled_readings]
    valid_range_data = [x for x in corrected_readings if 15 <= x <= 30]
    processed_data = valid_range_data[1:5:2]
    filtered_sum = sum(processed_data)
    outlier_check = [x for x in raw_readings if x > 50]
    temp_flag = len(outlier_check) > 0
    return filtered_sum

sensor_input = [20, 25, 30, 40, 50, 60]
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")