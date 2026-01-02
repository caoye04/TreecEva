def analyze_sensor_data(readings):
    adjusted_readings = [r * 1.5 for r in readings]
    valid_range = (20, 100)
    filtered_readings = [val for val in adjusted_readings if valid_range[0] <= val <= valid_range[1]]
    outlier_count = len(readings) - len(filtered_readings)
    filtration_score = sum(filtered_readings)
    return filtration_score

sensor_readings = [10, 15, 25, 30, 45, 60, 75, 90]
result = analyze_sensor_data(sensor_readings)
filtration_score = result
print(f"Target result: {filtration_score}")