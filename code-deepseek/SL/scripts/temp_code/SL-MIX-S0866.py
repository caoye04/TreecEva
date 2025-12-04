def calculate_network_checksum():
    header_data = [0x45, 0x00, 0x00, 0x3C]
    payload_data = [0x10, 0x11, 0x12, 0x13, 0x14]
    
    header_xor = header_data[0] ^ header_data[1] ^ header_data[2] ^ header_data[3]
    payload_xor = payload_data[0] ^ payload_data[1] ^ payload_data[2] ^ payload_data[3] ^ payload_data[4]
    
    mask_value = 0xFF
    final_checksum = (header_xor ^ payload_xor) & mask_value
    
    print(f"Result: {final_checksum}")
    return final_checksum

calculate_network_checksum()