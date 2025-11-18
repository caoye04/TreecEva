from math import gcd
from itertools import combinations

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

# Generate primes under 50
prime_numbers = sieve_of_eratosthenes(50)
valid_pairs = [
    (a, b) for a, b in combinations(prime_numbers, 2)
    if gcd(a, b) == 1 and (a * b) % 10 == 9
]
sorted_products = sorted([a * b for a, b in valid_pairs])
encryption_strength = sum(sorted_products[:len(sorted_products)//2])
print(f"Result: {encryption_strength}")