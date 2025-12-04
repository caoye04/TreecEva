# Delivery route optimization system

def calculate_distance(point_a, point_b):
    # Simple Euclidean distance calculation
    return ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) ** 0.5

# Warehouse locations (x, y coordinates)
warehouses = {
    'main': (0, 0),
    'north': (0, 50),
    'east': (30, 0),
    'west': (-40, 10)
}

# Delivery destinations
destinations = {
    'A': (15, 25),
    'B': (-10, 35),
    'C': (25, 5),
    'D': (-25, -15)
}

# Priority levels for each destination (higher = more important)
priorities = {'A': 3, 'B': 1, 'C': 2, 'D': 4}

# Weather conditions affecting certain routes (multiplier for distance)
weather_impact = {'north_to_A': 1.5, 'east_to_C': 0.8, 'main_to_D': 1.2}

# Calculate distances from each warehouse to each destination
route_distances = {}
for w_name, w_loc in warehouses.items():
    for d_name, d_loc in destinations.items():
        route_key = f"{w_name}_to_{d_name}"
        base_distance = calculate_distance(w_loc, d_loc)
        # Apply weather impact if applicable
        multiplier = weather_impact.get(route_key, 1.0)
        route_distances[route_key] = base_distance * multiplier

# Identify destinations that need immediate delivery (priority > 2)
high_priority = {d: loc for d, loc in destinations.items() if priorities[d] > 2}

# Calculate potential routes for high priority destinations
potential_routes = {}
for d_name, d_loc in high_priority.items():
    # Consider only main and north warehouses for high priority
    candidate_warehouses = {k: v for k, v in warehouses.items() 
                           if k in ['main', 'north', 'east']}
    
    for w_name, w_loc in candidate_warehouses.items():
        route_key = f"{w_name}_to_{d_name}"
        # Skip routes affected by severe weather
        if route_key in weather_impact and weather_impact[route_key] > 1.3:
            continue
            
        # Calculate fuel cost based on distance
        fuel_cost = route_distances[route_key] * 0.1
        
        # Calculate time penalty for longer routes
        time_penalty = max(0, route_distances[route_key] - 30) * 0.5
        
        # Skip less efficient routes
        efficiency_score = priorities[d_name] * 10 - fuel_cost - time_penalty
        if efficiency_score < 15:
            continue
            
        potential_routes[route_key] = route_distances[route_key]

# Add fallback route if no good options found
if not potential_routes:
    potential_routes['main_to_A'] = route_distances['main_to_A']

# Find the shortest viable route
optimal_route_distance = min(potential_routes.values())

# Calculate alternate metric (not used for final decision)
average_distance = sum(potential_routes.values()) / len(potential_routes)
distance_threshold = average_distance * 0.85

# Reconsider if shortest route is still too long
if optimal_route_distance > 50:
    backup_routes = {k: v for k, v in route_distances.items()
                     if 'west' in k and v < optimal_route_distance}
    if backup_routes:
        optimal_route_distance = min(backup_routes.values())

print(f"Result: {optimal_route_distance}")