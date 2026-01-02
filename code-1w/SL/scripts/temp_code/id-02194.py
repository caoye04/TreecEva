import itertools

# Simulated sensor data processing with noise filtering and integrity validation
def process_sensor_readings(raw_stream):
    readings = [x & 0xFF for x in raw_stream if x > 0]
    filtered = [r for r in readings if r % 3 != 0]
    
    # Irrelevant transformation: amplitude normalization (dead path)
    normalized = [round(r / 255.0, 3) for r in readings]
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0.0

    # Distractor variables: frequency analysis (unused)
    frequency_map = {val: filtered.count(val) for val in set(filtered)}
    rare_values = [k for k, v in frequency_map.items() if v < 2]

    # Critical path begins: windowed XOR aggregation
    window_size = 4
    aggregated = []
    for i in range(0, len(filtered) - window_size + 1):
        window = filtered[i:i+window_size]
        xor_result = 0
        for w in window:
            xor_result ^= w
        aggregated.append(xor_result)

    # Padding to ensure minimum length
    while len(aggregated) < 8:
        aggregated.append(aggregated[-1] ^ 0x55 if aggregated else 0xAA)

    # Secondary transformation: pairwise difference (distractor)
    diff_pairs = [aggregated[i+1] - aggregated[i] for i in range(len(aggregated)-1)]
    abs_diff_sum = sum(abs(d) for d in diff_pairs)

    # Real processing: slicing and rotation
    segment_a = aggregated[:4]
    segment_b = aggregated[4:8]
    rotated_b = segment_b[1:] + [segment_b[0]]

    # Construct payload with interleaving
    interleaved = list(itertools.chain.from_iterable(zip(segment_a, rotated_b)))
    padded_payload = interleaved + [sum(interleaved) & 0xFF]

    # Mask generation (partially relevant)
    masks = [(i * 257 + 13) & 0xFF for i in range(10)]
    mask_sequence = masks[2:6]  # Used later

    # Red herring: checksum from diff_pairs (never used)
    legacy_checksum = abs_diff_sum % 256

    # Decoy function call (no side effects)
    def validate_integrity(data, key):
        return sum(data) ^ (key * 3) & 0xFFFF

    dummy_test = validate_integrity(diff_pairs, 7)

    # Final payload construction (critical)
    final_payload = [padded_payload[i] ^ mask_sequence[i % 4] for i in range(len(padded_payload))]
    final_payload.append(sum(final_payload) & 0xFF)

    # Key statement
    checksum = final_payload[-1] ^ mask_sequence[0]

    # Unrelated telemetry summary
    telemetry_report = {
        'raw_count': len(raw_stream),
        'filtered_retained': len(filtered),
        'aggregate_length': len(aggregated),
        'padding_added': 8 - len(readings) if 8 > len(readings) else 0,
        'dummy_checksum': legacy_checksum,
        'validation_token': dummy_test
    }

    # Output result
    print(f"Result: {checksum}")
    return checksum

# Input data
sensor_data = [123, -5, 255, 6, 9, 150, 21, 77, 81, 0, 93]
result = process_sensor_readings(sensor_data)