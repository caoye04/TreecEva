import math
from collections import defaultdict

def calculate_sensor_density_grid(sensor_coords, grid_size=10):
    density_map = defaultdict(int)
    for x, y in sensor_coords:
        grid_x, grid_y = x // grid_size, y // grid_size
        density_map[(grid_x, grid_y)] += 1
    return density_map

def compute_coverage_area(density_map, influence_radius=5):
    total_area = 0
    for (gx, gy), count in density_map.items():
        # Each sensor contributes a circular area of influence
        sensor_area = math.pi * (influence_radius ** 2)
        # Overlapping areas are counted once but weighted by sensor count
        total_area += sensor_area * min(count, 3)  # Cap at 3 for normalization
    return total_area

def find_central_grid(density_map):
    max_density = max(density_map.values())
    central_grids = [key for key, value in density_map.items() if value == max_density]
    # Return the first central grid's coordinates as representative
    return central_grids[0] if central_grids else (0, 0)

# Simulated sensor coordinates in a 100x100 monitoring area
sensor_locations = [
    (12, 15), (18, 22), (25, 30), (12, 18), (45, 50),
    (55, 52), (58, 48), (70, 75), (72, 78), (75, 70),
    (13, 16), (19, 23), (47, 51), (56, 53), (71, 76)
]

# Process sensor data
grid_density = calculate_sensor_density_grid(sensor_locations)
central_location = find_central_grid(grid_density)
coverage_area = compute_coverage_area(grid_density)

# Calculate optimal coverage score based on density and area
optimal_coverage_score = int(coverage_area * (grid_density[central_location] / len(sensor_locations)) * 100)

print(f"Result: {optimal_coverage_score}")