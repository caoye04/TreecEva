def analyze_data_stream(stream_data):
    processed_values = []
    temp_buffer = []
    irrelevant_sum = 0
    
    # Process stream with irrelevant operations
    for idx, value in enumerate(stream_data):
        temp_buffer.append(value * 2)  # Misleading operation
        irrelevant_sum += value ** 2   # Dead calculation
        
        # Relevant filtering logic
        if idx % 3 == 0:
            processed_values.append(value + 5)
        elif idx % 3 == 1:
            processed_values.append(value * 3)
        else:
            processed_values.append(value - 2)  # Dead path for this input
    
    # More distractions
    fake_max = max(temp_buffer)  # Unused
    fake_min = min(stream_data)  # Unused
    
    return processed_values

def combine_metrics(data_a, data_b):
    combined = []
    misleading_product = 1
    
    # Zip and enumerate with distractions
    for i, (a_val, b_val) in enumerate(zip(data_a, data_b)):
        misleading_product *= a_val + b_val  # Red herring
        
        # Core logic with set operations
        unique_vals = {a_val, b_val, i}
        if len(unique_vals) == 3:
            combined.append(a_val + b_val + i)
        elif a_val > b_val:
            combined.append(a_val - b_val)  # Dead path
        else:
            combined.append(a_val * b_val)  # Dead path
    
    return combined

# Main execution with distractions
sensor_readings = [12, 8, 15, 6, 20, 10]
calibration_data = [3, 7, 2, 9, 4, 11]

# Irrelevant preprocessing
scaled_readings = [x * 1.5 for x in sensor_readings]  # Unused
shifted_calibration = [x + 10 for x in calibration_data]  # Unused

# Actual processing
processed_stream = analyze_data_stream(sensor_readings)
combined_results = combine_metrics(processed_stream, calibration_data)

# Final calculation with enumerate
enumerate_filtered = []
for index, value in enumerate(combined_results):
    if index % 2 == 0:
        enumerate_filtered.append(value)

# Dead code path
if sum(combined_results) > 100:
    final_metric = sum(combined_results)  # Never executed
else:
    final_metric = sum(enumerate_filtered)

print(f"Result: {final_metric}")