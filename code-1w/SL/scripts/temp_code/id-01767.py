def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.005 for x in raw_readings if x > 0]
    outliers = [i for i, v in enumerate(normalized) if v > 100]
    filtered = [v for v in normalized if v <= 100]

    # Key data transformation chain
    processed = []
    shift_key = sum(calibration_sequence) % 8
    for i, val in enumerate(filtered):
        shifted = val >> 2
        masked = shifted & 0xFF
        if i % 3 == 0:
            masked ^= 0xAA  # Bit flip pattern
        processed.append(masked)

    # Dead code path - never executed due to logic (misleading)
    secondary_buffer = []
    if len(outliers) > 100:
        for item in outliers:
            temp = item << 3
            temp |= 0x0F
            secondary_buffer.append(temp)

    # Core calculation with distractors
    base_metrics = {i: v * 1.75 for i, v in enumerate(processed)}
    adjusted_metrics = {}
    for idx, value in base_metrics.items():
        if idx % 4 == 0:
            adjusted_metrics[idx] = round(value * 0.88)
        elif idx % 4 == 2:
            adjusted_metrics[idx] = round(value * 1.02)
        else:
            adjusted_metrics[idx] = value  # No change

    # Use of zip and enumerate (required feature)
    timestamps = list(range(len(processed)))
    paired_data = list(zip(timestamps, processed))
    index_map = {ts: idx for idx, ts in enumerate(timestamps)}

    # Set operations as distractor (irrelevant to final result)
    unique_values = set(processed)
    expected_range = set(range(256))
    missing_in_sample = expected_range - unique_values  # Unused

    # Another decoy function embedded
    def validate_checksum(data):
        return sum(data) % 256 == 0  # Never called

    # Critical computation interwoven with noise
    aggregate_score = 0
    for i, (ts, val) in enumerate(paired_data):
        if val in unique_values and ts in index_map:  # Always true
            contribution = val ^ (ts & 0x0F)
            aggregate_score += contribution

    # Misleading intermediate that looks important
    entropy_proxy = len(unique_values) / 256.0
    scaling_hint = len(paired_data) // 4
    correction_factor = 0
    for k in sorted(adjusted_metrics.keys()):
        if k < scaling_hint:
            correction_factor += adjusted_metrics[k] % 7
        else:
            correction_factor -= adjusted_metrics[k] % 5

    # Final assignment with key variables
    temporal_weight = len(timestamps) // 2
    auxiliary_offset = sum(calibration_sequence[:3]) % 100
    final_diagnostic = aggregate_score + correction_factor

    # Output required result
    print(f"Result: {final_diagnostic}")

# Inputs
readings = [123, 45, 67, 89, 91, 105, 44, 33, 77, 88]
calib_seq = [17, 23, 19, 61, 55]
analyze_sensor_data(readings, calib_seq)