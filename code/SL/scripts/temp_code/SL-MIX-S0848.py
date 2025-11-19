import math
from itertools import combinations

def compute_variance(values):
    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# Weather station coordinates forming a triangle
weather_stations = {
    'Alpha': (2, 3),
    'Beta': (8, 7),
    'Gamma': (5, 11)
}

# Wind speed readings over time
wind_speeds = [12.4, 9.8, 15.2, 11.0, 13.6]

# Calculate pairwise distances between stations
pairwise_distances = {f"{k1}-{k2}": euclidean_distance(v1, v2) 
                     for (k1, v1), (k2, v2) in combinations(weather_stations.items(), 2)}

# Compute average distance
avg_distance = sum(pairwise_distances.values()) / len(pairwise_distances)

# Early exit condition based on distance threshold
if avg_distance < 5.0:
    stability_index = 0
else:
    # Compute wind speed variance
    speed_variance = compute_variance(wind_speeds)
    
    # Normalize variance using log scale
    normalized_variance = math.log(speed_variance + 1)
    
    # Stability index formula
    stability_index = round(avg_distance * normalized_variance, 2)

print(f"Result: {stability_index}")