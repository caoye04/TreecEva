import math
from functools import reduce

def normalize_coordinates(coords):
    if not coords:
        return []
    mean_x = sum(c[0] for c in coords) / len(coords)
    mean_y = sum(c[1] for c in coords) / len(coords)
    return [(round(x - mean_x, 2), round(y - mean_y, 2)) for x, y in coords]

def is_outlier(coord, threshold=2.0):
    return abs(coord[0]) > threshold or abs(coord[1]) > threshold

def compute_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Sensor data: list of (x,y) tuples
sensor_readings = [
    (10.5, 20.3),
    (11.2, 19.8),
    (15.0, 25.1),  # Outlier
    (9.8, 21.0),
    (10.1, 19.9),
    (10.3, 20.5)
]

# Step 1: Normalize coordinates
normalized_data = normalize_coordinates(sensor_readings)

# Step 2: Filter outliers using short-circuit evaluation
filtered_data = [point for point in normalized_data if not (abs(point[0]) > 2.0 or abs(point[1]) > 2.0)]

# Step 3: Compute centroid of filtered data
if filtered_data:  # Short-circuit protection
    centroid_x = sum(p[0] for p in filtered_data) / len(filtered_data)
    centroid_y = sum(p[1] for p in filtered_data) / len(filtered_data)
    centroid = (round(centroid_x, 3), round(centroid_y, 3))
else:
    centroid = (0.0, 0.0)

# Step 4: Calculate distances from centroid and find maximum
distances = [compute_distance(centroid, point) for point in filtered_data]
max_distance = max(distances) if distances else 0.0

# Step 5: Convert max_distance to integer for bitwise operations
scaled_distance = int(max_distance * 1000)  # Scale to preserve precision

# Step 6: Generate checksum using bitwise operations on coordinate pairs
checksum_components = []
for x, y in filtered_data:
    # Scale and convert to integers
    ix = int(x * 100) & 0xFF  # Mask to byte size
    iy = int(y * 100) & 0xFF  # Mask to byte size
    # Combine using XOR and shift operations
    component = ((ix << 4) | (iy >> 4)) ^ (ix & iy)
    checksum_components.append(component)

# Step 7: Final checksum computation
final_checksum = reduce(lambda a, b: (a ^ b) & 0xFFFF, checksum_components, scaled_distance)

print(f"Result: {final_checksum}")