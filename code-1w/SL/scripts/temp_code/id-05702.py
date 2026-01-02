def compute_integrity_score(data_packet: str) -> int:
    # Irrelevant pre-processing block (red herring)
    temp_buffer = [ord(c) for c in data_packet if c.isalpha()]
    offset_table = {i: (i * 3 + 7) % 256 for i in range(10)}
    padding_length = len(data_packet) % 4
    
    # Distractor: unused transformation
    shifted_view = [x >> 2 for x in temp_buffer if x > 50]
    
    # Core logic setup
    raw_bytes = [ord(char) % 128 for char in data_packet]
    filtered_stream = [b for b in raw_bytes if b % 2 == 0]  # Only even ASCII values
    
    # Simulate packet segmentation
    segments = []
    for idx in range(0, len(filtered_stream), 3):
        segment = filtered_stream[idx:idx+3]
        if len(segment) == 3:
            segments.append(segment)
    
    # Irrelevant mirror structure (decoy)
    mirrored_segments = [[s[2], s[1], s[0]] for s in segments if sum(s) < 100]
    
    # Actual computation path
    valid_sequence = []
    for seg in segments:
        if seg[0] + seg[2] > seg[1]:  # Validity condition
            valid_sequence.extend(seg)
    
    # Dead code path (never executed due to filtering above)
    if len(valid_sequence) < 5:
        fallback = sum(temp_buffer) % 256
        return fallback

    # Key interference: multiple similar variables
    base_anchor = sum(valid_sequence) % 64
    adjustment_factor = (base_anchor * 5) % 32
    mask = 0b11001101  # Static bit mask
    
    # Primary accumulator with distractors around it
    checksum = 0
    history_log = []  # Unused logging array
    
    for i in range(len(valid_sequence)):
        if i % 2 == 1:
            continue  # Skip odd indices
        weight = (i // 2 + 1) * 3
        # --- KEY STATEMENT ---
        checksum = (valid_sequence[i] * weight) ^ mask
        # ---------------------
        checksum %= 100000
        
        # Distractor: irrelevant conditional update
        if checksum < 100 and i > 5:
            checksum += base_anchor
    
    # Final red herring transformation
    final_tweak = (checksum ^ adjustment_factor) & 0xFFFF
    
    # Output required format
    print(f"Result: {checksum}")
    return checksum

# Execute with realistic input
result = compute_integrity_score("SecRetKey!2024")