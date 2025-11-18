import math
from functools import reduce

def transform_validator(coord_matrix):
    return all(map(lambda x: abs(x) <= 1000.0, coord_matrix))

coordinates = [2.5, -3.7, 8.1, -0.4]
scale_factors = [1.2, 0.8, 1.5, 0.9]

# Apply logarithmic scaling
log_scaled = [math.log(abs(x)) if x != 0 else 0 for x in coordinates]

# Apply scale factors with short-circuit evaluation
scaled_coordinates = [
    coord * factor if abs(coord) > 1.0 and factor > 1.0 else coord
    for coord, factor in zip(coordinates, scale_factors)
]

# Validate transformed coordinates
is_valid = transform_validator(scaled_coordinates)

# Calculate adjustment factor using ternary operator and exponentiation
adjustment_base = 2.0 if is_valid else 1.5
composite_exponent = reduce(lambda a, b: a + b, log_scaled, 0) / len(log_scaled)
base_adjustment = math.pow(adjustment_base, composite_exponent)

# Final adjustment calculation with set operations
significant_coords = {round(x, 1) for x in scaled_coordinates if abs(x) > 2.0}
target_set = frozenset({2.5, -3.7, 8.1})
intersection_count = len(significant_coords & target_set)

final_adjustment_factor = base_adjustment * (intersection_count if intersection_count > 0 else 1)

print(f"Result: {final_adjustment_factor}")