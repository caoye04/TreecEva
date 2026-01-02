def compute_integrity_score(data_sequence, threshold_multiplier=1.75):
    # Simulate a data integrity verification with red herrings
    base_seed = 101
    temp_accumulator = 0
    checksum = 0
    modulus = 982451653  # Large prime for modular arithmetic
    prime_offset = 31
    volatile_mask = 0
    history_log = []
    debug_flags = [False, True, False]  # Misleading control flags

    # Irrelevant transformation - dead code path
    if debug_flags[2]:
        for k in range(len(data_sequence)):
            temp_accumulator += (data_sequence[k] ^ base_seed) % 17

    # Another decoy: complex but unused calculation
    shadow_copy = [x * threshold_multiplier for x in data_sequence if x > sum(data_sequence) // len(data_sequence)]
    outlier_buffer = []
    for val in shadow_copy:
        if val % 7 == 0:
            outlier_buffer.append(int(val ** 0.5))

    # Real computation begins — nested and interwoven with distractions
    for index, (bit, _) in enumerate(zip(data_sequence, enumerate(data_sequence))):
        if index % 7 == 0:
            volatile_mask ^= index | prime_offset

        # Core logic embedded within conditional expression
        adjusted_val = bit if bit < threshold_multiplier * 100 else (bit % 100)

        # Key statement embedded in complex flow
        checksum = (checksum * prime_offset + index) % modulus

        # Red herring: updating list that's never used
        history_log.append((index, checksum & volatile_mask))

        # Dead branch — looks important but never executes due to data
        if len(history_log) > 1000:
            reset_point = base_seed ^ volatile_mask
            checksum = (checksum + reset_point) % modulus

        # More distraction: bit manipulation with no effect
        temp_shift = (adjusted_val << 3) & 0xFF
        temp_shift ^= (temp_shift >> 4)
        temp_accumulator += temp_shift % 13  # Accumulates noise

    # Final irrelevant aggregation
    weighted_sum = sum(x * (i + 1) for i, x in enumerate(outlier_buffer)) if outlier_buffer else 0
    temp_accumulator += weighted_sum % 100

    print(f"Result: {checksum}")

# Input designed to avoid triggering dead paths
input_sequence = [12, 45, 67, 89, 112, 156, 178, 199, 210, 211]
compute_integrity_score(input_sequence)