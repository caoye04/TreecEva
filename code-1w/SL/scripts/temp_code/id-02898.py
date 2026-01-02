def sensor_diagnostic_system():
    # Simulated sensor readings (temperature, pressure, humidity)
    raw_readings = [
        [23.5, 101.3, 45.0], [25.1, 102.0, 47.2], [22.8, 99.8, 44.1],
        [36.9, 115.4, 52.3], [24.0, 100.1, 46.0], [26.3, 103.7, 48.9],
        [21.7, 98.4, 43.5], [35.2, 112.8, 51.0], [27.4, 104.5, 49.3]
    ]

    # Irrelevant baseline metadata (distractor)
    device_info = {'model': 'XTR-9', 'firmware': '2.1.5', 'location': 'Sector_7'}
    calibration_offsets = {'temp': 0.2, 'pressure': -0.5, 'humidity': 1.1}
    status_flags = [0, 0, 1, 0, 0, 0, 0, 0, 0]  # Mostly unused

    # Thresholds for anomaly detection (used later)
    thresholds = {
        'temp_high': 30.0,
        'temp_low': 20.0,
        'pressure_high': 110.0,
        'pressure_low': 100.0,
        'humidity_high': 50.0
    }

    # Decoy function - never called (dead code path)
    def legacy_validation(data):
        return all(x > 0 for row in data for x in row)

    # Preprocessing: filter out readings where status flag is 1 (only index 2)
    filtered_readings = [
        reading for idx, reading in enumerate(raw_readings)
        if idx >= len(status_flags) or status_flags[idx] == 0
    ]

    # Apply fake 'calibration' using string-based logic (irrelevant offset application)
    calibrated = []
    offset_keys = list(calibration_offsets.keys())
    for i, row in enumerate(filtered_readings):
        temp_adj = row[0] + float('0.2')  # hardcoded to avoid using dict
        pressure_adj = row[1] + (-0.5)
        humidity_adj = row[2] + 1.1
        calibrated.append([temp_adj, pressure_adj, humidity_adj])

    # Extract high-risk candidates based on temperature > 30 (used)
    high_temp_indices = [i for i, r in enumerate(calibrated) if r[0] > 30.0]

    # Use enumerate and zip to create indexed tuples (partially relevant)
    labeled_data = [(f'S{idx}', *vals) for idx, vals in enumerate(calibrated)]
    names, temps, pressures, humidities = zip(*labeled_data)

    # Compute rolling average of pressure (distractor - not used in final result)
    pressure_rolling_avg = []
    window_size = 3
    for i in range(len(pressures) - window_size + 1):
        avg = sum(pressures[i:i+window_size]) / window_size
        pressure_rolling_avg.append(round(avg, 2))

    # Create threshold map with lambda functions (actually used)
    threshold_map = {
        'critical_temp': (lambda x: x > thresholds['temp_high']),
        'high_pressure': (lambda x: x > thresholds['pressure_high']),
        'high_humidity': (lambda x: x > thresholds['humidity_high'])
    }

    # Processed data: only keep rows with S label having odd number (meaningless filtering)
    processed_data = [
        (name, temp, pressure, humidity) for name, temp, pressure, humidity in labeled_data
        if int(name[1:]) % 2 == 1  # Only odd indices: S1, S3, S5, S7
    ]

    # Unused set operation (distractor)
    unique_temps = set(round(t, 1) for _, t, _, _ in processed_data)
    temp_categories = set()
    for t in unique_temps:
        if t < 25.0:
            temp_categories.add('cool')
        elif t < 30.0:
            temp_categories.add('normal')
        else:
            temp_categories.add('hot')

    # Real analysis function
    def analyze_readings(data, th_map):
        anomalies = 0
        for entry in data:
            _, t, p, h = entry
            # Check multiple conditions
            if th_map['critical_temp'](t):
                anomalies += 2
            if th_map['high_pressure'](p) and not th_map['critical_temp'](t):
                anomalies += 1
            if th_map['high_humidity'](h) and p > 105:
                anomalies += 1
        return max(anomalies, 1)  # At least 1 for safety

    # Key statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)

    # Dead-end calculation (misleading intermediate)
    aggregate_risk = 0
    for _, t, p, h in processed_data:
        risk_score = 0
        if t > 30: risk_score += 3
        if p > 110: risk_score += 2
        if h > 50: risk_score += 1
        aggregate_risk += risk_score  # Never used

    # Print result as required
    print(f"Target result: {final_diagnostic}")

    return final_diagnostic

# Execute and capture
result = sensor_diagnostic_system()