import math
from dataclasses import dataclass
from typing import List, Tuple

def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def calculate_polygon_perimeter(vertices: List[Tuple[float, float]]) -> float:
    perimeter = 0.0
    n = len(vertices)
    for i in range(n):
        perimeter += calculate_distance(vertices[i], vertices[(i + 1) % n])
    return perimeter

def calculate_polygon_area(vertices: List[Tuple[float, float]]) -> float:
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

# City block vertices (x, y coordinates forming a pentagon)
city_block_vertices = [(0, 0), (10, 0), (15, 8), (5, 12), (-2, 6)]
zoning_perimeter_threshold = 40
zoning_area_threshold = 100

block_perimeter = calculate_polygon_perimeter(city_block_vertices)
block_area = calculate_polygon_area(city_block_vertices)

# Short-circuit evaluation: permit required only if both conditions are met
permit_required = block_perimeter > zoning_perimeter_threshold and block_area > zoning_area_threshold

print(f"Perimeter: {block_perimeter:.2f}")
print(f"Area: {block_area:.2f}")
print(f"Result: {permit_required}")