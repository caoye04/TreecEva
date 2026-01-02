def calculate_performance(data):
    base_offset = 17
    adjustment_factor = 0
    cumulative_shift = 0

    # Preprocess: extract magnitude and sign indicators
    magnitudes = [abs(x) for x in data]
    signs = [1 if x >= 0 else -1 for x in data]

    # Misleading intermediate analysis (not directly used)
    avg_magnitude = sum(magnitudes) / len(magnitudes)
    peak_deviation = max(magnitudes) - min(magnitudes)
    adjustment_factor += avg_magnitude // 10

    # Key transformation using bitwise logic and shifts
    processed = []
    for i, val in enumerate(magnitudes):
        shifted = val << 1
        if i % 2 == 0:
            shifted ^= 3  # XOR mask on even indices
        processed.append(shifted)

    # Secondary pass with zip-based correlation check
    pairs = list(zip(processed, signs))
    correlated_sum = 0
    for idx, (val, sign) in enumerate(pairs):
        if sign == -1:
            correlated_sum += val // (idx + 1) if idx > 0 else 0

    # Accumulate core performance metric
    total_power = sum(processed)
    stability_penalty = len([p for p in processed if p > 50])

    # Red herring: unused diagnostic trace
    diagnostic_trace = []
    for i in range(len(processed)):
        diagnostic_trace.append((i, processed[i] & 7))  # Low-order bits, unused

    # Final computation with offset and penalty
    raw_score = total_power - stability_penalty * 4
    final_score = raw_score - base_offset + cumulative_shift

    return final_score

# Input data set
data_sequence = [12, -45, 23, 67, -11, 8, 34]

# Simulate auxiliary preprocessing (distractor)
decay_weights = [0.9 ** n for n in range(len(data_sequence))]
weighted_sum = sum(a * w for a, w in zip(data_sequence, decay_weights))

# Core execution point
final_score = calculate_performance(data_sequence)

# Output result
print(f"Result: {final_score}")