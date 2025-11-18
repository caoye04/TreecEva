from math import gcd
from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Frequency measurements from deep space signals
signal_frequencies = [22, 7, 14, 19, 25, 3, 11, 30, 13, 8]

# Filter out prime frequencies
prime_frequencies = list(filter(is_prime, signal_frequencies))

# Compute LCM of all prime frequencies
lcm_of_primes = reduce(lcm, prime_frequencies)

# Dynamic programming table for stability scores
stability_scores = [0] * (len(prime_frequencies) + 1)
stability_scores[0] = 1

for i in range(1, len(prime_frequencies) + 1):
    stability_scores[i] = stability_scores[i-1] * prime_frequencies[i-1] + i

# Apply weighting function
weighted_sum = sum(map(lambda x, y: x * y, prime_frequencies, stability_scores[:-1]))

# Final stability score calculation
final_stability_score = (lcm_of_primes + weighted_sum) % 1000

print(f"Result: {final_stability_score}")