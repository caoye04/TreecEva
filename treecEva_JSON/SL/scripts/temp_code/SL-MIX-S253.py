from functools import reduce
from math import gcd

def calculate_centroid(vertices):
    x = sum(v[0] for v in vertices) / len(vertices)
    y = sum(v[1] for v in vertices) / len(vertices)
    return (x, y)

def area_of_triangle(v1, v2, v3):
    return abs((v1[0]*(v2[1]-v3[1]) + v2[0]*(v3[1]-v1[1]) + v3[0]*(v1[1]-v2[1])) / 2.0)

def lcm(a, b):
    return abs(a*b) // gcd(a, b) if a and b else 0

initial_triangle = [(0, 0), (4, 0), (2, 3)]
triangle_stack = [initial_triangle]
refinement_count = 0
max_refinements = 5

while triangle_stack and refinement_count < max_refinements:
    current_triangle = triangle_stack.pop(0)
    area = area_of_triangle(*current_triangle)
    
    # Number theory condition: area must be divisible by a computed LCM
    area_lcm = lcm(int(current_triangle[0][0])+1, int(current_triangle[1][1])+1)
    
    if area_lcm == 0 or area % area_lcm != 0:
        continue
        
    centroid = calculate_centroid(current_triangle)
    
    # Generate three new triangles from the centroid
    new_triangles = [
        [current_triangle[0], current_triangle[1], centroid],
        [current_triangle[1], current_triangle[2], centroid],
        [current_triangle[2], current_triangle[0], centroid]
    ]
    
    valid_triangles = list(filter(lambda t: area_of_triangle(*t) > 0.5, new_triangles))
    
    if len(valid_triangles) >= 2:
        triangle_stack.extend(valid_triangles[:2])
        refinement_count += 1
    
    # Early termination if we've hit our limit
    if refinement_count >= max_refinements:
        break

# Additional geometric filtering using set operations
vertex_set = set()
for triangle in triangle_stack:
    for vertex in triangle:
        vertex_set.add(vertex)
        
unique_vertex_count = len(vertex_set)

if unique_vertex_count > 10:
    refinement_count += 1

print(f"Result: {refinement_count}")