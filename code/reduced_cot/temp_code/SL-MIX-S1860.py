from math import gcd
from functools import reduce
from operator import mul

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# Find first 5 primes
primes = sieve_of_eratosthenes(20)[:5]

# Calculate LCM of first 5 primes
N = reduce(lcm, primes)

# Secret key for the keystream
generator_key = 30

# Generate the sequence and count unique values
sequence_values = set()
for idx in range(1, N + 1):
    sequence_values.add(gcd(idx, generator_key))

unique_count = len(sequence_values)
print(f"Result: {unique_count}")