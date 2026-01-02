def analyze_sensor_stream(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize timestamps (not used in final result)
    timestamps = [r[0] for r in raw_readings]
    start_time = timestamps[0]
    normalized_times = [(t - start_time) * 1.0 for t in timestamps]

    # Distractor: complex-looking but unused transformation
    transformed_readings = []
    for i, r in enumerate(raw_readings):
        temp_val = r[1] * calibration_factor + (i % 7)
        if temp_val > 100:
            temp_val = (temp_val % 43) + 12
        transformed_readings.append((normalized_times[i], temp_val))

    # Actual relevant path begins: extract sensor values and filter anomalies
    sensor_values = [r[1] for r in raw_readings]
    valid_mask = [1 if 5 <= v <= 95 else 0 for v in sensor_values]

    # Use of enumerate and zip: relevant processing
    indexed_valid = [(i, sensor_values[i]) for i, valid in enumerate(valid_mask) if valid]
    filtered_data = [val for _, val in indexed_valid]  # Only values matter

    # Dead code path: defines alternate logic but never called
    def legacy_correction(data):
        return [d * 0.98 for d in data if d % 2 == 0]

    # Bitwise manipulation red herring
    checksum = 0
    for v in sensor_values:
        checksum ^= int(v) & 0xFF
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF

    # Decoy aggregation function
    outlier_score = sum(1 for v in sensor_values if v < 10 or v > 90)
    penalty_weight = outlier_score * 0.3

    # Real computation: dynamic threshold map based on data distribution
    mean_val = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in filtered_data) / len(filtered_data) if filtered_data else 0
    threshold_map = {
        'low': mean_val - variance_proxy * 0.5,
        'high': mean_val + variance_proxy * 0.5,
        'critical': mean_val + variance_proxy
    }

    # Core processing function (defined inside to increase nesting)
    def process_readings(data, thresholds):
        acc = 0
        history = []
        for idx, reading in enumerate(data):
            # Modular arithmetic with conditional update
            mod_index = idx % 4
            if mod_index == 0:
                acc += reading * 1.1
            elif mod_index == 1:
                acc -= reading * 0.2
            elif mod_index == 2:
                acc += (reading % 7) * 3
            else:
                acc = acc - (acc % (reading + 1)) if reading > 0 else acc

            # Accumulate history for decoy analysis
            history.append((idx, reading, acc))

        # Distractor: unused statistical summary
        avg_change = (history[-1][2] - history[0][2]) / len(history) if len(history) > 1 else 0
        volatility = sum(abs(history[i+1][2] - history[i][2]) for i in range(len(history)-1))

        # Final diagnostic depends only on accumulated value and thresholds
        if acc < thresholds['low']:
            return int(acc - 10)
        elif acc > thresholds['high']:
            return int(acc + 15)
        else:
            return int(acc)

    # Key assignment point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Red herring: additional unrelated diagnostics
    secondary_index = sum(1 for x in filtered_data if x > threshold_map['low']) * 2
    tertiary_flag = secondary_index & 0x1F

    # Output required variable
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated sensor input (deterministic)
data_stream = [
    (1609459200, 45), (1609459201, 50), (1609459202, 105), (1609459203, 60),
    (1609459204, 70), (1609459205, 5),   (1609459206, 80), (1609459207, 90),
    (1609459208, 25), (1609459209, 65)
]

# Execute with realistic calibration
result = analyze_sensor_stream(data_stream, calibration_factor=1.02)