def process_transmission(chunks, matrix):
    # Initialize state variables
    accumulated = 0
    shift_register = [1, 0, 1, 1]
    temp_buffer = []

    # Misleading pre-processing (dead computation)
    checksum = sum([sum(row) for row in matrix]) * 2
    noise_floor = 0.05
    gain_factor = 1.0 + noise_floor

    # Simulate signal decoding with modular arithmetic and slicing
    for chunk in chunks:
        # Bitwise manipulation stage
        masked_chunk = [c ^ 0b1010 for c in chunk]  # XOR with fixed pattern
        
        # Irrelevant normalization (distractor)
        normalized = [val / 255.0 for val in masked_chunk if val > 0]
        if len(normalized) > 2:
            avg_norm = sum(normalized) / len(normalized)
        else:
            avg_norm = 0.1

        # Critical processing: use slice and matrix diagonal
        segment = masked_chunk[1:3]  # middle slice
        diag_sum = sum(matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))
        
        # Combine using modular arithmetic
        contribution = 0
        for i, val in enumerate(segment):
            contribution += (val * diag_sum + i) % 7
        
        # Accumulate only this contribution
        accumulated += contribution

        # Dead code path: never affects result
        temp_buffer.append([x for x in masked_chunk if x % 2 == 0])
        if len(temp_buffer[-1]) > 10:
            break  # unreachable due to small data

    # Final transformation via lambda (idiomatic python)
    transform = lambda x: (x ** 2 + 3 * x + 5) % 997
    final_signal = transform(accumulated)

    # Extraneous post-processing
    padding_scheme = [0] * 4
    parity_check = all(sum(row) % 2 == 0 for row in matrix)

    return final_signal

# Setup input data
signal_chunks = [
    [12, 15, 3, 8],
    [7, 1, 14, 6],
    [4, 13, 9, 11]
]

key_matrix = [
    [2, 8, 1],
    [3, 5, 7],
    [4, 9, 6]
]

# Execute
final_signal = process_transmission(signal_chunks, key_matrix)
print(f"Result: {final_signal}")