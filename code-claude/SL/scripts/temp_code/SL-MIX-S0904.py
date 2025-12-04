# Calculate the optimal delivery route among different path options

delivery_points = [(3, 5), (7, 2), (1, 9), (8, 4)]
base_station = (0, 0)

# Distance between two points using Manhattan distance
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Euclidean distance for alternative calculations (not used in final result)
def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[0]) ** 2) ** 0.5

# Calculate distances from base station to each delivery point
distances = [manhattan_distance(base_station, point) for point in delivery_points]

# Track visited points and path lengths
visited = set()
path_options = []
max_distance = 0

# Find the maximum distance for scaling (not used in final result)
for dist in distances:
    max_distance = max(max_distance, dist)
    
# Calculate path options using different strategies
for i, start_point in enumerate(delivery_points):
    path_length = distances[i]  # Distance from base to first point
    
    # Collect distances between this point and all other points
    point_to_point_distances = []
    for j, end_point in enumerate(delivery_points):
        if i != j:
            point_to_point_distances.append(manhattan_distance(start_point, end_point))
    
    # Sort distances to simulate visiting nearest points first
    point_to_point_distances.sort()
    
    # Add distances in optimal order
    for dist in point_to_point_distances:
        path_length += dist
    
    # Add return distance to base
    return_distance = manhattan_distance(delivery_points[(i + len(point_to_point_distances)) % len(delivery_points)], base_station)
    path_length += return_distance
    
    path_options.append(path_length)

# Some alternative calculations that don't affect the result
alternative_factor = sum(distances) / len(distances)
distortion_value = max_distance - alternative_factor

# Find the shortest path length
optimal_path_length = min(path_options)

# Check if any paths are substantially longer (not used in final result)
long_paths = [p for p in path_options if p > 1.5 * optimal_path_length]

print(f"Result: {optimal_path_length}")