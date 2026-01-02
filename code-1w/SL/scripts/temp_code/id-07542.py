def analyze_sensor_data():
    # Simulated sensor readings with noise and calibration offsets
    raw_readings = [107, 214, -999, 321, 426, -999, 530, 635, 740, 845]
    calibration_map = {0: 0.98, 1: 1.02, 2: 0.95, 3: 1.05, 4: 0.99, 5: 1.01, 6: 0.97, 7: 1.03, 8: 0.96, 9: 1.04}
    timestamps = list(range(1000, 1010))
    status_flags = ['OK', 'OK', 'ERR', 'OK', 'OK', 'ERR', 'OK', 'OK', 'OK', 'OK']
    
    # Irrelevant transformation: time decay factor (not used in final result)
    time_decay = [round((t - 1000) * 0.1, 2) for t in timestamps]
    decay_correction = sum(time_decay) / len(time_decay) if time_decay else 0
    
    # Misleading intermediate: peak detection (unused)
    peaks = []
    for i in range(1, len(raw_readings) - 1):
        if raw_readings[i] > raw_readings[i-1] and raw_readings[i] > raw_readings[i+1]:
            peaks.append(i)
    
    # Distractor: secondary processing chain with dead end
    temp_buffer = []
    for val in raw_readings:
        if val != -999:
            temp_buffer.append(val * 0.1)  # scaled down, not used later
    processed_temp = [round(x + 0.5) for x in temp_buffer]
    
    # Core logic: reconstruct valid entries using multiple conditions
    calibrated_values = []
    for idx, (val, flag) in enumerate(zip(raw_readings, status_flags)):
        if val != -999 and flag == 'OK':
            corrected = val * calibration_map[idx]
            calibrated_values.append(round(corrected))
    
    # Conditional filtering based on dynamic threshold
    base_threshold = sum(calibrated_values) // len(calibrated_values)
    inclusion_mask = [True if v >= base_threshold * 0.8 else False for v in calibrated_values]
    
    # Another red herring: frequency analysis of digits (never used)
    digit_freq = {}
    for v in calibrated_values:
        for d in str(abs(v)):
            digit_freq[d] = digit_freq.get(d, 0) + 1
    avg_digit = sum(int(k) * v for k, v in digit_freq.items()) / sum(digit_freq.values()) if digit_freq else 0
    
    # Key data refinement step
    valid_entries = []
    for (val, mask) in zip(calibrated_values, inclusion_mask):
        if mask:
            valid_entries.append(val)
    
    # Dead code path: hypothetical backup correction (never triggered)
    if len(valid_entries) < 5:
        backup_factor = 1.2
        valid_entries = [int(x * backup_factor) for x in valid_entries]
    
    # Final aggregation - target execution point
    filtered_sum = sum(valid_entries)
    
    # Unused post-processing
    normalized = [round(v / filtered_sum * 100, 2) for v in valid_entries] if filtered_sum else []
    
    # Output target result
    print(f"Result: {filtered_sum}")

analyze_sensor_data()