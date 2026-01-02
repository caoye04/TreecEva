def analyze_sensor(stream, config):
    # Irrelevant transformation chain
    temp_buffer = [x * 1.05 for x in stream if x > 0]
    offset_correction = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    normalized = [x + offset_correction for x in temp_buffer]

    # Distractor: complex but unused signal filter
    def wavelet_smooth(data, level=3):
        result = data[:]
        for _ in range(level):
            result = [(result[i] + result[i+1]) / 2 for i in range(len(result)-1)]
        return result or [0]

    smoothed = wavelet_smooth(normalized)

    # Real processing begins: extract anomalies
    baseline = config.get('baseline', 25.0)
    tolerance = config.get('tolerance', 5.0)
    anomalies = []
    for i, val in enumerate(stream):
        if abs(val - baseline) > tolerance * 1.5:
            anomalies.append((i, val))

    # Distractor: dead code path with misleading statistics
    if len(anomalies) > 10:
        avg_gap = sum(anomalies[i+1][0] - anomalies[i][0] for i in range(len(anomalies)-1)) / (len(anomalies)-1)
        trend_score = len([a for a in anomalies if a[1] > baseline]) / len(anomalies)
    else:
        avg_gap = -999  # red herring
        trend_score = None

    # Key logic: filter and transform
    filtered_data = [val for idx, val in anomalies if val > baseline]

    # Complex mapping setup with irrelevant entries
    threshold_map = {
        'low_risk': 30.0,
        'med_risk': 35.0,
        'high_risk': 40.0,
        'critical': 50.0,
        'unused_mode': 60.0  # decoy
    }

    # Secondary distractor: character counting from sensor IDs (irrelevant)
    sensor_tag = "SNSR-ALPHA-7"
    case_converted = sensor_tag.lower()
    char_count = {c: case_converted.count(c) for c in set(case_converted)}
    group_summary = sum(1 for cnt in char_count.values() if cnt > 1)

    # Real function: used to compute final result
    def process_readings(readings, limits):
        if not readings:
            return 0
        count = len(readings)
        avg_val = sum(readings) / count
        level_flags = []
        for v in readings:
            if v >= limits['critical']:
                level_flags.append(3)
            elif v >= limits['high_risk']:
                level_flags.append(2)
            elif v >= limits['med_risk']:
                level_flags.append(1)
            else:
                level_flags.append(0)

        # Multi-step aggregation
        weighted_score = 0
        for idx, flag in enumerate(level_flags):
            weighted_score += flag * (idx + 1)  # position-weighted risk

        # Final computation using enumerate and zip (required Python features)
        indices = list(range(len(readings)))
        pairs = zip(readings, indices)
        adjustment = 0
        for val, pos in pairs:
            if val > 38 and pos % 2 == 0:
                adjustment += 2

        return int(avg_val) + weighted_score + adjustment

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output requirement
    print(f"Result: {final_diagnostic}")