import hashlib
import math

def calculate_spatial_hash(coords_tuple):
    coord_str = f"{coords_tuple[0]}:{coords_tuple[1]}"
    return int(hashlib.md5(coord_str.encode()).hexdigest()[:8], 16) % 1000

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Geospatial data processing pipeline
sensor_readings = [(37.7749, -122.4194), (40.7128, -74.0060), (51.5074, -0.1278)]
transformation_keys = [123, 456, 789]

# Step 1: Apply modular coordinate adjustments
adjusted_coords = [
    ((int(lat*10000) + transformation_keys[i]) % 9973, 
     (int(lon*10000) - transformation_keys[i]) % 9973)
    for i, (lat, lon) in enumerate(sensor_readings)
]

# Step 2: Calculate pairwise distances with logarithmic scaling
scaled_distances = []
for i in range(len(adjusted_coords)):
    for j in range(i+1, len(adjusted_coords)):
        dx = adjusted_coords[i][0] - adjusted_coords[j][0]
        dy = adjusted_coords[i][1] - adjusted_coords[j][1]
        euclidean_dist = math.sqrt(dx*dx + dy*dy)
        scaled_distances.append(math.log(euclidean_dist + 1))

# Step 3: Generate coordinate hashes and combine with number theory
coord_hashes = [calculate_spatial_hash(coord) for coord in adjusted_coords]
gcd_values = [gcd_extended(h, 9973)[0] for h in coord_hashes]

# Step 4: Create metadata mapping using dictionary comprehension
metadata_map = {
    f"sensor_{i}": {
        "hash": coord_hashes[i],
        "gcd": gcd_values[i],
        "transform_key": transformation_keys[i]
    }
    for i in range(len(sensor_readings))
}

# Step 5: Compute final metric through complex aggregation
final_metric = (
    sum(scaled_distances) * 
    (sum(metadata_map[s]["hash"] for s in metadata_map) % 1000) +
    (math.exp(sum(gcd_values) / len(gcd_values))) % 1000
)

print(f"Result: {int(final_metric)}")