def analyze_sensor_data(raw_readings, threshold=100.0, correction_factor=0.9):
    corrected_readings = [x * correction_factor for x in raw_readings]
    
    # Simulate auxiliary diagnostic data (not directly used)
    diagnostic_codes = {i: f'DBG{x:.1f}' for i, x in enumerate(corrected_readings) if x > 50}
    temp_buffer = [x for x in corrected_readings if x < 20]
    snapshot = corrected_readings[::2]  # Every other reading
    
    # Primary signal processing path
    normalized = [max(0, x - 10) for x in corrected_readings]
    categorized = {i: 'HIGH' if x > threshold else 'LOW' for i, x in enumerate(normalized)}
    
    # Filter and process final data
    valid_indices = [i for i, x in enumerate(normalized) if categorized[i] == 'LOW']
    extracted_data = [normalized[i] for i in valid_indices]
    padded_data = [0] + extracted_data + [0]  # Add guards
    diff_sequence = [padded_data[i+1] - padded_data[i] for i in range(len(padded_data)-1)]
    
    # Final filtering based on dynamic criteria
    moving_avg = sum(extracted_data) / len(extracted_data) if extracted_data else 0
    dynamic_offset = moving_avg * 0.1
    filtered_data = [x for x in extracted_data if x > dynamic_offset]
    
    # Irrelevant post-processing (distractor)
    stats_summary = {
        'count': len(extracted_data),
        'peak': max(extracted_data) if extracted_data else 0,
        'baseline': moving_avg
    }
    outlier_flags = [x for x in diff_sequence if abs(x) > 2*threshold]
    
    # Critical assignment
    filtered_sum = sum(filtered_data)
    return filtered_sum

# Simulated sensor input
data_stream = [120.5, 85.0, 150.3, 45.7, 67.2, 200.1, 30.4, 95.8]
result = analyze_sensor_data(data_stream)
print(f"Result: {result}")