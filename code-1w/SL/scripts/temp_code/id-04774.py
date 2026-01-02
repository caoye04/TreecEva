def sensor_calibration(raw_values):
    offset = 0.75
    calibrated = []
    for val in raw_values:
        adjusted = val * 1.02 + offset
        if adjusted > 100:
            adjusted = 98.5  # cap high readings
        calibrated.append(round(adjusted, 2))
    return calibrated

# Simulate environmental interference compensation
def apply_noise_filter(data):
    filter_kernel = [0.25, 0.5, 0.25]
    filtered = [data[0]]
    for i in range(1, len(data) - 1):
        weighted = (data[i-1] * filter_kernel[0] + 
                   data[i]   * filter_kernel[1] + 
                   data[i+1] * filter_kernel[2])
        filtered.append(round(weighted, 2))
    filtered.append(data[-1])
    return filtered

# Misleading function – not actually used in final calculation
def deprecated_analysis(seq):
    total = 0
    for x in seq:
        total += x ** 0.5
    return round(total, 2)

# Core processing pipeline
def preprocess_sensor_array(raw_stream):
    stage_one = sensor_calibration(raw_stream)
    stage_two = apply_noise_filter(stage_one)
    baseline_corrected = [val - 0.5 for val in stage_two]
    return [round(v, 2) for v in baseline_corrected]

# Characterize data distribution
summarize_stats = lambda arr: {
    'mean': sum(arr) / len(arr),
    'peak': max(arr),
    'variability': max(arr) - min(arr)
}

# Main diagnostic engine
def analyze_readings(clean_data):
    stats = summarize_stats(clean_data)
    
    # Irrelevant intermediate calculations (distractors)
    dummy_score = 0
    for val in clean_data:
        if val > stats['mean'] and val < stats['peak']:
            dummy_score += 1
    threshold = stats['mean'] + (stats['variability'] * 0.25)
    
    # Actual decision logic
    alert_level = 0
    above_threshold_count = 0
    for reading in clean_data:
        if reading > threshold:
            above_threshold_count += 1
    
    # Key computation path
    if above_threshold_count > len(clean_data) * 0.3:
        alert_level = 3
    elif above_threshold_count > 0:
        alert_level = 2
    else:
        alert_level = 1
    
    # Unused branching - red herring
    if stats['variability'] > 20:
        adjustment_factor = 1.5
    else:
        adjustment_factor = 1.0  # never used
    
    # Final diagnostic code
    final_diagnostic = (stats['peak'] // 10) * 10 + alert_level
    return int(final_diagnostic)

# Entry point
if __name__ == '__main__':
    # Example sensor input (simulated IoT device readings)
    raw_input_stream = [89.3, 95.1, 76.8, 102.4, 88.9, 94.2, 96.7, 73.5, 85.0, 91.8]
    
    # Dead code - misleading preprocessing
    temp_analysis = deprecated_analysis(raw_input_stream)
    
    # Relevant execution path
    processed_data = preprocess_sensor_array(raw_input_stream)
    final_diagnostic = analyze_readings(processed_data)
    print(f"Result: {final_diagnostic}")