from collections import defaultdict

# Simulate telemetry data processing with error masking and checksum validation
def process_telemetry_stream(raw_packets):
    packet_frequencies = defaultdict(int)
    cumulative_shift = 0
    data_sum = 0
    temp_buffer = []
    debug_flags = [False, True, False]

    for i, packet in enumerate(raw_packets):
        if len(packet) < 4:
            continue

        # Parse header and payload (first 2 and last 2 bytes)
        header = int(packet[:2], 16)
        payload = packet[2:-2]
        footer = int(packet[-2:], 16)

        # Irrelevant frequency tracking (distractor)
        packet_frequencies[header] += 1

        # Extract numeric values from payload characters
        payload_values = [ord(c) for c in payload if c.isalpha()]
        
        # Real computation: sum of ASCII values at even indices
        for j, val in enumerate(payload_values):
            if j % 2 == 0:
                data_sum += val * (i + 1)

        # Dead code path - never executed due to debug_flags
        if debug_flags[2] and i % 5 == 0:
            temp_buffer.append(sum(payload_values))

        # Bitwise manipulation chain with cumulative effect
        shift_step = (header ^ footer) & 0xF
        cumulative_shift = (cumulative_shift << 1) ^ shift_step
        if cumulative_shift > 255:
            cumulative_shift = cumulative_shift % 256

    # Secondary loop for rotational offset (only processes certain headers)
    rotation_factor = 0
    seen_headers = set()
    for packet in raw_packets:
        if len(packet) >= 4:
            hdr = int(packet[:2], 16)
            if hdr not in seen_headers:
                rotation_factor += (hdr >> 2) ^ 7
                seen_headers.add(hdr)
    
    # Extraneous string slicing and reversal (no impact)
    metadata_snippet = ''.join([p[:2] for p in raw_packets if len(p) >= 2])
    inverted_meta = metadata_snippet[::-1][:10]
    dummy_score = sum([int(inverted_meta[k:k+2], 16) for k in range(0, len(inverted_meta)-1, 2)]) % 99

    # Key computational step
    modulus = 982451653  # Large prime for modular arithmetic
    final_checksum = (data_sum + rotation_factor) % modulus

    # Red herring: unused conditional with complex logic
    if dummy_score > 50:
        alternate = (cumulative_shift * 2) % modulus
        final_checksum = min(final_checksum, alternate)

    print(f"Result: {final_checksum}")

# Input data - deterministic packet sequence
packets = [
    "A3xK9mZ", "B7yL2nQ", "C1zM5oP", "A3xN8pR", "D4wO1qS",
    "E9vP6rT", "F2uQ3sU", "G8tR7tV", "H6sS9uW", "I1rT4vX"
]

process_telemetry_stream(packets)