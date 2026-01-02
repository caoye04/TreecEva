def analyze_data_stream(raw_bytes):
    # Simulate decoding of a structured binary-like data stream
    segments = []
    temp_buffer = []

    for b in raw_bytes:
        if b % 7 == 0 and b > 10:
            temp_buffer.append(b * 2)
        elif b % 5 == 0:
            temp_buffer.append(b + 3)
        else:
            temp_buffer.append(b)

        if len(temp_buffer) >= 4:
            segments.append(temp_buffer[:4])
            temp_buffer = temp_buffer[4:]

    # Irrelevant transformation - dead-end path
    decoy_segments = []
    for seg in segments:
        flipped = [seg[-i] for i in range(1, len(seg)+1)]
        decoy_segments.append([x ^ 15 for x in flipped if x % 2 == 1])

    # Misleading statistical summary (distractor)
    average_val = sum(sum(seg) for seg in segments) / max(len(segments), 1)
    outlier_count = sum(1 for seg in segments for val in seg if val > 50)

    # Core logic begins here — actual relevant path
    flattened = [val for seg in segments for val in seg]
    if len(flattened) < 8:
        return -1

    # Extract payload using slicing and filtering
    payload_slice = flattened[2:10]
    filtered_payload = [x for x in payload_slice if x % 4 == 2]

    # Introduce tuple-based mapping (red herring)
    mode_map = [(i, 'HIGH') if x > 30 else (i, 'LOW') for i, x in enumerate(filtered_payload)]
    mode_counts = {'HIGH': 0, 'LOW': 0}
    for _, mode in mode_map:
        mode_counts[mode] += 1

    # Real computation chain starts
    base_shift = len(filtered_payload) * 3
    offset = (base_shift ** 2) // 7 - 12
    modulus = 97

    valid_sequence = []
    for val in filtered_payload:
        transformed = (val * 3) + 5
        if transformed % 2 == 0:
            valid_sequence.append(transformed // 2)
        else:
            valid_sequence.append(transformed)

    # Secondary distraction: simulate checksum history
    historical_checksums = []n    temp_sum = 0
    for idx, v in enumerate(valid_sequence):
        temp_sum += v * (idx + 1)
        historical_checksums.append(temp_sum % 1000)

    # Final critical computation with key variable
    checksum = 0
    for i in range(len(valid_sequence)):
        checksum = (valid_sequence[i] + offset) % modulus
        # This overwrites in each iteration — only last matters

    # Print result as required
    print(f"Result: {checksum}")

    # Unused but plausible-looking verification
    verification = sum(valid_sequence) % modulus
    debug_info = {
        'payload_slice_len': len(payload_slice),
        'filtered_count': len(filtered_payload),
        'offset_used': offset,
        'modulus': modulus
    }

    return checksum

# Input data — deterministic
input_stream = [12, 15, 22, 25, 8, 35, 18, 40, 23, 50, 14, 55]
result = analyze_data_stream(input_stream)