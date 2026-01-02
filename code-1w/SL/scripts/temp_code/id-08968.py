def analyze_sensor_readings():
    raw_readings = [107, 214, 198, 305, 187, 267, 324, 143, 202, 289]
    calibration_offset = 9
    adjusted_readings = [x - calibration_offset for x in raw_readings]

    # Irrelevant transformation: phase normalization (unused)
    normalized_phases = [(x % 360) / 360.0 for x in raw_readings]
    avg_phase = sum(normalized_phases) / len(normalized_phases)

    # Distractor: secondary filter that isn't used
    high_threshold = 250
    low_threshold = 150
    clipped_data = [min(max(x, low_threshold), high_threshold) for x in adjusted_readings]

    # Actual processing path
    outlier_buffer = []
    processed_data = []
    for val in adjusted_readings:
        if val % 2 == 0 and val > 190:
            processed_data.append(val)
        elif val < 100:
            outlier_buffer.append(val)

    # Secondary filtering using slicing and modular arithmetic
    if len(processed_data) > 4:
        processed_data = processed_data[1:-1]  # Remove first and last
    else:
        padding_value = (processed_data[-1] % 7) * 3
        processed_data.append(padding_value)

    # Final computation
    correction_factor = len(outlier_buffer) - 1
    processed_data = [x - correction_factor for x in processed_data]

    filtered_sum = sum(processed_data)
    return filtered_sum

result = analyze_sensor_readings()
print(f"Target result: {result}")