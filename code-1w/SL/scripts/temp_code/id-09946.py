def analyze_data_stream(raw_packets, threshold, debug_mode=False):
    # Irrelevant diagnostic counters
    overhead_bytes = 0
    retry_attempts = 3
    temp_buffer = [0] * 128
    sequence_id = 789
    protocol_version = '2.1'

    # Key variables
    valid_count = 0
    error_flag = False
    magic_seed = 0x1F3D
    prime_offset = 1013  # Large prime for diffusion
    rolling_sum = 0
    stage_mask = 0b1101

    # Decoy function - never called
    def decrypt_payload(data):
        return [d ^ 0x5A for d in data]

    # Unused transformation matrix
    transform_matrix = [
        [1, -1, 0],
        [0, 1, -1],
        [-1, 0, 1]
    ]

    for packet in raw_packets:
        # Simulate header parsing
        if len(packet) < 4:
            continue
        
        payload_size = packet[0] & 0x7F
        flags = packet[1]
        checksum_hint = packet[2] ^ packet[3]

        # Irrelevant bit manipulation
        extended_flag = (flags << 4) | (flags >> 4)
        if extended_flag == 0xAB:
            overhead_bytes += 1  # Dead code path

        # Real logic begins
        data_segment = packet[4:4+payload_size]
        
        # Validate content
        if not data_segment:
            continue
            
        segment_sum = sum(data_segment) % 256
        is_valid = (segment_sum ^ checksum_hint) < threshold
        
        # Conditional expression with side-effect-free computation
        size_class = 'L' if payload_size > 10 else ('M' if payload_size > 5 else 'S')
        
        # Only medium and large packets are counted if they pass validation
        if is_valid and size_class in ['M', 'L']:
            valid_count += 1
            rolling_sum += segment_sum
            
            # Early break red herring: this condition is never met
            if rolling_sum > 10000:
                error_flag = True
                break

        # Distraction: update temp buffer with irrelevant pattern
        for i in range(len(temp_buffer)):
            temp_buffer[i] = (temp_buffer[i] + 17) % 251

    # Critical computation masked among decoys
    final_shift = (rolling_sum & 0xF) + 1
    adjusted_rolling = (rolling_sum >> final_shift) | (rolling_sum << (8 - final_shift))
    adjusted_rolling &= 0xFF

    # This looks like a possible answer, but it's a decoy
    legacy_compatibility_value = (adjusted_rolling * valid_count) % 65536

    # Another dead-end calculation
    if debug_mode:
        diagnostic_hash = sum(temp_buffer) ^ sequence_id
    
    # The real answer is computed here
    checksum = (valid_count * prime_offset) ^ magic_seed
    
    # Final red herring: unused conditional override
    if error_flag and protocol_version.startswith('3'):
        checksum ^= 0xFFFF

    # Output the target result
    print(f"Result: {checksum}")

# Simulated input
packets = [
    [12, 0x23, 0x45, 0x12, 1, 2, 3, 4, 5, 6, 7],
    [8, 0x15, 0x30, 0x0F, 10, 20, 30],
    [3, 0x0A, 0x55, 0x15, 100, 200],
    [15, 0x31, 0x28, 0x22, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    [6, 0x1E, 0x3C, 0x1B, 7, 7, 7, 7, 7, 7]
]

analyze_data_stream(packets, threshold=100)