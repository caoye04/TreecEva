def analyze_access_codes(codes):
    # Convert hex codes to integers
    numeric_codes = [int(code, 16) for code in codes]
    
    # Create sets for odd and even positioned bits
    odd_bits = {i for i in range(0, 32, 2)}
    even_bits = {i for i in range(1, 32, 2)}
    
    # Compute initial mask using XOR of all codes
    initial_mask = 0
    for code in numeric_codes:
        initial_mask ^= code
    
    # Apply bit filtering using set operations
    filtered_mask = 0
    for i in range(32):
        if i in odd_bits and (initial_mask & (1 << i)):
            filtered_mask |= (1 << i)
    
    # Create a hash-based adjustment factor
    hash_factor = hash(str(numeric_codes)) & 0xFFFFFFFF
    
    # Final verification mask combines filtered mask with hash factor
    verification_mask = (filtered_mask & hash_factor) | (filtered_mask >> 2)
    
    return verification_mask

codes_list = ['0x1A3F', '0x7B2C', '0x4E8D', '0xF156']
verification_mask = analyze_access_codes(codes_list)
print(f"Result: {verification_mask}")