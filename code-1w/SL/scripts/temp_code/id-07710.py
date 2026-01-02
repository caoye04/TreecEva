def analyze_sequence(data_stream):
    # Irrelevant preprocessing: character frequency analysis (dead end)
    char_freq = {}
    for c in ''.join(data_stream):
        char_freq[c] = char_freq.get(c, 0) + 1

    # Misleading transformation chain
    shifted = [s[::-1].upper() for s in data_stream if len(s) > 3]
    reversed_chunks = list(map(lambda x: x[1], enumerate(shifted)))  # Unused

    # Core signal extraction (obscured)
    raw_signals = []
    for i, segment in enumerate(data_stream):
        if i % 2 == 0:
            raw_signals.append(sum([ord(ch) for ch in segment]) % 17)
        else:
            raw_signals.append(len(segment) ** 2 % 17)

    # Distractor: fake noise injection
    noise_pattern = [(i * 13) % 19 for i in range(len(raw_signals))]
    masked_signal = [s ^ n for s, n in zip(raw_signals, noise_pattern)]  # Looks important, unused later

    # Actual relevant path begins: encoding with side channel
    encoded_segments = []
    for idx, val in enumerate(raw_signals):
        temp = val
        temp ^= (idx * 3)  # Bit manipulation red herring
        temp += (idx % 5) * 2
        temp %= 97
        encoded_segments.append(temp)

    # Decoy function call (no effect)
    def apply_filter(x):
        return [e for e in x if e > 10]  # Never called

    # Weight assignment with misleading symmetry
    weights = []
    for j in range(len(encoded_segments)):
        weight = (j + 1) * 0.9
        weight -= (j % 3) * 0.1
        weights.append(round(weight, 2))

    # Spurious checksum (distractor)
    checksum = 0
    for x in weights:
        checksum = (checksum * 31 + int(x * 100)) % 10007

    # Critical operation buried in logic
    weighted_sum = 0
    norm_factor = 0
    for k in range(len(encoded_segments)):
        if k % 3 != 2:  # Selective inclusion
            weighted_sum += encoded_segments[k] * weights[k]
            norm_factor += weights[k]

    normalized_result = round(weighted_sum / norm_factor, 6) if norm_factor > 0 else 0

    # Secondary processing on alternate path
    alt_path = [x for x in encoded_segments if x % 4 == 0]
    alt_sum = sum(alt_path) // len(alt_path) if alt_path else 0  # Unused

    # Final aggregation using correct path
    final_diagnostic = int(normalized_result * 100) % 100000  # Key result

    # Dead code branches
    if len(str(final_diagnostic)) > 5:
        final_diagnostic //= 10

    # Output target
    print(f"Result: {final_diagnostic}")

# Execution entry
input_stream = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']
analyze_sequence(input_stream)