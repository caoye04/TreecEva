import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def harmonic_sum(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return 1 / values[0]
    mid = len(values) // 2
    left_sum = harmonic_sum(values[:mid])
    right_sum = harmonic_sum(values[mid:])
    return left_sum + right_sum

# Deep space prime frequency bands
prime_bands = [2, 3, 5, 7, 11]

# Calculate LCM of all prime bands using set operations
band_set = frozenset(prime_bands)
lcm_value = 1
for freq in band_set:
    lcm_value = lcm(lcm_value, freq)

# Generate harmonic components using list comprehension
harmonic_components = [f * 2 for f in prime_bands if f < 10]

# Compute harmonic sum using divide and conquer
h_sum = harmonic_sum(harmonic_components)

# Calculate final synchronization index
synchronization_index = int(lcm_value * h_sum)

print(f"Result: {synchronization_index}")