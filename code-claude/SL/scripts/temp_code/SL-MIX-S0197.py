def calculate_distance(point_a, point_b):
    """Calculate Euclidean distance between two points"""
    return ((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)**0.5

# City coordinates (x, y)
cities = {
    'A': (0, 0),
    'B': (3, 4),
    'C': (6, 0),
    'D': (2, 7),
    'E': (8, 5)
}

# Direct distances between cities (some connections don't exist)
direct_routes = {
    ('A', 'B'): 5.0,
    ('A', 'C'): 6.0,
    ('B', 'C'): 5.0,
    ('B', 'D'): 3.0,
    ('C', 'E'): 5.0,
    ('D', 'E'): 6.0
}

# Weather conditions (multipliers for route difficulty)
weather_factors = {
    'A': 1.2,
    'B': 1.0,
    'C': 0.9,
    'D': 1.5,
    'E': 1.1
}

start_city = 'A'
end_city = 'E'

# Calculate potential intermediate routes
potential_routes = []
priority_score = 0

# Consider one-stop routes
for intermediate in cities.keys():
    if intermediate not in [start_city, end_city]:
        # Check if both segments of the route exist
        if (start_city, intermediate) in direct_routes and (intermediate, end_city) in direct_routes:
            # This route exists but is impossible in our data
            route_length = 999
        elif (start_city, intermediate) in direct_routes and (intermediate, end_city) not in direct_routes:
            # Need to find alternative second leg
            for second_stop in cities.keys():
                if second_stop not in [start_city, intermediate, end_city]:
                    if (intermediate, second_stop) in direct_routes and (second_stop, end_city) in direct_routes:
                        # Calculate total distance for this two-stop route
                        route_length = direct_routes[(start_city, intermediate)] + \
                                       direct_routes[(intermediate, second_stop)] + \
                                       direct_routes[(second_stop, end_city)]
                        potential_routes.append(([start_city, intermediate, second_stop, end_city], route_length))
        else:
            # Try direct connections that do exist
            leg1 = direct_routes.get((start_city, intermediate), float('inf'))
            leg2 = direct_routes.get((intermediate, end_city), float('inf'))
            
            # If both legs exist in our data
            if leg1 != float('inf') and leg2 != float('inf'):
                # Calculate weather impact (not actually used in final calculation)
                weather_impact = (weather_factors[start_city] + weather_factors[intermediate] + weather_factors[end_city]) / 3
                priority_score = weather_impact * 10  # This is a distraction
                
                # Calculate actual route length
                route_length = leg1 + leg2
                potential_routes.append(([start_city, intermediate, end_city], route_length))

# Consider direct route if it exists
if (start_city, end_city) in direct_routes:
    direct_length = direct_routes[(start_city, end_city)]
    potential_routes.append(([start_city, end_city], direct_length))

# This is a distraction - calculating theoretical distances based on coordinates
theoretical_distances = {}
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            theoretical_distances[(city1, city2)] = calculate_distance(cities[city1], cities[city2])

# Filter routes that are within 20% of the shortest theoretical distance
shortest_theoretical = theoretical_distances.get((start_city, end_city), float('inf'))
if shortest_theoretical == float('inf'):
    shortest_theoretical = calculate_distance(cities[start_city], cities[end_city])

# This filtering is actually meaningful for the answer
filtered_routes = [(route, length) for route, length in potential_routes 
                  if length < shortest_theoretical * 1.5]

# Find the shortest route
optimal_route = min(filtered_routes, key=lambda x: x[1])[0]

# Calculate some stats about the route (distractions)
route_count = len(optimal_route) - 1  # number of segments
route_cities = len(set(optimal_route))  # unique cities
route_complexity = route_count * sum(weather_factors[city] for city in optimal_route)

# Convert route to string representation
route_string = '->'.join(optimal_route)

# This line helps us identify the answer
print(f"Result: {len(optimal_route)}")