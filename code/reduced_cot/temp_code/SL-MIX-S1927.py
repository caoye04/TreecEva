from math import gcd
from itertools import combinations

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Generate primes up to 100
prime_numbers = generate_primes(100)

# Find all pairs of primes whose sum is less than 50
valid_prime_pairs = [(p1, p2) for p1, p2 in combinations(prime_numbers, 2) if p1 + p2 < 50]

# Compute GCD of each pair's product with 210 (2*3*5*7)
gcd_results = {pair: gcd(pair[0] * pair[1], 210) for pair in valid_prime_pairs}

# Filter pairs where the GCD result is greater than 10
filtered_pairs = {pair: result for pair, result in gcd_results.items() if result > 10}

# Calculate encryption key using a lambda function
encryption_components = list(map(lambda p: p[0] * p[1] + max(filtered_pairs[p], 1), filtered_pairs))

# Final encryption key is the sum of all components plus the count of filtered pairs
encryption_key = sum(encryption_components) + len(filtered_pairs)

print(f'Result: {encryption_key}')