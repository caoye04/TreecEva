def validate_packet(packet_id, depth=0):
    if depth > 3:
        return 0
    mask = 0xF << (depth * 4)
    segment = (packet_id & mask) >> (depth * 4)
    if segment == 0:
        return 0
    xor_val = segment ^ ((segment << 1) & 0xF)
    rest = validate_packet(packet_id, depth + 1)
    return xor_val | (rest & ~(0xF << (depth * 4)))

packet_identifier = 0x1F3
checksum_result = validate_packet(packet_identifier)
print(f"Result: {checksum_result}")