def analyze_data_stream(raw_bytes, threshold=100):
    # Simulate preprocessing: filter and transform raw sensor data
    processed = [b for b in raw_bytes if b % 3 == 0]  # Keep multiples of 3
    shifted = [(b << 2) & 255 for b in processed]  # Bit shift and wrap within byte range

    # Irrelevant transformation: frequency analysis (not used later)
    freq_map = {}
    for byte in shifted:
        freq_map[byte] = freq_map.get(byte, 0) + 1
    entropy = 0.0
    total = len(shifted)
    for count in freq_map.values():
        p = count / total
        entropy -= p * __import__('math').log2(p) if p > 0 else 0

    # Decoy function: looks important but unused
    def decrypt_block(data, key=42):
        return [d ^ key for d in data]

    # Another red herring: checksum candidates computed but not all used
    candidate_sums = []
    for i in range(0, len(shifted), 2):
        if i + 1 < len(shifted):
            pair_sum = (shifted[i] + shifted[i+1]) % 256
            candidate_sums.append(pair_sum)

    # Real processing begins: find sequences above threshold
    segments = []
    current_seg = []
    for val in shifted:
        if val > threshold:
            current_seg.append(val)
        else:
            if len(current_seg) > 0:
                segments.append(current_seg)
                current_seg = []
    if current_seg:
        segments.append(current_seg)

    # Only consider the longest segment
    if not segments:
        valid_sequence = [0]
    else:
        valid_sequence = max(segments, key=len)

    # Apply complex masking logic with distractors
    base_mask = 0xAA  # Alternating bit pattern: 10101010
    inv_mask = ~base_mask & 255  # Inverted mask within byte
    rotation_count = len(valid_sequence) % 8

    # Misleading intermediate: circular rotation (unused)
    rotated_vals = []
    for v in valid_sequence:
        rotated = ((v << rotation_count) | (v >> (8 - rotation_count))) & 255
        rotated_vals.append(rotated)

    # Actual critical computation path
    mask = base_mask
    adjustment = len(valid_sequence) // 2
    if len(valid_sequence) > 4:
        adjustment += 5
    else:
        adjustment -= 2

    # Final loop with key assignment
    running_total = 0
    checksum = 0
    for i in range(len(valid_sequence)):
        if i % 2 == 0:
            temp_val = valid_sequence[i] + adjustment
            if temp_val > 200:
                mask ^= 0x55  # Toggle mask with 01010101
        # Key statement — target of the question
        checksum = (valid_sequence[i] ^ mask) + adjustment
        running_total += checksum

    # Output the target variable
    print(f"Result: {checksum}")

# Inputs for deterministic execution
raw_input = [12, 45, 72, 99, 105, 111, 130, 150, 160, 180, 201, 210, 240]
analyze_data_stream(raw_input)