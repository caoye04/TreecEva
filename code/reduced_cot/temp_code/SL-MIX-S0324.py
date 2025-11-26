packet_headers = [0x45, 0x00, 0x00, 0x3C, 0x1C, 0x46]
header_xor = 0
for i, header in enumerate(packet_headers):
    header_xor ^= header

protocol_flags = [0x01, 0x80, 0x40]
flag_xor = 0
for flag in protocol_flags:
    flag_xor |= flag

final_xor_value = header_xor & flag_xor
network_checksum = final_xor_value
print(f"Result: {network_checksum}")