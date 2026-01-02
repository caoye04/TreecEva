def analyze_sensor_data(raw_readings, calibration_offset=0.03):
    # Irrelevant preprocessing: normalize timestamps (unused)
    timestamps = [t % 86400 for t in range(len(raw_readings) + 5)]
    adjusted_readings = [r + calibration_offset for r in raw_readings if r > 0.1]

    # Distractor: complex filtering with unused branches
    filtered_data = []
    for idx, val in enumerate(adjusted_readings):
        if idx % 2 == 0 and val < 50:
            filtered_data.append(val ** 0.5)
        elif val > 40:
            temp_val = val * 0.9
            filtered_data.append(temp_val - 0.1)  # Dead logic path
        else:
            filtered_data.append(val)

    # Real computation begins: signal envelope detection
    envelope = [abs(x - sum(adjusted_readings) / len(adjusted_readings)) for x in adjusted_readings]
    threshold_base = sum(envelope) / len(envelope)
    max_threshold = max(envelope) * 0.85
    min_threshold = min(envelope) * 1.15 if min(envelope) > 0 else 0.1

    # Misleading transformation: unused frequency analysis
    fft_simulated = [envelope[i] * (-1)**i for i in range(len(envelope))]
    spectral_peaks = [p for p in fft_simulated if p > threshold_base]

    # Key data structure: rolling window metrics
    window_size = 3
    rolling_metrics = []
    for i in range(len(envelope) - window_size + 1):
        window = envelope[i:i+window_size]
        metric = (window[0] * 0.25) + (window[1] * 0.5) + (window[2] * 0.25)
        rolling_metrics.append(round(metric, 6))

    # Add decoy statistic (never used)
    outlier_count = sum(1 for m in rolling_metrics if m > max_threshold)
    baseline_drift = rolling_metrics[0] - rolling_metrics[-1] if len(rolling_metrics) > 1 else 0

    # Core logic buried among distractors
    aggregate_metrics = [m * 1.05 for m in rolling_metrics if m >= min_threshold]
    scaling_factor = len([x for x in adjusted_readings if x > threshold_base])

    # Red herring: unused recursive function
    def calculate_depth(value, depth=0):
        return depth if value <= 1 else calculate_depth(value // 2, depth + 1)
    
    irrelevant_tree_depth = calculate_depth(256)

    # Critical assignment buried in distractions
    final_diagnostic = aggregate_metrics[-1] + scaling_factor * (max_threshold - min_threshold)

    # Print required output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data (fixed for determinism)
sensor_input = [12.5, 18.3, 9.7, 22.1, 35.6, 41.2, 28.9]
analyze_sensor_data(sensor_input)