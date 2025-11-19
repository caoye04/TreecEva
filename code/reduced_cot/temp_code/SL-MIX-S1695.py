def xor_shift_checksum(packet_data):
    checksum = 0
    for byte_val in packet_data:
        checksum ^= byte_val
        if byte_val & 0x80:
            checksum = ((checksum << 1) | (checksum >> 7)) & 0xFF
        else:
            checksum = ((checksum >> 1) | (checksum << 7)) & 0xFF
    return checksum

def validate_packet(packet_data):
    base_checksum = xor_shift_checksum(packet_data)
    enhanced_checksum = base_checksum ^ 0xAA
    if (enhanced_checksum & 0xF0) != 0 and not (base_checksum & 0x0F == 0):
        final_signature = (enhanced_checksum << 2) & 0xFF
    else:
        final_signature = (enhanced_checksum >> 2) & 0xFF
    return final_signature

test_packet = [0xC3, 0x2F, 0x9A, 0x1D]
final_signature = validate_packet(test_packet)
print(f'Result: {final_signature}')