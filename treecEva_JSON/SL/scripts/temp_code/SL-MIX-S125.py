import re
from collections import defaultdict

def custom_hash(token, modulus):
    hash_val = 0
    for char in token:
        hash_val = (hash_val * 31 + ord(char)) % modulus
    return hash_val

def is_hex_token(s):
    return bool(re.match(r'^[0-9a-fA-F]+$', s))

token_stream = ['a1b2', 'c3d4', 'e5f6', 'a1b2', 'g7h8', 'c3d4', 'i9j0', 'a1b2', 'k1l2']
hash_freq = defaultdict(int)
collision_counter = 0
threshold = 3
modulus = 1009

for idx, token in enumerate(token_stream):
    if not is_hex_token(token):
        continue
    hash_val = custom_hash(token, modulus)
    hash_freq[hash_val] += 1
    if hash_freq[hash_val] == 2:
        collision_counter += 1
    elif hash_freq[hash_val] > 2:
        collision_counter += hash_freq[hash_val] - 1
    if collision_counter >= threshold:
        break

print(f"Result: {collision_counter}")