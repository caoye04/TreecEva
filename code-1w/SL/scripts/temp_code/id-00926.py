def compute_diagnostic_sequence():
    # Sensor readings simulation with noise filtering
    raw_signals = [23, 45, 67, 12, 89, 34, 56]
    filtered = [x for x in raw_signals if x > 30]  # Only significant signals

    # State initialization
    base_offset = 19
    temporal_factor = len(filtered) * 2
    accumulator = 0
    phase_shift = 0

    # Irrelevant intermediate: signal quality metric (not used later)
    quality_score = sum([x % 11 for x in raw_signals]) + base_offset

    # Main processing loop with nested logic
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            accumulator += val ^ (base_offset + i)
        else:
            accumulator -= val & (temporal_factor // (i + 1))

        # Additional state tracking (distractor)
        phase_shift = (phase_shift + val) % 25

    # Secondary computation: statistical moment (semi-relevant)
    squared_deviation = sum([(x - 50)**2 for x in filtered]) // len(filtered)

    # Aggregation with red herring variables
    offset_compensation = base_offset << 1  # Unused but computed
    correction_factor = 0
    for j in range(3):
        correction_factor += (squared_deviation >> j) & 1

    aggregated_value = accumulator + squared_deviation
    final_state = aggregated_value % 1024
    mask = 255

    # Key statement
    checksum = final_state ^ (aggregated_value & mask)

    # Dead code path (never executed, adds interference)
    if False:
        checksum *= 2
        checksum += phase_shift

    print(f"Result: {checksum}")

compute_diagnostic_sequence()