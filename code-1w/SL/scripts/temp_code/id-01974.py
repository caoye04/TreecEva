def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant pre-processing: normalize readings (not actually used in final result)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100, 2) for x in raw_readings]
    outlier_count = sum(1 for r in raw_readings if r > 95 or r < 5)

    # Distractor: complex but unused signal smoothing
    smoothed = []
    for i, val in enumerate(raw_readings):
        window = raw_readings[max(0, i-2):i+3]
        smoothed.append(sum(window) / len(window))

    # Actual relevant logic starts here
    baseline_score = 0
    for i, (idx, reading) in enumerate(enumerate(raw_readings)):
        if idx % 3 == 0 and reading > 40:
            baseline_score += reading * 0.1

    # Decoy function that looks important but isn't called
    def compute_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        return -sum(f * log(f) for f in freq.values())

    # Unused intermediate transformations
    shifted_data = [x << 1 for x in calibration_sequence if x % 2 == 0]
    inverted_map = {i: 100 - v for i, v in enumerate(calibration_sequence)}

    # Key conditional logic with red herring branches
    trigger_threshold = 0
    for c in calibration_sequence:
        if c > 70:
            trigger_threshold += 1
        elif c < 30:
            # This branch looks significant but doesn't affect final answer
            temp_adj = c * 1.5
            trigger_threshold -= 0.5  # Minor effect overshadowed

    # Another distraction: string-based validation (never used)
    status_flags = ['OK' if x > 50 else 'LOW' for x in raw_readings]
    flag_summary = ''.join(status_flags).count('OK')

    # Core calculation hidden among noise
    adjustment_log = []
    for i, c in enumerate(calibration_sequence):
        if i % 2 == 1:
            adjustment_log.append(c // 3)

    # Critical path: correction factor derived from sum of even-indexed calibrations
    correction_factor = 0
    for i, c in enumerate(calibration_sequence):
        if i % 2 == 0:
            correction_factor += c % 7

    # Dead code: complex bit manipulation that computes unused diagnostic
    unused_diagnostic = 0
    for x in raw_readings[:5]:
        unused_diagnostic ^= (x << 2) | (x >> 1)

    # Final aggregation uses only a subset of computed variables
    aggregate_threshold = len([c for c in calibration_sequence if c > 50])
    final_diagnostic = aggregate_threshold * (baseline_score + correction_factor)

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Return nothing; side effect prints result

# Input data
readings = [65, 72, 44, 83, 39, 52, 91, 48]
calibration = [88, 23, 67, 45, 71, 34, 59, 28]

# Execute function
analyze_sensor_data(readings, calibration)