def compute_integrity_score(data_block):
    # Irrelevant preprocessing step (dead code path)
    temp_buffer = [d ^ 0xAAAA for d in data_block]
    backup_copy = data_block[::-1]

    # Misleading checksum using XOR folding (not used in final result)
    legacy_checksum = 0
    for x in data_block:
        legacy_checksum ^= (x << 1) | (x >> 7)

    # Real computation begins: extract critical indices
    primary_index = data_block[3] % 8
    secondary_index = data_block[7] % 5

    # Distractor: complex but unused transformation chain
    transformed = []
    for i, val in enumerate(data_block):
        if i % 2 == 0:
            transformed.append((val * 3 + 7) % 256)
        else:
            transformed.append(val ^ (i * 5))

    # Decoy integrity check with red herring variables
    verification_flag = False
    error_counter = 0
    for v in transformed:
        if v in [0xFF, 0x00, 0xDE, 0xAD]:
            error_counter += 1
    verification_flag = (error_counter == 0)

    # Actual logic: derive key components via conditional expressions
    base_seed = data_block[0] if data_block[1] > 50 else data_block[2]
    offset = data_block[primary_index] if primary_index < 6 else 16
    multiplier = data_block[secondary_index + 2] if secondary_index != 4 else 9

    # Intermediate values with mixed arithmetic and bitwise ops
    raw_entropy = (base_seed + offset) * multiplier
    normalized = (raw_entropy // 17) & 0xFF

    # Conditional expression determining aggregation mode
    aggregation_mode = 'sum' if normalized % 2 == 0 else 'xor'
    
    # Aggregation logic
    aggregated_value = 0
    if aggregation_mode == 'sum':
        for i in range(1, len(data_block), 2):
            aggregated_value += data_block[i] * (i % 10)
    else:
        for i in range(0, len(data_block), 3):
            aggregated_value ^= data_block[i] >> 2

    # Red herring: floating point distraction (unused)
    try:
        precision_estimate = sum(data_block) / len(data_block)
        adjustment_factor = precision_estimate * 0.98765
        smoothed = int(adjustment_factor) & 0xFFFF
    except:
        smoothed = 0

    # Final key generation with nested conditionals
    if normalized > 100:
        final_key = ((normalized << 2) ^ 0xBEEF) & 0xFFFF
    elif normalized > 50:
        final_key = ((normalized << 1) ^ 0xCAFE) & 0xFFFF
    else:
        final_key = (normalized ^ 0xFACE) & 0xFFFF

    # Critical execution point
    mask = 0xFF if aggregated_value % 3 == 0 else 0xF0
    checksum = final_key ^ (aggregated_value & mask)

    # More irrelevant state updates
    log_entry = f"CHK:{checksum:04X} MODE:{aggregation_mode}"
    audit_trail = [checksum, base_seed, normalized, legacy_checksum]

    return checksum

# Input data block (deterministic seed)
data_stream = [12, 88, 45, 192, 77, 34, 201, 63, 111, 29]

# Execute and print target result
current_checksum = compute_integrity_score(data_stream)
print(f"Result: {current_checksum}")