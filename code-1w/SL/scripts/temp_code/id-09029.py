def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing: normalize data (not actually used in final path)
    normalized = [max(0.0, min(1.0, x / 100.0)) for x in raw_readings]

    # Real computation begins: extract anomalies
    anomalies = []
    for i, val in enumerate(raw_readings):
        if val > thresholds[i % len(thresholds)] or val < -thresholds[i % len(thresholds)]:
            anomalies.append((i, val))

    # Distractor: complex lambda chain with no impact
    transform = lambda x: (x[1] ** 2) + 5
    processed_anomalies = list(map(transform, filter(lambda x: x[1] > 0, anomalies)))

    # Key intermediate: severity scores
    severity_scores = []
    for idx, reading in anomalies:
        base_score = abs(reading) * 0.7
        time_weight = (idx + 1) * 0.3
        adjusted = base_score + time_weight
        if adjusted > 10:
            adjusted = 10 + (adjusted - 10) * 0.1  # dampen extreme values
        severity_scores.append(adjusted)

    # Dead code path: unused recursive function
    def recursive_dampen(x, depth=0):
        if depth >= 3 or x <= 1:
            return x
        return recursive_dampen(x * 0.9, depth + 1)

    # Another red herring: zip two unrelated sequences
    timestamps = list(range(len(raw_readings)))
    paired_with_time = list(zip(timestamps, raw_readings))
    avg_gap = sum(b - a for a, b in zip(timestamps, timestamps[1:])) / len(timestamps) if len(timestamps) > 1 else 0

    # Simulated diagnostic flags (partially relevant)
    diagnostics = []
    for score in severity_scores:
        if score > 8:
            diagnostics.append(3)
        elif score > 5:
            diagnostics.append(2)
        else:
            diagnostics.append(1)

    # Unused bitwise manipulation distraction
    bit_encoded = 0
    for d in diagnostics:
        bit_encoded ^= (d << 2)
        bit_encoded |= (d & 1)

    # Weight assignment (some weights are decoys)
    weights = [1.0, 0.5, 2.0, 1.5, 0.8]  # only first three matter due to truncation

    # Core aggregation logic (truncated to first 3)
    def aggregate_metrics(diagnostics, weights):
        truncated_diagnostics = diagnostics[:3]
        truncated_weights = weights[:3]
        weighted_sum = sum(d * w for d, w in zip(truncated_diagnostics, truncated_weights))
        norm_factor = sum(truncated_weights)
        if norm_factor == 0:
            return 0.0
        return weighted_sum / norm_factor

    # Final computation
    final_diagnostic = aggregate_metrics(diagnostics, weights)

    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Call with realistic inputs
analyze_sensor_data([120, -45, 60, 200, -300, 15], [50, 80, 60])