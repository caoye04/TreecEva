import itertools

# Simulated sensor array diagnostics with noise filtering and anomaly detection
def analyze_sensor_cluster(raw_readings, baseline_threshold=0.75):
    filtered_signals = []
    noise_floor = 0.1
    spike_count = 0
    cumulative_drift = 0.0
    temporal_gaps = []

    for idx, reading in enumerate(raw_readings):
        if idx > 0:
            gap = abs(reading - raw_readings[idx-1])
            temporal_gaps.append(gap)
            if gap > 0.8:
                spike_count += 1

        adjusted = reading - noise_floor
        if adjusted > baseline_threshold:
            filtered_signals.append(adjusted)

    # Distractor: unused transformation path
    if len(temporal_gaps) > 5:
        smoothed_gaps = [g * 0.9 for g in temporal_gaps if g < 1.0]
        average_smoothing = sum(smoothed_gaps) / len(smoothed_gaps) if smoothed_gaps else 0.0
        # Dead code branch - never impacts final result
        for i in range(len(filtered_signals)):
            filtered_signals[i] -= average_smoothing  # Irrelevant adjustment

    # Real signal processing branch
    valid_peaks = [sig for sig in filtered_signals if sig > baseline_threshold]
    peak_magnitude = sum(valid_peaks) if valid_peaks else 0.0

    # Bitwise telemetry signature (red herring)
    telemetry_checksum = 0
    for val in raw_readings[:4]:
        telemetry_checksum ^= int(val * 10) & 0xFF
    telemetry_checksum = telemetry_checksum | 0x10  # Constant flag set (unused)

    # Set operations for redundancy validation (distractor)
    primary_set = set(itertools.islice(raw_readings, 0, None, 2))
    secondary_set = set(itertools.islice(raw_readings, 1, None, 2))
    overlap_count = len(primary_set & secondary_set)
    redundancy_score = overlap_count * 0.05  # Computed but not used

    # Actual diagnostic logic (non-obvious due to distractions)
    duration_factor = len(raw_readings) // 10
    stability_modifier = 1 + (spike_count * -0.1)
    aggregate_score = (peak_magnitude * 100) + (duration_factor * 10)

    # Critical conditional: anomaly detection override
    if spike_count >= 3 and any(abs(g) > 1.2 for g in temporal_gaps):
        anomaly_flag = -50
    else:
        anomaly_flag = 10

    # Key statement
    final_diagnostic = aggregate_score + anomaly_flag

    # Multiple print statements to obscure relevance
    print(f"Signal peaks: {valid_peaks}")
    print(f"Telemetry checksum: {telemetry_checksum:02X}")
    print(f"Redundancy score: {redundancy_score:.3f}")
    print(f"Spike events: {spike_count}")

    return final_diagnostic

# Irrelevant global computation
CONSTANT_OFFSET = sum(i**2 for i in range(5))  # 30, unused

# Input data with embedded pattern
sensor_input = [0.2, 0.85, 0.15, 0.92, 0.05, 0.88, 0.79, 0.94, 0.11, 0.87, 0.93]

# Execution point of interest
result = analyze_sensor_cluster(sensor_input)

# Target result output
print(f"Result: {result}")