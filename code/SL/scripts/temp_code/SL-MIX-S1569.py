from math import gcd
from functools import reduce

# Prime factor lists for two RSA keys
key_a_primes = [17, 19, 23]
key_b_primes = [19, 29, 31]

# Find common primes between keys
common_primes = [p for p in key_a_primes if p in key_b_primes]

# Compute modular inverse dictionary for common primes under modulus 100
modulus = 100
inverse_map = {p: pow(p, -1, modulus) for p in common_primes if gcd(p, modulus) == 1}

# Filter out primes whose inverses are even
filtered_inverses = {p: inv for p, inv in inverse_map.items() if inv % 2 != 0}

# Aggregate key strength using product of filtered inverses
if filtered_inverses:
    aggregated_key_strength = reduce(lambda x, y: x * y, filtered_inverses.values(), 1)
else:
    aggregated_key_strength = 0

print(f"Result: {aggregated_key_strength}")