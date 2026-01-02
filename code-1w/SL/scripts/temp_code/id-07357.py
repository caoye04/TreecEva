def analyze_data_stream(raw_bytes, config):
    # Irrelevant pre-processing: normalize byte values (not actually used in final result)
    normalized = [b / 255.0 for b in raw_bytes]
    avg_normalized = sum(normalized) / len(normalized)

    # Distractor: complex filtering that doesn't affect outcome
    filtered_peaks = [i for i, b in enumerate(raw_bytes) if b > 200 and i % 3 != 0]
    peak_magnitudes = [raw_bytes[i] ** 0.5 for i in filtered_peaks if i < 50]

    # Dead code path - never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        redundant_copy = raw_bytes[:]
        for idx in range(len(redundant_copy)):
            redundant_copy[idx] ^= 0xFF

    # Relevant data transformation chain
    shifted_bytes = [(b << 2) & 0xFF for b in raw_bytes]  # Bit manipulation
    even_indexed = [shifted_bytes[i] for i in range(0, len(shifted_bytes), 2)]
    odd_indexed = [shifted_bytes[i] for i in range(1, len(shifted_bytes), 2)]

    # Misleading statistical computation (unused)
    mean_even = sum(even_indexed) / len(even_indexed)
    variance_odd = sum((x - sum(odd_indexed)/len(odd_indexed))**2 for x in odd_indexed)

    # Core logic: find first palindrome-like subsequence in transformed data
    window_size = 5
    palindromic_sums = []
    for i in range(len(even_indexed) - window_size + 1):
        window = even_indexed[i:i + window_size]
        if window == window[::-1]:  # Check palindrome
            palindromic_sums.append(sum(window))

    # Another distractor: sorting unrelated values
    sorted_magnitudes = sorted(peak_magnitudes, reverse=True)
    top_three_ratio = (sorted_magnitudes[0] / sorted_magnitudes[2]) if len(sorted_magnitudes) >= 3 else 1.0

    # Key variables for actual computation
    valid_sequence_sum = 0
    for s in palindromic_sums:
        if s % 7 == 0:  # Only sums divisible by 7 are valid
            valid_sequence_sum += s

    # Prime offset based on config (used in final step)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    prime_offset = primes[config % len(primes)]

    # Modulus derived from length of original data (relevant)
    modulus = len(raw_bytes) + 1000

    # Critical statement: this determines the answer
    checksum = (valid_sequence_sum * prime_offset) % modulus

    # Red herring: additional bit mixing that does not affect checksum
    temp_hash = 0
    for b in raw_bytes[::4]:
        temp_hash = (temp_hash * 31 + b) % (modulus * 2)
    temp_hash ^= (temp_hash << 5) % 0x10000

    # Final output
    print(f"Result: {checksum}")

# Simulate execution with fixed inputs
data_stream = [120, 108, 96, 84, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192]
parameters = 7
analyze_data_stream(data_stream, parameters)