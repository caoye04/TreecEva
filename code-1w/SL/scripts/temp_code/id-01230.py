def process_measurements(raw_readings, threshold):
    normalized = [round(x * 0.95, 2) for x in raw_readings]
    valid_range = {x for x in normalized if 10 <= x <= 100}
    filtered_data = [x for x in valid_range if x > threshold]
    sorted_data = sorted(filtered_data, reverse=True)
    adjustment_factor = 1.1
    adjusted_values = [x * adjustment_factor for x in sorted_data]
    filtered_sum = sum(filtered_data)
    return filtered_sum

readings = [105.0, 120.5, 95.3, 67.8, 150.2, 99.9, 110.1]
threshold = 98.0
calculated_sum = process_measurements(readings, threshold)
print(f"Result: {calculated_sum}")