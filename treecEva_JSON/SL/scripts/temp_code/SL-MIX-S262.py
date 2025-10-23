import math
from heapq import heappush, heappop

class Sensor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

def circle_intersection_area(s1, s2):
    d = math.sqrt((s1.x - s2.x)**2 + (s1.y - s2.y)**2)
    if d >= s1.radius + s2.radius:
        return 0
    if d <= abs(s1.radius - s2.radius):
        return min(math.pi * s1.radius**2, math.pi * s2.radius**2)
    
    r1, r2 = s1.radius, s2.radius
    alpha = math.acos((r1*r1 + d*d - r2*r2) / (2*r1*d))
    beta = math.acos((r2*r2 + d*d - r1*r1) / (2*r2*d))
    sector_area_1 = alpha * r1*r1
    sector_area_2 = beta * r2*r2
    triangle_area_1 = 0.5 * r1*r1 * math.sin(2*alpha)
    triangle_area_2 = 0.5 * r2*r2 * math.sin(2*beta)
    return (sector_area_1 - triangle_area_1) + (sector_area_2 - triangle_area_2)

def binary_search_closest(arr, target):
    left, right = 0, len(arr) - 1
    closest = arr[0]
    while left <= right:
        mid = (left + right) // 2
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return closest

# Main computation
sensors = [
    Sensor(0, 0, 5),
    Sensor(8, 0, 3),
    Sensor(4, 4, 4),
    Sensor(2, -3, 2)
]

overlap_heap = []
covered_areas = set()

for i in range(len(sensors)):
    for j in range(i+1, len(sensors)):
        area = circle_intersection_area(sensors[i], sensors[j])
        if area > 0:
            heappush(overlap_heap, -area)  # Max heap using negative values
            covered_areas.add(round(area, 5))

unique_overlaps = list(covered_areas)
sorted_unique_overlaps = sorted(unique_overlaps)
target_area = binary_search_closest(sorted_unique_overlaps, 3.5)

# Execution point Y
total_exposed_perimeter = 0
for sensor in sensors:
    total_exposed_perimeter += sensor.perimeter()

while overlap_heap:
    largest_overlap = -heappop(overlap_heap)
    if round(largest_overlap, 5) == target_area:
        total_exposed_perimeter -= largest_overlap * 0.75

print(f"Result: {round(total_exposed_perimeter, 2)}")