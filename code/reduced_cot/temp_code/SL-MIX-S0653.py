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

def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

sensor_readings = {
    'S1': [(0, 0), (4, 0), (4, 4), (0, 4)],
    'S2': [(1, 1), (3, 1), (2, 3)],
    'S3': [(0, 0), (5, 0), (5, 5), (0, 5), (2, 2)],
    'S4': [(10, 10), (12, 10), (12, 12), (10, 12)],
    'S5': [(0, 0), (1, 0), (0, 1)]
}

validated_sensors = 0
for sensor_id, points in sensor_readings.items():
    hull = convex_hull(points)
    area = polygon_area(hull)
    is_convex = len(hull) == len(points)
    sufficient_area = area > 10
    if is_convex and sufficient_area:
        validated_sensors += 1

print(f"Result: {validated_sensors}")