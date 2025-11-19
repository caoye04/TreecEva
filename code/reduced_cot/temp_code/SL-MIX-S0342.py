import math
from collections import deque

def triangle_area(a, b, c):
    # Using Heron's formula
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Initial mesh stack with triangle side lengths
mesh_stack = deque([
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17)
])

# Transformation operations
scale_factor = 2
area_multiplier = lambda x: x * scale_factor ** 2

# Process mesh transformations
processed_areas = []
while mesh_stack:
    sides = mesh_stack.pop()
    base_area = triangle_area(*sides)
    transformed_area = area_multiplier(base_area)
    processed_areas.append(transformed_area)

# Apply combinatorial aggregation
from itertools import combinations
aggregated_values = []
for combo in combinations(processed_areas, 2):
    aggregated_values.append(sum(combo) * math.log(sum(combo), 2))

# Calculate final surface area using matrix operations
import numpy as np
area_matrix = np.array(aggregated_values).reshape(3, 1)
weight_matrix = np.array([[1, -1, 2]])
final_surface_area = np.dot(weight_matrix, area_matrix)[0]

print(f"Result: {final_surface_area}")