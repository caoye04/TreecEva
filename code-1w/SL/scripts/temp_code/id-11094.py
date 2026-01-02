def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing: reverse string labels (distractor)
    labeled_sensors = ['sensor_' + x[::-1] for x in ['aeg', 'beg', 'ceg']]
    temp_buffer = []
    for val in raw_readings:
        if val > thresholds['upper']:
            temp_buffer.append(val * 0.9)  # Dampen high values (unused later)

    # Real data path begins: filter valid readings
    valid_readings = [v for v in raw_readings if v >= thresholds['lower']]
    sorted_readings = sorted(valid_readings)  # Sorting for median calculation

    # Compute statistical features (some are red herrings)
    mean_val = sum(sorted_readings) / len(sorted_readings)
    median_val = sorted_readings[len(sorted_readings)//2]
    variance_proxy = sum((x - mean_val) ** 2 for x in sorted_readings)
    std_dev_approx = variance_proxy ** 0.5

    # Bit manipulation decoy (irrelevant)
    bit_analysis = 0
    for i in range(3):
        bit_analysis ^= (len(raw_readings) << i)

    # Set operations for anomaly detection (core concept)
    expected_set = set(range(50, 150))
    observed_set = set(int(x) for x in sorted_readings)
    anomalies = observed_set - expected_set  # Out-of-bound readings
    anomaly_count = len(anomalies)

    # String-based status encoding (distractor)
    status_flags = []
    for a in anomalies:
        flag_str = f"ERR_{a}".replace('ERR', 'FAULT')
        status_flags.append(flag_str.lower())

    # Core diagnostic logic (buried among noise)
    base_score = 0
    for r in sorted_readings:
        if r < 60:
            base_score += 3
        elif r < 100:
            base_score += 1
        else:
            base_score -= 2

    # Secondary adjustment using modular arithmetic (valid path)
    cycle_adjustment = (len(valid_readings) % 7) * 5

    # Early return decoy (never reached due to condition)
    if len(raw_readings) < 0:  # Impossible condition
        return -999

    # Aggregation with misleading intermediate variables
    aggregate_score = base_score + cycle_adjustment
    correction_factor = 4

    # Critical assignment: this is the target execution point
    final_diagnostic = aggregate_score + correction_factor * anomaly_count

    # Dead code path: unreachable due to prior logic
    redundant_calc = None
    if False and temp_buffer:
        redundant_calc = max(temp_buffer) - min(temp_buffer)

    # Unused tuple unpacking (distractor)
    config_defaults = (200, 0.5, 'auto')
    max_limit, sensitivity, mode = config_defaults

    # Output the required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate sensor data
readings = [45, 55, 58, 95, 105, 160]
limits = {'lower': 50, 'upper': 200}
result = analyze_sensor_data(readings, limits)