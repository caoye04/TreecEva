def analyze_sensor_stream(raw_readings, threshold=42.5):
    # Simulate preprocessing stages with realistic variable transformations
    normalized = [round(x * 0.89 + 3.1, 2) for x in raw_readings]
    
    # Apply moving average filter (3-point window) to smooth data
    smoothed = []
    for i in range(1, len(normalized) - 1):
        avg_val = (normalized[i-1] + normalized[i] + normalized[i+1]) / 3
        smoothed.append(round(avg_val, 2))
    
    # Misleading secondary computation: peak detection (not used later)
    peak_count = 0
    for j in range(1, len(smoothed) - 1):
        if smoothed[j] > smoothed[j-1] and smoothed[j] > smoothed[j+1]:
            peak_count += 1
    
    # Slice central portion of data for analysis (focus on index 2:8)
    trimmed = smoothed[2:8]
    
    # Compute dynamic threshold based on local statistics (unused red herring)
    local_mean = sum(trimmed) / len(trimmed)
    deviation = [abs(x - local_mean) for x in trimmed]
    dynamic_threshold = local_mean - 0.5 * sum(deviation) / len(deviation)
    
    # Actual filtering logic based on fixed threshold
    filtered_data = [x for x in trimmed if x > threshold]
    
    # Introduce irrelevant scaling factor that's not applied
    legacy_scale = 1.07
    deprecated_offset = -2.1  # Unused in final logic
    
    # Key computational branch with early exit condition
    if len(filtered_data) == 0:
        return -999  # Fallback (not triggered in this case)
    
    # Correction factor derived from original stream properties
    base_magnitude = max(raw_readings) - min(raw_readings)
    correction_factor = 1.0 + (base_magnitude % 7) * 0.01
    
    # CRITICAL STATEMENT: Final score computation
    filtration_score = sum(filtered_data) * correction_factor
    
    # Dead code path: post-validation (never reached due to structure)
    if filtration_score < 0:
        reset_flag = True
        filtration_score = 0
    
    # Output result as required
    print(f"Result: {filtration_score}")

# Execute with representative sensor input
data_stream = [45.6, 47.2, 40.1, 48.9, 43.3, 50.5, 41.8, 46.7, 44.2, 49.1]
analyze_sensor_stream(data_stream)