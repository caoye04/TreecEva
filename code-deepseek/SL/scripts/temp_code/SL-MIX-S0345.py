def generate_mask(pattern_val):
    mask_data = [pattern_val << i for i in range(4)]
    unused_mask = [x ^ 0xFF for x in mask_data]
    return mask_data[2] & 0x7F

def process_crypto_key(key_bytes, mask_gen):
    key_hash = sum(key_bytes) % 256
    temp_val = (key_hash ^ mask_gen) & 0x3F
    
    # Distractor operations
    fake_checksum = sum([b << 2 for b in key_bytes]) % 1000
    redundant_xor = temp_val ^ fake_checksum
    dead_branch = redundant_xor if fake_checksum > 500 else redundant_xor + 1
    
    shifted_val = (temp_val << 2) | (temp_val >> 4)
    filtered_bytes = [b for b in key_bytes if (b & 0x1) == 0]
    byte_sum = sum(filtered_bytes) if filtered_bytes else 42
    
    result = (shifted_val + byte_sum) % 128
    return result

# Main execution with distractions
key_data = [0x1F, 0x8C, 0x47, 0x92, 0xE3]
mask_pattern = 0x17

# Irrelevant computations
aux_data = [x * 3 for x in range(10)]
aux_sum = sum(aux_data[::2])
shadow_var = aux_sum ^ mask_pattern

# Critical execution point
result = process_crypto_key(key_data, mask_pattern)

# More distractions
final_output = result + (shadow_var % 16)
print(f"Target result: {final_output}")