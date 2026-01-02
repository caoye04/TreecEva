def analyze_readings(sensor_data):
    adjusted_values = [val * 2 + 1 for val in sensor_data]
    
    offset = 5
    shifted_values = [v - offset for v in adjusted_values]
    
    processed_data = []
    for num in shifted_values:
        if num > 0:
            processed_data.append(int(num // 1.5))  # Apply integer division and rounding down
    
    temp_var = [x for x in processed_data if x < 0]  # Irrelevant filtering (distractor)
    filtered_sum = sum([x for x in processed_data if x % 3 == 0])
    
    extra_calc = len(processed_data) * 2  # Unused variable (minor distractor)
    return filtered_sum

sensor_input = [3, 7, 4, 8, 6]
result = analyze_readings(sensor_input)
print(f"Result: {result}")