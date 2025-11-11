def key_validator(func):
    def wrapper(key_segment):
        if key_segment & 0xF0 == 0xA0 and key_segment >> 4 != 0xB:
            return func(key_segment)
        return 0
    return wrapper

@key_validator
def encrypt_segment(segment):
    return (segment ^ 0x55) & 0xFF

key_parts = [0xA3, 0xB7, 0xA9, 0xC2, 0xA1]
encrypted_output = 0

for i, part in enumerate(key_parts):
    if i % 2 == 0 or (part | 0x0F) != 0xBF:
        processed = encrypt_segment(part)
        encrypted_output = encrypted_output | (processed << (i*8))
    else:
        encrypted_output = encrypted_output ^ (part << (i*8))

print(f"Result: {encrypted_output}")