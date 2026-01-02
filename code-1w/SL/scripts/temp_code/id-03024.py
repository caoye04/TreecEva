def analyze_data_packet(packet):
    # Parse packet components
    raw_parts = packet.split('-')
    segment_a = raw_parts[0]
    segment_b = raw_parts[1]
    segment_c = raw_parts[2]

    # Extract numeric identifiers
    id_a = int(segment_a[1:3], 16)
    id_b = int(segment_b[0:2], 16)
    id_c = sum([ord(c) for c in segment_c]) % 100

    # Validate format and length
    valid_format = len(segment_a) == 4 and len(segment_b) == 4 and len(segment_c) == 3
    valid_chars = all(c.lower() in '0123456789abcdef' for c in (segment_a + segment_b))
    valid_count = 0

    if valid_format and valid_chars:
        valid_count += 1
        temp_sum = 0
        for i in range(len(segment_c)):
            temp_sum += ord(segment_c[i]) * (i + 1)
        weighted = temp_sum // 3

        # Secondary validation based on weighted score
        if weighted > 300:
            valid_count += 2
        elif weighted > 200:
            valid_count += 1

        # Distractor: unused checksum variant
        legacy_checksum = (id_a + id_b) * 7 % 97
        buffer_size = 1024
        alignment_offset = buffer_size % 8

        # Bit manipulation key
        prime_offset = 17
        magic_key = id_c & 0xFF
        magic_key = magic_key ^ 0xAA
        magic_key = magic_key | 0x55
        magic_key = magic_key & 0xFF  # Ensure 8-bit

        # Key computation point
        checksum = (valid_count * prime_offset) ^ magic_key

        # Irrelevant post-processing (dead code path, not affecting result)
        if checksum < 0:
            normalized = checksum + 256
        else:
            normalized = checksum % 256

        extra_weight = len(segment_a.lstrip('0')) + len(segment_b.lstrip('0'))
        padding_ratio = extra_weight / 8.0 if extra_weight > 0 else 0.0

        return checksum
    else:
        return -1

# Simulated input packet
packet = 'A3F1-BB22-XyZ'
result = analyze_data_packet(packet)
print(f'Result: {result}')