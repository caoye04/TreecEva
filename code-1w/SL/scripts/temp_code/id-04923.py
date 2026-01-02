def compute_diagnostic_sequence():
    readings = [12, 8, 15, 6, 9, 14, 7]
    thresholds = [10, 7, 13, 5, 8, 12, 6]
    flags = [False] * len(readings)

    # Initial state analysis with distractor variables
    total_power = 0
    baseline_energy = 0
    for i, val in enumerate(readings):
        if val > thresholds[i]:
            flags[i] = True
        total_power += val ** 2
        baseline_energy += val * 0.8  # Irrelevant to final result

    # Secondary processing: normalize and detect bursts
    normalized = []
    burst_count = 0
    for i, (val, th) in enumerate(zip(readings, thresholds)):
        norm_val = (val - th) / (th + 1)
        normalized.append(round(norm_val, 3))
        if norm_val > 0.5:
            burst_count += 1

    # Tertiary transformation: create phase-aligned buffer (distractor structure)
    aligned_buffer = []
    phase_shift = 0
    for i in range(len(normalized)):
        shifted = int(abs(normalized[i] * 100)) % 7
        phase_shift ^= shifted  # Semi-relevant but not used later
        aligned_buffer.append(shifted)

    # Core checksum derivation with key logic
    checksum = 17
    offset = len(readings) % 5

    temp_accum = 0  # Distractor accumulator
    for index, (reading, flag) in enumerate(zip(readings, flags)):
        if flag:
            temp_accum += reading % 4  # Computation not affecting final answer

        # Key update point
        checksum = (checksum * 3) ^ (index + offset)

        # Additional misleading branch
        if reading & 1:
            checksum -= 2
        else:
            checksum += 1

    # Final irrelevant adjustment
    final_scale = sum(aligned_buffer) / (len(aligned_buffer) or 1)
    adjusted_checksum = int(checksum * (final_scale / 10 + 1))  # Not printed

    print(f"Result: {checksum}")

compute_diagnostic_sequence()