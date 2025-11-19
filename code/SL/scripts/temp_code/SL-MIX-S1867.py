import math

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

regions = [
    [(0, 0), (4, 0), (4, 3), (0, 3)],
    [(1, 1), (3, 1), (3, 2), (1, 2)],
    [(2, 2), (5, 2), (5, 4), (2, 4)]
]

scaling_factor = 2.0
adjustment_lambda = lambda area, factor: area * factor if area > 5 else area + factor

coverage_grid = [[0.0 for _ in range(6)] for _ in range(6)]

total_coverage = 0.0
for region_idx in range(len(regions)):
    raw_area = calculate_polygon_area(regions[region_idx])
    adjusted_area = adjustment_lambda(raw_area, scaling_factor)
    
    min_x = min(v[0] for v in regions[region_idx])
    max_x = max(v[0] for v in regions[region_idx])
    min_y = min(v[1] for v in regions[region_idx])
    max_y = max(v[1] for v in regions[region_idx])
    
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if coverage_grid[x][y] == 0.0:
                coverage_grid[x][y] = adjusted_area * 0.1
            total_coverage += coverage_grid[x][y]

total_coverage = round(total_coverage, 2)
print(f"Result: {total_coverage}")