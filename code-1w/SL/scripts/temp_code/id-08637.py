def analyze_sensor_data(raw_readings, threshold=0.75):
    # Irrelevant transformation: normalize readings (not used in final result)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in raw_readings if x > sum(raw_readings) / len(raw_readings)]

    # Distractor variables
    outlier_count = 0
    cumulative_noise = 0
    for val in raw_readings:
        if val < 50:
            outlier_count += 1
        else:
            cumulative_noise += val % 7

    # Real computation begins: frequency analysis
    freq_map = {}
    for r in raw_readings:
        freq_map[r] = freq_map.get(r, 0) + 1

    # Extract high-frequency values above threshold ratio
    total = len(raw_readings)
    high_freq_values = [k for k, v in freq_map.items() if v / total >= threshold]

    # Secondary distractor: string-based encoding of frequencies (red herring)
    freq_strings = [f"{k}:{v}" for k, v in freq_map.items()]
    encoded = set("|".join(freq_strings).replace(":", "x").split('|'))
    size_hint = len(encoded) * 2  # Misleading value

    # Bit manipulation layer (partially relevant)
    shifted_vals = []
    for v in high_freq_values:
        if v > 0:
            bit_shifted = (v << 2) ^ 0b1010  # XOR with arbitrary pattern
            shifted_vals.append(bit_shifted)

    # Another dead-end: combinatorics on shifted values (unused)
    from math import comb
    pair_count = 0
    for i in range(len(shifted_vals)):
        for j in range(i + 1, len(shifted_vals)):
            if shifted_vals[i] != shifted_vals[j]:
                pair_count += comb(2, 1)  # Always adds 2 per valid pair

    # Core logic path: only this affects the answer
    base_signal = sum(high_freq_values)  # Only non-empty if duplicates exist above threshold
    adjustment = len(raw_readings) % 9
    aggregate_score = (base_signal * 3) + adjustment

    # Redundant factor derived from unused components (distractor)
    decoy_sum = sum([len(s) for s in freq_strings]) + size_hint
    redundant_factor = decoy_sum % 17 if decoy_sum > 0 else 5

    # Key statement
    final_diagnostic = aggregate_score // (redundant_factor + 1)

    # Print required output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Simulated sensor input with deliberate structure
sensor_input = [120, 85, 120, 90, 120, 120, 85, 120, 90, 120]
analyze_sensor_data(sensor_input)