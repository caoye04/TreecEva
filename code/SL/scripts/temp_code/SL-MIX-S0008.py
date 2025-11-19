import base64

encoded_packets = [b'SGVsbG8=', b'V29ybGQ=', b'UHl0aG9u']

def calculate_checksum(text):
    return sum(ord(char) for char in text)

packet_checksums = []
for packet in encoded_packets:
    decoded_text = base64.b64decode(packet).decode('utf-8')
    checksum = calculate_checksum(decoded_text)
    packet_checksums.append(checksum)

final_security_checksum = sum(packet_checksums)
print(f"Result: {final_security_checksum}")