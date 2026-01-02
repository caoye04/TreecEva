def sensor_diagnostic():
    raw_signals = [23.5, 18.9, 45.2, 37.8, 12.1, 55.6, 31.3]
    calibration_offset = 1.2
    baseline_correction = sum(raw_signals) / len(raw_signals) - calibration_offset

    # Irrelevant preprocessing: signal smoothing with unused result
    smoothed = [round(x * 0.9 + baseline_correction * 0.1, 2) for x in raw_signals]
    normalized = [round((x - min(raw_signals)) / (max(raw_signals) - min(raw_signals)), 3) for x in raw_signals]

    # Distractor: unused statistical analysis
    mean_val = sum(normalized) / len(normalized)
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized)
    std_dev = variance ** 0.5

    # Relevant transformation
    processed_data = [int((x - 10) // 2) for x in raw_signals if x > 20]

    # Decoy function that's defined but not used
    def deprecated_filter(data):
        return [x for x in data if x % 2 == 0]

    # Set operations - relevant
    critical_range = {30, 40, 50, 60}
    threshold_set = {x for x in range(25, 55, 5)}
    auxiliary_set = {x * 2 for x in processed_data}

    # String-based distractor: unrelated metadata parsing
    device_info = "SensorNode_XYZ_Rev4"
    version_tag = device_info.split('_')[-1]
    is_updated = 'Rev' in device_info and version_tag > 'Rev2'

    # Bit manipulation red herring
    status_flag = 0b101010
    masked_flag = status_flag & 0b111100
    shifted_flag = masked_flag >> 2

    # Conditional logic with early returns (only one path matters)
    def analyze_readings(data, thresholds):
        if len(data) < 3:
            return -999  # dead path

        intersection_count = len(set(data) & thresholds)

        # Complex conditional with string method distraction
        debug_mode = "DISABLED".lower().startswith('debug')
        if debug_mode and intersection_count == 0:
            return 0

        # Core logic: modular arithmetic and recursion
        def recursive_sum(n):
            if n <= 1:
                return n
            return n + recursive_sum(n - 2)

        base_score = recursive_sum(intersection_count)

        # Tuple unpacking distraction
        config = (base_score, 100, len(auxiliary_set))
        score_weight, _, meta_size = config

        # Final computation - only this matters
        adjustment = len([x for x in processed_data if x in critical_range])
        final_score = base_score * 10 + adjustment

        # Dead branch with misleading high-value computation
        if False:
            temp = set(processed_data)
            temp.discard(99)
            overflow = sum(temp) ** 2
            final_score = overflow - 10000

        return final_score

    # Key assignment statement
    final_diagnostic = analyze_readings(processed_data, threshold_set)

    print(f"Result: {final_diagnostic}")

sensor_diagnostic()