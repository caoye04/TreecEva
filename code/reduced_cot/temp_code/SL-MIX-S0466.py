import math
from collections import defaultdict

class SensorNode:
    def __init__(self, x, y, next_node=None):
        self.x = x
        self.y = y
        self.next = next_node

def compute_spatial_hash(x, y, grid_size=10):
    """Hash function for spatial coordinates"""
    return (int(x) // grid_size, int(y) // grid_size)

def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Sensor data as linked lists
sensor_a = SensorNode(15.2, 22.7, SensorNode(16.8, 23.1, SensorNode(25.3, 30.5)))
sensor_b = SensorNode(14.9, 22.3, SensorNode(35.2, 40.1))
sensor_c = SensorNode(16.1, 23.5, SensorNode(24.8, 31.2, SensorNode(34.7, 39.8)))

# Group sensors
sensors = [sensor_a, sensor_b, sensor_c]

# Spatial clustering using hash maps
cluster_map = defaultdict(list)
proximity_threshold = 3.0

for i, sensor_head in enumerate(sensors):
    current = sensor_head
    while current:
        hash_key = compute_spatial_hash(current.x, current.y)
        point = (current.x, current.y, i)  # Include sensor ID
        
        # Check if any existing point in cluster is within proximity
        merged = False
        for existing_hash, points in cluster_map.items():
            for existing_point in points:
                if (distance((point[0], point[1]), (existing_point[0], existing_point[1])) < proximity_threshold and
                    existing_hash == hash_key):
                    cluster_map[existing_hash].append(point)
                    merged = True
                    break
            if merged:
                break
        
        if not merged:
            cluster_map[hash_key].append(point)
            
        current = current.next

# Count clusters with points from multiple sensors
cluster_count = 0
for points in cluster_map.values():
    sensor_ids = set(p[2] for p in points)
    if len(sensor_ids) > 1:
        cluster_count += 1
        
# Apply geometric correction factor
if cluster_count > 0:
    correction_factor = math.ceil(math.sqrt(cluster_count))
    cluster_count = cluster_count * correction_factor
else:
    cluster_count = -1

print(f"Result: {cluster_count}")