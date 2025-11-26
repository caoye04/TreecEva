def decode_sequence(seq):
    # Generate intermediate values (distraction)
    temp_sum = sum(seq) * 2
    temp_product = 1
    for val in seq:
        temp_product *= (val + 1)
    
    # Apply XOR operations with bitwise manipulation
    xor_result = seq[0]
    for i in range(1, len(seq)):
        xor_result ^= seq[i]
    
    # Set operations for pattern analysis (distraction)
    unique_values = set(seq)
    sorted_unique = sorted(unique_values)
    mid_value = sorted_unique[len(sorted_unique) // 2] if sorted_unique else 0
    
    # Slice operations and final computation
    pattern_slice = seq[1:4]
    slice_sum = sum(pattern_slice)
    
    # Main computation chain
    base_key = xor_result + slice_sum
    offset = len(seq) * 3
    
    # Final key generation (critical variable)
    cipher_key = (base_key - offset) % 256
    
    # Distraction: unused intermediate calculation
    unused_value = temp_sum - temp_product
    
    return cipher_key

# Input sequence
encoded_pattern = [45, 67, 89, 12, 34, 56, 78]
final_result = decode_sequence(encoded_pattern)
print(f"Result: {final_result}")