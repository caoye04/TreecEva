from collections import defaultdict, Counter
import math

# Simulate sensor readings with noise and validity flags
def analyze_sensor_data(readings):
    valid_count = 0
    total_signal = 0.0
    noise_floor = 0.05
    signal_peaks = []
    cumulative_xor = 0
    temp_flags = []

    # Irrelevant tracking for interference
    debug_log = []
    outlier_count = 0

    for i, (value, timestamp, is_valid) in enumerate(readings):
        if not is_valid:
            continue

        # Real processing begins
        adjusted_value = abs(value - noise_floor)
        if adjusted_value > 1.5:
            signal_peaks.append(adjusted_value)

        total_signal += adjusted_value
        valid_count += 1

        # Bitwise red herring
        int_repr = int(adjusted_value * 100)
        cumulative_xor ^= int_repr

        # Distractor logic - logs but doesn't affect result
        if adjusted_value < 0.8:
            debug_log.append(f'Low signal at {timestamp}')
            temp_flags.append(1)
        else:
            outlier_count += (adjusted_value > 2.0)

    # Compute peak statistics (semi-relevant)
    peak_avg = sum(signal_peaks) / len(signal_peaks) if signal_peaks else 0.0
    peak_max = max(signal_peaks) if signal_peaks else 0.0

    # Dummy histogram for interference
    hist_bins = defaultdict(int)
    for p in signal_peaks:
        bin_key = int(p * 2)  # Binning
        hist_bins[bin_key] += 1

    # Actual critical computation path
    base_score = total_signal * (valid_count ** 0.5)
    penalty = len(temp_flags) * 0.25
    bonus = int(peak_max * 10) if peak_max > 1.0 else 0

    final_score = int(base_score - penalty + bonus)

    # Dead code - never executed but looks relevant
    if False:
        fallback = Counter(debug_log)
        final_score = max(final_score, sum(fallback.values()))

    return final_score


# Generate deterministic input
readings_list = [
    (1.23, 1001, True), (0.45, 1002, True), (1.67, 1003, True),
    (2.11, 1004, True), (0.33, 1005, False), (1.89, 1006, True),
    (0.76, 1007, True), (2.01, 1008, True), (1.11, 1009, True)
]

# Execute
final_score = analyze_sensor_data(readings_list)
print(f'Target result: {final_score}')