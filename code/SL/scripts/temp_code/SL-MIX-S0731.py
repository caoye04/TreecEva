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

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Generate first 20 primes
prime_list = generate_primes(100)[:20]

# Create dictionary of semiprime products mapped to sum of factors
semiprime_map = {p1 * p2: p1 + p2 for i, p1 in enumerate(prime_list) for p2 in prime_list[i+1:] if p1 * p2 < 1000}

# Apply dynamic programming to calculate cumulative LCMs of the sums
sorted_sums = sorted(semiprime_map.values())
cumulative_lcm = [sorted_sums[0]]
for i in range(1, len(sorted_sums)):
    cumulative_lcm.append(lcm(cumulative_lcm[-1], sorted_sums[i]))

# Create sets for set operations
set_a = set(filter(lambda x: x % 3 == 0, cumulative_lcm))
set_b = set(filter(lambda x: x % 5 == 0, cumulative_lcm))
intersection_set = set_a & set_b

# Optimization counter using functional programming
optimized_lookup_count = reduce(lambda acc, _: acc + 1, intersection_set, 0)

print(f"Result: {optimized_lookup_count}")