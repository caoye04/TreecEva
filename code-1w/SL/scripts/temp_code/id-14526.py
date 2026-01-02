def analyze_frequency_signal(raw_samples, base_threshold=1024):
    # Irrelevant signal processing constants (distractors)
    noise_floor = 0.0314
    harmonic_mask = 0b110101
    gain_compensation = 1.87
    dummy_accumulator = 0

    # Real computation begins: process first 10 samples above threshold
    significant_samples = [x for x in raw_samples if x > base_threshold]
    truncated_data = significant_samples[:10]  # Slice to first 10 qualifying samples

    # Distractor: dead code path (never executed due to logic)
    if len(truncated_data) < 5:
        fallback_mode = True
        correction_vector = [0] * 5
        for i in range(len(correction_vector)):
            dummy_accumulator += i * noise_floor  # Misleading accumulation

    # Actual relevant transformations
    squared_magnitudes = [x ** 2 for x in truncated_data]
    sum_squares = sum(squared_magnitudes)
    sample_count = len(truncated_data)

    # Intermediate values with red herrings
    average_power = sum_squares / sample_count if sample_count else 0
    normalized_energy = int(average_power // 32)  # Integer division

    # Bit manipulation chain (relevant)
    bit_packed = 0
    for val in truncated_data:
        bit_packed ^= (val & 0xFF)  # XOR folding byte fragments

    # Decoy transformation (looks important but unused)
    spectral_weights = []
    for i in range(8):
        weight = (normalized_energy + i) % 7
        spectral_weights.append(weight * harmonic_mask)  # Unused list

    # Conditional mutation based on length parity (actual use)
    if len(truncated_data) % 2 == 0:
        adjusted_sum = normalized_energy + (bit_packed & 0xFFFF)
    else:
        adjusted_sum = normalized_energy - (bit_packed & 0xFFFF)

    # Rotation factor derived from slicing pattern
    slice_offset = len(raw_samples[::3])  # Every third element count
    rotation_factor = (slice_offset << 3) & 0xFF  # Left shift and mask

    # Key statement
    net_phase_shift = adjusted_sum ^ rotation_factor

    # Final distraction: unused control flow
    if net_phase_shift < 0:
        temp = ~net_phase_shift
        temp = temp % 1000
        # No assignment back, so irrelevant

    # Output target result
    print(f"Result: {net_phase_shift}")

# Simulate input and execution
data_stream = [950, 1030, 1120, 980, 1075, 1201, 1010, 1143, 1305, 1067, 1250, 1189, 1322]
analyze_frequency_signal(data_stream)