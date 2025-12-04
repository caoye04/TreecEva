def calculate_manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Sample coordinates of delivery locations (x, y)
delivery_locations = [
    (3, 4), (1, 2), (5, 6), (2, 8), (7, 3), (4, 1)
]

# Weather conditions affect which locations are accessible
weather_conditions = {
    'rain': [0.8, 1.2, 0.9, 1.0, 1.1, 0.7],  # multipliers for each location
    'sunny': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    'snow': [1.5, 1.3, 1.8, 1.6, 1.4, 1.7]
}

# Current weather and priority locations
current_weather = 'sunny'
priority_locations = [0, 2, 5]  # Indices of priority delivery locations

# Calculate weather impact (not used in final calculation)
weather_impact = sum(weather_conditions[current_weather])

# Filter locations based on custom criteria
traffic_density = [0.3, 0.7, 0.2, 0.5, 0.8, 0.1]
traffic_threshold = 0.5

filtered_indices = [i for i, density in enumerate(traffic_density) 
                  if density < traffic_threshold or i in priority_locations]

# Alternative filtering approach (not used)
alternative_indices = list(filter(lambda x: traffic_density[x] < 0.6, range(len(delivery_locations))))

# Get coordinates of filtered locations
filtered_coordinates = [delivery_locations[i] for i in filtered_indices]

# Function to calculate optimal path length
def calculate_path_length(coordinates):
    if not coordinates:
        return 0
    
    # Start from origin (0,0)
    current_position = (0, 0)
    total_distance = 0
    
    # Additional statistics (not used in final calculation)
    max_distance = 0
    min_distance = float('inf')
    
    # Visit each location in the given order
    for i, next_position in enumerate(coordinates):
        distance = calculate_manhattan_distance(current_position, next_position)
        total_distance += distance
        current_position = next_position
        
        # Update statistics
        max_distance = max(max_distance, distance)
        min_distance = min(min_distance, distance)
    
    # Return to origin
    return total_distance + calculate_manhattan_distance(current_position, (0, 0))

# Calculate alternative path (not used in final answer)
reversed_coordinates = filtered_coordinates[::-1]
alternative_path_length = calculate_path_length(reversed_coordinates)

# Calculate the optimal path length
optimal_path_length = calculate_path_length(filtered_coordinates)

# Calculate efficiency metric (not used)
efficiency = len(filtered_coordinates) / len(delivery_locations) * 100

print(f"Result: {optimal_path_length}")