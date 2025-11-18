import math
from itertools import combinations

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate base coordinates using modular arithmetic
base_coords = [(i**2 % 17, (i*3 + 5) % 13) for i in range(1, 21)]

# Filter coordinates within a circular boundary of radius 8 centered at (8, 6)
filtered_coords = [
    coord for coord in base_coords 
    if calculate_distance(coord, (8, 6)) <= 8
]

# Find all unique pairs of coordinates
coord_pairs = list(combinations(filtered_coords, 2))

# Calculate distances for each pair and find those within a specific modular class
valid_distances = [
    calculate_distance(pair[0], pair[1]) 
    for pair in coord_pairs 
    if int(calculate_distance(pair[0], pair[1])) % 7 == 3
]

# Compute master_key from valid distances
master_key = sum(
    int(dist) * ((idx + 1) ** 2) 
    for idx, dist in enumerate(valid_distances)
) % 1000

print(f"Result: {master_key}")