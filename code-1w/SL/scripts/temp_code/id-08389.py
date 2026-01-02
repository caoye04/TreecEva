def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature, humidity, pressure)
    raw_readings = [
        (23.4, 45.2, 1013.2), (24.1, 47.8, 1012.1), (19.5, 51.0, 1015.6),
        (22.8, 44.3, 1010.9), (35.6, 30.1, 1020.0), (20.2, 55.7, 1014.3),
        (21.0, 48.9, 1011.8), (25.5, 46.5, 1009.4), (18.9, 59.2, 1016.7),
        (26.7, 43.8, 1008.2)
    ]

    # Irrelevant baseline metadata (distractor)
    station_metadata = {
        'location': 'Grid-7B',
        'calibration_date': '2023-11-05',
        'firmware': 'v2.1.8'
    }

    # Thresholds for anomaly detection (used later)
    threshold_map = {
        'temp_high': 30.0,
        'temp_low': 20.0,
        'humidity_high': 50.0,
        'pressure_trend': -2.0
    }

    # Decoy transformation: string processing with no impact on result (distractor)
    status_flags = ['OK', 'WARN', 'CRITICAL']
    flag_summary = ''.join([f[0] for f in status_flags])  # 'OWC'

    # Extract timestamps (fake data - irrelevant)
    timestamps = [f'2023-12-01T0{i}:00:00Z' for i in range(10)]
    recent_times = [t for t in timestamps if 'T0' in t]

    # Destructuring with enumerate to filter valid sensors (real logic starts)
    filtered_data = []
    for idx, (temp, hum, press) in enumerate(raw_readings):
        if temp < 35.0 and hum > 30.0:  # Filter out extreme temp and low humidity
            filtered_data.append((idx, temp, hum, press))

    # Dead code path: never executed due to condition (red herring)
    backup_mode = False
    if len(filtered_data) > 20:
        backup_mode = True
        fallback_result = sum(press for _, _, _, press in raw_readings) / len(raw_readings)

    # Auxiliary function: computes rolling pressure delta (partially relevant)
    def compute_pressure_trend(data):
        if len(data) < 2:
            return 0.0
        deltas = []
        for i in range(1, len(data)):
            deltas.append(data[i][3] - data[i-1][3])  # pressure difference
        return sum(deltas) / len(deltas)

    avg_pressure_change = compute_pressure_trend(filtered_data)

    # Another decoy: zip with unrelated transformation
    indices, temps, hums, pressures = zip(*filtered_data)
    labeled_readings = list(zip(indices, [f'Sensor-{i}' for i in indices]))

    # String method distraction: building diagnostic tag (irrelevant)
    diagnostic_tag = 'ENV-' + 'SENSOR'.lower().replace('s', 'S') + '-CHK'

    # Core processing function (contains key logic)
    def process_readings(data, thresholds):
        high_temp_count = 0
        high_hum_count = 0
        total_score = 0.0

        for entry in data:
            _, temp, hum, press = entry

            # Count anomalies
            if temp > thresholds['temp_high']:
                high_temp_count += 1
            if hum > thresholds['humidity_high']:
                high_hum_count += 1

            # Scoring logic
            score_contrib = temp * 0.3 + hum * 0.2
            if temp < thresholds['temp_low']:
                score_contrib *= 1.2  # cold penalty
            total_score += score_contrib

            # Early termination if critical pattern found (short-circuit)
            if temp > 34.0 and hum < 35.0:
                return int(total_score) - 100  # emergency offset

        # Final computation combining multiple factors
        trend_factor = 1.0 if avg_pressure_change > threshold_map['pressure_trend'] else 0.8
        adjusted_score = total_score * trend_factor

        # Bit manipulation for "diagnostic hash" (only one bit matters)
        diagnostic_hash = (high_temp_count << 3) | (high_hum_count << 1) | 1
        severity_level = diagnostic_hash & 0b1111  # mask last 4 bits

        return int(adjusted_score) + severity_level

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Unused branching (dead code - distractor)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        audit_log = [f'DIAG: {final_diagnostic}']

    print(f"Result: {final_diagnostic}")

analyze_sensor_network()