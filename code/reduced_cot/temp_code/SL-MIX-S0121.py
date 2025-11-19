import heapq
import math
from functools import wraps

class SignalNode:
    def __init__(self, freq, next_node=None):
        self.frequency = freq
        self.next = next_node

def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

@call_counter
def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Create a linked list of signal frequencies
head = SignalNode(42)
head.next = SignalNode(70)
head.next.next = SignalNode(98)
head.next.next.next = SignalNode(126)

# Process frequencies with a min-heap
frequency_heap = []
current = head
while current:
    heapq.heappush(frequency_heap, current.frequency)
    current = current.next

# Extract two smallest frequencies and compute GCD
freq_a = heapq.heappop(frequency_heap)
freq_b = heapq.heappop(frequency_heap)
gcd_value = compute_gcd(freq_a, freq_b)

# Calculate statistical measures
remaining_frequencies = [freq for freq in frequency_heap]
mean_frequency = sum(remaining_frequencies) / len(remaining_frequencies)
variance = sum((x - mean_frequency) ** 2 for x in remaining_frequencies) / len(remaining_frequencies)

# Determine if mean is prime using generated primes
primes_up_to_200 = generate_primes(200)
is_mean_prime = int(mean_frequency) in primes_up_to_200

# Calculate final metric using ternary operator and multiple operations
final_metric = (gcd_value * 3 if is_mean_prime else gcd_value * 2) + int(math.sqrt(variance)) + (compute_gcd.calls * 5)

print(f"Result: {final_metric}")