from collections import defaultdict

def process_packet():
    # Packet data as list of bytes
    packet_bytes = [0x1A, 0x2B, 0x3C, 0x4D]
    
    # Initialize checksum
    initial_checksum = 0x55
    
    # Hash table for byte transformation mapping
    transform_map = {
        0x1A: 0xF0,
        0x2B: 0xE1,
        0x3C: 0xD2,
        0x4D: 0xC3
    }
    
    # Apply XOR with mapped values
    transformed_checksum = initial_checksum
    for b in packet_bytes:
        if b in transform_map:
            transformed_checksum ^= transform_map[b]
    
    # Apply bit shifts
    shifted_checksum = (transformed_checksum << 2) & 0xFF
    
    # Final adjustment with OR operation
    final_checksum = shifted_checksum | 0x03
    
    return final_checksum

# Execute the packet processing
final_checksum = process_packet()
print(f"Result: {final_checksum}")