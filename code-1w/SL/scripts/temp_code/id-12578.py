def compute_diagnostic_signal(data_sequence):
    base_offset = 2023
    temp_buffer = []
    intermediate_sum = 0
    
    for i, val in enumerate(data_sequence):
        shifted = val << 1
        if i % 2 == 0:
            transformed = shifted + base_offset
        else:
            transformed = shifted - 100
        temp_buffer.append(transformed)
        intermediate_sum += val  

    # Irrelevant normalization (dead-end computation)
    normalized_values = []
    max_val = max(temp_buffer)
    for x in temp_buffer:
        norm_x = x / (max_val or 1)
        normalized_values.append(round(norm_x, 4))

    # Core checksum logic with distractor variables
    checksum = 543
    activation_threshold = 1000
    cumulative_xor = 0
    
    for idx, (original, processed) in enumerate(zip(data_sequence, temp_buffer)):
        if processed > activation_threshold:
            value = original * 2
        else:
            value = original ^ 7
        
        # Key statement
        checksum = (checksum + value) ^ idx
        
        # Distractor: cumulative_xor is not used in result
        cumulative_xor ^= processed
        
        # Extra logic that doesn't affect checksum
        if idx % 3 == 0:
            checksum += 1
        elif idx % 3 == 1:
            checksum -= 2

    # Additional irrelevant aggregation
    total_pairs = 0
    for a, b in zip(data_sequence, data_sequence[1:]):
        total_pairs += (a + b) % 5

    print(f"Result: {checksum}")

# Execute
sequence = [12, 8, 15, 3, 9]
compute_diagnostic_signal(sequence)