import heapq
from collections import deque
from functools import reduce
from math import gcd

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def fibonacci_sequence(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Generate primes up to 50
prime_numbers = sieve_of_eratosthenes(50)

# Generate first 50 Fibonacci numbers
fib_sequence = fibonacci_sequence(50)

# Extract Fibonacci numbers at prime indices
prime_indexed_fibs = [fib_sequence[p] for p in prime_numbers if p < len(fib_sequence)]

# Initialize cryptographic components
hash_accumulator = 0
rolling_window = deque(maxlen=5)
max_heap = []

message = "CRYPTO_SYSTEM_V2"
encoded_values = []

# Process each character in the message
for char in message:
    # ASCII value encoding with prime-based offset
    ascii_val = ord(char)
    prime_offset = prime_numbers[len(encoded_values) % len(prime_numbers)]
    encoded_val = ascii_val ^ prime_offset  # XOR with prime
    encoded_values.append(encoded_val)
    
    # Update rolling window
    rolling_window.append(encoded_val)
    
    # Calculate hash component using prime-indexed Fibonacci
    fib_component = prime_indexed_fibs[len(encoded_values) % len(prime_indexed_fibs)]
    hash_component = (encoded_val * fib_component) % 1000000007
    
    # Push negative for max heap behavior
    heapq.heappush(max_heap, -hash_component)
    
    # Maintain heap size at 3
    if len(max_heap) > 3:
        heapq.heappop(max_heap)
    
    # Update accumulator with LCM of current value and top of heap
    if max_heap:
        top_value = -max_heap[0]
        hash_accumulator = lcm(hash_accumulator, top_value) if hash_accumulator else top_value

# Final hash computation
final_hash = reduce(lambda x, y: (x + y) % 1000000007, [hash_accumulator] + list(rolling_window), 0)

print(f"Result: {final_hash}")