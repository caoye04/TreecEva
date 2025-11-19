import math
from itertools import combinations
from dataclasses import dataclass
from typing import Set, Tuple

def calculate_triangle_area(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]) -> float:
    # Using shoelace formula for triangle area
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0)

@dataclass(frozen=True)
class SurveyPoint:
    x: float
    y: float
    elevation: int
    quality_flag: int  # Bitwise flag for data quality

# Simulated terrain survey data
survey_points = [
    SurveyPoint(0.0, 0.0, 125, 0b1101),
    SurveyPoint(3.0, 0.0, 130, 0b1111),
    SurveyPoint(0.0, 4.0, 135, 0b1110),
    SurveyPoint(3.0, 4.0, 128, 0b1100),
    SurveyPoint(1.5, 2.0, 140, 0b1111),
    SurveyPoint(5.0, 1.0, 120, 0b1001)
]

# Quality control bitmask - only accept points with flags having both bits 0 and 2 set
required_quality_mask = 0b0101
valid_points: Set[SurveyPoint] = set()

for point in survey_points:
    if (point.quality_flag & required_quality_mask) == required_quality_mask:
        valid_points.add(point)

# Generate all possible triangular combinations from valid points
potential_triangles = list(combinations(valid_points, 3))

validated_regions = 0
min_area_threshold = 1.0
max_elevation_diff = 15

for triangle in potential_triangles:
    p1, p2, p3 = triangle
    
    # Check elevation variance within triangle
    elevations = [p1.elevation, p2.elevation, p3.elevation]
    if max(elevations) - min(elevations) > max_elevation_diff:
        continue
    
    # Calculate triangle area
    area = calculate_triangle_area((p1.x, p1.y), (p2.x, p2.y), (p3.x, p3.y))
    
    # Apply minimum area constraint
    if area < min_area_threshold:
        continue
    
    # Compute centroid for further processing
    centroid_x = (p1.x + p2.x + p3.x) / 3.0
    centroid_y = (p1.y + p2.y + p3.y) / 3.0
    
    # Spatial filter using bitwise operations on coordinates
    cx_bits = int(centroid_x * 1000) & 0xFF
    cy_bits = int(centroid_y * 1000) & 0xFF
    
    # Accept triangles where XOR of coordinate bits is less than threshold
    if (cx_bits ^ cy_bits) < 100:
        validated_regions += 1

print(f"Result: {validated_regions}")