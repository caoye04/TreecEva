def process_sensor_array(raw_readings, config_params):
    # Irrelevant preprocessing: normalize timestamps (not used)
    timestamps = [r[0] for r in raw_readings if len(r) > 0]
    normalized_times = [(t - min(timestamps)) / (max(timestamps) - min(timestamps) + 1e-9) for t in timestamps]

    # Distractor: unused transformation
    inverted_signals = [1.0 / (abs(r[1]) + 1) for r in raw_readings if r[1] != 0]

    # Relevant: extract sensor_id and reading pairs
    sensor_data = [(r[2], r[1]) for r in raw_readings if len(r) == 3 and r[2] is not None]

    # Dead code path: never accessed due to hard return
    def deprecated_filter(x):
        return x > -999  # Unused

    if not config_params.get('active', False):
        return {'status': 'inactive', 'value': 0}  # Not triggered

    # Destructuring assignment with red herring
    baseline, tolerance, activation = config_params['base'], config_params['tolerance'], config_params['activation']
    mode_flag = config_params['mode']  # Unused in logic

    # Slice only active sensors based on configuration
    start_idx = config_params.get('offset', 0)
    end_idx = start_idx + config_params.get('window_size', len(sensor_data))
    sliced_data = sensor_data[start_idx:end_idx]

    # Group readings by sensor ID using dictionary
    grouped = {}
    for sid, val in sliced_data:
        if sid not in grouped:
            grouped[sid] = []
        grouped[sid].append(val)

    # Compute aggregate statistics (some irrelevant)
    averages = {}
    variances = {}  # Computed but not used later
    for sid, vals in grouped.items():
        avg = sum(vals) / len(vals)
        averages[sid] = avg
        variance = sum((v - avg) ** 2 for v in vals) / len(vals)
        variances[sid] = variance  # Distraction

    # Set operation: find anomalous sensors
    reference_sensors = {'S1', 'S2', 'S3', 'S4', 'S5'}
    deployed_sensors = set(grouped.keys())
    mismatched_sensors = reference_sensors.symmetric_difference(deployed_sensors)  # Misleading metric

    # Filter sensors based on average deviation from baseline
    filtered_ids = set()
    for sid, avg_val in averages.items():
        deviation = abs(avg_val - baseline)
        if deviation >= tolerance * 2:  # Strict filtering condition
            filtered_ids.add(sid)

    # Extract filtered data for analysis
    filtered_data = [item for item in sliced_data if item[0] in filtered_ids]

    # Create threshold map (complex structure, partially used)
    threshold_map = {}
    for sid in filtered_ids:
        base_th = baseline + tolerance
        hysteresis = 0.1 * base_th
        threshold_map[sid] = {
            'upper': base_th + hysteresis,
            'lower': base_th - hysteresis,
            'weight': 1.0  # Unused field
        }

    # Call final analysis function
    final_diagnostic = analyze_readings(filtered_data, threshold_map)
    return final_diagnostic


def analyze_readings(readings, thresholds):
    if not readings:
        return -1

    # Count per-sensor occurrences
    count_per_sensor = {}
    for sid, val in readings:
        count_per_sensor[sid] = count_per_sensor.get(sid, 0) + 1

    # Use set to deduplicate sensor IDs
    unique_sensors = set(count_per_sensor.keys())

    total_exceedances = 0
    for sid, val in readings:
        th = thresholds.get(sid, {})
        upper_limit = th.get('upper', 0)
        if val > upper_limit:
            total_exceedances += 1

    # Complex conditional expression
    adjustment_factor = 1.5 if len(unique_sensors) > 2 else (2.0 if total_exceedances > 5 else 1.2)

    # Final computation
    severity_score = (sum(count_per_sensor.values()) * adjustment_factor) + total_exceedances

    # Early return based on sensor count
    if len(unique_sensors) == 0:
        return 0

    return int(severity_score)

# Main execution block
if __name__ == '__main__':
    # Simulated input data: (timestamp, reading_value, sensor_id)
    sensor_input = [
        (1001, 102.3, 'S1'), (1002, 99.1, 'S2'), (1003, 150.5, 'S3'),
        (1004, 101.0, 'S1'), (1005, 89.2, 'S4'), (1006, 160.3, 'S3'),
        (1007, 95.4, 'S2'), (1008, 170.1, 'S5'), (1009, 103.2, 'S1'),
        (1010, 165.0, 'S3'), (1011, 91.0, 'S4'), (1012, 158.7, 'S5')
    ]

    config = {
        'active': True,
        'base': 100.0,
        'tolerance': 10.0,
        'activation': True,
        'mode': 'diagnostic',
        'offset': 0,
        'window_size': 12
    }

    result = process_sensor_array(sensor_input, config)
    print(f"Target result: {result}")