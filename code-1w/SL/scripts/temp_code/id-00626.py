def compute_diagnostic_signature():
    # System diagnostic parameters
    base_frequency = 440
    sample_rate = 44100
    harmonics = [1, 5, 7, 11, 13]
    phase_offset = 0.25

    # Irrelevant audio synthesis variables (distractors)
    amplitude_envelope = [0.1, 0.3, 0.8, 1.0, 0.9, 0.7, 0.5, 0.2]
    modulation_index = 4.0
    carrier_freq = base_frequency * 2

    # Core data buffer with diagnostic telemetry
    telemetry_stream = [
        0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70, 0x81,
        0x92, 0xA3, 0xB4, 0xC5, 0xD6, 0xE7, 0xF8, 0x09
    ]

    # Misleading checksums (decoy)
    crc16_table = [i for i in range(256)]  # Unused table
    rolling_avg = sum(harmonics) / len(harmonics)  # Not used in final result

    # Signal processing artifacts
    fft_magnitude = [0] * 16
    for i in range(16):
        angle = phase_offset * 2 * 3.14159 * i / 16
        fft_magnitude[i] = int(100 * ((i+1)**0.5))

    # Real computation begins here
    window_size = 4
    checksum = 0
    temp_factor = 7

    for i in range(0, len(telemetry_stream), window_size):
        segment = telemetry_stream[i:i + window_size]
        
        # Slice manipulation with bit operations
        if len(segment) == window_size:
            segment_sum = sum(s ^ (s << 1) & 0xFF for s in segment)
            parity_check = bin(segment_sum).count('1') % 2
            
            if parity_check:
                segment_sum = segment_sum >> 1
            
            # Key update point
            checksum = (checksum * 3) ^ (segment_sum % 256)
            
            # Dead code path - early return trap
            if checksum < 0:
                return -1  # Never reached
            
            # More irrelevant transformations
            temp_factor = (temp_factor + checksum) % 19

    # Additional decoy logic
    secondary_checksum = 0
    for b in telemetry_stream:
        secondary_checksum = (secondary_checksum << 1) ^ b
        if secondary_checksum > 255:
            secondary_checksum &= 0xFF

    # Final red herring: unused conditional branch
    if temp_factor in harmonics:
        checksum = checksum | 0x80  # Not triggered due to values

    print(f"Result: {checksum}")

compute_diagnostic_signature()