import itertools

def main():
    # Sensor data simulation (real values)
    raw_readings = [127, 255, 192, 64, 224, 32, 160, 96]
    calibration_offset = 32
    adjusted_readings = [r - calibration_offset for r in raw_readings]

    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(adjusted_readings)):
        window = adjusted_readings[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))

    # Data binning by category (partially relevant)
    categories = {}
    for val in adjusted_readings:
        band = val // 64
        categories[band] = categories.get(band, 0) + 1

    # Bitmask analysis for error detection (critical path)
    def has_quorum(bits):
        return bin(bits).count('1') >= 3

    def extract_flags(val):
        return val & 0b111111  # Keep last 6 bits

    flagged = list(map(extract_flags, adjusted_readings))
    quorum_check = list(map(has_quorum, flagged))

    # Decoy: Frequency analysis on bit patterns (irrelevant)
    pattern_freq = {}
    for f in flagged:
        pf = f"pattern_{f % 7}"
        pattern_freq[pf] = pattern_freq.get(pf, 0) + 1

    # Real processing begins: filter and transform
    valid_indices = [i for i, qc in enumerate(quorum_check) if qc]
    filtered_values = [adjusted_readings[i] for i in valid_indices]

    # Apply non-linear transformation (logarithmic scaling)
    import math
    transformed = []
    for v in filtered_values:
        if v > 0:
            transformed.append(math.log(v) * 10)
        else:
            transformed.append(0)

    # String-based tagging (uses string methods - required feature)
    labels = [f"sensor_{i}" for i in valid_indices]
    tag_summary = "-".join(labels).upper().replace("_", "X")
    tag_length = len(tag_summary)

    # Decoy: Permutation analysis (itertools - required feature)
    perm_count = 0
    for _ in itertools.permutations([1, 2, 3], 3):
        perm_count += 1

    # Critical aggregation
    baseline = sum(transformed) / len(transformed) if transformed else 0

    # Lambda-based dynamic thresholding (required feature)
    adaptive_thresh = lambda x: x * 1.5 if x < 20 else x * 0.8
    thresholds = list(map(adaptive_thresh, transformed))

    # Final diagnostic computation
    anomaly_score = sum(1 for t, th in zip(transformed, thresholds) if t > th)
    stability_index = len(filtered_values) * 100 / len(raw_readings)

    # Misleading intermediate (looks important)
    phantom_metric = (perm_count * tag_length) // (calibration_offset + 1)

    # Key statement
    processed_data = {
        'readings': transformed,
        'anomalies': anomaly_score,
        'stability': stability_index,
        'phantom': phantom_metric
    }

    def analyze_readings(data):
        readings = data['readings']
        anomalies = data['anomalies']
        stability = data['stability']

        # Complex weighting formula
        if readings:
            avg_reading = sum(readings) / len(readings)
            weight_factor = 0.3 * avg_reading + 0.5 * stability + 0.2 * (10 - anomalies)
            return round(weight_factor, 4)
        return 0.0

    final_diagnostic = analyze_readings(processed_data)
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()