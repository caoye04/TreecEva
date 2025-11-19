from math import gcd
from itertools import combinations

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def get_divisors(n):
    divs = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))

# System parameters
frequency_slots = [i/10 for i in range(1, 11)]  # 0.1 to 1.0
max_index = 15

# Calculate prime indices up to max_index
prime_indices = [i for i in range(2, max_index+1) if is_prime(i)]

# Compute divisor combinations weight
slot_divisors = [get_divisors(int(f*10)) for f in frequency_slots]
combination_weights = []
for div_list in slot_divisors:
    weight = 0
    for r in range(1, min(3, len(div_list)+1)):
        weight += len(list(combinations(div_list, r)))
    combination_weights.append(weight)

# Calculate signal coherence
signal_coherence = 0
for idx, prime_idx in enumerate(prime_indices):
    fib_value = fibonacci(prime_idx)
    harmonic_freq = frequency_slots[idx % len(frequency_slots)]
    weight = combination_weights[idx % len(combination_weights)]
    signal_coherence += fib_value * harmonic_freq * weight

print(f"Result: {int(signal_coherence)}")