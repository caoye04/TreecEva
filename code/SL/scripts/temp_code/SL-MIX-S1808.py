from math import gcd
from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Find primes in range [10, 30]
prime_pool = [n for n in range(10, 31) if is_prime(n)]

# Generate all unique pairs of primes
prime_pairs = list(combinations(prime_pool, 2))

# Calculate product of each pair
pair_products = [a * b for a, b in prime_pairs]

# Greedy adjustment: select numbers from 5 to 15 that are coprime with the sum of pair_products
initial_sum = sum(pair_products)
adjustment_candidates = list(range(5, 16))
co_prime_adjustments = []

for num in sorted(adjustment_candidates, reverse=True):  # greedy: try larger first
    if gcd(num, initial_sum) == 1:
        co_prime_adjustments.append(num)
        if len(co_prime_adjustments) == 3:  # limit to 3 adjustments
            break

# Final cryptographic key strength calculation
adjusted_sum = initial_sum + sum(co_prime_adjustments)
cryptographic_key_strength = adjusted_sum % 1000

print(f"Result: {cryptographic_key_strength}")