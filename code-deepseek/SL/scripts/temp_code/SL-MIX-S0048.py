def compute_checksum(blocks):
    data_blocks = [0xAB, 0xCD, 0xEF, 0x12]
    temp_buffer = [0xFF, 0x00]  # Distractor initialization
    checksum = 0
    
    # XOR all data blocks together
    for block in data_blocks:
        checksum ^= block
    
    # Additional unused calculation (distractor)
    unused_sum = sum(data_blocks) + len(temp_buffer)
    
    return checksum

data_blocks = [0xAB, 0xCD, 0xEF, 0x12]
final_hash = compute_checksum(data_blocks)
print(f"Result: {final_hash}")