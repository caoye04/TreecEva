from itertools import combinations

# Sensor data from three monitoring stations
data_a = {1, 2, 3, 4, 5, 6}
data_b = {4, 5, 6, 7, 8, 9}
data_c = {5, 6, 7, 8, 9, 10}

# Find all pairwise intersections between station data
pairwise_common = []
for pair in combinations([data_a, data_b, data_c], 2):
    intersection = pair[0] & pair[1]
    pairwise_common.append(intersection)

# Extract sizes of intersections and filter those above threshold
intersection_sizes = [len(s) for s in pairwise_common]
filtered_intersections = [size for size in intersection_sizes if size > 2]

# Final result
result = sum(filtered_intersections)
print(f"Result: {result}")