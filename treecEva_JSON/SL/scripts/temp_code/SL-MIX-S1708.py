import math
from itertools import combinations

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_integer_length(length):
    return abs(round(length) - length) < 1e-9

def calculate_area(a, b, c):
    return 0.5 * abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]))

def calculate_angles(a, b, c):
    # Calculate angles using law of cosines
    sides = [calculate_distance(a,b), calculate_distance(b,c), calculate_distance(c,a)]
    angles = []
    for i in range(3):
        opposite_side = sides[i]
        adjacent_sides = [sides[(i+1)%3], sides[(i+2)%3]]
        cosine_angle = (adjacent_sides[0]**2 + adjacent_sides[1]**2 - opposite_side**2) / (2 * adjacent_sides[0] * adjacent_sides[1])
        angle_rad = math.acos(max(-1, min(1, cosine_angle)))  # Clamp to avoid numerical errors
        angles.append(math.degrees(angle_rad))
    return angles

# Candidate survey points
survey_points = [(0, 0), (3, 0), (0, 4), (5, 0), (0, 12), (9, 12), (5, 5), (8, 1), (6, 8)]

# Generate all possible triangles
triangle_candidates = list(combinations(survey_points, 3))

valid_triangle_scores = []

for triangle in triangle_candidates:
    a, b, c = triangle
    
    # Calculate side lengths
    side_ab = calculate_distance(a, b)
    side_bc = calculate_distance(b, c)
    side_ca = calculate_distance(c, a)
    
    # Check if all sides have integer lengths
    if not (is_integer_length(side_ab) and is_integer_length(side_bc) and is_integer_length(side_ca)):
        continue
    
    # Calculate area
    area = calculate_area(a, b, c)
    
    # Check if area > 5
    if not (area > 5):
        continue
    
    # Check angles
    angles = calculate_angles(a, b, c)
    
    # Check if all angles >= 30 degrees
    if not all(angle >= 30 for angle in angles):
        continue
    
    # Calculate perimeter
    perimeter = side_ab + side_bc + side_ca
    
    # Calculate quality score
    quality_score = perimeter * area
    valid_triangle_scores.append(quality_score)

# Find maximum quality score
max_quality_score = max(valid_triangle_scores) if valid_triangle_scores else 0

print(f"Result: {int(max_quality_score)}")