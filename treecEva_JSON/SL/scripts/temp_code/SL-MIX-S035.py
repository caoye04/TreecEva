import math
import statistics
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

def generate_sequence(length):
    seq = []
    for i in range(1, length + 1):
        if i % 3 == 0:
            seq.append(i * 2)
        elif i % 3 == 1:
            seq.append(i ** 2)
        else:
            seq.append(i * (i + 1))
    return seq

# Generate sequence of length 20
sequence = generate_sequence(20)

# Extract elements at prime indices (1-based indexing)
prime_indexed_values = [sequence[i] for i in range(len(sequence)) if is_prime(i + 1)]

# Compute variance of these values
variance = statistics.variance(prime_indexed_values)

# Compute combinatorial coefficient C(10, 3)
comb_coeff = len(list(combinations(range(10), 3)))

# Apply bitwise XOR between variance (as integer) and combinatorial coefficient
resonance_score = int(variance) ^ comb_coeff

print(f"Result: {resonance_score}")