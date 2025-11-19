import heapq
from math import gcd
from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Initialize cryptographic components
processed_values_heap = []
prime_sequence = [n for n in range(2, 50) if is_prime(n)]
accumulated_hash = 1
modulus_base = 1000

# Process prime sequence with custom hashing
for idx, prime in enumerate(prime_sequence):
    if idx % 3 == 0:
        heapq.heappush(processed_values_heap, prime * 2)
    elif idx % 3 == 1:
        heapq.heappush(processed_values_heap, prime + 5)
    else:
        squared_val = prime ** 2
        heapq.heappush(processed_values_heap, squared_val if squared_val < 100 else prime)

# Apply reduction with GCD operations
while len(processed_values_heap) > 1:
    first = heapq.heappop(processed_values_heap)
    second = heapq.heappop(processed_values_heap)
    combined_gcd = gcd(first, second)
    accumulated_hash = (accumulated_hash * combined_gcd) % modulus_base
    heapq.heappush(processed_values_heap, combined_gcd)

# Final signature calculation with ternary logic
final_element = heapq.heappop(processed_values_heap)
cryptographic_signature = accumulated_hash if final_element > 10 else accumulated_hash // 2

print(f"Result: {cryptographic_signature}")