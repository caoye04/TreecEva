import re
from functools import reduce
from collections import defaultdict

def calculate_flatness_variance(elevations):
    mean = sum(elevations) / len(elevations)
    return sum((x - mean) ** 2 for x in elevations) / len(elevations)

def is_accessible(terrain_type):
    inaccessible_types = {'water', 'lava', 'cliff'}
    return terrain_type not in inaccessible_types

def proximity_bonus(coords, waypoints):
    min_dist = float('inf')
    for wp in waypoints:
        dist = ((coords[0] - wp[0]) ** 2 + (coords[1] - wp[1]) ** 2) ** 0.5
        if dist < min_dist:
            min_dist = dist
    return max(0, 10 - min_dist)  # Bonus decreases with distance

terrain_data = [
    {'id': 'A1', 'elevations': [100, 102, 99, 101, 100], 'type': 'grass', 'coords': (10, 20)},
    {'id': 'B2', 'elevations': [150, 200, 175, 180, 220], 'type': 'rock', 'coords': (30, 40)},
    {'id': 'C3', 'elevations': [105, 104, 106, 103, 105], 'type': 'sand', 'coords': (50, 60)},
    {'id': 'D4', 'elevations': [90, 95, 92, 94, 91], 'type': 'water', 'coords': (70, 80)}
]

waypoints = [(15, 25), (35, 45), (55, 65)]
scores = defaultdict(float)

for region in terrain_data:
    region_id = region['id']
    if not is_accessible(region['type']):
        continue
    flatness = calculate_flatness_variance(region['elevations'])
    bonus = proximity_bonus(region['coords'], waypoints)
    scores[region_id] = max(0, 100 - flatness) + bonus

valid_regions = [k for k in scores if scores[k] > 50]
pattern_matched_regions = [r for r in valid_regions if re.match(r'^[A-Z]\d$', r)]

if pattern_matched_regions and len(pattern_matched_regions) >= 1:
    base_score = reduce(lambda a, b: a + b, [scores[r] for r in pattern_matched_regions], 0)
    optimal_landing_score = int(base_score * 1.5) % 1000
else:
    optimal_landing_score = 0

print(f"Result: {optimal_landing_score}")