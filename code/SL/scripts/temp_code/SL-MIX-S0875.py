from heapq import heappush, heappop
from itertools import permutations
from functools import reduce
from math import gcd

def get_prime_factors(n):
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

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def calculate_composite_weight(factors):
    if not factors:
        return 0
    return reduce(lcm, factors, 1)

# Encryption key repository
encryption_keys = [12, 15, 21, 35]

# Priority queue for processing keys
priority_queue = []

# Process each encryption key
processed_weights = []
for key in encryption_keys:
    prime_factors = get_prime_factors(key)
    weight = calculate_composite_weight(prime_factors)
    heappush(priority_queue, (weight, key))
    processed_weights.append(weight)

# Generate permutations of unique prime factors from all keys
all_prime_factors = []
for key in encryption_keys:
    all_prime_factors.extend(get_prime_factors(key))
unique_primes = list(set(all_prime_factors))

perm_count = 0
prime_permutations_sum = 0
for perm in permutations(unique_primes):
    perm_count += 1
    # Convert permutation to a number for summation
    perm_number = sum(perm[i] * (10 ** i) for i in range(len(perm)))
    prime_permutations_sum += perm_number

# Retrieve keys in priority order and calculate cumulative xor
cumulative_xor = 0
while priority_queue:
    _, key_value = heappop(priority_queue)
    cumulative_xor ^= key_value

# Final cryptographic computation
final_key_component = (prime_permutations_sum % 1000) + cumulative_xor + perm_count
print(f"Result: {final_key_component}")