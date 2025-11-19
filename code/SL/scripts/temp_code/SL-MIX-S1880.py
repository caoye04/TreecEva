from math import gcd
from statistics import mean

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

# Generate primes up to 100
prime_list = sieve_of_eratosthenes(100)

# Select first 10 primes and their indices (1-based)
selected_primes = prime_list[:10]
indices = list(range(1, 11))

# Transformation function using lambda
transform = lambda p, idx: p ^ (idx * 3)

# Apply transformation
transformed_values = [transform(p, i) for i, p in zip(indices, selected_primes)]

# Compute mean of transformed values
average_transform = mean(transformed_values)

# Compute GCD of indices using functools.reduce
import functools
index_gcd = functools.reduce(gcd, indices)

# Security index calculation
security_index = int(average_transform) - index_gcd * 2

print(f"Result: {security_index}")