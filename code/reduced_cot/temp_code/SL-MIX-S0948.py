import hashlib
from itertools import permutations

document_tag = 'SEC'
salt_values = {'X1', 'Y2', 'Z3'}
combined_strings = [perm + salt for perm in [''.join(p) for p in permutations(document_tag)] for salt in salt_values]

# Dynamic programming table for character frequency
freq_table = {}
for s in combined_strings:
    for char in s:
        if char not in freq_table:
            freq_table[char] = 0
        freq_table[char] += 1

# Compute verification sum based on hash of frequency data
verification_sum = 0
for char, count in sorted(freq_table.items()):
    hash_input = f"{char}:{count}"
    hash_val = int(hashlib.md5(hash_input.encode()).hexdigest(), 16) % 1000
    verification_sum += hash_val

print(f"Result: {verification_sum}")