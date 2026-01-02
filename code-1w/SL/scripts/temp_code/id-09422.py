def analyze_sensor_data():
    # Simulated sensor readings over time (temperature, pressure, humidity)
    raw_readings = [
        (23.5, 101.3, 45), (24.1, 101.5, 47), (22.9, 100.9, 44),
        (25.3, 102.0, 50), (26.0, 102.2, 55), (25.8, 101.8, 53),
        (35.0, 115.0, 60), (26.2, 102.1, 54)
    ]

    # Thresholds for normal operation
    TEMP_THRESHOLD = 30.0
    PRESSURE_THRESHOLD = 110.0
    HUMIDITY_THRESHOLD = 58

    # Extract sequences using enumerate and zip
    temp_seq = [r[0] for r in raw_readings]
    press_seq = [r[1] for r in raw_readings]
    humid_seq = [r[2] for r in raw_readings]

    index_temp_pairs = list(enumerate(temp_seq))
    all_zipped = list(zip(temp_seq, press_seq, humid_seq))

    # Distractor: unused transformation
    normalized = [(t/100, p/100, h/100) for t, p, h in all_zipped]  # Not used

    # Identify anomalous indices
    anomaly_indices = []
    for i, (t, p, h) in enumerate(all_zipped):
        if t > TEMP_THRESHOLD or p > PRESSURE_THRESHOLD or h > HUMIDITY_THRESHOLD:
            anomaly_indices.append(i)

    # Distractor: redundant set creation
    anomaly_set = set(anomaly_indices)
    duplicate_check = {i for i in anomaly_indices if i in anomaly_set}  # Redundant

    # Compute moving average (window size 3) for temperature — only relevant part
    moving_averages = []
    for i in range(2, len(temp_seq)):
        window_avg = (temp_seq[i-2] + temp_seq[i-1] + temp_seq[i]) / 3
        moving_averages.append(round(window_avg, 2))

    # Compute deviation from moving average at anomaly points
    deviation_sum = 0
    for idx in anomaly_indices:
        if idx >= 2:  # Can compute moving average
            expected = moving_averages[idx - 2]
            actual = temp_seq[idx]
            deviation_sum += abs(actual - expected)

    # Distractor: irrelevant bitwise manipulation
    mask = 0b1101
    masked_deviation = int(deviation_sum) & mask  # Used nowhere

    # Scoring logic
    base_score = len(moving_averages) * 10
    penalty = len(anomaly_indices) * 15
    aggregate_score = base_score - penalty

    # Anomaly flag based on XOR pattern across sensors
    flags = []
    for t, p, h in all_zipped:
        high_t = 1 if t > TEMP_THRESHOLD else 0
        high_p = 1 if p > PRESSURE_THRESHOLD else 0
        high_h = 1 if h > HUMIDITY_THRESHOLD else 0
        combined_flag = high_t ^ high_p ^ high_h  # XOR across conditions
        flags.append(combined_flag)

    # Final flag is OR of all individual flags
    anomaly_flag = 0
    for f in flags:
        anomaly_flag |= f  # Will be 1 if any flag triggered

    # UNUSED distractor: complex dictionary aggregation
    stats_summary = {
        'count': len(raw_readings),
        'max_temp': max(temp_seq),
        'min_pressure': min(press_seq),
        'avg_humidity': sum(humid_seq) / len(humid_seq),
        'anomaly_count': len(anomaly_indices),
        'deviation_total': deviation_sum,
        'computed_flags': [f for f in flags if f == 1]
    }

    # UNUSED: nested dict traversal red herring
    deep_analysis = {}
    for k, v in stats_summary.items():
        if isinstance(v, list):
            deep_analysis[k] = {i: val for i, val in enumerate(v)}

    # Critical statement
    final_diagnostic = aggregate_score + anomaly_flag

    # Print result for evaluation
    print(f"Result: {final_diagnostic}")

analyze_sensor_data()