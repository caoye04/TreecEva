import re
from collections import defaultdict
from math import gcd
from itertools import permutations

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# Encoded message segments
segments = ['A1B2C3', 'D4E5F6', 'G7H8I9']
char_map = defaultdict(int)

# Process each segment
for segment in segments:
    # Extract numbers using regex
    numbers = list(map(int, re.findall(r'\d', segment)))
    # Extract characters using regex
    characters = re.findall(r'[A-Z]', segment)
    
    # For each character, add the LCM of extracted numbers to its map value
    for char in characters:
        char_map[char] += lcm(numbers[0], numbers[-1])

# Generate permutations of the map's values
values = list(char_map.values())
perms = list(permutations(values, 3))

# Calculate checksum from permutations
checksum = 0
for perm in perms:
    # Only consider permutations where the first element is the largest
    if perm[0] >= perm[1] and perm[0] >= perm[2]:
        checksum += perm[0] * perm[1] + perm[2]

# Apply final transformation using prime factors
final_value = sum(prime_factors(checksum))
checksum = checksum ^ final_value  # XOR with sum of its prime factors

print(f"Result: {checksum}")