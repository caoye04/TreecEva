import math
import re
from collections import deque
from functools import reduce
from itertools import product

def calculate_surface_roughness(elevation_grid, row, col, radius=2):
    rows, cols = len(elevation_grid), len(elevation_grid[0])
    neighbors = []
    for dr, dc in product(range(-radius, radius+1), repeat=2):
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            neighbors.append(elevation_grid[r][c])
    if len(neighbors) < 2:
        return float('inf')
    mean = sum(neighbors) / len(neighbors)
    variance = sum((x - mean) ** 2 for x in neighbors) / len(neighbors)
    return math.sqrt(variance)

def is_valid_landing_zone(elevation_grid, row, col):
    pattern = r'^[0-9]{3}$'  # Elevation values should be 3-digit numbers
    elevation_str = str(elevation_grid[row][col])
    if not re.match(pattern, elevation_str):
        return False
    # Check if all adjacent cells have valid elevation values
    rows, cols = len(elevation_grid), len(elevation_grid[0])
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            if not re.match(pattern, str(elevation_grid[r][c])):
                return False
    return True

def compute_landing_geometry_score(elevation_grid, row, col):
    # Calculate a geometric score based on relative elevations
    center_elev = elevation_grid[row][col]
    rows, cols = len(elevation_grid), len(elevation_grid[0])
    score = 0
    for dr, dc in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            neighbor_elev = elevation_grid[r][c]
            # Calculate slope-like metric
            distance = math.sqrt(dr**2 + dc**2)
            elevation_diff = abs(center_elev - neighbor_elev)
            if distance > 0:
                slope = elevation_diff / distance
                score += slope
    return score / 8.0

elevation_map = [
    [120, 125, 130, 135, 140],
    [115, 118, 122, 128, 138],
    [110, 114, 119, 125, 135],
    [108, 112, 117, 123, 130],
    [105, 110, 115, 120, 125]
]

# Process grid to find optimal landing zone
rows, cols = len(elevation_map), len(elevation_map[0])
max_score = -float('inf')
optimal_landing_score = 0

for i in range(rows):
    for j in range(cols):
        if is_valid_landing_zone(elevation_map, i, j):
            roughness = calculate_surface_roughness(elevation_map, i, j)
            geometry_score = compute_landing_geometry_score(elevation_map, i, j)
            # Combine metrics with weights
            combined_score = 0.6 * (1 / (1 + roughness)) + 0.4 * (1 / (1 + geometry_score))
            if combined_score > max_score:
                max_score = combined_score
                # Hash the position for uniqueness
                position_hash = hash((i, j)) % 1000
                optimal_landing_score = int(combined_score * 1000) + position_hash

print(f"Result: {optimal_landing_score}")