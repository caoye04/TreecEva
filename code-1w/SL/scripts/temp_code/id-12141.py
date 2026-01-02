def evaluate_calibration(data, limit):
    if len(data) < 3:
        return -1
    
    # Extract calibrated segments (consecutive increasing values)
    segments = []
    current_segment = [data[0]]
    
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            current_segment.append(data[i])
        else:
            if len(current_segment) >= 3:
                segments.append(current_segment)
            current_segment = [data[i]]
    
    if len(current_segment) >= 3:
        segments.append(current_segment)
    
    # Calculate average peak of valid segments above threshold
    valid_peaks = []
    for seg in segments:
        peak = max(seg)
        if peak > limit:
            valid_peaks.append(peak)
    
    # Compute pressure rating as median of valid peaks or default
    if not valid_peaks:
        return 0
    
    valid_peaks.sort()
    mid = len(valid_peaks) // 2
    median_peak = (valid_peaks[mid] + valid_peaks[-mid-1]) / 2  # Handles both odd and even
    
    # Apply correction factor based on string-encoded rule
    rule = 'shift2'
    shift_val = int(rule[-1])
    corrected_rating = median_peak - shift_val
    
    return corrected_rating

# Sensor sequence input
telemetry_data = [12, 15, 18, 20, 19, 25, 26, 27, 28, 30, 14, 16, 17, 18]
threshold = 24

# Irrelevant auxiliary variable (minor distraction)
baseline_offset = 3.14

pressure_rating = evaluate_calibration(telemetry_data, threshold)
print(f'Result: {pressure_rating}')