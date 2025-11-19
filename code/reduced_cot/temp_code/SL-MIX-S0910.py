from math import gcd
from itertools import combinations

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

tokens = [13, 21, 34, 55]
security_index = 0

# Phase 1: Bitwise aggregation
aggregated_mask = 0
for i, val in enumerate(tokens):
    if i % 2 == 0:
        aggregated_mask |= val << (i // 2)
    else:
        aggregated_mask ^= val

# Phase 2: Combinatorial amplification
combos = list(combinations(tokens, 2))
amplification_factor = 1
for x, y in combos:
    amplification_factor *= lcm(x, y)

# Phase 3: Prime weighting
prime_weights = []
def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for t in tokens:
    prime_weights.append(t if is_prime(t) else 1)

weighted_sum = sum(p * t for p, t in zip(prime_weights, tokens))

# Final calculation
security_index = (aggregated_mask + amplification_factor) % weighted_sum
print(f"Result: {security_index}")