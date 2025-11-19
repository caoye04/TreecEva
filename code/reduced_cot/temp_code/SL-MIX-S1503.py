import math

def parse_vertex(vertex_str):
    parts = vertex_str.split(',')
    return (float(parts[0]), float(parts[1]))

def apply_transformations(vertex, ops):
    x, y = vertex
    for op in ops:
        if op == 'reflect_x':
            y = -y
        elif op == 'rotate_90':
            x, y = -y, x
        elif op == 'scale_2':
            x, y = 2*x, 2*y
    return (x, y)

# Encoded vertex data
vertex_a_str = "1.0,2.0"
vertex_b_str = "4.0,6.0"
vertex_c_str = "7.0,2.0"

# Parse vertices
A = parse_vertex(vertex_a_str)
B = parse_vertex(vertex_b_str)
C = parse_vertex(vertex_c_str)

# Transformation sets encoded as strings
transform_set_1 = ['reflect_x', 'scale_2']
transform_set_2 = ['rotate_90']
transform_set_3 = ['scale_2', 'reflect_x', 'rotate_90']

# Apply divide-and-conquer approach: process each vertex with its transformation set
A_transformed = apply_transformations(A, transform_set_1)
B_transformed = apply_transformations(B, transform_set_2)
C_transformed = apply_transformations(C, transform_set_3)

# Calculate area using cross product formula
def triangle_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

# Compute area after all transformations
enclosed_area = triangle_area(A_transformed, B_transformed, C_transformed)

print(f"Result: {enclosed_area}")