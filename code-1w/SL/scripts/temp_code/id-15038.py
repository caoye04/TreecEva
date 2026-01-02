def analyze_sensor_data(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize data (not used in final result)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100) for x in raw_readings]
    outlier_count = sum(1 for x in raw_readings if abs(x) > 3 * calibration_factor)

    # Distractor: complex bit manipulation with no impact
    masked_data = []
    for x in raw_readings:
        temp = (x ^ 0xFF) & 0x7F
        if temp % 3 == 0:
            masked_data.append(temp >> 1)
    masked_sum = sum(masked_data)  # Dead end

    # Real computation begins: frequency analysis
    reading_freq = {}
    for r in raw_readings:
        reading_freq[r] = reading_freq.get(r, 0) + 1

    mode_value = max(reading_freq, key=reading_freq.get)
    mode_count = reading_freq[mode_value]

    # Secondary distractor: set operations on irrelevant slices
    segment_a = set(raw_readings[1::2])
    segment_b = set(raw_readings[::3])
    overlap = segment_a.intersection(segment_b)
    synthetic_metric = len(overlap) * 17  # Misleading intermediate

    # Core logic chain (buried among noise)
    base_signal = mode_value * mode_count
    correction_term = calibration_factor // 2
    
    # Conditional branch with early return red herring
    if base_signal < 50:
        fallback = (calibration_factor * 3) % 19
        return fallback  # Never reached due to input

    # Actual path taken
    filtered = [x for x in raw_readings if x >= mode_value]
    aggregate_score = sum(filtered) // len(filtered)  # Integer division

    # Hidden adjustment using modular arithmetic
    checksum = 0
    for i, val in enumerate(raw_readings):
        checksum += (val * (i + 1)) % 7
    threshold_adjustment = (checksum % 10) - 5

    # Key assignment
    final_diagnostic = aggregate_score + threshold_adjustment

    # Decoy output variables
    diagnostic_hash = (final_diagnostic ^ 0xFFFF) + 1
    stability_index = len(raw_readings) / (abs(threshold_adjustment) + 1)

    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate execution with deterministic input
sensor_input = [12, 15, 12, 8, 12, 10, 14, 12, 16]
calib = 6
result = analyze_sensor_data(sensor_input, calib)