import re
from functools import reduce

def project_coordinate(coord):
    x, y = coord
    return (x * 2 - y, y + x // 3)

def is_valid_zone(zone_id):
    return bool(re.match(r'^Z[1-9][0-9]*$', zone_id))

def calculate_density(points):
    return sum(p[0] + p[1] for p in points) // len(points) if points else 0

# Initial data
survey_zones = {
    'Z1': [(3, 5), (7, 2)],
    'A2': [(1, 1)],
    'Z3': [(4, 4), (6, 8), (2, 9)],
    'Z10': [(0, 0), (5, 5)]
}

# Processing pipeline
valid_zone_ids = list(filter(is_valid_zone, survey_zones.keys()))
transformed_zones = 0

for zone_id in valid_zone_ids:
    raw_points = survey_zones[zone_id]
    projected_points = list(map(project_coordinate, raw_points))
    density = calculate_density(projected_points)
    if density > 5:
        transformed_zones += 1
    elif density == 0:
        break

print(f"Result: {transformed_zones}")