from collections import defaultdict
from math import sqrt

# Route stop coordinates: (x, y) positions
route_stops = {
    'A': [(0, 0), (2, 2), (4, 1)],
    'B': [(1, 1), (3, 3), (5, 2)],
    'C': [(0, 2), (2, 4), (4, 3)]
}

# Calculate bounding box area for each route
route_areas = {}
for route, stops in route_stops.items():
    xs, ys = zip(*stops)
    area = (max(xs) - min(xs)) * (max(ys) - min(ys))
    route_areas[route] = area if area > 0 else 1  # Avoid zero area

# Count how many routes include each unique stop
stop_frequency = defaultdict(int)
unique_stops = set()
for stops in route_stops.values():
    stops_set = set(stops)
    unique_stops.update(stops_set)
    for stop in stops_set:
        stop_frequency[stop] += 1

# Compute spatial density as inverse of mean distance to centroid
route_density = {}
for route, stops in route_stops.items():
    n = len(stops)
    cx = sum(x for x, y in stops) / n
    cy = sum(y for x, y in stops) / n
    mean_dist = sum(sqrt((x - cx)**2 + (y - cy)**2) for x, y in stops) / n
    route_density[route] = 1 / mean_dist if mean_dist > 0 else 1

# Efficiency combines area and density, adjusted by stop uniqueness
base_efficiency = {
    route: route_areas[route] * route_density[route]
    for route in route_stops
}

# Adjustment factor based on stop redundancy
adjustment_factors = {
    route: sum(1 / stop_frequency[stop] for stop in set(stops)) / len(set(stops))
    for route, stops in route_stops.items()
}

# Final efficiency score with ternary operator for thresholding
final_efficiency_score = sum(
    base_efficiency[route] * adjustment_factors[route] * (1.5 if len(stops) > 2 else 1.0)
    for route, stops in route_stops.items()
)

print(f"Result: {round(final_efficiency_score, 2)}")