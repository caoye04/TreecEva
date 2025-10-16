from collections import defaultdict
from itertools import combinations
import math

def custom_position_hash(x, y):
    return hash(f"{x:.2f},{y:.2f}") % 1000000

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Sensor data: (sensor_id, [(x,y), (x,y), ...])
sensor_readings = [
    ('LIDAR_01', [(1.5, 2.3), (3.7, 4.1), (2.2, 5.8)]),
    ('RADAR_02', [(1.5, 2.3), (6.1, 3.9), (2.2, 5.8)]),
    ('SONAR_03', [(3.7, 4.1), (7.2, 1.5), (4.4, 6.7)])
]

# Process sensor data
unique_positions = set()
position_frequency = defaultdict(int)
encoded_positions = {}

for sensor_id, positions in sensor_readings:
    for x, y in positions:
        # Round to 2 decimal places for consistency
        x, y = round(x, 2), round(y, 2)
        unique_positions.add((x, y))
        position_frequency[(x, y)] += 1
        encoded_positions[(x, y)] = custom_position_hash(x, y)

# Convert to list for indexing
position_list = list(unique_positions)

# Calculate geometric properties
if len(position_list) >= 2:
    # Find maximum distance between any two points
    max_distance = 0
    for p1, p2 in combinations(position_list, 2):
        dist = euclidean_distance(p1, p2)
        if dist > max_distance:
            max_distance = dist
    
    # Calculate centroid
    centroid_x = sum(p[0] for p in position_list) / len(position_list)
    centroid_y = sum(p[1] for p in position_list) / len(position_list)
    
    # Count positions in each quadrant relative to centroid
    quadrant_counts = [0, 0, 0, 0]  # I, II, III, IV
    for x, y in position_list:
        if x >= centroid_x and y >= centroid_y:
            quadrant_counts[0] += 1
        elif x < centroid_x and y >= centroid_y:
            quadrant_counts[1] += 1
        elif x < centroid_x and y < centroid_y:
            quadrant_counts[2] += 1
        else:  # x >= centroid_x and y < centroid_y
            quadrant_counts[3] += 1
    
    # Combinatorial analysis: count triangles that can be formed
    triangle_count = len(list(combinations(position_list, 3)))
    
    # Security checksum calculation
    frequency_product = 1
    for freq in position_frequency.values():
        frequency_product *= freq
    
    hash_sum = sum(encoded_positions.values())
    
    # Final checksum combines geometric and combinatorial properties
    security_checksum = int((max_distance * 100) + 
                           (triangle_count * 10) + 
                           (sum(quadrant_counts) * 5) + 
                           (frequency_product * 3) + 
                           (hash_sum % 1000))
else:
    security_checksum = 0

print(f"Result: {security_checksum}")