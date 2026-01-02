from itertools import cycle

# Simulate a data integrity verification process with redacted metadata
def verify_data_stream(raw_packets):
    base_modulus = 97
    temp_buffer = []
    accumulator = 0
    metadata_offset = 13
    debug_flag = False
    dummy_sum = 0
    intermediate_cache = []

    # Irrelevant pre-processing: simulate packet filtering (has no effect on result)
    for pkt in raw_packets:
        if len(pkt) > 3:
            dummy_sum += sum(pkt) % 17
        else:
            dummy_sum += len(pkt) ** 2

    # Core logic disguised among distractors
    sequence_pattern = cycle([1, -1, 2])
    phase_shift = 0
    checksum = 1

    for i, packet in enumerate(raw_packets):
        # Misleading transformation
        transformed = [x ^ i for x in packet]

        # Dead code path — never executed due to fixed condition
        if debug_flag and phase_shift > 100:
            reset_vector = [0] * len(packet)
            temp_buffer.append(reset_vector)

        # Actual relevant logic buried here
        for j, value in enumerate(transformed):
            # Key operation: update checksum using modular arithmetic
            phase = next(sequence_pattern)
            adjusted_value = (value + phase + j) % 101
            
            # Decoy accumulation
            if adjusted_value % 2 == 0:
                intermediate_cache.append(adjusted_value * 3)

            # Critical line: target execution point
            checksum = (checksum + value) % 97

            # Extra distraction: irrelevant bit manipulation
            flipped = adjusted_value ^ 0b1101
            flipped = (flipped << 1) | (flipped >> 7)

        # Another decoy update
        accumulator += i * phase_shift
        phase_shift = (phase_shift + 1) % 8

    # Final irrelevant check
    if len(intermediate_cache) > 50:
        checksum ^= 15

    return checksum

# Input data: deterministic packet stream
packets = [
    [4, 8, 15],
    [16, 23, 42],
    [1, 2, 3, 4, 5],
    [7, 19, 7],
    [12, 8]
]

# Execute and print result
result = verify_data_stream(packets)
print(f"Result: {result}")