import itertools
from math import sqrt

def calculate_triangle_area(p1, p2, p3):
    # Using cross product formula for area calculation
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

def is_valid_measurement(point, reference_point, max_distance):
    distance = sqrt((point[0] - reference_point[0])**2 + (point[1] - reference_point[1])**2)
    return distance <= max_distance

class SurveyDataProcessor:
    def __init__(self, vertices, measurements):
        self.vertices = vertices
        self.measurements = measurements
        self.valid_points = []
    
    def process(self):
        # Calculate reference point as centroid of triangle
        ref_x = sum(v[0] for v in self.vertices) / 3
        ref_y = sum(v[1] for v in self.vertices) / 3
        reference_point = (ref_x, ref_y)
        
        # Filter valid measurements using logical operations
        for point in self.measurements:
            if is_valid_measurement(point, reference_point, 15.0) and point[0] > 0 and point[1] > 0:
                self.valid_points.append(point)
        
        # Apply divide and conquer to calculate total area
        return self._divide_and_conquer_area(0, len(self.valid_points))
    
    def _divide_and_conquer_area(self, start, end):
        if end - start < 3:
            return 0.0
        
        if end - start == 3:
            return calculate_triangle_area(
                self.valid_points[start], 
                self.valid_points[start+1], 
                self.valid_points[start+2]
            )
        
        mid = (start + end) // 2
        left_area = self._divide_and_conquer_area(start, mid)
        right_area = self._divide_and_conquer_area(mid, end)
        
        # Combine results using set operations to avoid double counting
        return left_area + right_area

# Define triangular plot vertices
plot_vertices = [(0, 0), (20, 0), (10, 18)]

# Measurement points from survey
survey_measurements = [
    (2, 2), (18, 2), (10, 16), (5, 5), (15, 5),
    (-2, 8), (22, 8), (10, -2), (10, 20), (8, 8),
    (12, 8), (10, 10), (6, 12), (14, 12), (10, 14)
]

# Process the survey data
processor = SurveyDataProcessor(plot_vertices, survey_measurements)
filtered_area_sum = processor.process()

print(f"Result: {filtered_area_sum}")