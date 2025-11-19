import math

# Define fountain radius and bench distance
fountain_radius = 5
bench_distance = 13

# Calculate areas using geometry
inner_circle_area = math.pi * fountain_radius ** 2
outer_circle_area = math.pi * bench_distance ** 2

# Compute ring area using ternary to ensure positive difference
ring_area = outer_circle_area - inner_circle_area if outer_circle_area > inner_circle_area else 0

print(f"Result: {ring_area}")