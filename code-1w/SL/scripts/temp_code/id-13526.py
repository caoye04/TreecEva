def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant pre-processing (distractor)
    normalized = [x / max(raw_readings) for x in raw_readings if x > 0]
    inverted_map = {i: val for i, val in enumerate(reversed(raw_readings))}

    # Dead code path (unused function)
    def apply_calibration(x):
        return x * 0.98 + 0.5  # Never called

    # Core logic disguised among distractors
    valid_readings = [x for x in raw_readings if thresholds[0] <= x <= thresholds[1]]
    outlier_count = len([x for x in raw_readings if x > thresholds[1]])

    # Bit manipulation red herring
    bitmask = 0b101010
    masked_values = [x & bitmask for x in raw_readings]

    # Set operations (required Python feature)
    unique_peaks = set(val for i, val in enumerate(raw_readings) if val > thresholds[1])
    expected_peaks = {thresholds[1] + 5, thresholds[1] + 10, thresholds[1] + 15}
    matched_peaks = unique_peaks.intersection(expected_peaks)
    peak_score = len(matched_peaks) * 100

    # Misleading statistical calculation (distractor)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance_proxy = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    stability_index = 1 / (variance_proxy + 1)  # Not actually used

    # Enumerate and zip usage (required Python feature)
    indexed_readings = list(enumerate(raw_readings))
    paired = list(zip([r for r in raw_readings], [r * 0.75 for r in raw_readings]))
    energy_sum = sum(b * 0.5 for a, b in paired if a > thresholds[0])

    # Character counting red herring (SUGGESTED paradigm)
    status_codes = ['OK', 'ERR', 'OK', 'WARN', 'OK']
    char_count = sum(len(code) for code in status_codes)  # Irrelevant

    # Main diagnostic chain
    base_signal = sum(valid_readings) // (len(valid_readings) or 1)
    noise_penalty = outlier_count * 15
    aggregate_score = base_signal - noise_penalty + peak_score

    # Multiple assignments distraction
    temp_a, temp_b = 42, 84
    temp_a, temp_b = temp_b, temp_a  # Swapped but unused

    # Correction based on bit condition (subtle relevant use)
    correction_factor = 0
    if len(raw_readings) & 1:  # Odd length check
        correction_factor += 50

    # UNUSED conditional branch (dead logic)
    debug_mode = False
    if debug_mode:
        print("Debug:", raw_readings[:2])

    # Key execution point
    final_diagnostic = aggregate_score + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Return nothing to avoid alternative outputs

# Execute with test data
sensor_inputs = [120, 150, 90, 200, 180, 95, 210, 170]
cutoff_limits = (100, 200)
analyze_sensor_data(sensor_inputs, cutoff_limits)