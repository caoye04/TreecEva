def compute_integrity_check():
    # Simulated system telemetry data (irrelevant block)
    temperature_readings = [23.4, 24.1, 22.9, 25.0, 26.3, 23.8]
    avg_temp = sum(temperature_readings) / len(temperature_readings)
    temp_alert = True if avg_temp > 25 else False
    calibration_offset = 0.05 * avg_temp if temp_alert else 0.0

    # Historical logs processing (dead path - never accessed)
    log_archive = {'entries': 1289, 'corrupted': 7, 'recovered': 4}
    if log_archive['corrupted'] > 5:
        recovery_rate = log_archive['recovered'] / log_archive['corrupted']
        log_archive['status'] = 'partial'
    else:
        log_archive['status'] = 'stable'

    # Core data payload (relevant)
    payload_data = [17, 89, 23, 44, 56, 13, 72, 31]
    mask_sequence = [0b1010, 0b0101, 0b1100, 0b0011] * 2  # Repeating XOR mask

    # Data transformation chain
    masked_values = []
    for i, val in enumerate(payload_data):
        masked_val = val ^ mask_sequence[i]  # Bitwise XOR masking
        adjusted = (masked_val + 17) % 101  # Modular arithmetic adjustment
        masked_values.append(adjusted)

    # Secondary obfuscation layer (distractor)
    obfuscation_table = {i: (i * 3 + 7) % 100 for i in range(10)}
    scrambled = [obfuscation_table[v % 10] for v in masked_values]
    checksum_candidate = sum(scrambled) % 10000

    # Red herring: security flag computation (unrelated)
    entropy_score = len(set(masked_values)) / len(masked_values)
    security_flag = 'HIGH' if entropy_score > 0.7 else 'LOW'
    debug_trace = [f"Step{i}: {v}" for i, v in enumerate(masked_values[:3])]

    # Critical variables for actual result
    data_sum = sum(masked_values)  # Used in final checksum
    metadata_key = 0x1A3F  # Hex key used in integrity check

    # Conditional override simulation (never triggers - misleading)
    override_enabled = False
    override_code = 42 if override_enabled else None
    if override_code == 42:
        data_sum = 500

    # Final integrity checksum (TARGET STATEMENT)
    checksum = (data_sum ^ metadata_key) % 8917

    # Post-check diagnostics (irrelevant)
    diagnostic_log = {
        'version': '2.1.7',
        'verified': checksum % 2 == 1,
        'timestamp': 1718943201,
        'checksum_base': data_sum,
        'key_used': hex(metadata_key)
    }

    # Output target result
    print(f"Result: {checksum}")

compute_integrity_check()