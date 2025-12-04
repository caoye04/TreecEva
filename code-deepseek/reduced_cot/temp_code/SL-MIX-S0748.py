def compute_checksum(data_stream, mask_pattern):
    # Distractor: unused variable
    temp_buffer = [i * 2 for i in range(10)]
    
    # Main computation
    checksum = 0
    data_bytes = [ord(c) if isinstance(c, str) else c for c in data_stream]
    
    # Misleading intermediate calculation
    xor_temp = mask_pattern ^ 0xFF
    shifted_xor = (xor_temp << 2) | (xor_temp >> 6)
    
    # Dead code path that looks relevant
    if len(data_bytes) > 100:
        checksum = sum(data_bytes) & 0xFFFF
        return checksum
    
    # Actual checksum calculation
    for i, byte_val in enumerate(data_bytes):
        if i % 2 == 0:
            checksum ^= (byte_val & mask_pattern)
        else:
            checksum ^= (byte_val | mask_pattern)
        
        # Red herring: unused operation
        rotated_byte = ((byte_val << 3) | (byte_val >> 5)) & 0xFF
    
    # Final adjustment with string method integration
    checksum_str = str(checksum)
    checksum = int(checksum_str.zfill(4)[-3:]) | (mask_pattern & 0x0F)
    
    return checksum

# Main execution
mask_pattern = 0x3A
data_stream = "K8P2Q9R"

# Irrelevant calculations that don't affect result
unused_calc = (mask_pattern * 7) // 3
padding_check = len(data_stream) * 2 + 5

final_result = compute_checksum(data_stream, mask_pattern)
print(f"Result: {final_result}")