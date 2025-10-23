import itertools
from collections import defaultdict

# Route data: list of stops with efficiency ratings
routes_data = [
    [('A', 8.5), ('B', 7.2), ('C', 9.1)],
    [('B', 7.2), ('D', 6.8), ('E', 8.0)],
    [('A', 8.5), ('C', 9.1), ('E', 8.0), ('F', 7.5)]
]

# Count frequency of each stop across all routes
stop_frequency = defaultdict(int)
for route in routes_data:
    for stop, _ in route:
        stop_frequency[stop] += 1

# Calculate weighted efficiency for each route
route_scores = []
for route in routes_data:
    weighted_sum = 0
    for stop, efficiency in route:
        weight = stop_frequency[stop]
        weighted_sum += efficiency * weight
    route_scores.append(weighted_sum)

# Compute final efficiency score using combinatorics
final_efficiency_score = 0
for combo in itertools.combinations(route_scores, 2):
    final_efficiency_score += combo[0] * combo[1]

print(f"Result: {final_efficiency_score}")