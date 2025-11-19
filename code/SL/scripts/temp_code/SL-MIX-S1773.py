def verify_segment(segment_data, depth=0):
    if depth > 3:
        return 0
    if not segment_data:
        return 1
    
    # Logical operations on segment values
    parity_check = (segment_data[0] & 0xF) ^ (segment_data[-1] & 0xF)
    size_valid = len(segment_data) >= 4 and len(segment_data) <= 16
    
    # Recursive validation of sub-segments
    mid = len(segment_data) // 2
    left_checksum = verify_segment(segment_data[:mid], depth + 1) if size_valid else 0
    right_checksum = verify_segment(segment_data[mid:], depth + 1) if size_valid else 0
    
    # Combine results with logical operations
    return (parity_check & (left_checksum | right_checksum)) if size_valid else (parity_check | (left_checksum ^ right_checksum))

# Packet data for verification
packet_segments = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70, 0x81]

# Process packet and calculate final checksum
final_checksum = verify_segment(packet_segments)
print(f"Result: {final_checksum}")