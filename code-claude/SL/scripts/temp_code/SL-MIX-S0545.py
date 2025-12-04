import itertools

def get_data_quality(strength, noise):
    # Calculate quality metric (not used in final result)
    quality = strength * 2 - noise
    return quality

def calculate_signal_strength(points, station):
    # Find the point with optimal signal characteristics
    best_point = None
    min_distance = float('inf')
    
    # Track some statistics for monitoring (not used in final calculation)
    total_points = len(points)
    points_checked = 0
    noise_levels = []
    
    for point in points:
        # Calculate Manhattan distance
        x_diff = abs(point[0] - station[0])
        y_diff = abs(point[1] - station[1])
        distance = x_diff + y_diff
        
        # Generate a noise level based on point coordinates (distraction)
        noise = (point[0] & point[1]) | (point[0] ^ 3)
        noise_levels.append(noise)
        
        # Track progress
        points_checked += 1
        
        # Find minimum distance point
        if distance < min_distance:
            min_distance = distance
            best_point = point
    
    # Calculate some metrics that aren't used for the answer
    avg_noise = sum(noise_levels) / len(noise_levels) if noise_levels else 0
    completion = points_checked / total_points * 100 if total_points > 0 else 0
    
    return min_distance

# Define base station coordinates
base_station = (15, 22)

# Generate potential signal points
raw_points = [(x, y) for x, y in itertools.product(range(10, 25, 3), range(15, 35, 4))]

# Filter points based on a validation rule
def validate_point(p):
    # Points must have coordinates where at least one is even
    return p[0] % 2 == 0 or p[1] % 2 == 0

# Apply validation
valid_points = [p for p in raw_points if validate_point(p)]

# Perform some data transformation (not relevant to final answer)
transformed_data = [(p[0] + 1, p[1] - 1) for p in raw_points]

# Calculate optimal signal strength distance
optimal_distance = calculate_signal_strength(valid_points, base_station)

# Apply a correction factor (not actually used)
correction = optimal_distance * 0.05

# Some additional processing on the data (distraction)
for i, point in enumerate(valid_points[:3]):
    signal = get_data_quality(10, i+2)
    if i == len(valid_points) - 1:
        break

print(f"Result: {optimal_distance}")