import re
from functools import reduce
from math import gcd

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

class Signal:
    def __init__(self, id_code, frequency):
        self.id_code = id_code
        self.frequency = frequency

signals = [
    Signal("ALPHA-739", 1024),
    Signal("BETA-283", 756),
    Signal("GAMMA-191", 1331),
    Signal("DELTA-449", 512)
]

# Process signals through validation pipeline
valid_signals = []
for signal in signals:
    # Pattern matching to check ID format
    if re.match(r'^[A-Z]+-\d+$', signal.id_code):
        # Check if frequency satisfies certain conditions
        factors = prime_factors(signal.frequency)
        unique_factors = list(set(factors))
        if len(unique_factors) >= 2 and all(is_prime(f) for f in unique_factors):
            valid_signals.append(signal)

# Calculate verification metrics
frequency_sum = sum(s.frequency for s in valid_signals)
frequency_product = reduce(lambda x, y: x * y, [s.frequency for s in valid_signals], 1)

# Bitwise operations on frequencies
bitwise_xor_result = 0
for s in valid_signals:
    bitwise_xor_result ^= s.frequency

# Compute LCM of all valid signal frequencies
lcm_result = valid_signals[0].frequency
for s in valid_signals[1:]:
    lcm_result = lcm_result * s.frequency // gcd(lcm_result, s.frequency)

# Final verification score calculation
verification_score = (frequency_sum & bitwise_xor_result) | (lcm_result ^ frequency_product)
print(f"Result: {verification_score}")