from math import gcd
from functools import reduce
from collections import defaultdict

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

# Generate primes up to 30
primes = sieve_of_eratosthenes(30)
prime_index_map = {prime: idx for idx, prime in enumerate(primes)}

# Initialize structures
factor_indices = defaultdict(list)
encryption_components = []

# Process numbers 4 through 20
for num in range(4, 21):
    temp_num = num
    for prime in primes:
        if prime * prime > temp_num:
            break
        if temp_num % prime == 0:
            count = 0
            while temp_num % prime == 0:
                temp_num //= prime
                count += 1
            factor_indices[num].extend([prime_index_map[prime]] * count)
    if temp_num > 1:  # Remaining prime factor
        factor_indices[num].append(prime_index_map[temp_num])

# Compute LCM of prime index lists
for indices in factor_indices.values():
    if indices:
        component = reduce(lcm, indices)
        encryption_components.append(component)

# Final encryption key calculation
encryption_key = sum(encryption_components) % 1000
print(f"Result: {encryption_key}")