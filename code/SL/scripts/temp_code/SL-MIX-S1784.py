import math
from functools import reduce

def quadrant_identifier(x, y):
    if x >= 0 and y >= 0:
        return 1
    elif x < 0 and y >= 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

# Sensor data: list of (x, y) coordinates
sensor_readings = [
    (3.5, 2.1),
    (-1.2, 4.8),
    (-5.6, -3.3),
    (2.7, -1.9),
    (0.0, 0.0),
    (3.5, 2.1),  # Duplicate
    (-1.2, 4.8)   # Duplicate
]

# Step 1: Identify unique quadrants using set operations
quadrant_ids = set(map(lambda point: quadrant_identifier(*point), sensor_readings))

# Step 2: Calculate base coverage score as sum of unique quadrants
base_coverage = sum(quadrant_ids)

# Step 3: Apply geometric transformation based on number of unique quadrants
unique_quadrant_count = len(quadrant_ids)
geometric_factor = math.sqrt(unique_quadrant_count) if unique_quadrant_count > 0 else 0

# Step 4: Compute adjusted score with ternary operator for edge case
adjusted_score = base_coverage * geometric_factor if geometric_factor != 0 else base_coverage

# Step 5: Normalize using functional reduction
normalization_factors = [1.2, 0.8, 1.5]
normalized_score = reduce(lambda acc, factor: acc * factor, normalization_factors, adjusted_score)

# Step 6: Final coverage score calculation with spatial adjustment
spatial_adjustment = 2.0 if unique_quadrant_count >= 3 else 1.0
final_coverage_score = int(normalized_score * spatial_adjustment)

print(f"Result: {final_coverage_score}")