from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

tokens = ['3', '+', '5', '*', '7', '-', '2']
values = [int(t) for t in tokens if t.isdigit()]

# Compute initial checksum as product of first two primes found
checksum = 2 * 3

# For each pair of consecutive values, update checksum using LCM and addition
for i in range(len(values) - 1):
    current_lcm = lcm(values[i], values[i+1])
    checksum += current_lcm

# Final adjustment: subtract GCD of all values from checksum
final_gcd = reduce(gcd, values)
checksum -= final_gcd

print(f"Result: {checksum}")