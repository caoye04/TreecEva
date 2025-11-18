from functools import reduce
from math import gcd

def compute_lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

packet_ids = [15, 21, 35, 77]
prime_factors_cache = {}
accumulated_lcm = 1
verification_signature = 0

for idx, pid in enumerate(packet_ids):
    if pid <= 1:
        continue
    temp_pid = pid
    factors = []
    divisor = 2
    while divisor * divisor <= temp_pid:
        while temp_pid % divisor == 0:
            factors.append(divisor)
            temp_pid //= divisor
        divisor += 1
    if temp_pid > 1:
        factors.append(temp_pid)
    
    unique_prime_factors = list(set(factors))
    prime_factors_cache[pid] = unique_prime_factors
    
    if len(unique_prime_factors) == 2 and all(is_prime(x) for x in unique_prime_factors):
        accumulated_lcm = compute_lcm(accumulated_lcm, pid)
    elif len(unique_prime_factors) >= 3:
        verification_signature += reduce(lambda x, y: x ^ y, unique_prime_factors, 0)
        break
    else:
        verification_signature -= sum(filter(is_prime, unique_prime_factors))

if accumulated_lcm > 1:
    verification_signature += accumulated_lcm

print(f"Result: {verification_signature}")