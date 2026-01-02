from collections import defaultdict, Counter
import math

# Simulated sensor data processing with noise filtering and diagnostic scoring
def analyze_sensor_readings(readings):
    raw_metrics = []
    noise_floor = 0.02
    signal_peaks = []
    aggregate_score = 0
    temp_buffer = []
    decoy_sum = 0  # Irrelevant accumulator (red herring)

    for idx, val in enumerate(readings):
        if abs(val) < noise_floor:
            continue
        transformed = round(math.log(abs(val) + 1e-5) * 100, 3)
        raw_metrics.append(transformed)
        
        if transformed > 50 and idx % 2 == 0:
            signal_peaks.append(transformed)

        # Dead code path: never executed due to condition mismatch
        if len(raw_metrics) == 1000:
            cleanup = [x for x in raw_metrics if x > 0]
            decoy_sum += sum(cleanup)

    # Misleading intermediate score
    pseudo_entropy = len(raw_metrics) * 1.5 if raw_metrics else 0

    # Real computation begins: analyze peak patterns
    peak_counts = defaultdict(int)
    for peak in signal_peaks:
        bucket = int(peak // 10)
        peak_counts[bucket] += 1

    dominant_band = max(peak_counts.keys()) if peak_counts else 0
    band_score = dominant_band * 17

    # String-based identifier parsing (irrelevant but plausible)
    device_tag = "SENSOR_X7G-TEMP"
    tag_parts = device_tag.split('_')
    version_code = tag_parts[-1].replace("-", "") if '-' in device_tag else ""
    version_value = sum(ord(c) for c in version_code) % 13

    # Set operation: determine anomaly overlap (distractor)
    expected_signals = {55.2, 61.3, 70.1, 85.6}
    detected_set = set(signal_peaks)
    anomaly_overlap = len(expected_signals.intersection(detected_set))

    # Actual score built from band_score and length metric
    base_diagnostic = len(signal_peaks) * 33
    if band_score > 0:
        base_diagnostic += band_score

    # Correction factor based on character frequency (plausible but indirect)
    all_chars = ''.join([device_tag, "LOG_PHASE_3"])
    char_freq = Counter(all_chars)
    frequent_letters = {k for k, v in char_freq.items() if v > 1}
    adjustment = len(frequent_letters) * 5

    # Decoy control flow with sorting (dead logic)
    sorted_metrics = sorted(raw_metrics, reverse=True)
    if sorted_metrics:
        median_idx = len(sorted_metrics) // 2
        median_val = sorted_metrics[median_idx]
        outlier_check = [x for x in sorted_metrics if x > median_val * 3]
        # Unused result

    # Critical assignment point
    correction_factor = adjustment - version_value
    final_diagnostic = aggregate_score + correction_factor  # <-- Key statement

    # Final red herring: unused conditional transformation
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) * 2
    elif final_diagnostic == 0:
        final_diagnostic = 19

    return final_diagnostic

# Input data with controlled properties
sensor_input = [
    0.001, 0.045, 0.003, 0.082, 0.012, 0.115, 0.008, 0.153, 0.005, 0.198,
    0.002, 0.251, 0.063, 0.312, 0.011, 0.385, 0.023, 0.467, 0.041, 0.562
]

result = analyze_sensor_readings(sensor_input)
print(f"Result: {result}")