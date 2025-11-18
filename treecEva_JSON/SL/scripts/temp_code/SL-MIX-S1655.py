import math
from itertools import combinations

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Prime coordinates in the installation grid
prime_coords = [2, 3, 5, 7, 11, 13]

# Calculate pairwise LCMs of prime coordinates
pairwise_lcms = [lcm(a, b) for a, b in combinations(prime_coords, 2)]

# Determine if coordinate sum is even
coord_sum = sum(prime_coords)
is_sum_even = coord_sum % 2 == 0

# Calculate base energy using geometric properties
base_energy = math.sqrt(sum(x**2 + y**2 for x in prime_coords for y in prime_coords))

# Apply conditional adjustment based on sum parity
adjustment = 1.5 if is_sum_even else 2.0
adjusted_energy = base_energy * adjustment

# Compute activation energy using ternary operator
activation_energy = adjusted_energy if len(pairwise_lcms) > 10 else adjusted_energy * 2

print(f"Result: {int(activation_energy)}")