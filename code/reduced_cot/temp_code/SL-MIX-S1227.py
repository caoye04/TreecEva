import math
from itertools import combinations
distance = lambda p1, p2: math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

class Sensor:
    def __init__(self, x, y, radius):
        self.position = (x, y)
        self.radius = radius

sensors = [Sensor(0, 0, 5), Sensor(3, 4, 3), Sensor(6, 0, 4), Sensor(2, 2, 2)]
total_overlap = 0
resource_base = 100

for s1, s2 in combinations(sensors, 2):
    d = distance(s1.position, s2.position)
    if d < (s1.radius + s2.radius) and (s1.radius > 2 or s2.radius > 2):
        overlap_area = max(0, min(s1.radius, s2.radius) * (s1.radius + s2.radius - d))
        total_overlap += int(overlap_area)

has_critical_overlap = total_overlap > 20 and any(s.radius > 4 for s in sensors)
adjusted_base = resource_base - (total_overlap if has_critical_overlap else total_overlap // 2)
optimized_resources = adjusted_base + (10 if has_critical_overlap else 0)

print(f"Result: {optimized_resources}")