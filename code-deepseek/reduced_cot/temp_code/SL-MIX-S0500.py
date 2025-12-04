def compute_final_key(initial_key, bit_mask):
    # Distractor: unused variable
    temp_shift = 3
    
    # Relevant computation: XOR with mask
    key_xor = initial_key ^ bit_mask
    
    # Distractor: misleading intermediate calculation
    fake_rotation = (key_xor << 2) & 0xFF
    
    # Relevant: bit rotation function
    def rotate_bits(value, shift):
        # Distractor: unused parameter manipulation
        shift = shift % 8 + 1
        return ((value << shift) | (value >> (8 - shift))) & 0xFF
    
    # Main computation path
    rotated = rotate_bits(key_xor, 1)
    
    # Distractor: dead code path
    if rotated > 200:
        backup_calc = (rotated * 2) - 50
    else:
        backup_calc = rotated + 100
    
    # Relevant: final adjustment
    final_key = (rotated | 0x0F) & 0x7F
    
    # Distractor: unused result from list comprehension
    checksum_values = [x for x in range(final_key, final_key + 5)]
    
    return final_key

# Initialization
cipher_key = 0b01101001  # 105 in decimal
mask_bits = 0b00110100   # 52 in decimal

# Distractor: irrelevant computation
offset_calc = (cipher_key >> 2) + mask_bits

# Critical execution point
final_key = compute_final_key(cipher_key, mask_bits)

# Distractor: misleading variable assignment
cipher_key = (final_key * 3) % 256

print(f"Result: {cipher_key}")