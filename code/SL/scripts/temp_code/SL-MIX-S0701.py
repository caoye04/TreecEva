from math import gcd
from collections import defaultdict

def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# Encoded waypoint distances
waypoint_distances = [84, 126, 180, 210]

# String-encoded angles for rotation (in degrees, as strings)
rotation_angles = ['45', '90', '135', '180']

# Calculate unique prime factors for each distance
prime_factor_sets = [prime_factors(dist) for dist in waypoint_distances]

# Flatten all prime factors into a single set of unique values
unique_primes = set().union(*prime_factor_sets)

# Sum of unique prime factors
prime_sum = sum(unique_primes)

# Convert rotation angles to integers and calculate their LCM
angle_values = [int(angle) for angle in rotation_angles]
angle_lcm = angle_values[0]
for angle in angle_values[1:]:
    angle_lcm = lcm(angle_lcm, angle)

# Apply geometric transformation: rotate coordinate by angle_lcm degrees
# For simplification, we use a discrete rotation model where
# every 90 degrees rotates a coordinate point (x,y) around origin
normalized_rotation = (angle_lcm // 90) % 4

# Base coordinate derived from prime sum
base_coordinate = prime_sum

# Apply rotation effect (simplified model)
if normalized_rotation == 0:
    final_cache_coordinate = base_coordinate
elif normalized_rotation == 1:
    final_cache_coordinate = -base_coordinate
elif normalized_rotation == 2:
    final_cache_coordinate = base_coordinate * -1
else:  # normalized_rotation == 3
    final_cache_coordinate = base_coordinate

print(f'Result: {final_cache_coordinate}')