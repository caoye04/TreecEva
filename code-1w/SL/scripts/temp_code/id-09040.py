def analyze_sensor_network():
    # Simulated environmental sensor network data
    raw_readings = [
        (101, [23.4, 18.9, 25.1, 20.3]),
        (102, [19.5, 21.2, 18.7, 20.1]),
        (103, [24.6, 25.8, 23.9, 26.1]),
        (104, [17.3, 16.9, 18.2, 17.5]),
        (105, [22.0, 20.8, 23.1, 21.9])
    ]

    # Irrelevant calibration metadata (distractor)
    calibration_log = {
        'device_101': {'offset': 0.12, 'gain': 1.03},
        'device_102': {'offset': -0.08, 'gain': 0.99},
        'device_103': {'offset': 0.15, 'gain': 1.01},
        'device_104': {'offset': -0.11, 'gain': 0.97},
        'device_105': {'offset': 0.05, 'gain': 1.02}
    }

    # Decoy function - looks important but unused (dead code path)
    def apply_calibration(data, calib):
        return [[(val + calib['offset']) * calib['gain'] for val in series] for series in data]

    # Historical baselines (misleading context)
    historical_averages = {
        'zone_a': 21.5,
        'zone_b': 19.8,
        'zone_c': 24.2,
        'zone_d': 17.0,
        'zone_e': 21.0
    }

    # Real processing begins: extract and flatten readings
    flattened = []
    for sensor_id, readings in raw_readings:
        for temp in readings:
            flattened.append((sensor_id, temp))

    # Group by sensor ID using enumerate (relevant)
    grouped = {}
    for idx, (sid, temp) in enumerate(flattened):
        if sid not in grouped:
            grouped[sid] = []
        grouped[sid].append((idx, temp))  # include index for no real reason (partial distractor)

    # Extract only temperatures, discarding indices (relevant simplification)
    temp_only = {}
    for sid, records in grouped.items():
        temp_only[sid] = [temp for _, temp in records]

    # Calculate moving averages (irrelevant computation)
    moving_averages = {}
    for sid, temps in temp_only.items():
        avgs = []
        for i in range(2, len(temps)):
            avgs.append(sum(temps[i-2:i+1]) / 3)
        moving_averages[sid] = avgs

    # Threshold policy map (critical for final logic)
    threshold_map = {
        101: {'low': 20.0, 'high': 25.0},
        102: {'low': 19.0, 'high': 22.0},
        103: {'low': 24.0, 'high': 26.0},
        104: {'low': 16.5, 'high': 18.0},
        105: {'low': 20.5, 'high': 23.5}
    }

    # Flag anomalous readings (core relevant logic)
    anomalies = []
    for sid, temps in temp_only.items():
        thresholds = threshold_map[sid]
        for temp in temps:
            if temp < thresholds['low'] or temp > thresholds['high']:
                anomalies.append((sid, temp))

    # Filter original data to only high-stability sensors (key step)
    stable_sensors = [101, 103, 105]  # manually defined (could be derived, but hardcoded here)
    filtered_data = {sid: temp_only[sid] for sid in stable_sensors if sid in temp_only}

    # Auxiliary statistic (distractor)
    variance_report = {}
    for sid, temps in filtered_data.items():
        mean = sum(temps) / len(temps)
        variance_report[sid] = sum((t - mean) ** 2 for t in temps) / len(temps)

    # Core diagnostic processor
    def process_readings(data, thresholds):
        diagnostic_score = 0
        # Use zip to pair sensors with their threshold sets (required idiom)
        for (sid, temps), (tid, thres) in zip(data.items(), thresholds.items()):
            assert sid == tid  # consistency check
            base_ref = thres['high'] - thres['low']
            for temp in temps:
                deviation = abs(temp - ((thres['low'] + thres['high']) / 2))
                # Only count significant deviations beyond half-range
                if deviation > base_ref * 0.5:
                    diagnostic_score += int(deviation * 10)  # amplify impact
        return diagnostic_score * len(data)  # scale by number of sensors

    # Final computation (target execution point)
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Dead-end reporting function (unused, misleading)
    def generate_compliance_report(score, anomalies):
        level = 'CRITICAL' if score > 100 else 'WARNING' if score > 50 else 'OK'
        return {'status': level, 'anomaly_count': len(anomalies)}

    # Print result as required
    print(f"Target result: {final_diagnostic}")

    # Return nothing; just ensure side effect occurs
    return None

# Execute the simulation
analyze_sensor_network()