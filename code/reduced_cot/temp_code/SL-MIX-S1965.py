from collections import defaultdict
import hashlib

def hash_point(x, y):
    coord_str = f"({x:.2f},{y:.2f})"
    return hashlib.md5(coord_str.encode()).hexdigest()[:8]

# Simulated geospatial data points
points = [
    (1.23, 4.56),
    (1.25, 4.58),
    (1.22, 4.55),
    (7.89, 3.21),
    (7.90, 3.22),
    (10.00, 20.00)
]

# Group points by hashed coordinates with proximity threshold
proximity_threshold = 0.05
hash_groups = defaultdict(list)

for x, y in points:
    base_hash = hash_point(round(x/proximity_threshold)*proximity_threshold, 
                          round(y/proximity_threshold)*proximity_threshold)
    hash_groups[base_hash].append((x, y))

# Calculate cluster density metrics
cluster_count = len(hash_groups)
total_points = len(points)
cluster_density = 0

if cluster_count > 0:
    max_cluster_size = max(len(group) for group in hash_groups.values())
    cluster_density = (max_cluster_size * 1000) // total_points

print(f"Result: {cluster_density}")