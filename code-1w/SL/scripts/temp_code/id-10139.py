def process_sensor_data(raw_readings):
    cleaned_data = [x for x in raw_readings if isinstance(x, (int, float)) and x >= 0]
    squared_values = list(map(lambda y: y ** 2, cleaned_data))
    valid_entries = [v for v in squared_values if v % 2 == 0]
    filtered_sum = sum(valid_entries)
    outlier_count = len([x for x in raw_readings if isinstance(x, (int, float)) and x > 100])
    status_flags = {"high_outliers": outlier_count > 5}
    return filtered_sum

readings = [10, -5, 'error', 7, 12, 101, 8, 3, 'N/A', 6]
result = process_sensor_data(readings)
filtered_sum = result
print(f"Target result: {filtered_sum}")