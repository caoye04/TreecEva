import heapq
from collections import namedtuple

# Define a sensor as a named tuple with x and y coordinates
Sensor = namedtuple('Sensor', ['x', 'y'])

# Initial sensor network
sensors = [
    Sensor(2, 3),
    Sensor(5, 7),
    Sensor(1, 8),
    Sensor(9, 2),
    Sensor(4, 4)
]

# Function to calculate Euclidean distance squared between two sensors
def distance_squared(s1, s2):
    return (s1.x - s2.x)**2 + (s1.y - s2.y)**2

# Initialize a min-heap with distances between all pairs of sensors
heap = []
for i in range(len(sensors)):
    for j in range(i + 1, len(sensors)):
        dist_sq = distance_squared(sensors[i], sensors[j])
        heapq.heappush(heap, dist_sq)

# Process sensor updates
new_sensors = [
    Sensor(0, 0),
    Sensor(10, 10)
]

for sensor in new_sensors:
    sensors.append(sensor)
    # Add new distances to heap
    for i in range(len(sensors) - 1):
        dist_sq = distance_squared(sensors[i], sensor)
        heapq.heappush(heap, dist_sq)

# Remove outdated distances from heap (simplified simulation)
# In a real implementation, we would track valid pairs
# Here we just pop a few to simulate maintenance
for _ in range(3):
    if heap:
        heapq.heappop(heap)

# The closest distance is the smallest value in the heap
closest_distance = heapq.heappop(heap)

print(f"Result: {closest_distance}")