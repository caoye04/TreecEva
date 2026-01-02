def sensor_diagnostic():
    raw_data = [14.2, 15.1, 13.8, 16.0, 14.5, 15.3, 13.9, 14.7]
    calibration_offsets = {'sensor_a': 0.12, 'sensor_b': -0.08, 'sensor_c': 0.15}
    base_threshold = 14.0

    # Irrelevant transformation: historical averages not used later
    historical_avg = sum([13.5, 14.1, 13.9, 14.3]) / 4
    temp_correction = [x * 1.02 for x in raw_data if x > 14.0]

    # Distractor: complex but unused data structure
    decoy_matrix = [[i + j * 0.1 for j in range(4)] for i in range(4)]
    for row in decoy_matrix:
        row.append(sum(row) / len(row))

    # Actual processing begins
    processed_metrics = [x + 0.05 for x in raw_data]  # minor correction

    # Misleading branch: looks important but doesn't affect final result
    if len(processed_metrics) > 5:
        smoothed = [processed_metrics[i] for i in range(0, len(processed_metrics), 2)]
    else:
        smoothed = processed_metrics.copy()

    # Unused function: red herring
    def validate_integrity(data):
        return all(x > 0 for x in data)

    # Another distractor variable
    outlier_flags = [i for i, x in enumerate(processed_metrics) if abs(x - base_threshold) > 1.5]

    # Real logic hidden among noise
    critical_zones = {i: val for i, val in enumerate(processed_metrics) if val > base_threshold}

    # Threshold map with decoy keys
    threshold_map = {
        'normal': base_threshold,
        'caution': base_threshold + 0.8,
        'alert': base_threshold + 1.5,
        'decoy_mode': 999.9  # never used
    }

    # Simulated device status (irrelevant)
    device_status = {'state': 'active', 'uptime': 1275, 'version': '2.1.0'}
    heartbeat_interval = device_status.get('uptime') % 60

    # Core analysis function
    def analyze_readings(metrics, thresholds):
        count_above_normal = sum(1 for v in metrics if v > thresholds['normal'])
        count_above_caution = sum(1 for v in metrics if v > thresholds['caution'])
        count_above_alert = sum(1 for v in metrics if v > thresholds['alert'])

        # Complex weighting formula
        severity_score = (
            count_above_normal * 1.0 +
            count_above_caution * 2.5 +
            count_above_alert * 5.0
        )

        # Early return red herring - condition not met
        if severity_score < 0:
            return -1

        adjustment_factor = 0.8 if count_above_alert > 0 else 1.1
        adjusted_score = severity_score * adjustment_factor

        # Final diagnostic is integer-rounded score
        return int(round(adjusted_score))

    # Key assignment statement
    final_diagnostic = analyze_readings(processed_metrics, threshold_map)

    # Dead code path
    if final_diagnostic < 0:
        final_diagnostic = 0

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Unused cleanup
    del decoy_matrix

    return final_diagnostic

# Execute and capture result
sensor_diagnostic()