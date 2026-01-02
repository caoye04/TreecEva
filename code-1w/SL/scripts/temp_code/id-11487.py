def analyze_sensor_data(raw_readings):
    # Irrelevant preprocessing: normalize string labels
    label_prefix = 'SENSOR'
    normalized_labels = [label_prefix + str(i) for i in range(len(raw_readings))]
    labeled_data = {lbl: val for lbl, val in zip(normalized_labels, raw_readings)}

    # Distractor: unused transformation path
    temp_offsets = [x % 7 for x in raw_readings if x > 50]
    offset_sum = sum(temp_offsets)  # Dead end

    # Core logic: extract critical thresholds
    filtered_readings = [x for x in raw_readings if 20 < x < 85]
    sorted_readings = sorted(filtered_readings)
    mid_index = len(sorted_readings) // 2
    median_reading = (sorted_readings[mid_index] + sorted_readings[~mid_index]) / 2

    # Bit manipulation decoy
    binary_flags = [x ^ 15 for x in raw_readings]
    flag_count = sum(1 for f in binary_flags if f & 1)  # Misleading metric

    # Real signal extraction via slicing
    signal_window = sorted_readings[1:-1]  # Exclude outliers
    baseline = sum(signal_window) / len(signal_window)

    # Secondary distraction: simulate calibration chains
    calibrations = []
    for i in range(3):
        calibrations.append((baseline * (i + 1)) // (i + 10))  # Complex but irrelevant

    adjustment = calibrations[1] if len(calibrations) > 1 else 0

    # Critical data structure: multi-step diagnostic pipeline
    metrics = {
        'baseline': baseline,
        'adjustment': adjustment,
        'range': sorted_readings[-1] - sorted_readings[0],
        'peak_ratio': sorted_readings[-1] / baseline
    }

    # Destructuring red herring
    _, _, span, _ = (metrics['baseline'], metrics['adjustment'], metrics['range'], metrics['peak_ratio'])

    # Real computation chain begins
    trend_sequence = [abs(x - baseline) for x in signal_window]
    smoothed_trend = [trend_sequence[i] + trend_sequence[i+1] for i in range(len(trend_sequence)-1)]
    decay_rate = 0.95
    weighted_decay = sum(smoothed_trend[i] * (decay_rate ** i) for i in range(len(smoothed_trend)))

    # Hidden dependency: case-sensitive key generation
    keys = ['A', 'B', 'C']
    key_map = {k: ord(k.lower()) for k in keys}
    hash_offset = key_map['B'] - key_map['A']  # Always 1, but obscured

    # Actual aggregation
    aggregate_metrics = [
        metrics['baseline'] * 2,
        weighted_decay / 2,
        span ** 1.5,
        hash_offset * 100
    ]

    # Final corrections with distractors
    safety_margin = len(normalized_labels)  # Looks like it's about safety, really just count
    correction_factor = len(temp_offsets) % 4  # Seemingly random, actually deterministic

    final_diagnostic = aggregate_metrics[-1] + correction_factor * safety_margin
    return final_diagnostic

# Simulated sensor inputs
readings = [67, 45, 89, 23, 78, 12, 67, 55, 81, 33, 90, 44]
result = analyze_sensor_data(readings)
print(f"Target result: {result}")