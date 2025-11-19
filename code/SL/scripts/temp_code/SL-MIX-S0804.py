import re
from collections import deque

# Encoded network packets (hex strings)
packets = ['4a', '5f', '7c', '6b', '5a', '4d', '7e', '6f']
rotation_keys = deque([0x15, 0x2a, 0x3f])

processed_chars = []
valid_ascii_pattern = re.compile(r'[ -~]')  # Printable ASCII range

def rotate_key():
    key = rotation_keys.popleft()
    rotation_keys.append(key)
    return key

for i, hex_byte in enumerate(packets):
    byte_val = int(hex_byte, 16)
    xor_key = rotate_key()
    decoded_byte = byte_val ^ xor_key
    
    # Check if decoded byte is a valid printable ASCII character
    char_candidate = chr(decoded_byte)
    if valid_ascii_pattern.match(char_candidate):
        processed_chars.append(decoded_byte)
    else:
        # Apply secondary decoding for non-printables
        secondary_key = (xor_key << 1) & 0xFF
        decoded_byte = byte_val ^ secondary_key
        char_candidate = chr(decoded_byte)
        if valid_ascii_pattern.match(char_candidate):
            processed_chars.append(decoded_byte)

# Calculate sum with position-weighted arithmetic
weighted_sum = 0
for pos, ascii_val in enumerate(processed_chars, 1):
    weighted_sum += ascii_val * (pos % 3 + 1)

decoded_character_sum = weighted_sum & 0xFFFF  # Final masking operation
print(f"Result: {decoded_character_sum}")