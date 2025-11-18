from collections import defaultdict
import math

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area

# Vessel trajectory data
polar_surveyor_positions = [
    (1, 2), (-3, 4), (2, -1), (-2, -3), (0, 0),
    (5, 1), (-1, -2), (3, 3), (-4, -1), (1, -4)
]

# Process positions
visited_coordinates = frozenset(polar_surveyor_positions)
quadrant_visits = set()

for x, y in visited_coordinates:
    if x > 0 and y >= 0:
        quadrant = 1
    elif x <= 0 and y > 0:
        quadrant = 2
    elif x < 0 and y <= 0:
        quadrant = 3
    else:  # x >= 0 and y < 0
        quadrant = 4
    quadrant_visits.add(quadrant)

unique_quadrants_count = len(quadrant_visits)
hull_vertices = convex_hull(list(visited_coordinates))
safety_perimeter_area = calculate_polygon_area(hull_vertices)

# Communication range factor calculation
if unique_quadrants_count > 0:
    communication_range_factor = int(safety_perimeter_area / unique_quadrants_count)
else:
    communication_range_factor = 0

print(f"Result: {communication_range_factor}")