import math
from functools import reduce

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

drone_waypoints = [(0, 0), (3, 4), (7, 1), (2, 6), (5, 5)]
terrain_factors = [1.0, 1.2, 0.9, 1.1]

segment_distances = [
    calculate_distance(drone_waypoints[i], drone_waypoints[i+1]) 
    for i in range(len(drone_waypoints)-1)
]

total_distance = sum(segment_distances)
avg_distance_per_segment = total_distance / len(segment_distances) if segment_distances else 0

adjusted_terrain_impact = reduce(lambda acc, tf: acc * tf, terrain_factors, 1.0)

is_long_route = total_distance > 15
complexity_bonus = 1.5 if is_long_route and len(segment_distances) > 3 else 1.0

final_efficiency_score = (
    avg_distance_per_segment * adjusted_terrain_impact * complexity_bonus
) if avg_distance_per_segment > 0 else 0

print(f"Result: {round(final_efficiency_score, 2)}")