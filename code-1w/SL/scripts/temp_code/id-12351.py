def compute_hamming_distance(sequence_a, sequence_b):
    total_hamming = 0
    temp_offset = 7  # irrelevant offset, not used in logic
    for i, (a, b) in enumerate(zip(sequence_a, sequence_b)):
        xor_result = a ^ b
        total_hamming += xor_result.bit_count()
    return total_hamming

# Input sequences
seq_a = [21, 14, 9]
seq_b = [26, 15, 10]

# Compute cumulative Hamming distance across pairs
total_hamming = compute_hamming_distance(seq_a, seq_b)
print(f"Result: {total_hamming}")