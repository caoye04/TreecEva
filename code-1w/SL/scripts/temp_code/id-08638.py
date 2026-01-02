def sensor_diagnostic_protocol():
    # Real data stream simulation (distractor: appears important but only partially used)
    raw_signal = [i * 3 + 2 for i in range(50)]
    filtered_noise = [x for x in raw_signal if x % 4 != 0]
    baseline_correction = sum(filtered_noise[:10]) // 10

    # Core diagnostic parameters
    thresholds = {'t1': 17, 't2': 23, 't3': 41}
    calibration_sequence = [thresholds['t1'] ^ 5, thresholds['t2'] | 3, thresholds['t3'] & 31]

    # Irrelevant health check (dead path)
    def system_health_check():
        health_flags = {"cpu": True, "memory": False}
        return sum([1 for k, v in health_flags.items() if v])

    # Unused transformation (distractor)
    inverted_map = {k: 100 // v for k, v in thresholds.items()}

    # Simulated sensor readings with anomalies
    sensor_readings = [18, 25, 44, 19, 22, 42, 20, 24, 39]

    # Data slicing and masking (relevant)
    primary_slice = sensor_readings[::2]  # Every other reading
    secondary_slice = sensor_readings[1::2]  # Offset slice

    # Bit manipulation for anomaly detection (relevant)
    anomaly_mask = 0
    for val in primary_slice:
        anomaly_mask ^= (val & 7)

    # Set operations to identify critical deviations (relevant)
    expected_range = set(range(18, 26))
    observed_set = set(secondary_slice)
    deviation_pool = observed_set - expected_range  # Only 42 and 24 are here

    # Threshold mapping using conditional logic (relevant)
    threshold_map = {}
    for key, thresh in thresholds.items():
        if len(deviation_pool) > 2:
            threshold_map[key] = thresh + 5
        else:
            threshold_map[key] = thresh - (anomaly_mask % 4)

    # Data processing with early termination (relevant)
    processed_data = []
    for x in secondary_slice:
        temp_val = x * 2 - baseline_correction
        if temp_val > 50:
            break
        processed_data.append(temp_val)

    # Critical function with multiple concepts
    def analyze_readings(data, limits):
        score = 0
        history = set()
        for item in data:
            history.add(item % 11)
            if item > limits['t1'] and item < limits['t2']:
                score += item // 3
            elif item >= limits['t2']:
                score -= item & 15
        # Use of slicing on history (relevant)
        sorted_hist = sorted(history)[::-1][:3]
        bonus = sum(sorted_hist) // 3
        return score + bonus

    # Misleading auxiliary analysis (distractor)
    def predict_failure_risk(readings):
        risk_level = 0
        for r in readings:
            if r > 40:
                risk_level += 1
        return risk_level * 100

    # Unused call (red herring)
    failure_prediction = predict_failure_risk(sensor_readings)

    # Key execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    print(f"Target result: {final_diagnostic}")

sensor_diagnostic_protocol()