from collections import defaultdict
from functools import reduce
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_in_northern_hemisphere(coord):
    return coord[1] > 0

def compute_survey_value(coordinates):
    # Filter coordinates in northern hemisphere
    northern_coords = list(filter(is_in_northern_hemisphere, coordinates))
    
    # Apply distance-based scoring using map
    origin = (0, 0)
    distances = list(map(lambda c: calculate_distance(origin, c), northern_coords))
    
    # Divide and conquer approach to find max distance
    def find_max_distance(dist_list):
        if len(dist_list) == 1:
            return dist_list[0]
        mid = len(dist_list) // 2
        left_max = find_max_distance(dist_list[:mid])
        right_max = find_max_distance(dist_list[mid:])
        return max(left_max, right_max)
    
    max_dist = find_max_distance(distances) if distances else 0
    
    # Logical constraint: only consider points beyond 5 units
    valid_points = [(northern_coords[i], distances[i]) for i in range(len(northern_coords)) if distances[i] > 5]
    
    # Calculate survey score using reduce
    survey_scores = [dist * (1 if coord[0] > 0 else -1) for coord, dist in valid_points]
    total_survey_score = reduce(lambda x, y: x + y, survey_scores, 0) if survey_scores else 0
    
    # Apply geometric weighting
    optimal_survey_score = int(total_survey_score * max_dist) if max_dist > 0 else 0
    
    return optimal_survey_score

# Candidate survey locations
survey_locations = [
    (-3, 4), (5, 2), (-1, -6), (7, 8),
    (0, 9), (-4, 3), (2, -5), (6, 7),
    (-2, 1), (3, -3), (8, 5), (-5, -2)
]

optimal_survey_score = compute_survey_value(survey_locations)
print(f"Result: {optimal_survey_score}")