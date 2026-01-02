def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing: normalize string labels (distractor)
    label_prefix = 'SNSR'
    formatted_labels = [label_prefix + str(i).zfill(3) for i in range(len(raw_readings))]
    normalized_data = [round(x * 0.987, 4) for x in raw_readings if x > 0]  # Partial filtering (misleading)

    # Core signal extraction (relevant path)
    valid_signals = []
    for val in raw_readings:
        if val < 0:
            continue
        if val % 2 == 0:
            val = val // 2
        if val % 3 == 0:
            val = val // 3
        valid_signals.append(val)

    # Decoy transformation chain (dead path)
    transformed_mirror = []
    for x in reversed(calibration_sequence):
        if x > 50:
            transformed_mirror.append(x - 50)
        else:
            transformed_mirror.append(x + 10)
    mirror_sum = sum(transformed_mirror[:3])  # Unused result

    # Auxiliary computation: checksum (red herring)
    checksum = 0
    for i, c in enumerate(calibration_sequence):
        checksum += c * (i + 1)
    checksum %= 1000

    # Key data derivation
    base_intensity = sum(valid_signals)
    activation_peaks = len([x for x in valid_signals if x > 10])
    suppression_events = len([x for x in valid_signals if x < 5])

    # Intermediate metric with conditional logic (necessary step)
    if activation_peaks > suppression_events:
        aggregate_measure = base_intensity + activation_peaks * 2
    else:
        aggregate_measure = base_intensity - suppression_events

    # Distractor variables (unused but plausible)
    temp_buffer = [base_intensity, mirror_sum, checksum]
    metadata_flag = True if len(temp_buffer) == 3 else False

    # Correction logic based on parity and magnitude
    if base_intensity % 2 == 0:
        correction_factor = 1.75
    else:
        correction_factor = 1.25

    # Offset determined by logical expression
    peak_ratio = activation_peaks / (suppression_events + 1)
    offset_value = 15 if peak_ratio > 1.5 else 7

    # Critical assignment
    final_diagnostic = aggregate_measure * correction_factor + offset_value

    # Print required output
    print(f"Result: {final_diagnostic}")

# Simulate execution
sensor_input = [24, -5, 18, 12, 9, 36, 3]
calib_seq = [45, 62, 33, 71, 29]
analyze_sensor_data(sensor_input, calib_seq)