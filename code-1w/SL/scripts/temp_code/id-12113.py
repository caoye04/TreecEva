def analyze_sensor_readings(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize timestamps (not used later)
    normalized_times = [(t - raw_readings[0][0]) * 1.0 for t, _ in raw_readings]
    readings_only = [val for _, val in raw_readings]

    # Distractor: Moving average filter (unused)
    moving_avg = []
    window_size = 3
    for i in range(len(readings_only)):
        if i >= window_size - 1:
            avg = sum(readings_only[i - window_size + 1:i + 1]) / window_size
            moving_avg.append(avg)

    # Relevant: Apply calibration and detect anomalies
    calibrated_readings = [v * calibration_factor for v in readings_only]
    anomalies = []
    for idx, val in enumerate(calibrated_readings):
        if abs(val) > 50 and idx % 2 == 0:
            anomalies.append(idx)

    # Distractor: Build metadata dictionary with unused fields
    sensor_metadata = {
        'unit': 'microvolts',
        'version': '2.1a',
        'anomaly_count_estimate': len(moving_avg),  # Misleading!
        'calibration_adjustment': calibration_factor
    }

    # Critical: Filter data based on dynamic thresholds
    filtered_data = []
    threshold_map = {}
    base_threshold = 42.0
    for i, val in enumerate(calibrated_readings):
        dynamic_thresh = base_threshold + (i % 5) * 2.5
        threshold_map[i] = dynamic_thresh
        if val < dynamic_thresh and i not in anomalies:
            filtered_data.append(val)

    # Dead code path: Unused correction pass
    if len(filtered_data) > 100:
        corrected = [x * 0.95 for x in filtered_data]
        filtered_data = corrected  # Never reached in this case

    # Key computation chain
    def compute_filtration(data, thresh_lookup):
        score = 0.0
        cumulative_shift = 0

        # Use enumerate and zip: Process pairs with indices
        paired = list(zip(data[:-1], data[1:]))
        for i, (prev_val, curr_val) in enumerate(paired):
            diff = curr_val - prev_val
            if diff > 0:
                score += diff * 0.7
            else:
                score -= abs(diff) * 0.3

        # Additional logic: Slicing and conditional adjustment
        mid_segment = data[len(data)//4 : len(data)//4*3]  # Central 50%
        if mid_segment:
            avg_mid = sum(mid_segment) / len(mid_segment)
            if avg_mid > 30:
                score *= 1.25
            elif avg_mid < 10:
                score *= 0.8

        # Bit manipulation red herring
        bit_encoded = 0
        for val in data[:8]:
            shifted = int(abs(val)) % 32
            bit_encoded |= (1 << (shifted % 8))
        # But bit_encoded is never used in score

        # Final adjustment based on threshold map sparsity
        valid_keys = [k for k in thresh_lookup.keys() if k < len(data) * 1.1]
        key_sum = sum(valid_keys)
        if key_sum % 7 == 0:
            score = int(score) + 5
        else:
            score = int(score) - 3

        return score

    # Execute critical statement
    filtration_score = compute_filtration(filtered_data, threshold_map)

    # Distractor: Unused secondary analysis
    def secondary_diagnostic(seq):
        return sum(1 for a, b in zip(seq, seq[1:]) if a > b)

    result_flag = False
    if filtration_score > 100:
        result_flag = True

    # Output target result
    print(f"Target result: {filtration_score}")