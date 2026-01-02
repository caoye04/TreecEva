import math
from collections import namedtuple

# Define a named tuple for hash analysis results
HashResult = namedtuple('HashResult', ['value', 'ones', 'zeros', 'is_balanced'])

def count_bits(num):
    ones = bin(num).count('1')
    zeros = num.bit_length() - ones
    return ones, zeros

def is_balanced_hash(ones, zeros):
    # Short-circuit evaluation: if either count is zero, GCD is the other count
    if ones == 0 or zeros == 0:
        return False
    return math.gcd(ones, zeros) > 1

# Precomputed hash values for analysis
hash_values = [0x1F, 0x2A, 0x3C, 0x45, 0x5E, 0x69, 0x77, 0x8B, 0x9D, 0xA4]

# Initialize result tracking
balanced_count = 0
hash_results = []

# Process each hash value
for val in hash_values:
    ones, zeros = count_bits(val)
    is_balanced = is_balanced_hash(ones, zeros)
    hash_results.append(HashResult(val, ones, zeros, is_balanced))
    # Increment count if hash is balanced
    balanced_count += is_balanced

print(f"Result: {balanced_count}")