def analyze_data_stream(raw_bytes, mask_threshold=128):
    # Real data processing variables
    filtered_segments = []
    temp_buffer = []
    total_segments = 0

    # Irrelevant tracking variables (distractors)
    avg_latency = 0.0
    packet_loss_count = 0
    retransmission_flag = False
    sync_offset = 512
    calibration_factor = 1.05

    for byte in raw_bytes:
        if byte > mask_threshold:
            temp_buffer.append(byte & (mask_threshold - 1))
        elif byte == 64:
            if len(temp_buffer) >= 3:
                filtered_segments.append(temp_buffer[:])
                total_segments += 1
            temp_buffer.clear()
        else:
            temp_buffer.append(byte | 16)

    # Dead code path - never reached due to logic above (red herring)
    if retransmission_flag and sync_offset > 500:
        for i in range(len(temp_buffer)):
            temp_buffer[i] = int(temp_buffer[i] * calibration_factor)

    # Only use first valid segment
    if not filtered_segments:
        return -1
    
    primary_segment = filtered_segments[0]

    # Initialize key computation variables
    base_shift = 7
    running_key = 0
    checksum = 0
    adjustment = 13
    sequence_weight = [i * 2 + 1 for i in range(100)]  # Unused array (distractor)

    # Simulated decryption prep (partially relevant)
    key_seed = sum(primary_segment) % 256
    if key_seed % 2 == 0:
        running_key = key_seed << 1
    else:
        running_key = key_seed >> 1

    # Decoy transformation (looks important but unused)
    transformed = []
    for x in primary_segment:
        transformed.append((x ^ 255) + 1)

    # Actual critical sequence generation
    valid_sequence = []
    for x in primary_segment:
        if x % 4 == 0:
            valid_sequence.append(x // 4)
        elif x % 3 == 0:
            valid_sequence.append(x * 2)
        else:
            valid_sequence.append(x + 5)

    # Secondary decoy loop (misleading accumulation)
    aggregate = 0
    for val in valid_sequence:
        aggregate += val * val
        if aggregate > 10000:  # Unlikely condition
            break

    # Final checksum calculation with conditional expression
    for i in range(len(valid_sequence)):
        if i % 2 == 0:
            adjustment = 13 if running_key < 100 else 21
        else:
            adjustment = -7
        # Key statement: what is the value of 'checksum' after this line?
        checksum = (valid_sequence[i] ^ running_key) + adjustment
        running_key = (running_key + valid_sequence[i]) % 199

    # Additional irrelevant output suppression
    debug_mode = False
    if debug_mode:
        print(f'Debug: {aggregate}, {len(transformed)}')

    print(f"Result: {checksum}")