def analyze_temperatures(raw_readings):
    scaled_readings = [round(temp * 1.8 + 32, 1) for temp in raw_readings]  # Convert to Fahrenheit
    valid_range = lambda x: 68 <= x <= 78
    filtered_readings = list(filter(valid_range, scaled_readings))
    adjustment_factor = 0.9
    processed_data = [x * adjustment_factor for x in filtered_readings][::2]  # Every other reading
    auxiliary_calc = len(scaled_readings) // 2 + 1
    temp_offset = 5
    adjusted_count = auxiliary_calc - temp_offset
    filtered_sum = sum(processed_data)
    return filtered_sum

result = analyze_temperatures([20.0, 21.5, 22.0, 23.0, 19.5, 24.0])
print(f"Target result: {result}")