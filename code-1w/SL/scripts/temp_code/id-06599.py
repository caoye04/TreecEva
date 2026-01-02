def analyze_signal_pattern(raw_readings, threshold=0.75):
    # Irrelevant preprocessing: normalize and filter noise (distractor logic)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in normalized if x > threshold]

    # Misleading statistical summary (dead path)
    avg_filtered = sum(filtered) / len(filtered) if filtered else 0.0
    peak_magnitude = max(normalized) ** 2

    # Core diagnostic chain begins here
    binary_flags = []
    for i, val in enumerate(raw_readings):
        toggle = (i % 3 == 0) and (val > 5)
        parity_bit = (val ^ i) & 1
        binary_flags.append(1 if toggle or parity_bit else 0)

    # Complex transformation using zip and enumerate (required idiom)
    paired_metrics = []
    for idx, (a, b) in enumerate(zip(binary_flags, binary_flags[1:])):
        metric = (a + b) * (idx + 1)
        if idx % 2 == 0:
            metric = metric ** 0.5 if metric > 0 else 0
        paired_metrics.append(metric)

    # Red herring: frequency analysis with unused result
    freq_map = {}
    for bit in binary_flags:
        freq_map[bit] = freq_map.get(bit, 0) + 1
    dominant_state = max(freq_map, key=freq_map.get)

    # Decoy checksum calculation (never used)
    checksum = 0
    for i in range(len(raw_readings)):
        if i in [2, 5, 8]:
            checksum ^= raw_readings[i]
    checksum = (checksum * 17) % 256

    # Actual signal path: cycle detection and aggregation
    cycle_count = 0
    for j in range(2, len(paired_metrics)):
        if paired_metrics[j] > paired_metrics[j-1] and binary_flags[j] != binary_flags[j-2]:
            cycle_count += 1

    base_energy = sum(raw_readings[:4])
    aggregate_score = base_energy // (len(paired_metrics) or 1)

    # Obfuscated correction via bitwise and modular arithmetic
    temp_shift = (cycle_count << 2) ^ 7
    correction_factor = abs(temp_shift - (temp_shift % 5))

    # Key assignment - this is where the answer is determined
    final_diagnostic = aggregate_score + correction_factor * (cycle_count % 4)

    # Output required format
    print(f"Result: {final_diagnostic}")

    # Unused trailing logic to increase interference
    if final_diagnostic < 0:
        backup_mode = True
        recovery_state = [x for x in reversed(raw_readings) if x % 2 == 1]
    else:
        audit_log = [(i, raw_readings[i]) for i in range(0, len(raw_readings), 3)]

    return final_diagnostic

# Input data with meaningful domain context (sensor array readings)
data_stream = [3, 8, 6, 12, 4, 7, 9, 11, 2]
analyze_signal_pattern(data_stream)