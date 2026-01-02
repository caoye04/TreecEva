def analyze_sequence(signal_str: str) -> int:
    # Irrelevant signal metadata (distractor variables)
    signal_id = "SIG-X9281"
    timestamp = "2024-05-21T10:30:45Z"
    source_node = 7
    protocol_version = "v3.1"

    # Decoy processing functions (dead code path)
    def decrypt_payload(data):
        return data[::-1]  # Unused

    def validate_header(head):
        return len(head) == 8 and head.isalnum()  # Never called

    # Real computation begins
    segments = signal_str.split('-')
    filtered_parts = []
    for segment in segments:
        cleaned = segment.strip().upper()
        if cleaned.startswith('X'):
            continue
        if len(cleaned) > 0 and cleaned[0].isdigit():
            filtered_parts.append(cleaned[:4])  # Truncate to first 4 chars

    # Secondary filtering based on character composition
    alphanumeric_only = []
    for part in filtered_parts:
        if part.isalnum() and not part.isdigit() and not part.isalpha():
            alphanumeric_only.append(part)

    # Count valid entries (core logic)
    valid_count = 0
    total_chars = 0
    special_flag = False

    for token in alphanumeric_only:
        vowel_count = sum(1 for c in token.lower() if c in 'aeiou')
        digit_count = sum(1 for c in token if c.isdigit())
        if vowel_count >= 1 and digit_count >= 1:
            valid_count += 1
        total_chars += len(token)
        if token.endswith('9'):
            special_flag = True  # Distractor flag, not used later

    # Position-based weight calculation (uses string slicing)
    weights = []    
    for i, token in enumerate(alphanumeric_only):
        mid_char_value = 0
        if len(token) >= 3:
            mid_char = token[len(token)//2]
            mid_char_value = ord(mid_char) - ord('A') if mid_char.isalpha() else int(mid_char)
        weight = (i + 1) * mid_char_value
        weights.append(weight)

    # Aggregate weight with modular reduction
    raw_weight = sum(weights)
    position_weight = max(1, raw_weight % 50) if raw_weight > 0 else 1

    # Checksum computation - target execution point
    checksum = (valid_count * position_weight) % 97

    # More red herrings below
    backup_checksum = 0
    if len(alphanumeric_only) > 0:
        last_len = len(alphanumeric_only[-1])
        backup_checksum = (last_len * 13) ^ 97  # Dead end

    temp_buffer = [0] * 8
    for k in range(len(temp_buffer)):
        temp_buffer[k] = (k * 17) % 251  # Filler computation

    metadata_summary = f"{signal_id}|{timestamp}"  # Unused string concat
    debug_trace = ''.join(sorted(set(signal_str.replace('-', ''))))[:10]  # Slicing distractor

    return checksum

# Input with deliberate noise and structure
input_signal = 'X7A2-M3B9-N8C4-P1D6-QRST-9L5M'
result = analyze_sequence(input_signal)
print(f"Result: {result}")