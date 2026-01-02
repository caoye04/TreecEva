def analyze_data_stream(data_packets, keys):
    # Irrelevant pre-processing: frequency analysis (dead code path)
    frequencies = {}
    for packet in data_packets:
        freq = sum(1 for c in str(packet) if c.isdigit())
        frequencies[packet] = freq  # Unused beyond this point

    # Distractor variables: energy metrics (no impact on result)
    total_energy = 0.0
    energy_log = []
    for k in keys:
        energy = (k ** 2) * 0.05
        energy_log.append(energy)
        total_energy += energy

    # Real computation begins: initialization
    base_value = 0
    modulus = 982451653  # Large prime for modular arithmetic
    temp_buffer = []

    # Simulated decryption key expansion (partly irrelevant)
    expanded_keys = []
    for i, k in enumerate(keys):
        expanded = (k + i * 17) | 0xABCDE
        if i % 2 == 0:
            expanded ^= 0xF0F0F
        expanded_keys.append(expanded)

    # Core logic with distractors interwoven
    checksum = 0
    debug_flags = [False] * len(data_packets)

    for idx, (packet, _) in enumerate(zip(data_packets, keys * (len(data_packets) // len(keys) + 1))):
        # Misleading intermediate transformation
        transformed = packet ^ 0x12345
        normalized = abs(transformed) % 100000

        # Dead code: diagnostic trace (never used)
        if normalized > 50000:
            debug_flags[idx] = True
            anomaly_score = normalized / 99999.0

        # Actual relevant calculation chain
        shift_factor = (idx + 1) % 7
        shifted = (normalized << shift_factor) & 0xFFFFFFF

        # Key update step
        base_value += shifted

        # Red herring: entropy simulation
        entropy_pool = 0
        for _ in range(3):
            entropy_pool = (entropy_pool * 789) ^ (shifted & 0xFF)
            entropy_pool %= 1000000

        # Critical statement with real answer contribution
        scaled_index = idx * 31
        checksum = (base_value ^ scaled_index) % modulus

        # Decoy storage (unused later)
        temp_buffer.append({'index': idx, 'value': checksum, 'key': expanded_keys[idx % len(expanded_keys)]})

    # Final red herring: post-processing that doesn't affect checksum
    final_diagnostic = sum(1 for x in temp_buffer if x['value'] > 500000)
    total_energy += final_diagnostic * 0.1

    print(f"Result: {checksum}")

# Inputs
packets = [12345, 67890, 23456, 78901, 34567]
keys = [987, 654, 321]
analyze_data_stream(packets, keys)