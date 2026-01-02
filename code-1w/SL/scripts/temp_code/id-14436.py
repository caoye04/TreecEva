from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def analyze_readings(data_stream):
    raw_counts = defaultdict(int)
    signal_peaks = []
    temp_buffer = []
    checksum = 0
    normalization_factor = 1.0
    decoy_sum = 0  # Irrelevant accumulator

    for i, val in enumerate(data_stream):
        raw_counts[val] += 1
        if val > 50 and i % 2 == 0:
            signal_peaks.append(val)
        elif val < 10:
            temp_buffer.append(val ** 2)
        checksum ^= val  # Bitwise distraction

    # Dead code path - never used in final result
    if len(temp_buffer) > 5:
        average_noise = sum(temp_buffer) / len(temp_buffer)
        for x in temp_buffer:
            decoy_sum += abs(x - average_noise)

    # Real processing begins here
    peak_count = len(signal_peaks)
    unique_signals = len(raw_counts)

    # Simulated diagnostic stages
    stage_weights = [0.8, 1.2, 0.9, 1.1]
    diagnostics = []
    for shift in range(4):
        shifted_peaks = [p >> shift for p in signal_peaks]  # Bit manipulation red herring
        diagnostics.append(sum(shifted_peaks) * stage_weights[shift])

    aggregate_score = sum(diagnostics) / 4

    # Distractor: complex but unused calculation
    entropy = 0.0
    total = sum(raw_counts.values())
    for count in raw_counts.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)

    # Critical computation chain
    outlier_flags = 0
    for a, b in zip(data_stream, data_stream[1:]):
        if (a ^ b) & 1:  # XOR pattern check
            outlier_flags += 1

    noise_ratio = outlier_flags / (len(data_stream) - 1) if len(data_stream) > 1 else 0
    correction_factor = unique_signals - peak_count

    # Key statement
    final_diagnostic = aggregate_score + correction_factor * (1 - noise_ratio)

    # Additional irrelevant transformation
    inverted_map = {v: k for k, v in enumerate(sorted(set(data_stream)))}
    sorted_diagnostics = sorted(diagnostics, reverse=True)
    weighted_rank = sum(i * val for i, val in enumerate(sorted_diagnostics))

    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data crafted for deterministic output
data_sequence = [12, 55, 34, 67, 55, 23, 78, 55, 12, 89, 91, 55, 12, 34, 67, 44, 55, 78]
analyze_readings(data_sequence)
