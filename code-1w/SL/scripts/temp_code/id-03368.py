def analyze_sensor_data():
    # Simulated sensor readings from multiple sources
    sensor_inputs = [23.4, 19.8, 20.1, 25.5, 18.9, 22.3, 20.0, 21.7]
    calibration_offsets = [0.1, -0.2, 0.05, 0.3, -0.15, 0.0, 0.2, -0.1]

    # Irrelevant auxiliary data (distraction)
    device_ids = ['D9F2', 'A1C7', 'B8E3', 'Z9X1', 'M4N6', 'P7Q5', 'R2S8', 'T3U9']
    location_tags = ['north', 'south', 'east', 'west', 'center', 'northeast', 'southwest', 'midfield']

    corrected_readings = []
    for i, reading in enumerate(sensor_inputs):
        corrected = reading + calibration_offsets[i]
        if corrected > 22.0:
            status_flag = 1
        elif corrected < 20.0:
            status_flag = -1
        else:
            status_flag = 0
        corrected_readings.append((corrected, status_flag))

    # Dead code path - never executed due to logic above (red herring)
    legacy_mode = False
    if legacy_mode:
        temp_buffer = [0] * len(sensor_inputs)
        for j in range(len(temp_buffer)):
            temp_buffer[j] = sensor_inputs[j] * 1.01

    # Distractor: complex but unused data transformation
    paired_diagnostics = list(zip(device_ids, location_tags, sensor_inputs))
    sorted_pairs = sorted(paired_diagnostics, key=lambda x: x[2], reverse=True)
    top_three_devices = [pair[0] for pair in sorted_pairs[:3]]

    # Real computation begins here — heavily buried
    base_values = [val for val, _ in corrected_readings]
    valid_range_count = sum(1 for v in base_values if 19.5 <= v <= 21.5)

    # Bit manipulation decoy (looks important but unused)
    checksum = 0
    for val in sensor_inputs:
        int_part = int(abs(val))
        checksum ^= int_part << 2
        checksum |= int_part >> 1

    # More distractions: fake anomaly detection
    anomalies = []
    for idx, (val, flag) in enumerate(corrected_readings):
        if flag != 0 and idx % 2 == 0:
            anomalies.append((idx, val))

    # Actual relevant logic chain starts here
    average_corrected = sum(base_values) / len(base_values)
    deviation_scores = [abs(v - average_corrected) for v in base_values]
    aggregate_score = sum(deviation_scores) * valid_range_count

    # Unused sorting distraction
    sorted_deviation_indices = [i for i, _ in sorted(enumerate(deviation_scores), key=lambda x: x[1], reverse=True)]

    # Key variables for final calculation
    temperature_factor = base_values[0] - base_values[-1]
    phase_shift = len([d for d in deviation_scores if d > 1.0])

    # Critical statement buried among distractions
    final_diagnostic = aggregate_score + temperature_factor * phase_shift

    # Another red herring: attempt to reprocess using enumerate and zip (unused)
    indexed_map = list(enumerate(zip(base_values, calibration_offsets)))
    processed_map = []
    for index, (value, offset) in indexed_map:
        if index % 3 == 0:
            processed_map.append(value * 0.95 + offset)

    # Final output
    print(f"Result: {final_diagnostic}")

analyze_sensor_data()