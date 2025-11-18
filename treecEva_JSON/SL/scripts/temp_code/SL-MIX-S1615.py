from collections import defaultdict
import itertools
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

# Initialize variables
quadratic_residues = defaultdict(list)
primes_under_30 = [p for p in range(2, 30) if is_prime(p)]
encryption_key = 0

# Compute quadratic residues for each prime
for prime in primes_under_30:
    for i in range(prime):
        residue = (i * i) % prime
        if residue not in quadratic_residues[prime]:
            quadratic_residues[prime].append(residue)

# Nested loop processing
for prime, residues in quadratic_residues.items():
    combinations_count = 0
    for r1, r2 in itertools.combinations(residues, 2):
        if (r1 + r2) % prime == 1:
            combinations_count += 1
    if combinations_count > 0:
        # Update encryption key using LCM
        encryption_key = lcm(encryption_key, prime * combinations_count)

# Final adjustment
if encryption_key % 2 == 0:
    encryption_key >>= 2  # Right shift by 2 (equivalent to integer division by 4)
else:
    encryption_key ^= 0xF  # XOR with 15

print(f"Result: {encryption_key}")