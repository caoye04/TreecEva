from functools import reduce
from math import gcd

def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def boundary_points(vertices):
    n = len(vertices)
    boundary = 0
    for i in range(n):
        j = (i + 1) % n
        dx = vertices[j][0] - vertices[i][0]
        dy = vertices[j][1] - vertices[i][1]
        boundary += gcd(abs(dx), abs(dy))
    return boundary

# Vertices of the polygon (must be lattice points)
vertex_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]

# Calculate area using the shoelace formula
computed_area = polygon_area(vertex_coordinates)

# Count boundary lattice points
boundary_lattice_points = boundary_points(vertex_coordinates)

# Apply Pick's theorem: Area = I + B/2 - 1 => I = Area - B/2 + 1
interior_points = int(computed_area - boundary_lattice_points / 2 + 1)

print(f"Result: {interior_points}")