def analyze_readings(sensor_data):
    filtered_data = [x for x in sensor_data if x > 0]
    squared_values = [x ** 2 for x in filtered_data]
    average_raw = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    
    # Distractor: irrelevant transformation
    inverted = [1/x for x in filtered_data if x != 0]
    temp_sum = sum(inverted) * 0.1  # Not used later
    
    # Destructuring assignment with partial use
    first, *rest = filtered_data
    peak_value = max(rest) if rest else first
    
    # Conditional branch with dead path
    offset_correction = 0
    if len(filtered_data) > 100:
        offset_correction = 5  # Dead code (length won't exceed)
    elif len(filtered_data) > 50:
        offset_correction = 3
    else:
        offset_correction = 1
    
    adjusted = [x + offset_correction for x in filtered_data]
    processed_data = [x for x in adjusted if x < 50]  # Further filtering
    
    # Helper function defined inside (increases nesting)
    def calculate_adjusted_average(data):
        if not data:
            return 0
        base_avg = sum(data) / len(data)
        
        # Secondary distractor computation
        variance_proxy = sum((x - base_avg) ** 2 for x in data) / len(data) if data else 0
        stability_factor = 1.0 if variance_proxy < 10 else 0.8
        
        # Final relevant calculation
        return int(base_avg * stability_factor + len(data))
    
    final_score = calculate_adjusted_average(processed_data)
    
    # Irrelevant aggregation
    total_pairs = 0
    for i in range(len(filtered_data)):
        for j in range(i + 1, len(filtered_data)):
            if abs(filtered_data[i] - filtered_data[j]) < 5:
                total_pairs += 1
    
    # Unused nested loop over slices
    slice_maxima = []
    for k in range(2, 5):
        for start in range(0, len(squared_values) - k + 1):
            window = squared_values[start:start+k]
            slice_maxima.append(max(window))
    
    return final_score

# Input data generation (deterministic)
data_source = [3, 7, -2, 8, 0, 12, 5, 9, 11, 4, 6, 10, 13, -5, 1, 2, 14, 16, 15, 17]
result = analyze_readings(data_source)
print(f"Result: {result}")