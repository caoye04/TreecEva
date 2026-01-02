def analyze_signal_pattern(raw_samples, threshold=0.75):
    # Irrelevant pre-processing (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    outliers = [i for i, x in enumerate(normalized) if x > 0.9]
    spike_count = len([x for x in raw_samples if x > 100])

    # Key data transformation with meaningful operations
    binary_flags = []
    for idx, val in enumerate(raw_samples):
        if val % 2 == 0 and idx % 3 != 0:
            binary_flags.append(1)
        else:
            binary_flags.append(0)

    # Compute weighted phase shift (red herring computation)
    phase_shift = 0
    for i in range(1, len(raw_samples)):
        phase_shift += abs(raw_samples[i] - raw_samples[i-1]) * (i % 4)
    phase_shift /= len(raw_samples)

    # Actual relevant logic: character counting in hex representation
    hex_representations = [hex(x)[2:] for x in raw_samples]
    vowel_count = 0
    hex_vowels = 'abcdef'
    for h in hex_representations:
        for c in h:
            if c in hex_vowels:
                vowel_count += 1

    # Tuple unpacking and multiple assignments (relevant)
    total_sum, valid_entries = 0, 0
    for x in raw_samples:
        if x > 0:
            total_sum += x
            valid_entries += 1

    average_value = total_sum / valid_entries if valid_entries else 0

    # Bit manipulation chain (partly relevant, partly distractor)
    accumulator = 0
    for x in raw_samples[:5]:
        temp = (x ^ 255) & 0x7F
n        accumulator ^= temp

    # Decoy function call (dead path)
    def compute_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        entropy = 0
        for f in freq.values():
            p = f / len(data)
            entropy -= p * log(p)
        return entropy

    # Unused intermediate result (misleading)
    entropy_diagnostic = compute_entropy(raw_samples) if len(raw_samples) > 1 else 0

    # Conditional branch with early exit (not taken, but looks important)
    if len(outliers) > 10:
        return -999  # Dead code under current input

    # Core logic: count uppercase-worthy transformations
    case_conversion_points = 0
    for s in hex_representations:
        upper_version = s.upper()
        if any(c in 'ABCDEF' for c in s):
            case_conversion_points += 1

    # Critical calculation chain
    base_metric = vowel_count * case_conversion_points
    adjustment = len([x for x in binary_flags if x == 1])

    # Simultaneous assignment (relevant)
    aggregate_score, correction_factor = base_metric, 0

    # Complex conditional with nested logic
    if average_value > 50:
        if case_conversion_points > 3:
            correction_factor = 17
        else:
            correction_factor = 5
    elif phase_shift > 200:
        correction_factor = 10
    else:
        correction_factor = -3

    # Distractor: unused list comprehension with zip and enumerate
    indexed_pairs = [(i, a, b) for i, (a, b) in enumerate(zip(raw_samples, binary_flags)) if a % 10 == 0]
    auxiliary_total = sum(idx * val for idx, val, _ in indexed_pairs)

    # Final answer computation point
    final_diagnostic = aggregate_score + correction_factor

    print(f"Result: {final_diagnostic}")

# Input data with deterministic behavior
samples = [120, 150, 188, 205, 132, 97, 244, 177, 102, 251]
analyze_signal_pattern(samples)