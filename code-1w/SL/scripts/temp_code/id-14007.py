def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant pre-processing: string manipulation on metadata
    sensor_tag = 'SNSR-7X'
    normalized_tag = sensor_tag.lower().replace('-', '_')
    version_info = 'v2.1.0'
    if '2.1' in version_info:
        compatibility_flag = True
    else:
        compatibility_flag = False

    # Distractor: unused data transformation
    inverted_readings = [round(1 / x, 6) for x in raw_readings if x != 0]
    offset_shadow = sum(inverted_readings[:3]) * 0.1 if len(inverted_readings) > 3 else 0

    # Actual relevant logic begins: bitwise alignment of calibration
    aligned_phases = []
    for i, (ref, cal) in enumerate(zip(raw_readings, calibration_sequence)):
        shifted = (ref ^ cal) << 1  # XOR then left shift
        if shifted > 100:
            shifted = shifted ^ 0xFF  # bit flip mask
        aligned_phases.append(shifted)

    # Red herring: complex-looking but unused statistical block
    mean_aligned = sum(aligned_phases) / len(aligned_phases) if aligned_phases else 0
    variance_proxy = sum((x - mean_aligned) ** 2 for x in aligned_phases) / len(aligned_phases) if aligned_phases else 0
    entropy_simulator = 0
    for x in aligned_phases:
        if x > 0:
            entropy_simulator -= (x / 1000) * round(__import__('math').log(x / 1000), 4)

    # Real signal extraction: slicing and enumeration with conditional integration
    signal_envelope = 0
    for idx, val in enumerate(aligned_phases[5:15]):  # Focus on window
        if idx % 2 == 0:
            signal_envelope += val >> 2  # Right shift by 2
        else:
            signal_envelope -= val & 0x0F  # Mask last 4 bits

    # Decoy function call with no side effects
    def noise_estimator(data):
        return sum(x ** 0.5 for x in data if x > 0) * 0.01
    _ = noise_estimator(raw_readings)

    # Critical path: compute aggregate score using character count from encoded rule
    encoding_rule = 'AdjustForPhaseDrift'
    upper_count = len([c for c in encoding_rule if c.isupper()])  # 4 uppercase letters
    base_offset = 42
    aggregate_score = signal_envelope + (upper_count * base_offset)

    # Correction factor derived from string slicing and bitwise check
    slice_key = encoding_rule[6:11]  # 'ForPh'
    char_sum = sum(ord(c) for c in slice_key)
    parity_check = char_sum & 1  # LSB determines adjustment
    correction_factor = -5 if parity_check else 5

    # Final computation - this is the target statement
    final_diagnostic = aggregate_score + correction_factor

    # Dead code path - never executed due to fixed condition
    if len(raw_readings) < 0:
        fallback = sum(raw_readings) // 2
        final_diagnostic = fallback

    return final_diagnostic

# Execution context
readings = [120, 85, 93, 102, 77, 114, 68, 97, 131, 88, 73, 105, 99]
calibration = [50, 45, 63, 52, 87, 44, 78, 37, 21, 58, 93, 45, 69]
result = analyze_sensor_data(readings, calibration)
print(f"Result: {result}")