from functools import reduce

def count_bits_recursive(value):
    if value == 0:
        return 0
    return (value & 1) + count_bits_recursive(value >> 1)

security_keys = [0b110101, 0b101010, 0b111000]
combined_key = reduce(lambda x, y: x ^ y, security_keys)

if combined_key & 0b100000:
    adjustment = 5
else:
    adjustment = count_bits_recursive(combined_key)

encryption_strength = (combined_key & 0b1111) + adjustment
print(f"Result: {encryption_strength}")