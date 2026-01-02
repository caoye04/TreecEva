def compute_integrity_fields():
    # Simulated telemetry packet processing with red herrings
    raw_payload = [23, 17, 8, 42, 15, 91, 73]
    config_flags = {'mode': 3, 'debug': False, 'version': 2}
    temp_buffer = []

    # Irrelevant transformation 1: unused normalization
    normalized = [round(x / sum(raw_payload) * 100, 2) for x in raw_payload]
    avg_normalized = sum(normalized) / len(normalized)

    # Relevant data path begins
    data_sum = sum(x for x in raw_payload if x % 2 == 1)  # Sum odd values only

    # Misleading intermediate: looks important but unused
    parity_chain = 0
    for x in raw_payload:
        parity_chain ^= x << 1
        parity_chain &= 0xFFFFFFFF

    # Simulated metadata extraction
    header_value = config_flags['mode'] * 1000 + config_flags['version'] * 10
    metadata_key = (header_value ^ 0xAAAA) & 0xFFFF

    # Dead code path: never executed but looks plausible
    if config_flags['debug']:
        audit_log = []
        for i, v in enumerate(raw_payload):
            audit_log.append(f"{i}:{v}")

    # Conditional expression (required Python feature)
    scaling_factor = 1.5 if config_flags['version'] > 1 else 1.0
    scaled_sum = data_sum * scaling_factor

    # Buffer overflow simulation - irrelevant
    for _ in range(3):
        temp_buffer.extend([0] * 8)
        temp_buffer = temp_buffer[:32]

    # Critical computation: checksum using bitwise operations
    checksum = (data_sum ^ metadata_key) & 0xFFFF

    # Distraction: another checksum-like variable (decoy)
    secondary_checksum = (sum(raw_payload) ^ 0x5555) & 0xFFFF

    # Unused recursive function (red herring)
    def traverse_tree(depth):
        return 1 if depth <= 0 else traverse_tree(depth - 1) + depth
    
    # Final output
    print(f"Result: {checksum}")

compute_integrity_fields()