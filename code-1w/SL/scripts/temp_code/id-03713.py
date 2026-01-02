def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant pre-processing: Normalize data (not used in final path)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in raw_readings if x > thresholds[0]]

    # Distractor: unused statistical computation
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    z_scores = [(x - mean_val) / (variance ** 0.5) for x in raw_readings]

    # Real logic begins: detect anomalies using thresholding
    anomalies = []
    for i, val in enumerate(raw_readings):
        if val > thresholds[1] and i % 2 == 0:
            anomalies.append(i)

    # Distractor: dead code path (never executed due to condition)
    secondary_flags = []
    if len(anomalies) > 100:
        secondary_flags = [i for i, x in enumerate(raw_readings) if x < thresholds[2]]

    # Key transformation: compute rolling window peaks
    peak_magnitudes = []
    for i in range(2, len(raw_readings)):
        window = raw_readings[i-2:i+1]
        if window[1] == max(window):
            peak_magnitudes.append(window[1])

    # Use of lambda and zip: create weighted pairs (only some are used)
    weights = [0.5, 1.0, 0.75, 0.25]
    weighted_pairs = list(zip(peak_magnitudes[:len(weights)], weights))
    weighted_values = list(map(lambda pair: pair[0] * pair[1], weighted_pairs))

    # Distractor: unused dictionary aggregation
    stats_summary = {
        'count': len(raw_readings),
        'anomaly_rate': len(anomalies) / len(raw_readings),
        'peaks_detected': len(peak_magnitudes),
        'phantom_metric': sum(z_scores) * 0.01
    }

    # Real path: compute diagnostic trend via cumulative filter
    trend_signal = []
    for i, mag in enumerate(peak_magnitudes):
        if i % 3 == 0:
            trend_signal.append(mag * 0.8)
        elif mag > thresholds[2]:
            trend_signal.append(mag * 1.1)
        else:
            trend_signal.append(mag * 0.9)

    # Aggregate metrics with offset correction
    aggregate_metrics = [sum(trend_signal[:i+1]) for i in range(len(trend_signal))]
    if not aggregate_metrics:
        aggregate_metrics = [0]

    # Correction factor based on anomaly positions (only last one matters)
    base_correction = len(anomalies) % 7
    adjustment_map = {i: i**2 - 3*i for i in range(8)}
    correction_factor = adjustment_map.get(base_correction, 0)

    # Critical execution point
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Red herring: alternate calculation never used
    fallback_score = sum(weighted_values) - stats_summary['phantom_metric']
    temp_offset = sum(1 for x in z_scores if abs(x) > 2)

    return final_diagnostic

# Input data
sensor_log = [12, 45, 67, 89, 56, 91, 34, 78, 88, 95, 43, 68, 77, 82, 90]
limits = [40, 60, 85]

result = analyze_sensor_data(sensor_log, limits)
print(f"Target result: {result}")