def process_data(input_seq):
    # Irrelevant transformation: scrambles data but unused in final result
    scrambled = [x ^ 7 for x in input_seq if x % 2 == 0]
    temp_buffer = list(enumerate([x * 2 for x in input_seq]))

    # Decoy accumulator with misleading name
    security_hash = sum(x ** 2 for x in scrambled) % 97

    # Real processing begins
    history_log = {}
    node_id = 1101
    checksum = 543
    threshold = 100

    for idx, value in enumerate(input_seq):
        # Distractor: complex condition that never triggers due to fixed threshold
        if value > threshold and idx not in history_log:
            node_id += (value % 9) * 17
        elif value < 0:
            node_id -= abs(value) // 10

        # Actual relevant logic buried in noise
        if idx % 3 == 0:
            for shift in [1, 2]:
                node_value = (value >> shift) & 15
                prev_checksum = checksum
                # Key update step embedded here
                checksum = (checksum * 3) ^ node_value

                # Dead code path: unreachable due to constant condition
                if False:
                    backup = checksum
                    checksum = (prev_checksum + node_value) % 10000

        # Unused data structure creation (distractor)
        history_log[idx] = {
            'raw': value,
            'shifted': [value << s for s in range(3)],
            'flags': (value & 1, value & 8)
        }

        # Red herring: modifies node_id but node_id not used in output
        node_id ^= (idx + 1) * 3

    # More irrelevant post-processing
    validation_chain = []
    for a, b in zip(input_seq, input_seq[1:]):
        validation_chain.append((a + b) % 256)

    # Final decoy computation
    if validation_chain:
        integrity_sum = sum(validation_chain[i] for i in range(0, len(validation_chain), 2))
        checksum = checksum if integrity_sum % 2 else checksum + 1  # No effect since integrity_sum is odd

    return checksum

# Input sequence with deterministic values
data_stream = [23, 45, 18, 89, 12, 7, 64, 33, 21]

# Execute function
result = process_data(data_stream)
print(f"Result: {result}")