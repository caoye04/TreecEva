def analyze_sensor_data():
    # Simulated sensor readings (temperature in millidegrees)
    raw_readings = [23450, 24120, 22980, 25670, 26100, 23890, 24010, 25340]
    
    # Irrelevant calibration constants (distractor)
    calibration_offsets = [120, -85, 203, -47, 156, 99, -112, 68]
    adjusted_offsets = [abs(x) ** 0.5 for x in calibration_offsets]  # Unused path

    # Time indices and valid window tracking
    time_indices = list(range(len(raw_readings)))
    valid_window = []
    for i, temp in enumerate(raw_readings):
        if 23000 < temp < 26000:
            valid_window.append(i)
    
    # Secondary filter using zip (relevant)
    filtered_pairs = list(zip(valid_window, [raw_readings[i] for i in valid_window]))
    high_freq_events = 0
    for idx, val in filtered_pairs:
        if val > 24000:
            high_freq_events += 1
    
    # Decoy statistical analysis (dead path)
    mean_offset = sum(calibration_offsets) / len(calibration_offsets) if calibration_offsets else 0
    variance_proxy = sum((x - mean_offset) ** 2 for x in calibration_offsets) / len(calibration_offsets)  # Unused

    # Primary processing: normalize and detect anomalies
    normalized = [x // 100 for x in raw_readings]  # To whole degrees
    anomalies = 0
    for i in range(1, len(normalized)):
        if abs(normalized[i] - normalized[i-1]) > 1:
            anomalies += 1

    # Bit manipulation for fault masking (relevant)
    fault_signature = 0
    for val in raw_readings[:4]:
        fault_signature ^= (val >> 12) & 0xF  # Use top nibble of first four
    
    # Aggregate score computation (critical)
    base_score = sum(normalized) * 3
    anomaly_penalty = anomalies * 150
    event_bonus = high_freq_events * 97
    aggregate_score = base_score - anomaly_penalty + event_bonus

    # Reliability factor from fault signature and valid data length
    reliability_factor = len(valid_window) or 1
    reliability_factor += (fault_signature & 3)  # Add lower 2 bits

    # Dead code: simulated redundancy check
    redundant_sum = 0
    for group in enumerate(zip(raw_readings[::2], raw_readings[1::2])):
        redundant_sum += (group[1][0] + group[1][1]) // 1000  # Not used

    # Final diagnostic calculation (key statement)
    final_diagnostic = aggregate_score // reliability_factor

    # Print result as required
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

analyze_sensor_data()