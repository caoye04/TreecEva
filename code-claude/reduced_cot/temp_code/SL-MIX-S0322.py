def calculate_manhattan(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def calculate_euclidean(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def find_redundant_points(locations, threshold=1.5):
    redundant = set()
    for i, p1 in enumerate(locations):
        for j, p2 in enumerate(locations):
            if i != j and i not in redundant and j not in redundant:
                if calculate_euclidean(p1, p2) < threshold:
                    redundant.add(j)
    return redundant

def calculate_distance(locations):
    if not locations:
        return 0
    # The actual calculation we care about
    distance = 0
    for i in range(len(locations) - 1):
        distance += calculate_manhattan(locations[i], locations[i + 1])
    return distance

# Sensor locations on a grid (x, y)
all_locations = [
    (0, 0), (2, 3), (5, 1), (3, 5), (7, 2), 
    (1, 4), (4, 3), (6, 0), (2, 2), (5, 4)
]

# Environmental conditions (irrelevant for distance calculation)
conditions = {'temperature': 22.5, 'humidity': 65, 'wind': 12}

# Filter locations based on various criteria
def apply_sensor_filters(locations, env_conditions):
    # Calculate sensor quality scores (irrelevant complexity)
    quality_scores = {}
    for i, loc in enumerate(locations):
        base_score = (loc[0] * 0.7 + loc[1] * 0.3) * 10
        temp_factor = env_conditions['temperature'] / 20
        wind_penalty = env_conditions['wind'] * 0.5
        quality_scores[i] = max(0, base_score * temp_factor - wind_penalty)
    
    # This filtering is misleading and doesn't affect final result
    filtered_by_quality = []
    quality_threshold = 15
    for i, loc in enumerate(locations):
        if quality_scores[i] > quality_threshold:
            filtered_by_quality.append(loc)
    
    # Sort by x coordinate (another distraction)
    filtered_by_quality.sort(key=lambda p: p[0])
    
    # The actual filtering we need - every other point starting from the first
    return [loc for i, loc in enumerate(locations) if i % 2 == 0]

# Process sensor data with weather adjustments (irrelevant)
def process_sensor_data(locations, conditions):
    processed_data = []
    for i, loc in enumerate(locations):
        x_adjusted = loc[0] + (conditions['wind'] / 10)
        y_adjusted = loc[1] - (conditions['humidity'] - 60) / 20
        processed_data.append((round(x_adjusted, 1), round(y_adjusted, 1)))
    return processed_data

# Main processing pipeline
processed_locations = process_sensor_data(all_locations, conditions)
quality_threshold = 20 if conditions['temperature'] > 25 else 15

# This is a distraction - not used in final calculation
redundant_indices = find_redundant_points(all_locations)
nonredundant_locations = [loc for i, loc in enumerate(all_locations) if i not in redundant_indices]

# The actual filtering that matters for our answer
filtered_locations = apply_sensor_filters(all_locations, conditions)

# Calculate various metrics (most are distractions)
total_sensors = len(all_locations)
active_sensors = len(filtered_locations)
sensor_density = active_sensors / (max(p[0] for p in all_locations) * max(p[1] for p in all_locations))

# Misleading calculation that's not used
alternative_path = calculate_euclidean(filtered_locations[0], filtered_locations[-1])

# This is the key statement that computes our answer
optimal_path_length = calculate_distance(filtered_locations)

# Distraction - different path calculations
circular_path_length = optimal_path_length + calculate_manhattan(filtered_locations[-1], filtered_locations[0])

print(f"Result: {optimal_path_length}")