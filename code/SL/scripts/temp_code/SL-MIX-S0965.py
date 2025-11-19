from collections import deque
import itertools

def decode_hex_stream(hex_string):
    return bytes.fromhex(hex_string)

def rotate_key(key_deque, positions):
    key_deque.rotate(positions)
    return key_deque[0]

# Encoded message and encryption keys
encoded_message = "4a6b7c3d5e2f"
encryption_keys = [0x1F, 0x3A, 0x7E, 0xC3]

# Initialize data structures
message_bytes = decode_hex_stream(encoded_message)
key_ring = deque(encryption_keys)
cipher_sum = 0

# Process each byte with rotating key XOR
for i, byte_val in enumerate(message_bytes):
    current_key = rotate_key(key_ring, i & 0x03)  # Rotate by i mod 4
    transformed = byte_val ^ current_key         # XOR transformation
    
    # Apply secondary transformation based on bit patterns
    if (transformed & 0xF0) > 0x80:              # Check high nibble
        transformed ^= 0xAA
    else:
        transformed &= 0x55
    
    # Update accumulator with masked value
    cipher_sum += (transformed & 0x7F)

# Final adjustment using itertools
adjustment_pairs = list(itertools.combinations(encryption_keys, 2))
adjustment_sum = sum(a ^ b for a, b in adjustment_pairs)
cipher_sum ^= (adjustment_sum & 0xFF)

print(f"Result: {cipher_sum}")