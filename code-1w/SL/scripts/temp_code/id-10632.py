def analyze_sensor_readings(readings):
    threshold = 25.0
    base_offset = 1.5
    temp_buffer = [r + base_offset for r in readings]
    
    # Misleading transformation: not used in final result
    normalized = [round((r - min(temp_buffer)) / (max(temp_buffer) - min(temp_buffer)) * 100) for r in temp_buffer]
    spike_count = 0
    for i in range(1, len(temp_buffer)):
        if temp_buffer[i] - temp_buffer[i-1] > 10:
            spike_count += 1
    
    # Actual relevant logic starts here
    valid_range = [r for r in temp_buffer if 20 < r < 40]
    outlier_mask = [i for i, r in enumerate(temp_buffer) if r >= 40]
    correction_factor = 0.85 if len(outlier_mask) < 3 else 0.6
    
    # Key slicing operation to extract mid-segment data
    mid_segment = valid_range[len(valid_range)//4 : len(valid_range)//4*3]
    
    # Introduce irrelevant statistical distraction
    mean_value = sum(temp_buffer) / len(temp_buffer)
    variance = sum((x - mean_value) ** 2 for x in temp_buffer) / len(temp_buffer)
    std_deviation = variance ** 0.5
    
    # Filtering based on dynamic condition
    filtered_data = [int(x) for x in mid_segment if x % 2 == 1]  # Only odd integers
    
    # Dead code path - never executed due to logic
    if len(valid_range) > 100:
        filtered_data.extend([0]*5)
    
    # Critical assignment point
    filtration_score = sum(filtered_data) * correction_factor
    
    # Unrelated logging variables
    log_entry = f"Processed {len(readings)} inputs with {spike_count} spikes"
    debug_state = {'status': 'complete', 'steps': 4}
    
    return filtration_score

# Simulated sensor input
data_stream = [22.1, 24.8, 26.3, 35.7, 19.4, 28.9, 41.2, 23.5, 27.8, 30.1, 20.0, 25.6]
result = analyze_sensor_readings(data_stream)
print(f"Result: {result}")