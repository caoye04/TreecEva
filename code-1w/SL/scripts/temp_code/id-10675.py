def analyze_sensor_data(raw_readings, calibration_offset):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.98 + 3 for x in raw_readings]
    filtered = [x for x in normalized if x > 20]

    # Real processing begins
    base_metrics = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            base_metrics.append(val ** 0.5)
        else:
            base_metrics.append(val // 4)

    # Misleading intermediate (looks important but unused)
    temp_adjustment = sum(normalized) / len(normalized) - calibration_offset

    # Core logic: compute diagnostic indices
    index_map = {}
    for idx, (a, b) in enumerate(zip(base_metrics[:-1], base_metrics[1:])):
        diff = abs(b - a)
        if diff > 5:
            index_map[idx] = diff * 1.5

    # Decoy function call (never used)
    def compute_variance(data):
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)

    # Actual aggregation
    spike_count = len(index_map)
    aggregate_score = sum(index_map.values())

    # Red herring: complex-looking but irrelevant bitwise logic
    mask = 0b1101
    masked_values = [i ^ mask for i in range(spike_count)]
    decoy_entropy = sum(masked_values) % 17

    # Correction based on calibration and pattern density
    density_ratio = len([x for x in raw_readings if x > 50]) / len(raw_readings)
    if density_ratio > 0.3:
        correction_factor = calibration_offset * 2.5
    else:
        correction_factor = -calibration_offset * 1.2

    # Dead code path (never executed due to input constraints)
    if False:
        fallback = sum(normalized) * 0.1
        correction_factor += fallback  # unreachable

    # Critical assignment
    final_diagnostic = aggregate_score + correction_factor

    # Unused set operations (distractor)
    unique_spikes = set(index_map.keys())
    expected_peaks = set(range(0, len(raw_readings), 3))
    overlap = unique_spikes & expected_peaks  # computed but not used

    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data (fixed for determinism)
data_stream = [12, 64, 8, 72, 16, 80, 24, 88, 32, 96]
offset = 4

# Execute
result = analyze_sensor_data(data_stream, offset)