def analyze_sensor_data(raw_readings, threshold=100):
    # Irrelevant preprocessing: normalize data (unused path)
    normalized = [x / max(raw_readings) * 100 for x in raw_readings if x > 0]
    filtered = [x for x in raw_readings if x < threshold]

    # Distractor: complex but unused transformation chain
    transformed = []
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            transformed.append(val ** 0.5 * (i + 1))
        else:
            transformed.append(val // (i + 1) + 2)

    # Real computation begins: detect anomalies using sliding window
    window_size = 3
    rolling_averages = []
    for i in range(len(filtered) - window_size + 1):
        window = filtered[i:i + window_size]
        avg = sum(window) / len(window)
        rolling_averages.append(round(avg, 2))

    # Secondary distractor: bit manipulation with no impact
    bit_analysis = 0
    for x in filtered:
        bit_analysis ^= (x << 1) | 1
        bit_analysis &= 0xFFFF  # Clamp to 16 bits

    # Key metric: find peaks above dynamic baseline
    baseline = sum(rolling_averages) / len(rolling_averages)
    peaks = [v for v in rolling_averages if v > baseline * 1.1]

    # Destructuring and multiple assignments (red herring)
    (a, b), (c, d) = zip(peaks[::2], peaks[1::2]) if len(peaks) >= 4 else ((0, 0), (0, 0))

    # Actual signal extraction via frequency analysis (simplified)
    peak_diffs = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    freq_score = sum(abs(d) for d in peak_diffs) if peak_diffs else 0.0

    # Hidden logic: correction factor derived from list slicing and enumeration
    indices_of_peaks = [i for i, v in enumerate(rolling_averages) if v in peaks]
    stride = indices_of_peaks[1] - indices_of_peaks[0] if len(indices_of_peaks) > 1 else 1
    segment = rolling_averages[::stride][:3]  # Slice with computed stride

    # Core calculation path (non-obvious)
    aggregate_metrics = []
    for idx, val in enumerate(segment):
        noise = (idx + 1) * 0.1
        adjusted = val - noise
        aggregate_metrics.append(round(adjusted, 3))

    # Final correction based on statistical deviation (key step)
    deviations = [(m - baseline) for m in aggregate_metrics]
    correction_factor = int(sum(deviations) * 10) // 2

    # Critical assignment: target execution point
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Dead code path: function defined but not called
    def calibrate_system():
        return sum(transformed) / len(transformed)

    # Unused variable assignments (distractors)
    outlier_count = len([x for x in raw_readings if x > threshold * 2])
    scaling_factor = 1.0 / (outlier_count + 1)
    checksum = bit_analysis ^ len(normalized)

    # Output required result
    print(f"Result: {final_diagnostic}")

# Simulate sensor input (deterministic)
data_stream = [85, 110, 92, 97, 108, 88, 95, 103, 89, 94]
analyze_sensor_data(data_stream, threshold=105)