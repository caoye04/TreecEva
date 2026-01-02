def analyze_sensor_data(raw_readings):
    # Preprocess: filter out invalid entries using string-based flags
    valid_readings = []
    flagged_count = 0
    temp_buffer = []

    for entry in raw_readings:
        if isinstance(entry, str):
            cleaned = entry.strip().lower()
            if 'err' in cleaned or 'fail' in cleaned:
                flagged_count += 1
                continue
            elif cleaned.isdigit():
                temp_buffer.append(int(cleaned))
        elif isinstance(entry, int) and entry >= 0:
            temp_buffer.append(entry)

    # Simulate noise filtering with moving average (not used in final logic)
    smoothed = []
    for i in range(len(temp_buffer)):
        window = temp_buffer[max(0, i-2):i+1]
        smoothed.append(sum(window) / len(window))

    # Core diagnostic logic
    base_score = sum(temp_buffer) // (len(temp_buffer) or 1)
    
    # Secondary metrics (distractors)
    peak_value = max(temp_buffer) if temp_buffer else 0
    reading_variance = sum((x - base_score) ** 2 for x in temp_buffer) / (len(temp_buffer) or 1)
    entropy_proxy = 0
    for x in temp_buffer:
        if x > 0:
            entropy_proxy -= (x / (base_score * len(temp_buffer))) * (x / (base_score * len(temp_buffer)))

    # Anomaly detection based on pattern length
    pattern_summary = ''.join(str(x % 10) for x in temp_buffer)
    repeated_sequence = any(pattern_summary[i:i+2] == pattern_summary[i+2:i+4] 
                           for i in range(len(pattern_summary) - 3))
    
    sequence_risk = 3 if repeated_sequence else 0
    
    # Determine correction factor using bitwise analysis of base characteristics
    bit_analysis = peak_value ^ int(reading_variance)
    correction_factor = (bit_analysis & 7) or 1  # Ensure non-zero

    # Final adjustment logic
    anomaly_offset = abs(flagged_count - sequence_risk)
    final_diagnostic = base_score + anomaly_offset * correction_factor

    # Dead code branch - never executed under normal input
    if False and len(smoothed) > 100:
        fallback = sum(smoothed[::5])
        final_diagnostic = fallback // 10

    return final_diagnostic

# Input data with mixed types and embedded string flags
sensor_input = [15, ' 20 ', 'ERR01', 25, 30, 'fail', '35', 40, ' 45 ', 'FAIL', 50]
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")