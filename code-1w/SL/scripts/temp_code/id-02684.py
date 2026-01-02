def process_sensor_array():
    # Simulated environmental sensor readings (temperature, humidity, pressure)
    raw_readings = [
        (23.5, 45.2, 1013.2), (24.1, 47.8, 1012.9), (19.8, 52.1, 1014.1),
        (20.2, 50.3, 1013.8), (22.0, 48.7, 1013.0), (25.3, 46.5, 1012.5),
        (18.7, 55.6, 1014.5), (26.0, 44.0, 1012.0), (21.5, 49.0, 1013.4)
    ]

    # Irrelevant transformation: convert to string representations
    str_readings = [f'{t:.1f},{h:.1f},{p:.1f}' for t, h, p in raw_readings]
    parsed_back = [tuple(map(float, s.split(','))) for s in str_readings]  # Redundant round-trip

    # Distractor: secondary fake sensor data with no impact
    gps_coordinates = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]
    elevation_data = {coord: idx * 150 + 10 for idx, coord in enumerate(gps_coordinates)}

    # Actual filtering: isolate readings where temperature > 20 and humidity < 50
    filtered_data = [entry for entry in raw_readings if entry[0] > 20 and entry[1] < 50]

    # Threshold configuration map (key: metric index, value: alert threshold)
    threshold_map = {
        0: 24.0,  # temp threshold
        1: 46.0,  # humidity threshold
        2: 1013.0  # pressure threshold
    }

    # Decoy structure: unused complex default dictionary
    from collections import defaultdict
    history_log = defaultdict(lambda: {'count': 0, 'values': []})
    for i, reading in enumerate(raw_readings):
        history_log[f'sensor_{i % 3}']['count'] += 1
        history_log[f'sensor_{i % 3}']['values'].append(reading[0])

    # Distractor: set operations with no downstream effect
    unique_temps = set(round(t) for t, _, _ in raw_readings)
    expected_days = set(range(1, 10))
    overlap_count = len(unique_temps.intersection(expected_days))  # unused

    # Secondary filtering: only high-pressure stability readings
    stable_pressure = [p for _, _, p in filtered_data if abs(p - 1013.0) < 0.8]
    pressure_variance = sum((p - 1013.0) ** 2 for p in stable_pressure) / len(stable_pressure) if stable_pressure else 0

    # Diagnostic analysis function (closure to add complexity)
    def analyze_readings(data, thresholds):
        alerts = 0
        metrics = ['temperature', 'humidity', 'pressure']
        severity_weights = {0: 1.2, 1: 0.8, 2: 0.5}

        # Enumerate over data points with zip to align with dummy labels
        labels = [f'reading_{i}' for i in range(len(data))]
        for label, (t, h, p) in zip(labels, data):
            values = [t, h, p]
            for i, (val, lim) in enumerate(zip(values, thresholds.values())):
                if val > lim:
                    alerts += severity_weights[i]

        # Complex decoy calculation with dictionaries and enumeration
        trend_analysis = {}
        for idx, (temp, hum, _) in enumerate(data):
            adjusted_index = idx + 1
            trend_analysis[f'point_{idx}'] = {
                'index': adjusted_index,
                'ratio': hum / (temp + 0.1),
                'flag': hum / (temp + 0.1) > 2.0
            }

        # Unused but misleading intermediate result
        high_ratio_points = {k: v for k, v in trend_analysis.items() if v['flag']}
        correlation_score = len(high_ratio_points) * 0.3 if high_ratio_points else 0.0

        # Real return value buried among distractions
        base_alerts = int(alerts)
        adjustment = 17 if pressure_variance < 0.3 else -5
        return base_alerts * 100 + adjustment

    # Key execution point
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    
    # Additional red herring: dictionary pop operations
    temp_summary = {"avg": sum(t for t,_,_ in filtered_data)/len(filtered_data), "count": len(filtered_data)}
    temp_summary.pop("count", None)  # irrelevant mutation

    # Final output
    print(f"Result: {final_diagnostic}")

process_sensor_array()