def analyze_sensor_data(raw_readings, calibration_factor=1.05):
    # Irrelevant pre-processing: Normalize data (not used in final path)
    normalized = [x * calibration_factor for x in raw_readings if x > 0]
    filtered = [x for x in normalized if x < 1000]

    # Distractor variables and dead logic path
    temp_buffer = []
    for val in raw_readings:
        if val % 7 == 0:
            temp_buffer.append(val ** 0.5)

    # Real computation begins: transform critical subset
    critical_indices = [i for i in range(len(raw_readings)) if i % 3 == 0 and raw_readings[i] > 0]
    transformed = []
    for i in critical_indices:
        shifted = raw_readings[i] >> 2
        adjusted = shifted ^ 15
        transformed.append(adjusted)

    # Secondary distractor: complex but unused calculation chain
    entropy_proxy = 0
    for x in raw_readings:
        if x > 0:
            entropy_proxy += (x & 5) * (x | 3)
    entropy_proxy = entropy_proxy % 100 if entropy_proxy else 0

    # Core logic hidden among noise
    baseline = sum(transformed[:4]) // len(transformed[:4]) if transformed else 0
    offset_map = [baseline + i * 3 for i in range(8)]
    aggregate_metrics = [(x * 2) - 5 for x in offset_map]

    # Simulated processing loop with misleading counters
    processed_count = 0
    for step in range(len(raw_readings)):
        if step % 4 == 0:
            processed_count += 1
        elif step % 5 == 0:
            processed_count -= 1  # Red herring adjustment

    # Anomaly detection decoy (partially relevant)
    anomalies = [x for x in raw_readings if (x ^ 10) < 50]
    raw_anomaly_sum = sum(anomalies) // 2 if anomalies else 42
    anomaly_score = raw_anomaly_sum - 17

    # Key assignment — this is the target execution point
    final_diagnostic = aggregate_metrics[processed_count] + anomaly_score

    # Unrelated post-processing (dead code)
    checksum = 0
    for i, v in enumerate(aggregate_metrics):
        checksum ^= (v + i) & 255

    print(f"Result: {final_diagnostic}")

# Hidden seed ensures deterministic behavior
sensor_input = [128, -5, 42, 73, 0, 15, 96, 23, 88, 101, 34, 7, 55]
analyze_sensor_data(sensor_input)