import math
from itertools import combinations

# Sensor coordinates and their effective ranges
sensor_data = {
    'A': (0.0, 0.0, 1.5),
    'B': (2.0, 1.0, 1.2),
    'C': (1.0, 3.0, 1.8),
    'D': (4.0, 2.0, 1.0),
    'E': (3.0, 4.0, 1.6)
}

def calculate_overlap_area(sensor1, sensor2):
    x1, y1, r1 = sensor_data[sensor1]
    x2, y2, r2 = sensor_data[sensor2]
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if distance >= r1 + r2:
        return 0.0
    elif distance <= abs(r1 - r2):
        return math.pi * min(r1, r2)**2
    else:
        r1_sq, r2_sq, d_sq = r1**2, r2**2, distance**2
        part1 = r1_sq * math.acos((d_sq + r1_sq - r2_sq) / (2 * distance * r1))
        part2 = r2_sq * math.acos((d_sq + r2_sq - r1_sq) / (2 * distance * r2))
        part3 = 0.5 * math.sqrt((-distance + r1 + r2) * (distance + r1 - r2) * (distance - r1 + r2) * (distance + r1 + r2))
        return part1 + part2 - part3

coverage_map = {}
for s1, s2 in combinations(sensor_data.keys(), 2):
    overlap = calculate_overlap_area(s1, s2)
    if s1 not in coverage_map:
        coverage_map[s1] = 0.0
    if s2 not in coverage_map:
        coverage_map[s2] = 0.0
    coverage_map[s1] += overlap
    coverage_map[s2] += overlap

optimal_stations = frozenset([station for station, overlap in coverage_map.items() if overlap > 2.0])
optimal_stations_count = len(optimal_stations)
print(f"Result: {optimal_stations_count}")