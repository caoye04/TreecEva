from functools import reduce
from collections import namedtuple

def encode_char(c):
    return ord(c) ^ 0b10101010

def decode_value(v):
    return chr(v ^ 0b10101010)

def tokenize_and_transform(message):
    tokens = [message[i:i+3] for i in range(0, len(message), 3)]
    transformed_map = {token: reduce(lambda x, y: x | y, [encode_char(c) for c in token]) for token in tokens if len(token) == 3}
    return transformed_map

def apply_cipher_rules(token_dict):
    # Apply a transformation rule: if MSB is set, rotate bits left by 2
    updated = {}
    for k, v in token_dict.items():
        if v & 0x80:
            rotated = ((v << 2) | (v >> 6)) & 0xFF
            updated[k] = rotated
        else:
            updated[k] = v
    return updated

def compute_sorted_sum(transformed_tokens):
    # Sort keys by the number of 1-bits in their values
    sorted_keys = sorted(transformed_tokens.keys(), key=lambda k: bin(transformed_tokens[k]).count('1'))
    # Sum values at odd indices in the sorted list
    total = 0
    for i in range(1, len(sorted_keys), 2):
        total += transformed_tokens[sorted_keys[i]]
    return total

# Main execution
secret_message = "CRYPTOGRAPHY_CHALLENGE"
token_mappings = tokenize_and_transform(secret_message)
cipher_mappings = apply_cipher_rules(token_mappings)
cipher_sum = compute_sorted_sum(cipher_mappings)
print(f"Result: {cipher_sum}")