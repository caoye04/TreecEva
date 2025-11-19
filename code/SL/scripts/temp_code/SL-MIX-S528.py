import math
from itertools import combinations

def calculate_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def process_terrain_data(sensor_readings):
    # State definitions for terrain classification
    TERRAIN_STATES = {'undefined': 0, 'flat': 1, 'decline': 2, 'valley': 3}
    current_state = TERRAIN_STATES['undefined']
    
    # Extract z-coordinates for depth analysis
    depths = [point[2] for point in sensor_readings]
    sorted_depths = sorted(depths)
    
    # Initialize tracking variables
    deepest_point_z = sorted_depths[0]
    previous_depth = sorted_depths[0]
    
    # Process depths to classify terrain and find deepest point
    for depth in sorted_depths[1:]:
        if depth < previous_depth:
            if current_state in [TERRAIN_STATES['undefined'], TERRAIN_STATES['flat']]:
                current_state = TERRAIN_STATES['decline']
            elif current_state == TERRAIN_STATES['decline']:
                current_state = TERRAIN_STATES['valley']
        elif depth > previous_depth:
            if current_state == TERRAIN_STATES['decline']:
                current_state = TERRAIN_STATES['valley']
        else:  # depth == previous_depth
            if current_state == TERRAIN_STATES['undefined']:
                current_state = TERRAIN_STATES['flat']
        
        # Update deepest point if necessary
        if depth < deepest_point_z:
            deepest_point_z = depth
        previous_depth = depth
    
    # Additional processing: calculate pairwise distances between sensor points
    distances = [calculate_distance(p1, p2) for p1, p2 in combinations(sensor_readings, 2)]
    avg_distance = sum(distances) / len(distances) if distances else 0
    
    # Adjust deepest point based on spatial distribution
    if avg_distance > 100 and current_state == TERRAIN_STATES['valley']:
        deepest_point_z -= 5  # Calibration adjustment for wide valleys
    
    return deepest_point_z

# Sensor data: (x, y, z) coordinates where z represents depth (negative values indicate depth below sea level)
sensor_data = [
    (120.5, 200.3, -45.2),
    (125.7, 195.8, -67.4),
    (130.2, 210.1, -58.9),
    (118.9, 198.4, -72.1),
    (127.3, 205.6, -50.3)
]

deepest_point_z = process_terrain_data(sensor_data)
print(f"Result: {deepest_point_z}")