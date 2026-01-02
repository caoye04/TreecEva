from functools import reduce
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_resonant_frequency(freq):
    factors = prime_factors(freq)
    if len(factors) != 2 or factors[0] == factors[1]:
        return False
    p, q = sorted(factors)
    return freq % (p + q) == p

candidate_frequencies = [15, 21, 35, 77, 91, 143, 187, 221, 247, 299, 323, 391, 437, 493, 527, 551, 589, 667, 703, 713]

resonant_freqs = list(filter(is_resonant_frequency, candidate_frequencies))

harmonic_indices = list(map(lambda x: max(prime_factors(x)), resonant_freqs))

accumulator = lambda acc, val: acc + val if acc + val <= 100 else acc
final_sum = reduce(accumulator, sorted(harmonic_indices, reverse=True), 0)

print(f"Result: {final_sum}")