import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

flour_requirements = [120, 150, 180, 300]
total_recipes = len(flour_requirements)

# Calculate LCM of all requirements to find the minimal package size
optimal_package_size = reduce(lcm, flour_requirements)

print(f"Result: {optimal_package_size}")