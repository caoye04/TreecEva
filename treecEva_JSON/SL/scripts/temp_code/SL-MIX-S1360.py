from collections import namedtuple
import math

# Define a position record using namedtuple
Position = namedtuple('Position', ['x', 'y', 'timestamp'])

# Robot movement log
movement_log = [
    Position(x=3, y=4, timestamp=1),
    Position(x=-1, y=5, timestamp=2),
    Position(x=0, y=-2, timestamp=3),
    Position(x=6, y=-3, timestamp=4),
    Position(x=-4, y=0, timestamp=5)
]

# Calculate Euclidean distance from origin for each position
distances = [math.sqrt(pos.x**2 + pos.y**2) for pos in movement_log]

# Sort distances in ascending order
sorted_distances = sorted(distances)

# Compute the area of triangles formed by consecutive positions (treated as vectors from origin)
triangle_areas = []
for i in range(len(movement_log) - 2):
    p1, p2, p3 = movement_log[i], movement_log[i+1], movement_log[i+2]
    # Using the cross product formula for area of triangle from three points
    area = abs(p1.x*(p2.y - p3.y) + p2.x*(p3.y - p1.y) + p3.x*(p1.y - p2.y)) / 2
    triangle_areas.append(area)

# Sum of sorted distances multiplied by the number of unique triangle areas
geometric_factor = sum(sorted_distances) * len(set(triangle_areas))

# Efficiency score is defined as the geometric factor divided by the maximum distance
max_distance = max(sorted_distances)
efficiency_score = geometric_factor / max_distance if max_distance != 0 else 0

print(f"Result: {efficiency_score}")