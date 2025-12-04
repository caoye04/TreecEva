# Travel route optimization system

# Weather conditions (1-5 scale, 1=excellent, 5=severe)
weather_factor = 4

# Base distances in kilometers
direct_distance = 120
scenic_distance = 165
alternate_distance = 145

# Traffic congestion factors (multipliers)
direct_traffic = 1.2
scenic_traffic = 0.9
alternate_traffic = 1.1

# Calculate potential fuel consumption (liters)
direct_fuel = direct_distance * 0.08
scenic_fuel = scenic_distance * 0.075
alternate_fuel = alternate_distance * 0.085

# Apply terrain difficulty adjustment
terrain_difficulty = 3
direct_adjustment = direct_distance + (terrain_difficulty * 2)
scenic_adjustment = scenic_distance - (terrain_difficulty * 5)
alternate_adjustment = alternate_distance + (terrain_difficulty * 1)

# Calculate time estimates (minutes)
direct_path = direct_distance * direct_traffic
scenic_route = scenic_distance * scenic_traffic
alternate_route = alternate_distance * alternate_traffic

# Potential stops along each route
direct_stops = 2
scenic_stops = 5
alternate_stops = 3

# Rest time per stop (minutes)
stop_duration = 15

# Total journey times including stops
direct_total_time = direct_path + (direct_stops * stop_duration)
scenic_total_time = scenic_route + (scenic_stops * stop_duration)
alternate_total_time = alternate_route + (alternate_stops * stop_duration)

# Select optimal path length based on weather
optimal_path_length = min(direct_path, scenic_route) if weather_factor < 3 else alternate_route

# Calculate cost estimate for selected route
cost_per_km = 0.25
total_cost = optimal_path_length * cost_per_km

print(f"Result: {optimal_path_length}")