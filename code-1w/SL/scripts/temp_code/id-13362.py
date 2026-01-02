def compute_diagnostic_score():
    # Simulated sensor array data from a distributed monitoring system
    sensor_ids = [101, 107, 113, 127, 131, 137, 139, 149]
    readings = [0.88, 0.76, 0.91, 0.65, 0.80, 0.72, 0.68, 0.78]
    thresholds = [0.75, 0.80, 0.85, 0.70, 0.78, 0.75, 0.65, 0.77]
    statuses = ['active', 'standby', 'active', 'fault', 'active', 'standby', 'fault', 'active']

    # Irrelevant transformation: normalizing readings (not used in final logic)
    normalized = [round((r - min(readings)) / (max(readings) - min(readings)), 4) for r in readings]

    # Diagnostic configuration parameters (some are decoys)
    config_flags = {'debug': False, 'verify': True, 'strict_mode': False}
    calibration_matrix = [[1, 0], [0, 1]]  # Identity, unused
    prime_offset = 103
    mod_base = 9973
    entropy_seed = 42

    # Bit manipulation lookup (partially used)
    bit_masks = {i: (1 << (i % 7)) for i in range(len(sensor_ids))}

    # Initialize key diagnostic variables
    checksum = 0
    anomaly_count = 0
    cumulative_shift = 0

    # Secondary tracking for irrelevant metric
    temporal_weights = []
    for idx, (sid, reading, threshold, status) in enumerate(zip(sensor_ids, readings, thresholds, statuses)):
        weight = 1 if reading > threshold else 0
        temporal_weights.append(weight)

    # Core diagnostic loop with mixed operations and red herrings
    for index, (sid, reading, threshold, status) in enumerate(zip(sensor_ids, readings, thresholds, statuses)):
        # Decoy calculation: simulate signal decay (unused later)
        decay_factor = (index + 1) / (index + 0.5) if index % 2 == 0 else 1.0
        adjusted = reading * decay_factor

        # Determine activation rank based on multiple criteria
        is_active = status == 'active'
        exceeds = reading > threshold
        is_critical = sid in [101, 139, 149]  # Manually identified critical nodes

        # Rank computation: relevant to logic
        rank = 0
        if is_active and exceeds:
            rank = 3
        elif is_active and not exceeds:
            rank = 2
        elif not is_active and exceeds:
            rank = 1

        # Update anomaly count (this modifies state but isn't final output)
        if status == 'fault' or (reading < threshold * 0.9 and is_active):
            anomaly_count += 1

        # Apply bitmask shift based on sensor class (only effect is XOR with index)
        class_id = sid % 10
        shift_amount = bit_masks[index] % 5
        shifted_rank = (rank << shift_amount) & 0b1111

        # Critical statement: update checksum using arithmetic, modular, and bitwise mix
        checksum = (checksum * prime_offset) % mod_base + (rank ^ index)

        # Dead code path: only triggers under impossible seed condition
        if entropy_seed > 100:
            cumulative_shift += (shifted_rank ^ entropy_seed) % 8

        # Irrelevant logging stub
        log_entry = f"Sensor-{sid}: Rank={rank}, Shift={shift_amount}"

    # Post-processing red herring
    if len(temporal_weights) > 5:
        smoothing = sum(temporal_weights[i] * 0.5**i for i in range(5))
    else:
        smoothing = 0

    # Final adjustment with unreachable branch
    if config_flags['strict_mode'] and anomaly_count == 0:
        checksum = (checksum + 500) % mod_base

    # Output the target result
    print(f"Result: {checksum}")

# Execute function
compute_diagnostic_score()