def compute_diagnostic_sequence():
    # Simulated sensor data from a distributed system
    raw_readings = [189, 245, 112, 198, 201, 155, 176, 223, 134, 145, 167, 202, 111, 133, 154]

    # Irrelevant signal smoothing (distractor)
    smoothed = [raw_readings[i] for i in range(len(raw_readings)) if i == 0 or raw_readings[i] != raw_readings[i-1]]
    trend_offset = sum(smoothed[::2]) - sum(smoothed[1::2])

    # Critical diagnostic variables
    threshold = 140
    activation_flags = []
    debug_trace = []

    # Primary processing with red herrings
    for i, value in enumerate(raw_readings):
        if value < threshold:
            activation_flags.append(1)
            debug_trace.append(f'LOW_{i}')
        elif value > threshold + 50:
            activation_flags.append(3)
            debug_trace.append(f'HIGH_{i}')
        else:
            activation_flags.append(2)
            debug_trace.append(f'MED_{i}')

    # Dead code path - never executed due to constant condition (distractor)
    if False:
        backup_state = [x ^ 255 for x in raw_readings]
        recovery_hash = sum(backup_state) % 1000

    # Bit manipulation chain with decoy logic
    temp_shift = 0
    for flag in activation_flags[:5]:
        temp_shift = (temp_shift << 1) | (flag & 1)

    # Unused transformation (red herring)
    mirrored_indices = [len(raw_readings) - 1 - i for i in range(len(raw_readings))]
    reversed_sum = sum(raw_readings[i] for i in mirrored_indices[::3])

    # Core algorithm buried in noise
    base_key = 1984
    iteration_count = 0
    checksum = 0

    for idx, reading in enumerate(raw_readings):
        if idx % 2 == 0 and activation_flags[idx] != 1:
            # Key update step
            checksum += (reading ^ base_key) & 0xFF
            checksum = checksum % 9761
            iteration_count += 1

        # Decoy conditional that looks important
        if idx in [3, 7, 11]:
            dummy = (reading * 1103515245 + 12345) & 0xFFFFFFFF

    # Secondary processing on flags
    pattern_mask = 0
    for j in range(min(iteration_count, 4)):
        pattern_mask = (pattern_mask << 2) | (activation_flags[j] & 3)

    # Final index derived from complex but partially irrelevant logic
    final_index = (pattern_mask + temp_shift) % len(raw_readings)

    # CRITICAL STATEMENT: target execution point
    checksum = (checksum * 3) ^ final_index

    # Unrelated telemetry output (misleading)
    telemetry_summary = {
        'avg': sum(raw_readings) / len(raw_readings),
        'peak': max(raw_readings),
        'events': len(debug_trace)
    }

    # Correct result output
    print(f"Result: {checksum}")

compute_diagnostic_sequence()