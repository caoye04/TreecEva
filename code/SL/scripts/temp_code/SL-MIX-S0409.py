def compute_data_integrity(data_stream):
    # Initialize tracking variables
    primary_sum = 0
    secondary_mask = 0xFF
    checksum_accumulator = 0
    temp_buffer = []
    validation_flag = True
    
    # Process data stream with bitwise operations
    for i, byte_val in enumerate(data_stream):
        # Main computation path
        primary_sum += byte_val
        if i % 2 == 0:
            checksum_accumulator ^= byte_val
        else:
            checksum_accumulator |= (byte_val & 0x0F)
        
        # Distractor operations - never used in final result
        temp_buffer.append(byte_val * 2)
        secondary_mask = (secondary_mask << 1) & 0xFF
    
    # Additional processing with misleading variables
    offset_adjust = len(data_stream) * 3
    parity_check = sum(data_stream) % 256
    
    # Dead code path - never executed
    if validation_flag and offset_adjust > 100:
        unused_result = parity_check + offset_adjust
    
    # Final transformation with multiple operations
    mask_transform = (secondary_mask ^ 0xAA) | (primary_sum & 0x55)
    checksum_accumulator = (checksum_accumulator << 2) & 0xFF
    
    # Critical execution point
    final_hash = checksum_accumulator ^ mask_transform
    
    print(f"Result: {final_hash}")
    return final_hash

# Test execution
data_bytes = [0x12, 0x34, 0x56, 0x78, 0x9A]
compute_data_integrity(data_bytes)