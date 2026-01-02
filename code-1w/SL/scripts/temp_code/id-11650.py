def compute_diagnostic_signature():
    # Simulated telemetry packet processing with embedded integrity check
    raw_payload = 'aB3#kP9!mQ2$vJ7*eF8@nR5&wE4^tH6'

    # Irrelevant transformation path 1: character classification
    digit_count = sum(c.isdigit() for c in raw_payload)
    upper_count = sum(c.isupper() for c in raw_payload)
    symbol_count = sum(c in '!@#$%^&*' for c in raw_payload)

    # Distractor: unused statistical profile
    profile_key = (digit_count * 17 + upper_count * 13 + symbol_count * 11) % 1009

    # Real data path begins: extract digits and map positions
    extracted_digits = [int(c) for c in raw_payload if c.isdigit()]
    positional_weights = [i + 1 for i in range(len(extracted_digits))]

    # Misleading accumulation - looks important but unused
    weighted_sum_fake = sum(d * (w % 4 + 1) for d, w in zip(extracted_digits, positional_weights))

    # Real computation: use only odd-positioned digits (1-indexed)
    relevant_digits = [d for i, d in enumerate(extracted_digits) if (i + 1) % 2 == 1]

    # Secondary filter: only digits greater than 3 contribute
    filtered_data = [d for d in relevant_digits if d > 3]

    # Compute primary data sum
    data_sum = sum(filtered_data) * 37  # Amplification factor

    # Intermediate derivation with string method distraction
    shift_token = ''.join(sorted(set(raw_payload), key=raw_payload.index))
    offset_char = shift_token[5]
    ascii_offset = ord(offset_char.lower()) - ord('a')

    # Bit manipulation chain
    temp_a = data_sum >> 2
    temp_b = temp_a ^ 0x1F
    temp_c = (temp_b + ascii_offset) & 0xFF
    intermediate = (temp_c * 13 + 5) % 97

    # Prime base derived from payload characteristics
    unique_letters = len([c for c in raw_payload if c.isalpha()])
    prime_base = 101 + (unique_letters % 12) * 2
    while any(prime_base % i == 0 for i in range(2, int(prime_base**0.5)+1)):
        prime_base += 2

    # Critical statement with target variable
    checksum = (data_sum ^ intermediate) % prime_base

    # Dead code path - never executed but looks related
    if digit_count < 0:  # Impossible condition
        backup_frame = [d ^ 7 for d in extracted_digits]
        checksum = sum(backup_frame) % 101

    # Unused alternate algorithm
    def crc_simulate(seq):
        crc = 0
        for b in seq:
            crc ^= b * 19
            crc = (crc << 1) % 256
        return crc

    # Output the actual result
    print(f"Result: {checksum}")

compute_diagnostic_signature()