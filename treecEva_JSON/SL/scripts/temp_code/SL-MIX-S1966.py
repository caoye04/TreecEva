import re
from collections import defaultdict
from functools import reduce
import math

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std_dev(data):
    return math.sqrt(calculate_variance(data))

# Sonar sweep data (depth measurements in meters)
sonar_sweep_1 = "1200,1210,1205,1220,1215,9999,1208,1212,1207,1218"
sonar_sweep_2 = "1195,1202,1209,1211,1204,1217,1206,1213,1201,1219"
sonar_sweep_3 = "1203,1214,1208,1216,1205,1212,1209,1215,1207,1221"

# Parse and tokenize depth measurements
parsed_depths = []
for sweep in [sonar_sweep_1, sonar_sweep_2, sonar_sweep_3]:
    depths = list(map(int, re.findall(r'\d+', sweep)))
    parsed_depths.extend(depths)

# Filter outliers using statistical analysis
std_dev_threshold = 2
dataset_mean = sum(parsed_depths) / len(parsed_depths)
dataset_std_dev = calculate_std_dev(parsed_depths)
filtered_depths = [d for d in parsed_depths if abs(d - dataset_mean) <= std_dev_threshold * dataset_std_dev]

# Spatial clustering of similar depths (group depths within 5 meters)
cluster_map = defaultdict(list)
for depth in filtered_depths:
    cluster_key = round(depth / 5) * 5
    cluster_map[cluster_key].append(depth)

# Calculate cluster boundary areas assuming circular clusters with radius based on cluster spread
cluster_areas = {}
for centroid, members in cluster_map.items():
    if len(members) > 1:
        spread = max(members) - min(members)
        radius = spread / 2
        area = math.pi * (radius ** 2)
        cluster_areas[centroid] = area
    else:
        cluster_areas[centroid] = 0

# Identify significant clusters (area > 50 square meters)
significant_clusters = {k: v for k, v in cluster_areas.items() if v > 50}

# Count significant clusters after applying dynamic programming optimization for overlapping regions
sorted_centroids = sorted(significant_clusters.keys())
significant_cluster_count = 0
last_processed = float('-inf')

for centroid in sorted_centroids:
    # Apply DP approach to avoid double counting overlapping clusters
    if centroid - last_processed > 10:  # Minimum separation to be considered distinct
        significant_cluster_count += 1
        last_processed = centroid

print(f"Result: {significant_cluster_count}")