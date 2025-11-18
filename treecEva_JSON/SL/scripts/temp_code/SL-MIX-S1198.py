from collections import defaultdict

def generate_modular_sequence(base, modulus, length):
    sequence = []
    current = base
    for _ in range(length):
        sequence.append(current)
        current = (current * base) % modulus
    return sequence

# Initialize cryptographic parameters
prime_modulus = 97
generator_base = 5
block_size = 8

# Generate modular sequences for verification
sequence_a = generate_modular_sequence(generator_base, prime_modulus, block_size)
sequence_b = generate_modular_sequence(generator_base**2, prime_modulus, block_size//2)

# Create verification maps using dictionary comprehension
verification_map = {i: (sequence_a[i] + sequence_b[i % len(sequence_b)]) % prime_modulus 
                   for i in range(block_size)}

# Apply logical filtering for valid blocks
valid_blocks = {k: v for k, v in verification_map.items() 
                if (v % 2 == 0) and (v > 20) or (k < 4 and v < 50)}

# Compute verification key using divide and conquer approach
def compute_verification_key(data_dict):
    keys = list(data_dict.keys())
    if len(keys) == 0:
        return 0
    if len(keys) == 1:
        return data_dict[keys[0]]
    mid = len(keys) // 2
    left_dict = {k: data_dict[k] for k in keys[:mid]}
    right_dict = {k: data_dict[k] for k in keys[mid:]}
    left_result = compute_verification_key(left_dict)
    right_result = compute_verification_key(right_dict)
    return (left_result ^ right_result) % prime_modulus

# Final computation
verification_key = compute_verification_key(valid_blocks)
print(f"Result: {verification_key}")