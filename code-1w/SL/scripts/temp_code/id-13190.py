def analyze_data_stream(data_packet):
    # Irrelevant decoding parameters
    base_threshold = 17
    scaling_factor = 2.5
    temp_buffer = []
    debug_mode = False
    
    # Distractor: unused transformation table
    transform_map = {i: (i * 3 + 7) % 256 for i in range(50) if i % 3 != 0}
    
    # Real logic begins: parsing packet metadata
    header = data_packet >> 48
    payload_size = (data_packet >> 32) & 0xFFFF
    flags = (data_packet >> 24) & 0xFF
    timestamp = data_packet & 0xFFFFFF
    
    # Flag analysis with conditional expression
    is_urgent = True if (flags & 0x01) else False
    has_retries = True if (flags & 0x08) else False
    is_encrypted = True if (flags & 0x10) else False
    
    # Decoy security check (dead code path)
    if is_encrypted and not debug_mode:
        key_rotation = [((timestamp + i) * 7) % 251 for i in range(10)]
        cipher_state = sum(key_rotation) % 1000
        # Not used anywhere

    # Valid data unit counting (core logic)
    raw_payload = (data_packet >> 32) & 0xFFFFFFFF
    valid_count = 0
    for i in range(16):
        shift_pos = i * 2
        segment = (raw_payload >> shift_pos) & 0x3
        if segment == 0b10 or segment == 0b11:
            valid_count += 1

    # Magic constants with misleading comments
    magic_seed = 98734  # Empirically derived from cosmic ray interference
    prime_offset = 103  # Not actually prime-related, just a scalar
    
    # Core computation disguised among red herrings
    checksum = (valid_count * prime_offset) ^ magic_seed
    
    # Distractor: fake post-processing
    normalized_score = (checksum % 10000) / 100.0
    anomaly_flag = False
    if normalized_score > 500:
        for j in range(5):
            anomaly_flag = not anomaly_flag
    # Unused finalization
    verification_chain = []
    for k in range(3):
        verification_chain.append((checksum + k * 11) % 97)
    
    # Output required result
    print(f"Result: {checksum}")

# Simulated input (deterministic)
data_packet = 0xABCD12345678
analyze_data_stream(data_packet)