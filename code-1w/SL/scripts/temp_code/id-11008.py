def process_sensor_data(raw_readings, calibration_factor, noise_floor):
    # Irrelevant preprocessing: normalize timestamps (not used in final result)
    timestamps = [r[0] for r in raw_readings]
    normalized_times = [(t - timestamps[0]) / 1000 for t in timestamps]

    # Extract sensor values and apply misleading calibration
    sensor_values = [r[1] for r in raw_readings]
    calibrated = [v * calibration_factor for v in sensor_values]  # Red herring: not directly used

    # Distractor: frequency domain transformation (dead end)
    spectrum = []
    for i in range(len(calibrated) - 1):
        spectrum.append(abs(calibrated[i+1] - calibrated[i]))
    smoothed_spectrum = [s ** 0.5 for s in spectrum if s > noise_floor]

    # Real path begins: filter based on quality metric (index 2)
    quality_flags = [r[2] for r in raw_readings]
    valid_indices = [i for i, q in enumerate(quality_flags) if q == 1]

    # Use enumerate to track positions and zip to reassemble
    filtered_metrics = []
    for idx, (time, val, qual) in enumerate(raw_readings):
        if qual == 1:
            adjusted_val = val * (0.9 + idx * 0.02)  # Progressive drift correction
            filtered_metrics.append((idx, adjusted_val))

    # Distractor: secondary validation chain (unused)
    consistency_check = True
    for i, (_, v) in enumerate(filtered_metrics[:-1]):
        if abs(v - filtered_metrics[i+1][1]) > 5.0:
            consistency_check = False
            break

    # Baseline calculation with artificial offset
    baseline_components = [v for _, v in filtered_metrics[:5]]
    baseline_threshold = sum(baseline_components) / len(baseline_components) + 2.5

    # Decoy aggregation method
    rolling_averages = []
    window_size = 3
    for i in range(len(filtered_metrics) - window_size + 1):
        window = [filtered_metrics[i+j][1] for j in range(window_size)]
        rolling_averages.append(sum(window) / window_size)

    # Key analysis function (depends only on filtered_metrics and baseline_threshold)
    def analyze_readings(metrics, threshold):
        high_deviation_count = 0
        cumulative_drift = 0.0
        for pos, value in metrics:
            deviation = value - threshold
            if deviation > 1.5:
                high_deviation_count += 1
                cumulative_drift += deviation
        # Final diagnostic combines count and weighted drift
        return int((high_deviation_count * 100) + round(cumulative_drift, 2))

    # Dead code path: entropy calculation (never called)
    def calculate_entropy(data):
        from math import log
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        total = len(data)
        return -sum((count/total) * log(count/total) for count in freq.values())

    # Critical assignment - this determines the answer
    final_diagnostic = analyze_readings(filtered_metrics, baseline_threshold)
    
    # Print result for verification
    print(f"Result: {final_diagnostic}")

# Simulate input data
input_readings = [
    (1609459200, 10.0, 1), (1609459210, 11.2, 1), (1609459220, 12.1, 0),
    (1609459230, 13.5, 1), (1609459240, 14.8, 1), (1609459250, 15.0, 1),
    (1609459260, 16.2, 1), (1609459270, 17.9, 1)
]

# Execute main logic
process_sensor_data(input_readings, calibration_factor=1.05, noise_floor=0.1)