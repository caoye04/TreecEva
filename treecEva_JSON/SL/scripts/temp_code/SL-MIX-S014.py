def transform_packet(seed):
    # Apply left shift by 3 and mask to 8 bits
    stage1 = (seed << 3) & 0xFF
    # XOR with 0b10101010
    stage2 = stage1 ^ 0xAA
    # Right shift by 2 and mask again
    stage3 = (stage2 >> 2) & 0xFF
    # Final XOR with original seed
    final_checksum = stage3 ^ seed
    return final_checksum

packet_seed = 0b11001010
final_checksum = transform_packet(packet_seed)
print(f'Result: {final_checksum}')