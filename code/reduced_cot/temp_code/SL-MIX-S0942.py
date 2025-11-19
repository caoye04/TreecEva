from math import gcd
from functools import reduce

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Generate first 7 primes
primes = sieve_of_eratosthenes(20)[:7]

# Calculate the special sequence using exponential prime factorization
encryption_sequence = []
for n in range(1, len(primes) + 1):
    term = 1
    for i in range(n):
        term *= primes[i] ** (i + 1)
    encryption_sequence.append(term)

# Compute all pairwise XORs between consecutive terms
consecutive_xors = [
    encryption_sequence[i] ^ encryption_sequence[i+1] 
    for i in range(len(encryption_sequence)-1)
]

# Apply greedy approach: find GCD of all XOR results
crypto_key = reduce(gcd, consecutive_xors)

print(f"Result: {crypto_key}")