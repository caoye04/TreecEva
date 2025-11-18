import math
from functools import reduce
from itertools import combinations

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def coverage_variance(points):
    if len(points) < 2:
        return 0
    distances = [calculate_distance(p1, p2) for p1, p2 in combinations(points, 2)]
    mean_dist = sum(distances) / len(distances)
    return sum((d - mean_dist)**2 for d in distances) / len(distances)

# Sensor coordinates (x, y)
sensor_locations = [(0, 0), (3, 4), (6, 8), (2, 1), (7, 3), (1, 7)]

# Process sensor data with context manager for resource handling
class SensorAnalyzer:
    def __enter__(self):
        self.processed_points = []
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def filter_effective_sensors(self, locations, min_distance=2.0):
        # Use lambda and filter to identify sensors that are sufficiently separated
        effective = list(filter(lambda pair: calculate_distance(pair[0], pair[1]) > min_distance, 
                              combinations(locations, 2)))
        # Extract unique points using set comprehension
        unique_points = list(set([point for pair in effective for point in pair]))
        return unique_points
    
    def compute_coverage_metric(self, points):
        if not points:
            return 0
        # Calculate geometric properties
        centroid_x = sum(p[0] for p in points) / len(points)
        centroid_y = sum(p[1] for p in points) / len(points)
        
        # Distance from origin to centroid
        centroid_distance = math.sqrt(centroid_x**2 + centroid_y**2)
        
        # Statistical measure of point distribution
        spatial_variance = coverage_variance(points)
        
        # Short-circuit evaluation for efficiency
        return round(centroid_distance * (spatial_variance > 0 and math.log(spatial_variance + 1) or 1), 2)

with SensorAnalyzer() as analyzer:
    effective_sensors = analyzer.filter_effective_sensors(sensor_locations)
    optimal_coverage_score = analyzer.compute_coverage_metric(effective_sensors)
    
print(f"Result: {optimal_coverage_score}")