from math import gcd
from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate first 5 primes greater than 20
primes = []
candidate = 21
while len(primes) < 5:
    if is_prime(candidate):
        primes.append(candidate)
    candidate += 1

# Calculate product of these primes
prime_product = reduce(lambda x, y: x * y, primes)

# Euler's totient function φ(35)
# Since 35 = 5 * 7, φ(35) = (5-1)*(7-1) = 24
totient_35 = 24

# Apply modular reduction
session_checksum = prime_product % totient_35

print(f"Result: {session_checksum}")