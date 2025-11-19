from collections import namedtuple
import base64

def encode_transform(value):
    return int.from_bytes(base64.b64encode(str(value).encode()), 'big')

def decode_transform(value):
    try:
        byte_length = (value.bit_length() + 7) // 8
        bytes_val = value.to_bytes(byte_length, 'big')
        return int(base64.b64decode(bytes_val).decode())
    except:
        return value >> 2

PacketHeader = namedtuple('PacketHeader', ['src_port', 'dst_port', 'seq_num', 'ack_num'])

header_fields = PacketHeader(8080, 443, 123456789, 987654321)

# Initialize checksum components
initial_hash = 0xCAFEBABE
port_xor = header_fields.src_port ^ header_fields.dst_port
seq_masked = header_fields.seq_num & 0xFFFFFFF0
ack_shifted = header_fields.ack_num >> 4

# Apply encoding transformation
encoded_seq = encode_transform(seq_masked)
checksum_stage1 = initial_hash ^ encoded_seq

# Apply conditional logic and decoding
decoded_ack = decode_transform(ack_shifted) if ack_shifted > 1000 else ack_shifted << 2
checksum_stage2 = checksum_stage1 & (decoded_ack | 0xFF)

# Final adjustment with bitwise operations
adjusted_port = port_xor << 3 if port_xor % 2 == 0 else port_xor >> 1
final_checksum = (checksum_stage2 ^ adjusted_port) & 0xFFFFFFFF

print(f"Result: {final_checksum}")