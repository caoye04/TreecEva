# Calculate the optimal delivery route length for a food delivery service

# Distance matrix between locations (in kilometers)
distances = [
    [0, 5, 9, 4],
    [5, 0, 7, 3],
    [9, 7, 0, 2],
    [4, 3, 2, 0]
]

# Restaurant locations to visit (indexes in the distance matrix)
locations = [0, 2, 3]

# Weather condition affects travel time (not distance)
weather_factor = 1.2
traffic_density = [0.8, 1.0, 1.5, 0.9]  # Traffic density for each location

# Calculate estimated travel times
travel_times = {}
for i in range(len(distances)):
    for j in range(len(distances[i])):
        if i != j:
            travel_times[(i, j)] = distances[i][j] * weather_factor * traffic_density[j]

# Generate possible route permutations
route_options = [[0]]
for loc in locations[1:]:
    if loc not in route_options[0]:
        route_options[0].append(loc)

# Calculate route lengths for different starting points
candidate_routes = {}
delivery_times = {}

# Try different starting points (irrelevant for the final answer)
alternate_starts = [1, 2]
for start in alternate_starts:
    potential_time = sum(travel_times.get((i, i+1), 0) for i in range(start, len(locations)-1))
    delivery_times[start] = potential_time

# Calculate the actual route lengths
for i in range(len(route_options)):
    route = route_options[i]
    route_length = 0
    
    # Calculate total distance of this route
    for j in range(len(route) - 1):
        route_length += distances[route[j]][route[j+1]]
    
    # Add return to starting point
    route_length += distances[route[-1]][route[0]]
    
    # Store the route length
    candidate_routes[i] = route_length

# Possible optimization strategies (not used in final calculation)
optimization_weights = [0.7, 0.9, 1.1]
weighted_routes = {i: candidate_routes[i] * optimization_weights[1] for i in candidate_routes}

# Find the shortest route
optimal_route_length = min(candidate_routes.values())
optimal_route_index = min(candidate_routes, key=candidate_routes.get)

# Calculate alternative metrics (not used for answer)
alternative_metric = sum(distances[i][j] for i in range(len(distances)) for j in range(len(distances[i])) if i < j)
average_segment = optimal_route_length / len(locations)

print(f"Result: {optimal_route_length}")