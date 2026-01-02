def analyze_sensor_stream(raw_stream, config):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in raw_stream if x > 0]
    baseline = sum(normalized) / len(normalized) if normalized else 0
    adjusted = [x - baseline for x in normalized]

    # Key data transformation chain
    window_size = config.get('window', 5)
    step_size = config.get('step', 2)
    rolling_averages = []

    for i in range(0, len(adjusted) - window_size + 1, step_size):
        window = adjusted[i:i + window_size]
        avg = sum(window) / window_size
        rolling_averages.append(round(avg, 3))

    # Distractor: unused statistical analysis
    variance = sum((x - baseline) ** 2 for x in adjusted) / len(adjusted) if adjusted else 0
    std_dev = variance ** 0.5
    outlier_threshold = baseline + 2 * std_dev
    outliers = [x for x in adjusted if abs(x) > outlier_threshold]  # Dead code path

    # Relevant filtering based on dynamic criteria
    trend_signal = [x for x in rolling_averages if x > -0.5]
    if len(trend_signal) == 0:
        trend_signal = [0]

    magnitude_score = sum(abs(x) for x in trend_signal)
    peak_response = max(trend_signal)

    # Secondary distractor: complex but irrelevant frequency simulation
    sample_rate = config.get('rate', 100)
    time_points = [i / sample_rate for i in range(len(rolling_averages))]
    phase_shifted = [round(peak_response * (t % 0.1), 4) for t in time_points]
    harmonic_energy = sum(abs(x) for x in phase_shifted[:10])  # Unused metric

    # Core logic disguised among distractions
    def process_readings(data_slice, thresh):
        if not data_slice:
            return -999
        clipped = [min(max(x, -thresh), thresh) for x in data_slice]
        return round(sum(clipped) / len(clipped), 4)

    critical_band = trend_signal[1::2]  # Slice operation (required)
    threshold = config.get('sensitivity', 3.0)

    # Decoy function call with misleading name
    def compute_stability_index(seq):
        if len(seq) < 2:
            return 0
        diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
        return round(sum(diffs) / len(diffs), 4)

    stability = compute_stability_index(rolling_averages)  # Computed but unused

    # Actual key computation buried in logic
    filtered_data = [x * 1.75 for x in critical_band if x < peak_response * 0.9]
    if not filtered_data:
        filtered_data = [0.5]

    final_diagnostic = process_readings(filtered_data, threshold)

    # Output required format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate execution
sensor_input = [2.1, -1.3, 0.9, 3.4, -2.2, 1.8, 0.5, -0.7, 2.0, 1.1, -3.0, 4.2, -1.1]
settings = {'window': 4, 'step': 1, 'sensitivity': 2.8, 'rate': 50}
analyze_sensor_stream(sensor_input, settings)