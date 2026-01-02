def analyze_signal_stream(raw_samples):
    # Irrelevant preprocessing block (dead path)
    if len(raw_samples) < 5:
        return -999  # decoy return

    # Initialize multiple variables, many irrelevant
    temp_buffer = [0] * len(raw_samples)
    accumulator = 0
    shift_register = 0
    control_flag = False
    meta_sequence = []
    padding_offset = 17
    dummy_counter = 0

    for i in range(len(raw_samples)):
        sample = raw_samples[i]
        if i % 4 == 0 and sample > 0:
            shift_register ^= sample << 1
        elif i % 3 == 0:
            shift_register ^= sample >> 2
        else:
            shift_register += (sample ^ 255)

        temp_buffer[i] = (sample * 3 + 7) % 256
        if sample % 2 == 1:
            meta_sequence.append(sample & 63)

        # Red herring: complex-looking but unused computation
        dummy_counter += (sample ^ (i * 13)) & 0xF
        _ = (dummy_counter * dummy_counter) % 101  # unused

    # Another decoy transformation
    decoy_data = temp_buffer[::-1]
    for j in range(len(decoy_data)):
        decoy_data[j] = (decoy_data[j] ^ 171) ^ padding_offset

    # Actual relevant logic begins here — buried under noise
    filtered = [x for x in raw_samples if x > 10 and x < 200]
    if len(filtered) < 3:
        filtered.append(42)

    # Key slicing operation (required feature)
    window = filtered[1:-1] if len(filtered) > 4 else filtered

    # Bit manipulation chain with XOR and AND (suggested paradigm)
    mask = 0
    for val in window:
        mask ^= (val << 1) & 255
    mask &= 127

    # Boolean logic with short-circuiting (suggested paradigm)
    control_flag = (len(window) > 2) and (mask > 0) or (shift_register % 2 == 1)

    if control_flag:
        accumulator += mask * 2
    else:
        accumulator -= mask

    # Construct payload with known structure
    header = [107, 206, 12]
    body = [accumulator % 256]
    footer = [len(window), mask ^ 42]
    final_payload = header + body + footer

    # Multiple irrelevant variables to distract
    validation_hash = 0
    for k, v in enumerate(final_payload):
        validation_hash += (v ^ k) * 11
    validation_hash %= 10000

    # Unused recursive-like distraction
    def calc_noise(x):
        if x <= 1:
            return 1
        return x + calc_noise(x - 2)

    noise_value = calc_noise(len(final_payload))  # not used

    # Critical statement: extract checksum using XOR and sum
    mask_sum = sum([mask, len(window), shift_register & 0xFF]) & 0xFF
    checksum = final_payload[-1] ^ mask_sum  # <-- key execution point

    # Print result as required
    print(f"Result: {checksum}")

    # Decoy output
    debug_info = {'buffer_len': len(temp_buffer), 'flag': control_flag}
    return None  # ignored

# Inputs
samples = [15, 88, 192, 47, 13, 76, 201, 33, 94]
analyze_signal_stream(samples)