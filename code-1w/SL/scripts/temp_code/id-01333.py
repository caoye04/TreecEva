def analyze_sensor_data(raw_readings, calibration_offset=1.05):
    # Irrelevant preprocessing: normalize timestamps (unused)
    timestamps = [t % 86400 for t in range(len(raw_readings) + 5)]
    normalized_times = [ts / max(timestamps) for ts in timestamps if ts > 100]

    # Distractor: complex but unused frequency transformation
    freq_domain = []
    for i in range(len(raw_readings)):
        val = 0
        for j in range(0, len(raw_readings), 2):
            val += raw_readings[j] * (i % (j + 1) if j != 0 else 1)
        freq_domain.append(val % 100)

    # Actual relevant data path begins here
    filtered_readings = [x for x in raw_readings if x > 0]  # Remove negative noise
    window_size = 3
    smoothed = []
    for i in range(len(filtered_readings) - window_size + 1):
        window = filtered_readings[i:i + window_size]
        smoothed.append(sum(window) / len(window))

    # Compute rolling thresholds (some used, some not)
    thresholds = [min(smoothed), max(smoothed), sum(smoothed) / len(smoothed)]
    deviation_scores = [abs(x - thresholds[2]) for x in smoothed]

    # Unused decoy: entropy calculation
    probability_dist = [dev / sum(deviation_scores) for dev in deviation_scores[::2]]
    entropy = 0
    for p in probability_dist:
        if p > 0:
            entropy -= p * __import__('math').log(p)

    # Key metric derivation
    trend_analysis = []
    for i in range(1, len(smoothed)):
        trend_analysis.append(1 if smoothed[i] > smoothed[i-1] else -1)

    # Extract pattern signature using slicing and tuple unpacking
    first_trend, *middle_trends, last_trend = trend_analysis
    pattern_signature = (first_trend, last_trend, len(middle_trends))

    # Diagnostic metrics with distractor variables
    spike_count = sum(1 for d in deviation_scores if d > thresholds[2] * 0.5)
    baseline_shift = abs(thresholds[1] - thresholds[0])
    stability_index = (thresholds[1] - thresholds[0]) / (thresholds[2] + 1e-5)

    # Red herring: unused recursive function
    def calculate_depth(n):
        return 1 + calculate_depth(n // 2) if n > 1 else 0
    
    recursion_test = calculate_depth(128)  # Computed but irrelevant

    # Core logic: inject artificial bias based on pattern signature
    if pattern_signature[0] == 1 and pattern_signature[1] == -1:
        temperature_bias = 12.5
    elif pattern_signature[2] % 2 == 0:
        temperature_bias = -8.3
    else:
        temperature_bias = 0.0

    # Aggregate multiple metrics (only last one matters)
    aggregate_metrics = [
        spike_count * 2,
        int(baseline_shift / 3),
        int(stability_index * 100),
        recursion_test * 5,
        pattern_signature[2] * 3
    ]

    # Critical assignment - this determines the answer
    final_diagnostic = aggregate_metrics[-1] + temperature_bias * 0.75

    # Output required result
    print(f"Result: {final_diagnostic}")

# Simulate sensor input
sensor_input = [23.1, -5.2, 18.9, 25.4, 12.7, -3.3, 30.1, 27.6, 19.8]
analyze_sensor_data(sensor_input)