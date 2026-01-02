def analyze_data_stream(raw_input):
    # Preprocess: clean and validate input string
    cleaned = raw_input.strip().lower()
    if not cleaned.isalnum():
        cleaned = ''.join(ch for ch in cleaned if ch.isalpha())

    # Irrelevant transformation: character frequency analysis (distractor)
    freq_map = {}
    for ch in cleaned:
        freq_map[ch] = freq_map.get(ch, 0) + 1
    entropy_approx = 0.0
    for count in freq_map.values():
        prob = count / len(cleaned)
        entropy_approx -= prob * __import__('math').log2(prob)

    # Decoy computation: hash-like but unused final value
    decoy_hash = 0
    for i, ch in enumerate(cleaned):
        decoy_hash += ord(ch) * (31 ** i)
    decoy_hash %= 1000003

    # Extract numeric tokens from original (potential data payload)
    digits = ''.join([c for c in raw_input if c.isdigit()])
    if not digits:
        digits = '123456'

    # Parse sequence and apply transformations
    try:
        base_sequence = int(digits[:6])
    except ValueError:
        base_sequence = 654321

    # Apply bit manipulation chain with distractors
    inverted = 0
    temp = base_sequence
    for _ in range(6):
        inverted = (inverted << 1) | (temp & 1)
        temp >>= 1

    # Conditional branch based on string property (red herring)
    modifier = 1
    if len(cleaned) > 5 and cleaned[0] in 'aeiou':
        modifier = -1
    else:
        modifier = 1  # neutral effect

    # Real computational path begins here
    valid_sequence = base_sequence ^ inverted  # Bitwise symmetry check

    # Linear search for control offset (mixed relevance)
    offset_candidates = [17, 23, 41, 53]
    offset = 0
    for val in offset_candidates:
        if val > (len(cleaned) * modifier):
            offset = val
            break
    if offset == 0:
        offset = 97

    # Set-based duplicate detection in digit sequence (distractor)
    seen = set()
    has_duplicate = False
    for d in digits:
        if d in seen:
            has_duplicate = True
            break
        seen.add(d)

    # Unused recursive helper (dead code path)
    def calculate_depth(n):
        if n <= 1:
            return 1
        return n + calculate_depth(n // 2)

    # Primary masking operation with bitwise logic
    mask = 0xFFFFF  # 20-bit mask
    checksum = (valid_sequence ^ offset) & mask

    # Post-check: irrelevant formatting validation
    format_valid = raw_input.count('(') == raw_input.count(')') and raw_input.find('-') != -1

    # Final unrelated string method chain (distractor)
    metadata_tag = raw_input.upper().replace(' ', '_').lstrip('_').rstrip('_')
    tag_length = len(metadata_tag)

    return checksum

# Main execution
input_str = 'A1B2C3D4E5!@#'
data_checksum = analyze_data_stream(input_str)
print(f"Result: {data_checksum}")