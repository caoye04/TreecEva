def compute_integrity_code(sequence):
    # Irrelevant pre-processing: character frequency analysis (dead path)
    char_freq = {}
    for c in sequence:
        char_freq[c] = char_freq.get(c, 0) + 1
    unique_chars = len(char_freq)
    entropy = 0.0
    for count in char_freq.values():
        p = count / len(sequence)
        entropy -= p * __import__('math').log2(p) if p > 0 else 0

    # Distractor: unused transformation pipeline
    transformed = ''.join(chr((ord(c) + 7) % 95 + 32) for c in sequence)
    reversed_seq = transformed[::-1]
    dummy_sum = sum(ord(c) for c in reversed_seq[:10])

    # Relevant data path begins here
    raw_values = [ord(c) * 3 + 1 for c in sequence]
    filtered = [v for v in raw_values if v % 2 == 1]  # Keep only odd values

    # Complex conditional expression (python idiom)
    base_offset = 256 if len(filtered) > 10 else (128 if len(filtered) > 5 else 64)

    # Multi-step computation with nested logic
    temp = 0
    for i, val in enumerate(filtered):
        if i % 3 == 0:
            temp += val * 2
        elif i % 3 == 1:
            temp += val >> 2
        else:
            temp += val ^ (i * 3)

    data_sum = temp ^ base_offset

    # Bit manipulation chain with distractors
    flags = 0b110101
    mode_flag = flags & 0b11
    shift_control = (flags >> 2) & 0b111
    parity_check = (flags >> 5) & 1

    # Unused flag combinations (red herring)
    if mode_flag == 1:
        mask = 0xFFFF
    elif mode_flag == 2:
        mask = 0xFF0F
    else:
        mask = 0xF0FF  # This is always used

    # Critical operation buried in logic
    modulus = 10007
    checksum = (data_sum ^ mask) % modulus

    # Dead code: post-checksum transformations
    encoded_checksum = ((checksum << 3) | (checksum >> 10)) & 0xFFFF
    validation_string = f"CHK{encoded_checksum:05X}"
    final_verify = sum(ord(c) for c in validation_string) % 100

    return checksum

# Input string with non-uniform distribution
input_sequence = "A1B2C3D4E5F6G7!"
result = compute_integrity_code(input_sequence)
print(f"Result: {result}")