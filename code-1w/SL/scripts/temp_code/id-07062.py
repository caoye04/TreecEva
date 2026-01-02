def analyze_sensor_data(raw_readings):
    # Irrelevant preprocessing: normalize timestamps (not used)
    timestamps = [r[0] for r in raw_readings]
    normalized_times = [(t - timestamps[0]) / 1000 for t in timestamps]

    # Extract sensor values and apply irrelevant smoothing filter
    sensor_values = [r[1] for r in raw_readings]
    smoothed = [sensor_values[0]]
    for i in range(1, len(sensor_values)):
        smoothed.append(0.7 * sensor_values[i] + 0.3 * smoothed[i-1])

    # Distractor: frequency domain analysis (unused)
    fft_magnitude = sum(s * s for s in smoothed) ** 0.5
    peak_frequency = fft_magnitude / len(smoothed) if fft_magnitude > 1 else 0

    # Relevant: detect anomalies using thresholding
    threshold = sum(sensor_values) / len(sensor_values) * 1.15
    anomalies = []
    for idx, val in enumerate(sensor_values):
        if val > threshold:
            anomalies.append((idx, val))

    # Distractor: secondary anomaly detection with different logic (never accessed)
    edge_anomalies = []
    for i in range(1, len(sensor_values)-1):
        if abs(sensor_values[i] - sensor_values[i-1]) > 20:
            edge_anomalies.append(i)

    # Compute rolling max over window size 3 (slicing operation)
    rolling_max = []
    for i in range(2, len(sensor_values)):
        rolling_max.append(max(sensor_values[i-2:i+1]))

    # Compute decay-corrected average from anomalies (red herring)
    decay_weights = [0.9**i for i in range(len(anomalies))]
    weighted_sum = sum(anomalies[i][1] * decay_weights[i] for i in range(len(anomalies))) if anomalies else 0
    corrected_avg = weighted_sum / sum(decay_weights) if decay_weights else 0

    # Real processing path begins here — cross-reference with rolling stats
    spike_indices = [a[0] for a in anomalies if a[1] > 45]
    spike_window_data = sensor_values[spike_indices[0]:spike_indices[-1]+1] if spike_indices else [0]

    # Compute multi-stage diagnostic metrics
    base_metric = min(spike_window_data) if spike_window_data else 0
    spread = max(spike_window_data) - base_metric
    density = len(spike_window_data) / (spike_indices[-1] - spike_indices[0] + 1) if len(spike_indices) > 1 else 0

    # Aggregate rolling statistics (slice last 4 elements)
    if len(rolling_max) >= 4:
        recent_peaks = rolling_max[-4:]
    else:
        recent_peaks = rolling_max
    
    avg_recent_peak = sum(recent_peaks) / len(recent_peaks) if recent_peaks else 0

    # Hidden correction factor based on index arithmetic
    mid_idx = len(raw_readings) // 2
    offset_val = raw_readings[mid_idx][1]
    adjustment = (offset_val % 7) * 1.7

    # Final aggregation with slicing and adjustment
    aggregate_metrics = [
        base_metric * 1.1,
        spread * 0.85,
        density * 100,
        avg_recent_peak,
        adjustment
    ]

    # Dead code: predictive confidence model (unreachable)
    def predict_failure(risk_score):
        if risk_score > 90:
            return "CRITICAL"
        elif risk_score > 60:
            return "WARNING"
        else:
            return "STABLE"

    # Key statement — answer depends on this
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Print result for observable output
    print(f"Result: {final_diagnostic}")

    # Unused cleanup function (decoy)
    def reset_buffers():
        nonlocal smoothed, normalized_times
        smoothed.clear()
        normalized_times = []

    return final_diagnostic

# Simulated sensor input data (timestamp, reading)
correction_factor = 13.4
sensor_input = [
    (1678886400, 23), (1678886410, 25), (1678886420, 27),
    (1678886430, 48), (1678886440, 52), (1678886450, 49),
    (1678886460, 30), (1678886470, 75), (1678886480, 73),
    (1678886490, 70), (1678886500, 35)
]

# Execute
analyze_sensor_data(sensor_input)
