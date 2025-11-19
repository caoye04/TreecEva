import math
from collections import defaultdict

def decode_message(encoded_msg, base):
    return int(math.log(encoded_msg, base))

def modular_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

# Protocol initialization
participants = {'Alice', 'Bob', 'Charlie'}
encoded_public_keys = {243, 1024, 3125}  # 3^5, 2^10, 5^5
shared_primes = frozenset({3, 5})
base_conversion_map = {3: 27, 5: 125}

# Decode public keys using logarithms
private_exponents = defaultdict(int)
for key in encoded_public_keys:
    for prime in shared_primes:
        if key % prime == 0:
            private_exponents[prime] = decode_message(key, base_conversion_map[prime])

# Compute shared secret using modular exponentiation
modulus = 1009
shared_secret_key = 1
for prime, exponent in private_exponents.items():
    shared_secret_key *= modular_pow(prime, exponent, modulus)
    shared_secret_key %= modulus

print(f"Result: {shared_secret_key}")