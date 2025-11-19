from math import gcd
from itertools import combinations

def validate_triangle(pods):
    a, b, c = sorted(pods)
    # Check if indices form a valid triangle in circular arrangement
    return (b - a) + (c - b) + (a + len(pods) - c) == len(pods)

# Number of pods arranged in a circle
N = 7
pods = list(range(N))
valid_formations_count = 0

# Generate all possible triangles
for combo in combinations(pods, 3):
    # Apply geometric validation
    if validate_triangle(combo):
        # Count only if at least one pod has even index
        if any(index % 2 == 0 for index in combo):
            valid_formations_count += 1

# Account for rotational symmetry by dividing by N
valid_formations_count //= N

print(f"Result: {valid_formations_count}")