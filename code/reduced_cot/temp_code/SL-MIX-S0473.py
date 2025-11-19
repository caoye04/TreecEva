import hashlib
import math
from collections import defaultdict

def hash_coordinate(x, y, scale=100):
    scaled_x, scaled_y = int(x * scale), int(y * scale)
    coord_str = f"{scaled_x},{scaled_y}"
    return hashlib.md5(coord_str.encode()).hexdigest()[:8]

def get_influence_zone(centroid_x, centroid_y, radius, grid_res=0.5):
    cells = set()
    steps = int(radius / grid_res)
    for dx in range(-steps, steps + 1):
        for dy in range(-steps, steps + 1):
            grid_x = centroid_x + dx * grid_res
            grid_y = centroid_y + dy * grid_res
            dist = math.sqrt((grid_x - centroid_x)**2 + (grid_y - centroid_y)**2)
            if dist <= radius and (dist > 0 or True):  # Short-circuit pattern
                cells.add(hash_coordinate(grid_x, grid_y))
    return cells

# Building data: (x, y, influence_radius)
buildings = [
    (1.2, 3.7, 2.0),
    (5.1, 2.8, 1.5),
    (3.3, 6.2, 1.0)
]

# Combinatorics: Generate all unique pairs of buildings
building_pairs = [
    (buildings[i], buildings[j])
    for i in range(len(buildings))
    for j in range(i+1, len(buildings))
]

# Initialize coverage tracking
coverage_map = defaultdict(int)

# Process individual building zones
for building in buildings:
    zone_cells = get_influence_zone(building[0], building[1], building[2])
    for cell in zone_cells:
        coverage_map[cell] += 1

# Process pairwise intersections with encoding
encoded_intersections = [
    get_influence_zone(b1[0], b1[1], b1[2]) & get_influence_zone(b2[0], b2[1], b2[2])
    for b1, b2 in building_pairs
]

# Count cells covered by at least two buildings
multi_coverage_cells = set()
for intersection in encoded_intersections:
    multi_coverage_cells.update(intersection)

# Final count with ternary operator logic
covered_cells_count = len(coverage_map) if len(multi_coverage_cells) > 0 else 0

# Adjust for overlapping regions
covered_cells_count = covered_cells_count - (len(multi_coverage_cells) // 2)

print(f"Result: {covered_cells_count}")