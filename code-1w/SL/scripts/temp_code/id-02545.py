def analyze_data_stream(raw_sequence, threshold=1024):
    # Simulate sensor data calibration with red herrings
    calibrations = [i ** 2 % 256 for i in range(15)]
    temp_buffer = [x | 0x55 for x in calibrations if x < 128]
    snapshot_log = {idx: val * 3 for idx, val in enumerate(temp_buffer[:10])}

    # Irrelevant signal smoothing (dead-end computation)
    smoothed = []
    for i in range(1, len(temp_buffer) - 1):
        avg_val = (temp_buffer[i-1] + temp_buffer[i] + temp_buffer[i+1]) // 3
        smoothed.append(avg_val)

    # Core checksum processor (actual relevant logic)
    checksum = 0xACE1
    activation_flags = [False, True, True, False]
    lookup_shift = {k: (k * 2 + 1) % 7 for k in range(8)}

    # Decoy transformation on raw data (never used)
    transformed = ''.join([chr((ord(c) + 5) % 90 + 32) for c in 'encrypted_data_placeholder'])

    # Real processing begins here
    filtered_values = [x for x in raw_sequence if x > 0 and x.bit_length() <= 10]

    metadata_index = []
    for index, value in enumerate(filtered_values):
        if index % 3 == 0:
            metadata_index.append(index * 2)

        # Distractor: complex but unused bit manipulation
        decoy_op = (value ^ 0xBEEF) >> 2
        decoy_op = (decoy_op * 3) & 0xFF

        # Conditional branching with misleading flag usage
        is_active = activation_flags[index % len(activation_flags)]
        shift_param = lookup_shift.get(value % 8, 5)

        if value > threshold:
            checksum += value % 100
        else:
            processed_value = (value ^ (value << 1)) & 0xFF
            processed_value = processed_value ^ (processed_value >> 2)
            
            # Key statement — this updates the actual answer
            checksum = (checksum << 1) ^ processed_value & 0xFFFF

            # Additional irrelevant post-processing
            if processed_value in snapshot_log:
                snapshot_log[processed_value] -= 1

    # Dead code path: never executed due to filter above
    overflow_dump = []
    for x in raw_sequence:
        if x > threshold * 2:
            overflow_dump.append(x.to_bytes(2, 'little'))

    # Final irrelevant string analysis using zip and enumerate (required features)
    tag_sequence = ['A', 'B', 'C', 'D']
    for i, (tag, val) in enumerate(zip(tag_sequence, calibrations[::3])):
        if val % 2 == 0:
            checksum ^= ord(tag) * i  # Minor influence, but not critical

    return checksum

# Input data with deterministic values
input_stream = [12, 257, 3, 1025, 98, 0, 7, 513, 14, 2049, 22]

# Execute function
result = analyze_data_stream(input_stream)
print(f"Result: {result}")