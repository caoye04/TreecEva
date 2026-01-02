def analyze_sensor_data(raw_readings, threshold=75):
    # Simulate preprocessing: normalize and flag anomalies
    normalized = [round(x * 0.98 + 2.1, 2) for x in raw_readings]
    anomaly_flags = {i: abs(normalized[i] - raw_readings[i]) > 10 for i in range(len(raw_readings))}

    # Irrelevant transformation: frequency analysis (dead logic)
    frequency_map = {}
    for val in raw_readings:
        freq = len([x for x in raw_readings if x == val])
        frequency_map[val] = freq
    avg_frequency = sum(frequency_map.values()) / len(frequency_map) if frequency_map else 0

    # Decoy calculation: weighted average with unused coefficients
    weights = [0.1, 0.2, 0.3]
    weight_sum = sum(weights)
    decoy_avg = sum(normalized[i] % 3 * weights[i % 3] for i in range(len(normalized))) / len(normalized) if normalized else 0

    # Core logic: identify valid readings above dynamic threshold
    dynamic_caps = [min(val, 100 + (idx % 5)) for idx, val in enumerate(normalized)]
    capped_above_threshold = [val for val in dynamic_caps if val > threshold]

    # Misleading intermediate: transform but don't use
    transformed_outliers = []
    for i, val in enumerate(dynamic_caps):
        if val > 95 and i % 2 == 0:
            transformed_outliers.append(val * 1.5 - 7.7)

    # Conditional suppression: simulate calibration offset
    calibrated_results = []
    for val in capped_above_threshold:
        if val > 85:
            calibrated_results.append(val - 5.5)
        elif val > 80:
            calibrated_results.append(val - 2.0)
        else:
            calibrated_results.append(val)

    # Secondary filter: exclude values close to harmonic of threshold
    harmonic_block = threshold * 0.66  # ~50
    filtered_results = [val for val in calibrated_results if abs(val - harmonic_block) > 5]

    # Critical assignment point
    filtered_total = sum(filtered_results)

    # Unused diagnostic dump (distractor)
    diagnostics = {
        "raw_count": len(raw_readings),
        "anomalies_found": sum(anomaly_flags.values()),
        "peak_value": max(normalized) if normalized else 0,
        "decoy_metric": decoy_avg,
        "suppressed_count": len(transformed_outliers)
    }

    return filtered_total

# Simulated sensor input
sensor_input = [88, 92, 70, 96, 83, 77, 91, 65, 94, 87]
result = analyze_sensor_data(sensor_input, threshold=78)
filtered_total = result
print(f"Target result: {filtered_total}")