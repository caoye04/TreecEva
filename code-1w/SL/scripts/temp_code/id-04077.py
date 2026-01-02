def analyze_signal_pattern(raw_readings, calibration_sequence):
    # Irrelevant transformation: frequency mirroring (unused)
    mirrored_spectrum = [abs(x - 50) for x in raw_readings if x > 25]

    # Distractor: dead code path with plausible-looking analysis
    if len(calibration_sequence) < 10:
        baseline_noise = sum([x ** 0.5 for x in calibration_sequence]) * 0.1
    else:
        temp_buffer = [x for x in calibration_sequence if x % 2 == 0]
        processed = list(set(temp_buffer))
        baseline_noise = sum(processed) / len(processed) if processed else 0

    # Real logic begins: extract peaks above dynamic threshold
    dynamic_threshold = sum(raw_readings) / len(raw_readings) * 0.6
    significant_peaks = [x for x in raw_readings if x > dynamic_threshold]

    # Distractor: complex but unused bitwise operation chain
    decoy_state = 0
    for i in range(len(calibration_sequence)):
        decoy_state ^= calibration_sequence[i]
        decoy_state = (decoy_state << 1) & 0xFF

    # Compute peak distribution entropy (red herring with partial use)
    peak_distribution = {}
    for p in significant_peaks:
        rounded = int(p // 5)
        peak_distribution[rounded] = peak_distribution.get(rounded, 0) + 1

    entropy = 0.0
    total_peaks = len(significant_peaks)
    for count in peak_distribution.values():
        if count > 0 and total_peaks > 0:
            prob = count / total_peaks
            entropy -= prob * __import__('math').log(prob, 2)

    # Actual signal metric: weighted sum of top three peaks
    sorted_peaks = sorted(significant_peaks, reverse=True)
    top_three_weighted = sum(peak * (3 - i) for i, peak in enumerate(sorted_peaks[:3]))

    # Distractor: unused recursive function definition
    def trace_path(node, visited):
        if node <= 1:
            return 1
        return trace_path(node - 2, visited + [node]) + trace_path(node - 3, visited + [node])

    # Conditional expression determining aggregation mode
    aggregation_mode = 'enhanced' if len(significant_peaks) >= 4 else 'basic'

    # Set-based interference: irrelevant domain overlap check
    expected_range = set(range(15, 85))
    observed_set = set(int(x) for x in raw_readings)
    coverage_rate = len(observed_set & expected_range) / len(expected_range)

    # Dictionary accumulation of secondary metrics (mostly unused)
    diagnostics = {
        'peak_count': len(significant_peaks),
        'entropy': round(entropy, 4),
        'coverage': round(coverage_rate, 4),
        'mode': aggregation_mode
    }

    # Real computation branch
    if aggregation_mode == 'enhanced':
        aggregate_score = top_three_weighted * 1.75
    else:
        fallback_weights = {0: 1.0, 1: 1.5, 2: 2.0}
        aggregate_score = sum(
            sorted_peaks[i] * fallback_weights.get(i, 2.5) 
            for i in range(min(3, len(sorted_peaks)))
        )

    # Threshold adjustment based on calibration mean (key dependency)
    calib_mean = sum(calibration_sequence) / len(calibration_sequence)
    threshold_adjustment = 15 if calib_mean > 40.0 else -10

    # Critical execution point
    final_diagnostic = aggregate_score + threshold_adjustment

    # Output requirement
    print(f"Result: {final_diagnostic}")

# Execution with sample data
readings = [32, 45, 67, 23, 55, 78, 41]
calibration = [48, 39, 44, 52, 46, 41, 50, 45]
analyze_signal_pattern(readings, calibration)