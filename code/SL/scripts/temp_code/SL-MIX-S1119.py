import heapq
import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Deep space transmission data
transmission_data = [23, 45, 67, 89, 12, 34, 56, 78, 91, 103, 113, 131, 151, 173, 191]

# Extract prime numbers from transmission
cosmic_primes = list(filter(is_prime, transmission_data))

# Create a max heap with negative values (since Python has min heap)
cosmic_heap = []
for prime in cosmic_primes:
    heapq.heappush(cosmic_heap, -prime)

# Process the heap to create frequency map
frequency_map = {}
while cosmic_heap:
    prime = -heapq.heappop(cosmic_heap)
    frequency_map[prime] = frequency_map.get(prime, 0) + 1

# Calculate prime products using reduce
prime_keys = list(frequency_map.keys())
product_of_primes = reduce(lambda x, y: x * y, prime_keys, 1)

# Calculate statistical measures
mean_frequency = sum(frequency_map.values()) / len(frequency_map)
variance_components = [(v - mean_frequency) ** 2 for v in frequency_map.values()]
frequency_variance = sum(variance_components) / len(variance_components)

# Apply number theory operations
pairwise_lcm = 1
for i in range(len(prime_keys)):
    for j in range(i+1, len(prime_keys)):
        pairwise_lcm = lcm(pairwise_lcm, lcm(prime_keys[i], prime_keys[j]))

# Compute cosmic index using ternary operator and logical operations
is_balanced_transmission = len(cosmic_primes) > 10 and frequency_variance < 1.0
transmission_strength = product_of_primes if is_balanced_transmission else sum(prime_keys)

cosmic_index = (transmission_strength * pairwise_lcm) // int(mean_frequency) if frequency_variance > 0 else 0

print(f"Result: {cosmic_index}")