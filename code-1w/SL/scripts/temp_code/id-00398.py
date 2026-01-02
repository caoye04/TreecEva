def sensor_diagnostic_system():
    raw_signals = [0.78, 1.21, 0.45, 2.01, 1.67, 0.94, 3.12, 2.55]
    calibration_factor = 1.08
    baseline_offset = 0.15
    sample_window = 5
    max_threshold = 2.9
    min_threshold = 0.5
    spike_count = 0
    smoothed_values = []
    trend_magnitude = 0.0
    historical_peaks = []

    # Irrelevant signal normalization (distractor)
    normalized_signals = [round((x - min(raw_signals)) / (max(raw_signals) - min(raw_signals)), 3) for x in raw_signals]
    temp_storage = {f'idx_{i}': val for i, val in enumerate(normalized_signals)}

    # Actual processing chain
    calibrated_readings = [round(x * calibration_factor + baseline_offset, 3) for x in raw_signals]

    # Moving average smoothing (relevant)
    for i in range(len(calibrated_readings)):
        if i >= sample_window - 1:
            window_avg = sum(calibrated_readings[i - sample_window + 1:i + 1]) / sample_window
            smoothed_values.append(round(window_avg, 3))

    # Detect spikes above dynamic threshold (relevant)
    dynamic_floor = sum(smoothed_values) / len(smoothed_values) if smoothed_values else 1.0
    for val in smoothed_values:
        if val > dynamic_floor * 1.45:
            spike_count += 1
            historical_peaks.append(val)

    # Dead code path - never executed due to constant condition (distractor)
    debug_mode = False
    if debug_mode and len(historical_peaks) > 10:
        trend_magnitude = sum(historical_peaks) / len(historical_peaks)
        print(f'Debug trend: {trend_magnitude}')

    processed_data = smoothed_values[::2]  # Take every other reading

    # Lambda function used for threshold logic (required Python feature)
    threshold_func = lambda x: 1 if x > dynamic_floor * 1.3 else 0

    # Simulated diagnostic analysis with bit manipulation red herring
    def analyze_readings(data, scorer):
        score_accum = 0
        bit_flag = 0b101
        mask_shift = 3

        # Real scoring logic
        for reading in data:
            if reading > dynamic_floor:
                score_accum += int(reading * 10) % 7

        # Irrelevant bitwise operations (distractor)
        masked_result = bit_flag << mask_shift
        checksum_verify = (masked_result ^ 0b1101) & 0b1111
        dummy_state = [checksum_verify >> i for i in range(3)]  # Unused list

        # Final decision logic
        severity_level = len([r for r in data if r > dynamic_floor * 1.2])
        base_diagnostic = score_accum * 3 + severity_level

        # Another dead computation (distractor)
        if len(dummy_state) == 10:
            base_diagnostic += 100

        return base_diagnostic

    final_diagnostic = analyze_readings(processed_data, threshold_func)
    print(f'Target result: {final_diagnostic}')

sensor_diagnostic_system()