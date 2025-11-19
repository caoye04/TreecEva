from collections import defaultdict
import re
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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Protocol initialization
shared_base = 5
prime_modulus = 23
secret_a = 6
secret_b = 15

# Key exchange computation
public_a = (shared_base ** secret_a) % prime_modulus
public_b = (shared_base ** secret_b) % prime_modulus

# Session key derivation
intermediate_key = (public_b ** secret_a) % prime_modulus

# Hash-like transformation using string operations
hex_string = hex(intermediate_key)[2:]  # Remove '0x' prefix
reversed_hex = hex_string[::-1]

# Pattern matching to extract digits
pattern = r'[0-9]'
digits = re.findall(pattern, reversed_hex)
transformed_digits = list(map(int, digits))

# Combinatorics: compute permutations of first three digits if available
perm_count = 0
if len(transformed_digits) >= 3:
    perm_count = math.factorial(len(transformed_digits[:3]))

# Number theory: find next prime after perm_count
next_prime_candidate = perm_count + 1
while not is_prime(next_prime_candidate):
    next_prime_candidate += 1

# Final session key calculation using LCM
session_key = lcm(intermediate_key, next_prime_candidate)

print(f"Result: {session_key}")