import itertools

# Function to calculate distance between cities (not used in final calculation)
def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# City coordinates (x, y)
cities = {
    'A': (0, 0),
    'B': (3, 4),
    'C': (6, 3),
    'D': (2, 7),
    'E': (8, 1)
}

# Pre-calculated distances between cities
distances = {
    ('A', 'B'): 5,
    ('A', 'C'): 6.7,
    ('A', 'D'): 7.3,
    ('A', 'E'): 8.1,
    ('B', 'C'): 3.2,
    ('B', 'D'): 3.6,
    ('B', 'E'): 5.4,
    ('C', 'D'): 4.2,
    ('C', 'E'): 2.8,
    ('D', 'E'): 6.3
}

# Ensure all city pairs are in the distances dictionary
for city1, city2 in itertools.combinations(cities.keys(), 2):
    if (city1, city2) not in distances and (city2, city1) not in distances:
        # This won't be executed as all pairs are already defined
        distances[(city1, city2)] = calculate_distance(cities[city1], cities[city2])

# Get distance between any two cities
def get_distance(city1, city2):
    if (city1, city2) in distances:
        return distances[(city1, city2)]
    elif (city2, city1) in distances:
        return distances[(city2, city1)]
    else:
        # This won't be needed as all distances are pre-defined
        return calculate_distance(cities[city1], cities[city2])

# Calculate some statistics about the distances (not used for final answer)
total_distance = sum(distances.values())
avg_distance = total_distance / len(distances)
max_dist = max(distances.values())
min_dist = min(distances.values())

# Find the shortest path from A to E visiting all cities exactly once
routes = list(itertools.permutations(['B', 'C', 'D']))
best_route = None
shortest_distance = float('inf')

for route in routes:
    current_distance = get_distance('A', route[0])
    for i in range(len(route) - 1):
        current_distance += get_distance(route[i], route[i+1])
    current_distance += get_distance(route[-1], 'E')
    
    if current_distance < shortest_distance:
        shortest_distance = current_distance
        best_route = ['A'] + list(route) + ['E']

# Extract the shortest path segments
shortest_path = []
for i in range(len(best_route) - 1):
    shortest_path.append(get_distance(best_route[i], best_route[i+1]))

# Calculate the optimal path length
optimal_path_length = sum(shortest_path)

# Alternate calculation method (not used for final answer)
alternate_length = 0
for i in range(len(best_route) - 1):
    alternate_length += get_distance(best_route[i], best_route[i+1])

print(f"Result: {optimal_path_length}")
