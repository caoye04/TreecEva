def compute_diagnostic_score(data):
    # Irrelevant transformation (dead path)
    temp_buffer = [x * 2 for x in data if x % 3 == 0]
    temp_buffer = [t ^ 5 for t in temp_buffer]

    # Real processing begins: filtering and shifting
    filtered = [x for x in data if x > 10 and x < 100]
    shifted = [(val << 2) & 255 for val in filtered]

    # Decoy accumulation (not used in final result)
    decoy_sum = 0
    for item in temp_buffer:
        decoy_sum += item * 3
        if decoy_sum > 1000:
            decoy_sum -= 500

    # Actual signal path: slicing and bitwise mixing
    frame_a = shifted[::2]  # Every other element
    frame_b = shifted[1::2]

    # Misleading intermediate hash (never finalized)
    fake_hash = 0
    for x in shifted + [len(temp_buffer)]:
        fake_hash = (fake_hash ^ x) * 7 % 97

    # Real digest computation
    rolling_xor = 0
    for i, val in enumerate(frame_a):
        if i % 2 == 0:
            rolling_xor ^= (val + len(frame_b)) & 255
        else:
            rolling_xor ^= (val >> 1) & 255

    # Secondary pattern on frame_b
    inverted = [255 - b for b in frame_b]
    sum_inv = sum(inverted) % 256

    # Combine into base digest
    base_digest = [rolling_xor, sum_inv, len(frame_a), len(frame_b)]

    # Apply non-linear transform via slicing logic
    extended = base_digest * 2
    windowed = extended[2:6]  # Extract middle section

    # Red herring: floating point conversion (unused)
    float_trace = [w / 4.7 for w in windowed]
    avg_float = sum(float_trace) / len(float_trace)

    # Final digest calculation
    final_digest = []
    for j in range(4):
        mixed = windowed[j] ^ windowed[(j+2)%4]
        mixed = (mixed + j*j) % 256
        final_digest.append(mixed)

    # Correction factor based on original data parity
    parity_count = sum(1 for x in data if x % 2 == 1)
    correction_factor = (parity_count * 3) % 256

    # Key statement
    checksum = final_digest[-1] ^ correction_factor

    # Unrelated logging output (distractor)
    log_entry = f"Processed {len(filtered)} records with {decoy_sum} buffer trace."

    # Output target result
    print(f"Result: {checksum}")

    return checksum

# Input data
sensor_readings = [12, 15, 9, 22, 64, 33, 8, 105, 48, 77, 2, 91]

result = compute_diagnostic_score(sensor_readings)