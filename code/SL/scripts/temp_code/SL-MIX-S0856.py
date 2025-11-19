from math import gcd
from functools import lru_cache

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

@lru_cache(maxsize=None)
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

observation_window = 120
primes = sieve_of_eratosthenes(observation_window)
prime_cursor = 0
signal_signature = []

for idx in range(1, observation_window + 1):
    if idx > 1 and all(idx % p != 0 for p in primes[:prime_cursor+1]):
        prime_cursor = min(prime_cursor + 1, len(primes) - 1)
    current_prime = primes[prime_cursor]
    stellar_value = gcd(idx, current_prime)
    signal_signature.append(stellar_value)

weighted_aggregation = 0
for i, sig in enumerate(signal_signature):
    fib_weight = fibonacci(i % 20)
    weighted_aggregation += sig * fib_weight

cosmic_coherence_score = weighted_aggregation % 1000
print(f"Result: {cosmic_coherence_score}")