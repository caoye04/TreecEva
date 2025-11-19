from collections import defaultdict
import math

def calculate_sensor_coverage(sensor_positions, coverage_radius=5):
    grid_points = [(x, y) for x in range(-10, 11) for y in range(-10, 11)]
    coverage_map = defaultdict(int)
    
    for sensor in sensor_positions:
        sx, sy = sensor
        for px, py in grid_points:
            distance = math.sqrt((px - sx)**2 + (py - sy)**2)
            if distance <= coverage_radius:
                coverage_map[(px, py)] += 1
    
    return coverage_map

def optimize_monitoring_grid(coverage_data):
    max_coverage = max(coverage_data.values())
    optimal_points = [point for point, count in coverage_data.items() if count == max_coverage]
    
    # Calculate geometric center of optimal points
    if len(optimal_points) > 1:
        center_x = sum(p[0] for p in optimal_points) / len(optimal_points)
        center_y = sum(p[1] for p in optimal_points) / len(optimal_points)
        
        # Find point closest to geometric center
        min_distance = float('inf')
        representative_point = None
        
        for point in optimal_points:
            distance = math.sqrt((point[0] - center_x)**2 + (point[1] - center_y)**2)
            if distance < min_distance:
                min_distance = distance
                representative_point = point
    else:
        representative_point = optimal_points[0] if optimal_points else (0, 0)
    
    return representative_point, max_coverage

# Sensor network configuration
sensor_network_a = [(0, 0), (3, 4), (-2, 5)]
sensor_network_b = [(-3, -4), (6, -2), (1, 7), (-5, 1)]

# Process both networks
coverage_a = calculate_sensor_coverage(sensor_network_a)
coverage_b = calculate_sensor_coverage(sensor_network_b)

# Merge coverage maps
combined_coverage = defaultdict(int)
for point in set(coverage_a.keys()) | set(coverage_b.keys()):
    combined_coverage[point] = coverage_a.get(point, 0) + coverage_b.get(point, 0)

# Optimize monitoring grid
optimal_location, optimal_coverage = optimize_monitoring_grid(combined_coverage)

print(f"Result: {optimal_coverage}")