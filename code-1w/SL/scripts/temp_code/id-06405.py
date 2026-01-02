def process_data_stream(raw_bytes, config_flags):
    # Simulate low-level bit manipulation for data integrity verification
    state = 0
    temp_accum = 0
    mask = 0xFFFF
    debug_trace = []

    for byte in raw_bytes:
        if byte % 3 == 0:
            temp_accum += byte ^ 255
        elif byte % 5 == 0:
            temp_accum -= byte >> 2
        else:
            state ^= (byte << 3) & mask
            state += byte & 0xF

    # Irrelevant secondary processing path (dead branch due to fixed config)
    secondary_state = 0
    if config_flags.get('legacy_mode') and config_flags.get('debug_trace'):
        for b in raw_bytes:
            secondary_state += b * b
        secondary_state = secondary_state % 97

    # Conditional expression with red herring variables
    mode = 'fast' if config_flags.get('priority') == 'high' else 'safe'
    buffer_limit = 1024 if mode == 'fast' else 256

    # Unused but plausible-looking security padding
    padding_length = (buffer_limit - len(raw_bytes)) % 8
    security_nonce = (state ^ 0xABCDEF) & 0xFF if padding_length > 4 else 0

    # Core logic: checksum depends only on state and mode
    def finalize_hash(s, m):
        result = s * 31
        if m == 'safe':
            result ^= 0x55AA
        else:
            result ^= 0xAA55
        return (result + (result >> 8)) & 0xFFFFFF

    # Decoy function that looks important but is never called
    def compute_legacy_crc(data):
        crc = 0
        for d in data:
            for _ in range(8):
                if (crc ^ d) & 1:
                    crc = (crc >> 1) ^ 0xEDB88320
                else:
                    crc >>= 1
                d >>= 1
        return crc & 0xFFFFFFFF

    # Distractor: complex-looking but unused intermediate calculation
    weighted_sum = sum(b * (i + 1) for i, b in enumerate(raw_bytes) if i % 2 == 0)
    normalized_score = weighted_sum / len(raw_bytes) if raw_bytes else 0
    capped_value = min(normalized_score, 500)

    # Critical execution point
    checksum = finalize_hash(state, mode)

    # Print final result as required
    print(f"Result: {checksum}")

    # More irrelevant post-checksum operations
    audit_log = []
    if config_flags.get('audit'):
        audit_log.append({"final_checksum": checksum, "size": len(raw_bytes)})

    return checksum

# Fixed input to ensure deterministic output
input_bytes = [120, 85, 42, 193, 77, 38, 144, 201]
flags = {'priority': 'low', 'legacy_mode': False, 'audit': False}

# Execute
process_data_stream(input_bytes, flags)