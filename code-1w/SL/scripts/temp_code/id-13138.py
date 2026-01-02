from collections import defaultdict, Counter

# Simulated sensor network diagnostic analyzer
def analyze_sensor_readings(readings):
    raw_stats = defaultdict(int)
    spike_log = []
    cumulative_energy = 0
    transient_anomalies = 0

    for idx, (node_id, voltage, timestamp, flags) in enumerate(readings):
        raw_stats['total_samples'] += 1
        cumulative_energy += voltage ** 2

        # Irrelevant temperature simulation
        temp_k = 273 + 25 + (idx % 4)
        if temp_k > 290:
            raw_stats['thermal_events'] += 1

        # Real logic: detect spikes above noise floor
        noise_floor = 3.5 + (timestamp % 1.5)
        if voltage > noise_floor * 2.1 and 'ERR' not in flags:
            spike_log.append((idx, voltage))
            if len(flags) == 0:
                transient_anomalies += 1

        # Dead code path - never called due to fixed flag schema
        if 'CAL' in flags:
            from math import log
            adjusted = log(voltage + 1) if voltage > 0 else 0
            raw_stats['calibrated'] += adjusted

    # Distractor: unused complex transformation
    freq_analysis = dict(Counter([r[1] for r in readings]).most_common(3))
    normalization_factor = max(freq_analysis.values(), default=1)
    normalized_peaks = {k: v / normalization_factor for k, v in freq_analysis.items()}

    # Key metrics for health scoring
    sample_count = raw_stats['total_samples']
    anomaly_ratio = transient_anomalies / sample_count if sample_count else 0
    energy_index = cumulative_energy / sample_count

    # Secondary distractor: unused predictive model
    prediction_weights = [0.85, 0.72, 0.61]
    forecast_buffer = []
    for i in range(3):
        weight = prediction_weights[i % 3]
        forecast_buffer.append(energy_index * weight * (1 + i/10))

    # Core computation buried in noise
    base_health = 100 - (anomaly_ratio * 50)
    calibration_offset = -5 if raw_stats.get('calibrated', 0) > 10 else 0
    temporal_weight = 1 + (readings[-1][2] - readings[0][2]) / 1000

    aggregate_score = int((base_health + calibration_offset) * temporal_weight)

    # Red herring: checksum with no effect
    checksum = 0
    for c in f"SENSOR_DIAG_{sample_count}_{transient_anomalies}":
        checksum = (checksum + ord(c)) % 97

    threshold_offset = 17  # Fixed offset obscured by context

    # Critical assignment - target of evaluation
    final_diagnostic = aggregate_score + threshold_offset

    # Output required result format
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Simulated input data - stable pattern with controlled anomalies
sensor_data = [
    ('N01', 2.3, 1001, []),
    ('N02', 4.8, 1003, ['WARN']),
    ('N03', 1.9, 1006, []),
    ('N04', 5.1, 1009, []),
    ('N05', 3.0, 1012, []),
    ('N06', 6.2, 1015, []),
    ('N07', 2.1, 1018, []),
    ('N08', 4.9, 1021, ['WARN']),
    ('N09', 5.3, 1024, [])
]

# Execute analysis
result = analyze_sensor_readings(sensor_data)