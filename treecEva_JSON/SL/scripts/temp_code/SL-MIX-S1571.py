import math
from itertools import combinations
def calculate_centroid(points):
    x_coords, y_coords = zip(*points)
    return (sum(x_coords) / len(points), sum(y_coords) / len(points))

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_variance(coords):
    mean = sum(coords) / len(coords)
    return sum((x - mean) ** 2 for x in coords) / len(coords)

# Sensor candidate locations
sensor_locations = [(2, 3), (5, 7), (8, 1), (1, 9), (6, 4)]
coverage_radii = [1.5, 2.0, 1.2, 2.5, 1.8]

# Calculate centroid of all sensor locations
network_centroid = calculate_centroid(sensor_locations)

# Find sensor pairs within 5 units of each other
adjacent_pairs = []
for pair in combinations(range(len(sensor_locations)), 2):
    if euclidean_distance(sensor_locations[pair[0]], sensor_locations[pair[1]]) < 5.0:
        adjacent_pairs.append(pair)

# Compute variance of x-coordinates and y-coordinates
x_coords, y_coords = zip(*sensor_locations)
x_variance = compute_variance(x_coords)
y_variance = compute_variance(y_coords)

# Determine optimal coverage score
is_well_distributed = len(adjacent_pairs) > 3 and x_variance > 5.0 and y_variance > 5.0
max_radius = max(coverage_radii) if coverage_radii else 0
optimal_coverage_score = round(max_radius * len(adjacent_pairs)) if is_well_distributed else 0

print(f"Result: {optimal_coverage_score}")