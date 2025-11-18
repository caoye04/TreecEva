import math
from itertools import combinations

def calculate_circle_intersection_area(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d >= r1 + r2:  # Circles don't overlap
        return 0
    if d <= abs(r1 - r2):  # One circle inside another
        return math.pi * min(r1, r2)**2
    
    # General case: partial overlap
    angle1 = math.acos((r1*r1 + d*d - r2*r2) / (2*r1*d))
    angle2 = math.acos((r2*r2 + d*d - r1*r1) / (2*r2*d))
    sector1 = r1*r1 * angle1
    sector2 = r2*r2 * angle2
    triangle1 = r1*r1 * math.sin(angle1) * 0.5
    triangle2 = r2*r2 * math.sin(angle2) * 0.5
    return sector1 + sector2 - triangle1 - triangle2

# Sensor positions and detection radii
sensor_network = [
    {'pos': (0, 0), 'radius': 5},
    {'pos': (4, 0), 'radius': 3},
    {'pos': (0, 3), 'radius': 4},
    {'pos': (3, 4), 'radius': 2}
]

coverage_threshold = 5.0
optimal_coverage_count = 0

for s1, s2 in combinations(sensor_network, 2):
    x1, y1 = s1['pos']
    r1 = s1['radius']
    x2, y2 = s2['pos']
    r2 = s2['radius']
    
    intersection_area = calculate_circle_intersection_area(x1, y1, r1, x2, y2, r2)
    if intersection_area >= coverage_threshold:
        optimal_coverage_count += 1
    elif intersection_area > 0:
        # Adjust count based on partial coverage
        optimal_coverage_count += int(intersection_area // 2)

# Apply correction factor based on network density
network_density = len([s for s in sensor_network if s['radius'] > 3])
optimal_coverage_count *= network_density if network_density > 0 else 1

print(f"Result: {optimal_coverage_count}")