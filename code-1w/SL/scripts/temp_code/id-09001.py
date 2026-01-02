def analyze_sensor_data(raw_readings, calibration_offset=0.73):
    # Irrelevant preprocessing: string cleaning (distractor)
    sensor_tag = 'SNSR-TEMP-042'
    cleaned_tag = sensor_tag.lower().replace('-', '_').strip('_')
    tag_length = len(cleaned_tag)
    unused_checksum = sum(ord(c) for c in cleaned_tag) % 256

    # Decoy data structure with misleading calculations
    decoy_buffer = [0] * 8
    for i in range(len(decoy_buffer)):
        decoy_buffer[i] = (i * calibration_offset * 100) % 47
    peak_decoy = max(decoy_buffer)

    # Real signal processing path (nested logic)
    filtered_readings = []
    for val in raw_readings:
        if val < 0:
            adjusted = abs(val) ** 0.5
        elif val == 0:
            adjusted = calibration_offset
        else:
            adjusted = val * 0.9 + calibration_offset
        filtered_readings.append(round(adjusted, 6))

    # Bit manipulation red herring (irrelevant to final result)
    binary_fingerprint = 0
    for x in [tag_length, len(raw_readings), int(calibration_offset * 100)]:
        binary_fingerprint ^= (x << 2) & 0xFF
    masked_fingerprint = binary_fingerprint & 0b11110000

    # Set operations used meaningfully but partially distracting
    expected_indices = set(range(len(raw_readings)))
    outlier_indices = {i for i, v in enumerate(filtered_readings) if v > 50}
    valid_indices = expected_indices - outlier_indices
    trimmed_readings = [filtered_readings[i] for i in sorted(valid_indices)]

    # Conditional expression chain with logical operations
    base_aggregate = sum(trimmed_readings)
    length_factor = len(trimmed_readings) if len(trimmed_readings) > 3 else 1
    safety_override = False
    override_flag = (len(outlier_indices) > 2) or (base_aggregate < 10)

    # Multi-step conditional with nested evaluation
    if override_flag and 'TEMP' in sensor_tag:
        aggregate_score = base_aggregate * 1.15
    elif not override_flag and tag_length > 10:
        aggregate_score = base_aggregate * 0.95
    else:
        aggregate_score = base_aggregate * 1.05  # Correct path taken

    # Temperature bias calculation – depends on string method outcome
    suffix_match = sensor_tag.endswith('042')
    version_code = ''.join([c for c in sensor_tag if c.isdigit()])
    version_valid = version_code.startswith('04') and len(version_code) == 3

    if suffix_match and version_valid:
        temperature_bias = 7.28
    else:
        temperature_bias = -3.41

    # Critical statement
    final_diagnostic = aggregate_score + temperature_bias

    # Dead code path – never executed due to logic above
    if masked_fingerprint < 0:
        final_diagnostic *= 0.5
        final_diagnostic += 100  # unreachable

    return final_diagnostic

# Main execution
readings = [12.1, -16.4, 0, 88.7, 45.2, 3.9]
calib_level = 0.73
result = analyze_sensor_data(readings, calib_level)
print(f"Target result: {result}")