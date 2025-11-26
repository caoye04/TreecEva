import itertools

def process_crypto_payload(data_stream, bit_mask):
    # Initialize tracking variables (some irrelevant)
    temp_sum = 0
    checksum = 0
    parity_check = 1
    
    # Process data with bitwise operations
    masked_data = [(byte ^ bit_mask) for byte in data_stream]
    
    # Irrelevant computation path
    for i in range(len(masked_data) // 2):
        temp_sum += masked_data[i] * 2  # Dead code path - result unused
    
    # Key logic: XOR reduction with conditional filtering
    filtered_data = [x for x in masked_data if x % 3 != 0]
    
    # Misleading intermediate calculation
    intermediate = sum(masked_data) // len(masked_data) if masked_data else 0
    
    # Actual computation: XOR chain with itertools cycle
    xor_chain = 0
    mask_cycle = itertools.cycle([1, 3, 7, 15])
    for value in filtered_data:
        xor_chain ^= (value & next(mask_cycle))
    
    # Final adjustment with tuple unpacking
    adjustments = (5, 3, 8, 2)
    a, b, c, d = adjustments
    final_xor = xor_chain ^ ((a + c) - (b - d))
    
    # Return actual result (ignoring misleading variables)
    return final_xor

# Main execution with distractions
encrypted_data = [45, 78, 123, 67, 89, 234, 56, 189]
mask_pattern = 0x7F

# Distractor variables
backup_copy = encrypted_data[:]
validation_flag = sum(encrypted_data) > 500
shadow_result = process_crypto_payload(backup_copy, 0x3F)  # Different mask

# Actual computation
final_result = process_crypto_payload(encrypted_data, mask_pattern)

# Print only the relevant result
print(f"Target result: {final_result}")