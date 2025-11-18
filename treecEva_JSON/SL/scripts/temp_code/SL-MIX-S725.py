def xor_cipher(data, key):
    return data ^ key

def rotate_left(value, shift, bits=32):
    shift %= bits
    return ((value << shift) | (value >> (bits - shift))) & ((1 << bits) - 1)

session_id = 0x1F2E3D4C
encryption_key = 0xA5B6C7D8

# Stage 1: XOR with key
stage1 = xor_cipher(session_id, encryption_key)

# Stage 2: Left rotate by 7 bits
stage2 = rotate_left(stage1, 7)

# Stage 3: Apply mask from string hash
mask_string = "SECURITY_PROTOCOL_V2"
mask = hash(mask_string) & 0xFFFFFFFF
stage3 = stage2 & mask

# Stage 4: Short-circuit evaluation with conditions
if (stage3 >> 16) > 0x7FFF and (stage3 & 0xFF) != 0:
    secure_token = stage3 | 0xF0F0F0F0
else:
    secure_token = stage3 & 0x0F0F0F0F

print(f"Result: {secure_token}")