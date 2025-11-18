import heapq
import math

drone_positions = [
    (3, 4, 0),
    (1, 1, 1),
    (0, 5, 2),
    (2, 2, 2),
    (6, 8, 0)
]

# Calculate Euclidean distances from origin
landing_heap = [(math.sqrt(x**2 + y**2 + z**2), (x, y, z)) for x, y, z in drone_positions]
heapq.heapify(landing_heap)

# Process first two landings
for _ in range(2):
    heapq.heappop(landing_heap)

# Get the third drone to land
third_landing_distance, third_drone_position = heapq.heappop(landing_heap)

# Round to nearest integer for clean output
result = round(third_landing_distance)
print(f"Result: {result}")