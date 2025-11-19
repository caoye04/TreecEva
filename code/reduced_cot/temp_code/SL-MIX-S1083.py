from math import log2, exp
from itertools import permutations
from collections import namedtuple

def calculate_entropy(keys):
    return sum(log2(k + 1) for k in keys if k > 0)

def apply_mask(value, mask_set):
    masked = 0
    for i, bit in enumerate(reversed(bin(value)[2:])):
        if int(bit) and (i in mask_set):
            masked |= (1 << i)
    return masked

# Base cipher components
CipherKey = namedtuple('CipherKey', ['primary', 'secondary'])
base_keys = [CipherKey(8, 3), CipherKey(4, 7), CipherKey(2, 5)]
mask_positions = frozenset({0, 2, 4, 6})

# Generate all primary key permutations
permuted_primaries = list(permutations([k.primary for k in base_keys]))

# Calculate entropy-weighted combination scores
combination_scores = []
for perm in permuted_primaries:
    entropy = calculate_entropy(perm)
    combo_value = int(exp(entropy))
    masked_combo = apply_mask(combo_value, mask_positions)
    combination_scores.append(masked_combo)

# Final security score aggregation
security_score = sum(combination_scores) % 1000
print(f'Result: {security_score}')