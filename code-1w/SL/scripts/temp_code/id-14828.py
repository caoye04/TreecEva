def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 0.98 for x in raw_readings if x > 0]
    offset_map = {i: val % 7 for i, val in enumerate(calibration_sequence)}

    # Dead code path - never executed due to condition
    auxiliary_buffer = []
    if len(raw_readings) < 5:
        for item in raw_readings:
            auxiliary_buffer.append(item ** 2)

    # Core signal extraction (relevant)
    filtered = [x for x in raw_readings if x >= 50 and x <= 200]
    base_energy = sum(filtered) / len(filtered) if filtered else 0

    # Bit manipulation decoy (misleading intermediate)
    encoded_flag = 0
    for val in calibration_sequence[:4]:
        encoded_flag ^= (val << 2) | (val & 3)
    encoded_flag = (encoded_flag & 0xFF) ^ 0xAA

    # Unused statistical analysis (red herring)
    mean_deviation = 0
    if len(normalized) > 0:
        mean_val = sum(normalized) / len(normalized)
        mean_deviation = sum(abs(x - mean_val) for x in normalized) / len(normalized)

    # Conditional masking with zip (real but indirect contribution)
    paired_offsets = list(zip(filtered, calibration_sequence))
    adjusted_peaks = []
    for i, (val, cal) in enumerate(paired_offsets):
        if i % 3 == 0:
            adjusted_peaks.append(val - (cal % 9))
        elif i % 3 == 1:
            adjusted_peaks.append(val + (cal % 5))
        else:
            adjusted_peaks.append(val)

    # Fake recursive trap (never called)
    def integrate_noise(level, depth):
        if depth == 0:
            return level
        return integrate_noise(level + 1, depth - 1)

    # Actual accumulation logic
    aggregate_score = 0
    for idx, peak in enumerate(adjusted_peaks):
        if idx % 2 == 0:
            aggregate_score += int(peak // 3)
        else:
            aggregate_score -= int(peak % 11)

    # Decoy transformation chain
    temp_result = base_energy * 1.5
    temp_result = abs(temp_result - 100)
    temp_result = round(temp_result, 2)

    # Critical correction from side channel
    parity_check = sum(1 for x in calibration_sequence if x % 2 == 0)
    correction_factor = 0
    if parity_check >= 3:
        correction_factor = 17
    else:
        correction_factor = -8

    # Final computation (key statement)
    final_diagnostic = aggregate_score + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Irrelevant cleanup
    del normalized, offset_map, paired_offsets

    return final_diagnostic

# Inputs
sensor_input = [65, 72, 210, 88, 94, 45, 115, 130]
calib_seq = [12, 18, 24, 7, 30, 3]

# Execution
result = analyze_sensor_data(sensor_input, calib_seq)