import re
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Cryptographic key processing
hex_key = "A7B3F9C2E5D1"
tokens = re.findall(r'[0-9A-F]', hex_key)
prime_digits = [int(t, 16) for t in tokens if is_prime(int(t, 16))]

# Geometric coordinate transformation
coordinates = [(p, p*2 % 10) for p in prime_digits]
transformed_coords = [(x^3, y|5) for x, y in coordinates]

# Bitwise cipher computation
bitwise_accumulator = 0
for x, y in transformed_coords:
    bitwise_accumulator ^= (x << 2) & (y >> 1)

# Modular arithmetic with LCM
modulus_base = lcm(7, 13)
final_cipher_value = (bitwise_accumulator + sum(prime_digits)) % modulus_base

print(f"Result: {final_cipher_value}")