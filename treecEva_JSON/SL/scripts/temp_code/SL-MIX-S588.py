from math import gcd

# Prime numbers for RSA-like calculation
p, q = 11, 17
n = p * q

# Using list comprehension to find numbers coprime to n
coprime_numbers = [i for i in range(1, n) if gcd(i, n) == 1]
coprime_count = len(coprime_numbers)

print(f"Result: {coprime_count}")