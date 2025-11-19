from functools import reduce
from math import gcd

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

signal_segments = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
prime_masks = generate_primes(20)[:len(signal_segments)]

encoded_signals = list(map(lambda x, y: x ^ (y << 1), signal_segments, prime_masks))
transformed_signals = [s >> (1 if s & 1 == 0 else 0) for s in encoded_signals]

pairwise_gcd = [gcd(transformed_signals[i], transformed_signals[i+1]) for i in range(len(transformed_signals)-1)]
checksum = reduce(lambda acc, val: acc ^ val, pairwise_gcd, 0) if pairwise_gcd else 0
checksum = checksum if checksum != 0 else (0x55 if len(signal_segments) > 3 else 0xAA)

print(f"Result: {checksum}")