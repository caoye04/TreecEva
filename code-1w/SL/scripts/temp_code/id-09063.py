def analyze_sensor_data(raw_stream, threshold=0.75):
    # Irrelevant preprocessing: case conversion and character counting
    metadata_tag = 'SENSOR_DIAG_V2'
    shifted_tag = metadata_tag.lower().replace('_', '')
    tag_length = len(shifted_tag)
    temp_offset = tag_length * 0.1

    # Simulate raw signal unpacking (only some values matter)
    signal_slice = raw_stream[::2]  # Every other reading - actual relevant data
    calibration_peaks = [x for x in raw_stream if x > threshold]
    noise_floor = sum(1 for x in raw_stream if x < 0.1)

    # Distractor: unused complex transformation
    def wavelet_transform(data):
        return [data[i] - data[i-1] for i in range(1, len(data))] + [0]

    transformed = wavelet_transform(raw_stream)  # Dead code path

    # Real logic begins: count valid pulses above dynamic baseline
    baseline = sum(signal_slice) / len(signal_slice)
    pulse_count = 0
    for val in signal_slice:
        if val > baseline * 1.1:
            pulse_count += 1

    # Secondary validation via symmetry check on first half
    mid = len(signal_slice) // 2
    front_half = signal_slice[:mid]
    back_half = signal_slice[mid:]
    if len(front_half) == len(back_half):
        reverse_sum_diff = sum(abs(a - b) for a, b in zip(front_half, reversed(back_half)))
        symmetry_score = 1 / (1 + reverse_sum_diff)
    else:
        symmetry_score = 0.5

    # Aggregate preliminary metrics
    quality_weight = len(calibration_peaks) / len(raw_stream)
    aggregate_score = pulse_count * 100 + int(symmetry_score * 100)

    # Correction based on auxiliary conditions (bit manipulation red herring)
    flag_register = 0xA3
    masked_flags = flag_register & 0x0F
    parity_check = bin(masked_flags).count('1') % 2
    correction_factor = 5 if parity_check else -5

    # Dead-end conditional with no effect
    if noise_floor > 10:
        adjustment_curve = [i ** 0.5 for i in range(noise_floor)]
        temp_offset -= sum(adjustment_curve)  # Unused

    # Critical assignment - this determines the answer
    final_diagnostic = aggregate_score + correction_factor

    # Unrelated string processing distraction
    log_entry = f'DIAG:{final_diagnostic:04d}'
    rotated_chars = log_entry[-4:] + log_entry[:-4]
    checksum_val = sum(ord(c) for c in rotated_chars) % 256

    # Final irrelevant list grouping
    groups = {}
    for x in raw_stream:
        key = int(x * 10)
        if key not in groups:
            groups[key] = []
        groups[key].append(x)

    # Output the required result
    print(f'Result: {final_diagnostic}')
    return final_diagnostic

# Input data with deterministic pattern
input_stream = [0.2, 0.82, 0.15, 0.91, 0.08, 0.88, 0.12, 0.76, 0.3, 0.79]
analyze_sensor_data(input_stream)