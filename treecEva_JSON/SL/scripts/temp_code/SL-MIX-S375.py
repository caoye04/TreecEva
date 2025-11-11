import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

# Generate first 5 prime numbers
primes = [2, 3, 5, 7, 11]

# Calculate LCM of the first 5 primes
lcm_primes = lcm_of_list(primes)

# Use LCM as exponent in modular exponentiation
base = 3
modulus = 1000
secure_key = pow(base, lcm_primes, modulus)

print(f"Result: {secure_key}")