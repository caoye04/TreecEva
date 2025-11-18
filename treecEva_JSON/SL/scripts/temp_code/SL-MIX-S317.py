from collections import Counter
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

def prime_weight(num):
    factors = []
    d = 2
    while d * d <= num:
        while (num % d) == 0:
            factors.append(d)
            num //= d
        d += 1
    if num > 1:
        factors.append(num)
    prime_factors = [f for f in factors if is_prime(f)]
    return sum(prime_factors)

hex_hashes = ['a1b2c3d4', '1e2f3a4b', 'deadbeef', 'cafebabe']
weights = []

for h in hex_hashes:
    val = int(h, 16)
    weight = prime_weight(val)
    weights.append(weight)

# Normalize weights using mean adjustment
mean_weight = sum(weights) / len(weights)
normalized_weights = [(w - mean_weight) ** 2 for w in weights]
variance = sum(normalized_weights) / len(normalized_weights)

# Apply modular arithmetic with a cryptographic constant
MOD_CONST = 997  # Large prime
mod_values = [int(w * 1000) % MOD_CONST for w in normalized_weights]

# Compute anomaly score as weighted checksum
anomaly_score = sum(mod_values[i] * (i + 1) for i in range(len(mod_values))) % MOD_CONST

print(f"Result: {anomaly_score}")