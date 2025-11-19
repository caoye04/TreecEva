from collections import defaultdict
from math import gcd
from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def extract_primes_from_hex(hex_token):
    value = int(hex_token, 16)
    primes = []
    for i in range(2, min(value + 1, 100)):  # Limit search for efficiency
        if value % i == 0 and is_prime(i):
            primes.append(i)
    return primes[:3]  # Only first three primes

hex_tokens = ['0x1A', '0x2F', '0x3B', '0x4E']
prime_map = defaultdict(list)

for token in hex_tokens:
    prime_factors = extract_primes_from_hex(token)
    if prime_factors:
        prime_map[token].extend(prime_factors)

# Short-circuit evaluation to ensure we have enough data
if not prime_map or len(prime_map) < 3:
    verification_signature = 0
else:
    all_primes = []
    for primes in prime_map.values():
        all_primes.extend(primes)
    
    # Calculate LCM of all unique primes
    unique_primes = list(set(all_primes))
    lcm_value = 1
    for p in unique_primes:
        lcm_value = lcm_value * p // gcd(lcm_value, p)
    
    # Apply combinatoric transformation only if we have sufficient primes
    if len(unique_primes) >= 4 and lcm_value > 10:
        combinatoric_factor = len(list(combinations(unique_primes, 2)))
        verification_signature = lcm_value * combinatoric_factor
    else:
        verification_signature = lcm_value

print(f"Result: {verification_signature}")