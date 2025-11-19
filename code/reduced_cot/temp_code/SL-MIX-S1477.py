import math
from itertools import combinations

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

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Processed frequency data from vibration sensors
sensor_readings = [24, 35, 49, 56, 77, 81, 98]
threshold = 3

# Dictionary comprehension to map each reading to its unique prime factors
frequency_prime_map = {r: list(set(prime_factors(r))) for r in sensor_readings}

# Merge dictionaries to create a flat view of all primes involved
prime_pool = {}
for reading, primes in frequency_prime_map.items():
    prime_pool.update({p: prime_pool.get(p, 0) + 1 for p in primes})

# Identify which readings have at least one prime factor greater than threshold
valid_readings = [r for r in sensor_readings if any(p > threshold for p in frequency_prime_map[r])]

# Count resonance pairs using short-circuit evaluation and GCD
resonance_count = 0
for a, b in combinations(valid_readings, 2):
    # Short-circuit: skip if either number is not composed of qualifying primes
    if not (any(p > threshold for p in frequency_prime_map[a]) and 
            any(p > threshold for p in frequency_prime_map[b])):
        continue
    # Compute GCD only when necessary
    gcd_val = math.gcd(a, b)
    if gcd_val > threshold:
        resonance_count += 1

print(f"Result: {resonance_count}")