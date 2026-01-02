def analyze_data_stream(data_packets):
    # Irrelevant processing: signal strength simulation
    signal_strength = sum([len(p) * 0.75 for p in data_packets if len(p) > 3])
    threshold = 15.0
    quality_flag = signal_strength > threshold

    # Distractor: network latency compensation (unused)
    latency_shift = 0
    for packet in data_packets:
        if 'X' in packet:
            latency_shift += hash(packet) % 7

    # Real computation begins: extract payload sequences
    raw_payloads = []
    for pkt in data_packets:
        cleaned = ''.join([c for c in pkt if c.isalpha() or c.isdigit()])
        if cleaned:
            raw_payloads.append(cleaned)

    # Extract numeric digits from each payload
    digit_sequences = []
    for payload in raw_payloads:
        digits = [int(c) for c in payload if c.isdigit()]
        if digits:
            digit_sequences.append(digits)

    # Compute sequence_sum: sum of last digit of each sequence
    sequence_sum = 0
    for seq in digit_sequences:
        sequence_sum += seq[-1]  # Last digit only

    # Distractor: character frequency analysis (not used in final result)
    char_freq = {}
    for payload in raw_payloads:
        for c in payload:
            char_freq[c] = char_freq.get(c, 0) + 1

    # Another red herring: palindrome check on payloads
    palindromes_found = 0
    for payload in raw_payloads:
        if len(payload) > 1 and payload == payload[::-1]:
            palindromes_found += 1

    # Key transformation: apply modulo-based shift
    base_offset = 97
    transformed_values = []
    for i, payload in enumerate(raw_payloads):
        val = sum(ord(c.lower()) - base_offset for c in payload if c.isalpha())
        transformed_values.append(val % 16)

    # Compute primary key through list comprehension with filtering
    valid_transforms = [v for v in transformed_values if v % 3 == 0]
    if not valid_transforms:
        valid_transforms = [0]
    primary_key = sum(valid_transforms) * len(valid_transforms)

    # Secondary key via set operations: unique even digits
    all_even_digits = set()
    for seq in digit_sequences:
        all_even_digits.update({d for d in seq if d % 2 == 0})
    secondary_key = sum(all_even_digits) if all_even_digits else 1

    # Final key derived from modular arithmetic
    final_key = (primary_key + secondary_key) % 256

    # Critical statement: compute checksum using bitwise operations
    checksum = final_key ^ (sequence_sum & 255)

    # Unrelated logging output (dead code path)
    debug_log = []
    for i in range(3):
        debug_log.append(f"Step {i}: nop")

    # Output the target result
    print(f"Result: {checksum}")

# Input data - deterministic packet stream
data_stream = [
    "AX4B2", "CXX", "D9M5N1", "RSTUV", "K7L", "ABBA", "X0Y0Z0"
]

analyze_data_stream(data_stream)