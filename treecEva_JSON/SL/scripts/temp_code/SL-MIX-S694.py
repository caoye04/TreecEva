import math

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

# Generate primes less than 30
prime_pool = [num for num in range(2, 30) if is_prime(num)]

# Custom entropy calculation using lambda
entropy_fn = lambda freq: math.log(freq) * math.exp(freq % 3)

# Accumulate scores using set operations for filtering
valid_frequencies = set(prime_pool) & frozenset(range(5, 25))

signal_scores = []
for freq in sorted(valid_frequencies):
    if freq > 10:
        score = entropy_fn(freq)
        signal_scores.append(score)
    else:
        adjusted_freq = freq ** 2
        score = entropy_fn(adjusted_freq)
        signal_scores.append(score)

# Calculate final entropy using GCD adjustment
from functools import reduce
gcd_all = reduce(math.gcd, prime_pool[:5])

final_entropy_signal = sum(signal_scores) / gcd_all
final_entropy_signal = int(final_entropy_signal)

print(f"Result: {final_entropy_signal}")