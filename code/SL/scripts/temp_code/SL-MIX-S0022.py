from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def generate_primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Initialize cryptographic parameters
initial_values = [12, 18, 24, 30]
prime_set = frozenset(generate_primes_up_to(30))

# Step 1: Calculate LCM of initial values
lcm_result = reduce(lcm, initial_values)

# Step 2: Find GCD of LCM result and a prime from our set
reference_prime = max(prime_set)
gcd_result = gcd(lcm_result, reference_prime)

# Step 3: Apply modular arithmetic with prime counting
modulus_base = len(prime_set) * 7
intermediate_mod = (lcm_result % modulus_base) + (gcd_result << 2)

# Step 4: Final key derivation using bit operations and arithmetic
shift_amount = bin(intermediate_mod).count('1')  # Count set bits
cryptographic_key = (intermediate_mod ^ (shift_amount * 3)) & 0xFF

print(f"Result: {cryptographic_key}")