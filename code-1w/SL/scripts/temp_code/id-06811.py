def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing: normalize data (not used in final result)
    normalized = [x / max(raw_readings) for x in raw_readings]
    inverted = [1 - val for val in normalized if val < 0.9]

    # Distractor: complex frequency analysis with unused outcome
    frequency_map = {}
    for reading in raw_readings:
        freq = raw_readings.count(reading)
        frequency_map[reading] = freq
    entropy_approx = 0
    for freq in frequency_map.values():
        if freq > 1:
            entropy_approx += freq * freq

    # Real computation begins: extract key thresholds
    thresholds = []
    for i, val in enumerate(calibration_sequence):
        if i % 2 == 0 and val > 50:
            thresholds.append(val // (i + 1))

    # Use of zip to align metadata (some relevant, some not)
    timestamps = [100, 105, 110, 115, 120]
    labeled_data = list(zip(timestamps, raw_readings))
    active_segments = [td[1] for td in labeled_data if td[0] % 10 == 0]

    # Dead code path: never executed due to condition
    backup_correction = 0
    if len(active_segments) > 100:
        for idx, seg in enumerate(active_segments):
            backup_correction += seg * idx

    # Core logic chain
    base_energy = sum(active_segments)  # Step 1
    outlier_count = 0
    for val in raw_readings:
        if val < 30 or val > 95:
            outlier_count += 1  # Step 2

    # Conditional branching based on parity
    if outlier_count % 2 == 0:  # Step 3
        adjustment_multiplier = 3
    else:
        adjustment_multiplier = -2

    # Bit manipulation red herring
    bit_analysis = 0
    for val in calibration_sequence:
        bit_analysis ^= (val << 2) & 0xFF  # Unused transformation

    # Slicing operation with partial relevance
    window_slice = raw_readings[2:7:2]  # Elements at index 2, 4, 6
    transient_peak = max(window_slice) if window_slice else 0  # Step 4

    # Multiple assignment distraction
    (alpha, beta, gamma) = (10, 20, 30)
    gamma = transient_peak // 5  # Step 5

    # Conditional expression influencing flow
    correction_factor = gamma if gamma > 4 else 12  # Step 6

    # Data structure cross-reference
    stats_bundle = {
        'peaks': [x for x in raw_readings if x > 80],
        'stable': [x for x in raw_readings if 40 <= x <= 70]
    }
    peak_concentration = len(stats_bundle['peaks']) * 2  # Step 7

    # Aggregate score construction
    aggregate_score = base_energy + peak_concentration  # Step 8

    # Key statement
    final_diagnostic = aggregate_score + correction_factor * adjustment_multiplier

    # Final red herring: unused conditional reassignment
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) >> 1

    return final_diagnostic

# Execution context
sensor_input = [85, 90, 25, 70, 95, 65, 30, 88]
calib_seq = [60, 45, 72, 55, 88, 50, 63]
result = analyze_sensor_data(sensor_input, calib_seq)
print(f"Target result: {result}")