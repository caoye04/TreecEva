def encode_layer(data):
    return ''.join(chr(ord(c) ^ 0x5C) for c in data)

def decode_layer(data):
    return ''.join(chr(ord(c) ^ 0x3A) for c in data)

packet_signature = "SECURITY_PACKET_2023"
transformed_data = encode_layer(packet_signature)
reversed_chunks = [transformed_data[i:i+4][::-1] for i in range(0, len(transformed_data), 4)]
consolidated_string = ''.join(reversed_chunks)
decoded_payload = decode_layer(consolidated_string)
byte_values = [ord(c) for c in decoded_payload]
sorted_values = sorted(set(byte_values))
threat_indicator = 0
for idx, val in enumerate(sorted_values):
    if val & 0x01:
        threat_indicator += val << (idx % 4)
    else:
        threat_indicator -= val >> (idx % 3)
print(f"Result: {threat_indicator}")