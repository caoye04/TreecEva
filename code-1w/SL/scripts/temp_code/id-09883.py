def analyze_data_stream(data_packet):
    # Irrelevant preprocessing: base conversion with unused results
    raw_hex = ''.join(format(ord(c), '02x') for c in data_packet)
    temp_blocks = [raw_hex[i:i+4] for i in range(0, len(raw_hex), 4)]
    decoy_value = sum(int(b, 16) for b in temp_blocks if len(b) == 4) % 97

    # Distractor: checksum-like operations that are never used
    legacy_checksum = 0
    for ch in data_packet[:10]:
        legacy_checksum += ord(ch) * 3
    legacy_checksum &= 0xFF

    # Real computation begins: extract payload segment
    payload = data_packet[12:36]  # Critical slicing: only this portion matters

    # Misleading compression simulation (dead path)
    compressed_hint = ''.join(chr(ord(c) >> 2) for c in payload)
    size_prediction = len(compressed_hint) * 2 + 10  # Unused

    # Core logic: character frequency analysis
    char_count = 0
    for char in payload:
        if char in 'AEIOUaeiou':
            char_count += 1
        elif char.isalpha():
            char_count += 2  # Consonants count double

    # Secondary distraction: timestamp embedding (irrelevant)
    timestamp_tag = [ord(data_packet[i]) for i in [1, 4, 7] if i < len(data_packet)]
    noise_factor = sum(timestamp_tag) % 50 if timestamp_tag else 25

    # Actual signal path: process numeric contributions
    numeric_part = []
    for c in data_packet:
        if c.isdigit():
            numeric_part.append(int(c))

    # Real calculation chain starts here
    base_sum = sum(n * (n + 1) for n in numeric_part)  # Triangular number contribution
    scaled_sum = base_sum * 3

    # Combine with payload length (slicing dependency)
    length_mod = len(payload) ** 2
    intermediate = scaled_sum + length_mod

    # Introduce bit manipulation red herring
    bit_fiddle = intermediate
    for _ in range(3):
        bit_fiddle = ((bit_fiddle << 1) | (bit_fiddle >> 15)) & 0xFFFF
    # But we don't use bit_fiddle!

    # True computation continues independently
    offset_correction = 17
    if len(numeric_part) > 2:
        offset_correction = numeric_part[0] * 10 + numeric_part[1]

    final_sum = intermediate // 2 + offset_correction

    # Final key operation: XOR with vowel/consonant count mod 256
    checksum = final_sum ^ (char_count % 256)

    # Output required format
    print(f"Result: {checksum}")

# Simulated data input
transmission = "HDR@2023!LOGIC_FLOW#X9P8M5K2V"
analyze_data_stream(transmission)