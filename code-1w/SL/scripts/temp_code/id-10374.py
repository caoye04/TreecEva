def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature, humidity, pressure)
    raw_readings = [
        (23.4, 45.2, 1013.2), (24.1, 47.8, 1012.7), (19.5, 60.1, 1014.1),
        (22.8, 55.3, 1013.8), (35.6, 30.0, 1010.5), (20.1, 58.7, 1014.0),
        (21.9, 50.4, 1013.1), (25.3, 44.9, 1012.9), (18.7, 62.3, 1014.3),
        (26.0, 43.1, 1012.5)
    ]

    # Irrelevant baseline calibration data (distractor)
    calibration_offsets = {'temp': 0.3, 'hum': -1.2, 'pres': 0.8}
    adjusted_offsets = [calibration_offsets[k] * 0.95 for k in calibration_offsets]

    # Thresholds for anomaly detection (used later)
    threshold_map = {
        'high_temp': 30.0,
        'low_humid': 40.0,
        'crit_pres': 1011.0
    }

    # Misleading secondary thresholds (red herring)
    safety_envelope = {
        'temp_range': (15.0, 32.0),
        'humid_range': (35.0, 65.0),
        'pres_range': (1010.0, 1015.0)
    }

    # Initial filtering: exclude high temp anomalies
    temp_filtered = [r for r in raw_readings if r[0] <= threshold_map['high_temp']]

    # Compute rolling averages (unused distractor)
    temp_series = [r[0] for r in raw_readings]
    rolling_avg = []
    window_size = 3
    for i in range(len(temp_series) - window_size + 1):
        rolling_avg.append(sum(temp_series[i:i+window_size]) / window_size)

    # Additional derived metrics (some irrelevant)
    derived_metrics = []
    for i, reading in enumerate(raw_readings):
        idx_score = abs(reading[0] - 20.0) * (i + 1)  # Decoy metric
        stability_index = reading[2] / (reading[1] + 1) if reading[1] > 0 else 0
        derived_metrics.append((idx_score, stability_index))

    # Actual processing path begins here
    def evaluate_stability(temp, humid, pres):
        # Complex logic with nested conditions
        base_risk = 0
        if temp > 25.0:
            base_risk += 2
        elif temp < 20.0:
            base_risk += 1

        if humid < threshold_map['low_humid']:
            base_risk += 2

        if pres < threshold_map['crit_pres']:
            base_risk += 3

        adjustment = 0
        if temp > 22.0 and humid > 50.0:
            adjustment -= 1  # Compensating factor
        if pres > 1013.0:
            adjustment += 1

        return base_risk + adjustment

    # Secondary filter based on pressure threshold
    filtered_data = []
    for entry in temp_filtered:
        if entry[2] >= 1012.0:  # Real filter condition
            filtered_data.append(entry)

    # Use of enumerate and zip (required python features)
    indexed_scores = {}
    for idx, (t, h, p) in enumerate(filtered_data):
        score = evaluate_stability(t, h, p)
        indexed_scores[idx] = score

    enhancement_factors = [1.1, 0.9, 1.0, 1.2, 0.8, 1.0, 1.1, 0.95]
    paired_data = list(zip(indexed_scores.values(), enhancement_factors[:len(indexed_scores)]))

    adjusted_scores = [score * factor for score, factor in paired_data]

    # Dead code path - never executed due to length mismatch (distractor)
    if len(enhancement_factors) > 10:
        surplus = [x * 1.5 for x in enhancement_factors[10:]]
        adjusted_scores.extend(surplus)

    # Core transformation function
    def process_readings(data_list, limits):
        aggregate = 0
        severity_map = {0: 0, 1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32}  # Exponential weighting

        for temp, hum, pres in data_list:
            risk_level = 0
            if temp > 25.0:
                risk_level += 2
            if hum < limits['low_humid']:
                risk_level += 2
            if pres < limits['crit_pres']:
                risk_level += 3
            if temp < 20.0 and pres > 1013.5:
                risk_level -= 1  # Conditional mitigation

            # Map to exponential scale
            aggregate += severity_map.get(risk_level, 64)

        # Combine with index-based weight
        final_shift = 0
        for i, _ in enumerate(data_list):
            if i % 2 == 1:
                final_shift += i * 0.5

        return int(aggregate - final_shift)

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Unused diagnostic trace (distractor)
    debug_snapshot = []
    for i, row in enumerate(zip(raw_readings, derived_metrics)):
        debug_snapshot.append(f"Entry {i}: {row}")

    print(f"Result: {final_diagnostic}")

analyze_sensor_network()