import itertools
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

def decode_scaling_factor(metadata_str):
    char_sum = sum(ord(c) for c in metadata_str if c.isalpha())
    digit_product = 1
    has_digits = False
    for c in metadata_str:
        if c.isdigit():
            digit_product *= int(c)
            has_digits = True
    if not has_digits:
        digit_product = 1
    return char_sum * digit_product

survey_zones_vertices = [
    [(0, 0), (4, 0), (4, 3)],
    [(1, 1), (5, 1), (5, 4), (1, 4)],
    [(2, 2), (6, 2), (6, 5)]
]

zone_metadata = ["ZoneA-12", "ZoneB-34", "ZoneC-56"]

all_vertices = list(itertools.chain.from_iterable(survey_zones_vertices))
hull_points = convex_hull(all_vertices)

# Calculate area using Shoelace formula
n = len(hull_points)
area = 0.0
for i in range(n):
    j = (i + 1) % n
    area += hull_points[i][0] * hull_points[j][1]
    area -= hull_points[j][0] * hull_points[i][1]
survey_area = abs(area) / 2.0

scaling_factors = [decode_scaling_factor(meta) for meta in zone_metadata]
total_scaling = sum(scaling_factors)

normalized_survey_area = survey_area * math.log(total_scaling)

print(f"Result: {normalized_survey_area}")