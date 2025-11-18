import itertools

# Generate all 3-character permutations of lowercase letters
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
password_permutations = list(itertools.permutations(lowercase_letters, 3))

# Calculate memory estimate (each character is 1 byte, so 3 bytes per permutation)
permutation_count = len(password_permutations)
memory_estimate = permutation_count * 3

print(f"Result: {memory_estimate}")