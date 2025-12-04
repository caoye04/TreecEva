import itertools

def calculate_distance(x1, y1, x2, y2):
    # Manhattan distance between two points
    return abs(x2 - x1) + abs(y2 - y1)

# Sensor readings data: (x1, y1, x2, y2) coordinates
sensor_data = [
    (3, 5, 8, 9),
    (2, 4, 6, 7),
    (1, 1, 5, 4),
    (7, 2, 9, 9),
    (0, 3, 4, 2)
]

# Filter out invalid readings based on a threshold
threshold = 10
validity_flags = [True, False, True, True, False]

# Process data for visualization (not used in final calculation)
visualization_data = []
for i, data in enumerate(sensor_data):
    if validity_flags[i]:
        x1, y1, x2, y2 = data
        midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
        visualization_data.append((data, midpoint))

# Apply conditional filtering with lambda
filter_condition = lambda d: d[0] > 0 and d[1] > 0 and d[2] > 0 and d[3] > 0
sensor_data = list(filter(filter_condition, sensor_data))

# Combine data sources using zip and filtering
valid_coordinates = [coord for coord, valid in zip(sensor_data, validity_flags) if valid]

# Compute alternative paths (not used in final answer)
alternative_paths = list(itertools.permutations(valid_coordinates))
alt_distances = [sum(calculate_distance(p1[2], p1[3], p2[0], p2[1]) 
               for p1, p2 in zip(path, path[1:])) 
               for path in alternative_paths[:2]]  # Only calculate first two permutations

# Calculate total distance using map and lambda
total_distance = sum(map(lambda x: calculate_distance(*x), valid_coordinates))

# Some additional processing that doesn't affect the result
avg_x = sum(x1 + x2 for x1, y1, x2, y2 in valid_coordinates) / (len(valid_coordinates) * 2)
avg_y = sum(y1 + y2 for x1, y1, x2, y2 in valid_coordinates) / (len(valid_coordinates) * 2)

print(f"Result: {total_distance}")