from functools import reduce
import itertools

def generate_masks(base_seed, count):
    masks = []
    current = base_seed
    for _ in range(count):
        masks.append(current)
        current = (current * 1103515245 + 12345) & 0x7fffffff
    return masks

def custom_decode(value):
    hex_str = hex(value)[2:]
    decoded = 0
    for char in hex_str:
        if '0' <= char <= '9':
            decoded = (decoded << 4) | (ord(char) - ord('0'))
        elif 'a' <= char <= 'f':
            decoded = (decoded << 4) | (ord(char) - ord('a') + 10)
    return decoded

initial_fragment = 0b11010111
mask_list = generate_masks(0x12345, 4)
encoded_fragment = reduce(lambda x, y: x ^ y, mask_list, initial_fragment)
shifted_key = encoded_fragment >> 3
session_key = custom_decode(shifted_key)
print(f"Result: {session_key}")