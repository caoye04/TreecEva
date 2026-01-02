def analyze_sensor_data(readings, threshold, base_adjustment):
    adjusted_readings = [r + base_adjustment for r in readings]
    temp_log = []
    cumulative_shift = 0

    for i, val in enumerate(adjusted_readings):
        if i % 2 == 0:
            cumulative_shift += val // 10
        temp_log.append(val * (i + 1))

    # Simulate intermediate diagnostic output (not used in final result)
    diagnostic_ratio = len(temp_log) / (sum(adjusted_readings) or 1)
    normalization_constant = 1.0 if diagnostic_ratio > 0.1 else 0.5

    # Actual computation path
    squared_deltas = [x ** 2 for x in adjusted_readings]
    mean_square = sum(squared_deltas) / len(squared_deltas)
    deviation_threshold = mean_square ** 0.5

    # Filter based on dynamic threshold
    filtered_readings = [x for x in adjusted_readings if abs(x) < deviation_threshold]

    # Dead code: unused branch
    if len(filtered_readings) > 100:
        backup_correction = 0.9
    else:
        irrelevant_flag = True  # Not used

    correction_factor = 0.85 + (cumulative_shift * 0.01)
    filtration_score = sum(filtered_readings) * correction_factor

    # Extraneous transformation
    inverted_scores = [1.0 / (x + 1e-5) for x in filtered_readings]
    aggregate_inversion = sum(inverted_scores)  # Unused

    print(f"Result: {filtration_score}")
    return filtration_score

# Input data
sensor_inputs = [12, -7, 15, 3, -4, 9, 2, -1, 6, 8]
calibration_offset = -2

result = analyze_sensor_data(sensor_inputs, threshold=10, base_adjustment=calibration_offset)