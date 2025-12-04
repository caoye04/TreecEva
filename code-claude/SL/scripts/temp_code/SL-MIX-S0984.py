from collections import defaultdict, Counter

# Delivery route optimization system
# Calculate the most efficient delivery route based on distance and traffic

traffic_levels = {'low': 1.0, 'medium': 1.3, 'high': 1.7, 'extreme': 2.2}

# Base distances between locations (in km)
distances = {
    'warehouse_to_downtown': 15,
    'warehouse_to_suburbs': 22,
    'warehouse_to_industrial': 18,
    'downtown_to_suburbs': 12,
    'downtown_to_industrial': 9,
    'suburbs_to_industrial': 14
}

# Current traffic conditions on each segment
traffic_conditions = {
    'warehouse_to_downtown': 'high',
    'warehouse_to_suburbs': 'low',
    'warehouse_to_industrial': 'medium',
    'downtown_to_suburbs': 'extreme',
    'downtown_to_industrial': 'medium',
    'suburbs_to_industrial': 'low'
}

# Calculate adjusted distances based on traffic
adjusted_distances = {route: distance * traffic_levels[traffic_conditions[route]] 
                     for route, distance in distances.items()}

# Weather impact factors (not used in final calculation)
weather_factors = {'sunny': 0, 'cloudy': 0.1, 'rainy': 0.25, 'snowy': 0.5}
current_weather = 'rainy'

# Fuel consumption based on vehicle type (not used in final calculation)
fuel_rates = {'van': 0.12, 'truck': 0.2, 'bike': 0.0}
current_vehicle = 'truck'

# Possible delivery routes from warehouse to all locations
routes = defaultdict(float)

# Direct routes from warehouse
routes['route_A'] = adjusted_distances['warehouse_to_downtown']
routes['route_B'] = adjusted_distances['warehouse_to_suburbs']
routes['route_C'] = adjusted_distances['warehouse_to_industrial']

# Calculate compound routes
# Route D: warehouse → downtown → suburbs
routes['route_D'] = adjusted_distances['warehouse_to_downtown'] + adjusted_distances['downtown_to_suburbs']

# Route E: warehouse → downtown → industrial
routes['route_E'] = adjusted_distances['warehouse_to_downtown'] + adjusted_distances['downtown_to_industrial']

# Route F: warehouse → suburbs → industrial
routes['route_F'] = adjusted_distances['warehouse_to_suburbs'] + adjusted_distances['suburbs_to_industrial']

# Count route segments (distractor calculation)
segment_counter = Counter([segment for route in routes for segment in route.split('_')])

# Apply potential weather impact (distractor - not used for final calculation)
weather_adjusted_routes = {route: distance * (1 + weather_factors[current_weather])
                          for route, distance in routes.items()}

# Calculate fuel costs (distractor - not used for final calculation)
fuel_costs = {route: distance * fuel_rates[current_vehicle] 
              for route, distance in routes.items()}

# Find the route with minimum adjusted distance
optimal_route = min(routes, key=lambda x: routes[x])

# For validation purposes, calculate the actual distances
print(f"All routes: {dict(routes)}")
print(f"Optimal route: {optimal_route}")
print(f"Distance of optimal route: {routes[optimal_route]}")
