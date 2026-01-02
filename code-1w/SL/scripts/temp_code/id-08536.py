def analyze_sensor_data(raw_readings):
    filtered_data = [x for x in raw_readings if x > 0]
    baseline = sum(filtered_data) // len(filtered_data) if filtered_data else 0

    # Irrelevant transformation: frequency analysis (dead path)
    frequency_map = {}
    for val in raw_readings:
        frequency_map[val] = frequency_map.get(val, 0) + 1
    max_frequency = max(frequency_map.values(), default=0)

    # Distractor: unused statistical calculations
    squared_devs = [(x - baseline) ** 2 for x in filtered_data]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    std_deviation = variance ** 0.5

    # Character counting in hex representation (red herring)
    hex_strings = [hex(x)[2:] for x in filtered_data]
    char_count = sum(len(s) for s in hex_strings)
    vowel_count = sum(s.count('a') + s.count('e') + s.count('f') for s in hex_strings)  # 'a','e','f' as hex letters

    # Bit manipulation decoy
    xor_fingerprint = 0
    for x in filtered_data:
        xor_fingerprint ^= (x << 1) | (x >> 3)
    masked_fingerprint = xor_fingerprint & 0xFFFF

    # Actual signal processing chain (nested logic)
    adjusted_values = []
    for val in filtered_data:
        if val % 2 == 0:
            processed = val // 2
            if processed % 3 == 0:
                processed = (processed ^ 5) + 2
            else:
                processed = processed * 3
        else:
            processed = val * 2
            if processed > 50:
                processed -= 17
        adjusted_values.append(processed)

    # Secondary filtering based on transformed values
    valid_adjustments = [v for v in adjusted_values if v < 100]

    # Complex aggregation with distractor-weighted sum
    weight_sequence = [i % 4 + 1 for i in range(len(valid_adjustments))]
    weighted_sum = sum(a * w for a, w in zip(valid_adjustments, weight_sequence))

    # Real computation path begins here
    aggregate_score = sum(valid_adjustments)  # Core diagnostic base

    # Conditional correction using string-based key
    status_key = "diagnostics_active"
    activation_flag = sum(1 for c in status_key if c in 'aeiou') % 4  # counts vowels

    if activation_flag > 2:
        correction_factor = len(valid_adjustments)
    elif activation_flag == 2:
        correction_factor = -len(valid_adjustments)
    else:
        correction_factor = baseline // 10

    # Key statement
    final_diagnostic = aggregate_score + correction_factor

    # Dead-end logging
    log_entry = f"FINAL:{hex(final_diagnostic)}"
    is_valid_log = any(c.isupper() for c in log_entry)

    return final_diagnostic

# Input data
sensor_input = [12, -5, 24, 0, 18, 33, -1, 42]

# Execution
result = analyze_sensor_data(sensor_input)
print(f"Result: {result}")