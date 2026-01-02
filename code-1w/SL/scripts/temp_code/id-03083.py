def analyze_sensor_data(raw_values):
    base_threshold = 42
    scaling_factor = 1.75
    temp_buffer = []
    filtered = [x for x in raw_values if x > base_threshold * 0.5]

    # Irrelevant transformation (dead-end computation)
    squared_offset = sum((x ** 2 for x in filtered if x < 60))
    normalized = list(map(lambda val: (val - base_threshold) * scaling_factor, filtered))

    # Distractor variables with misleading names
    stability_index = 0
    fluctuation_mask = []
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            stability_index += val * 0.1
        else:
            fluctuation_mask.append(val % 3.0)

    # Core logic begins here
    aggregate = sum(normalized)
    correction_term = len(filtered) * 0.3
    activation_score = int(aggregate - correction_term)

    # Simulate auxiliary system state (not used in final result)
    system_health = "OK" if sum(fluctuation_mask) > 5 else "WARNING"
    diagnostic_log = {"entries": len(raw_values), "ignored": len(raw_values) - len(filtered)}

    def apply_calibration(data, score):
        offset = sum(d % 7 for d in data[:5]) // 2
        adjustment = (score + offset) & 0xFF  # Bitwise limit to byte range
        return adjustment if adjustment > 0 else 1

    final_diagnostic = apply_calibration(raw_values, activation_score)

    # Print required output
    print(f"Result: {activation_score}")

analyze_sensor_data([38, 45, 52, 33, 61, 47, 55])