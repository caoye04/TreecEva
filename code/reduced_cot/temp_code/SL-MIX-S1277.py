import math
from itertools import combinations

def calculate_angle(p1, p2, p3):
    # Calculate angle at p2 using dot product
    a = (p1[0] - p2[0], p1[1] - p2[1])
    b = (p3[0] - p2[0], p3[1] - p2[1])
    dot_product = a[0]*b[0] + a[1]*b[1]
    magnitude_a = math.sqrt(a[0]**2 + a[1]**2)
    magnitude_b = math.sqrt(b[0]**2 + b[1]**2)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    cos_angle = dot_product / (magnitude_a * magnitude_b)
    # Clamp to avoid numerical errors
    cos_angle = max(-1, min(1, cos_angle))
    return math.acos(cos_angle)

def is_valid_triangle(triangle_vertices, min_angle_rad):
    points = list(triangle_vertices)
    if len(points) != 3:
        return False
    # Check all three angles
    for i in range(3):
        p1, p2, p3 = points[i], points[(i+1)%3], points[(i+2)%3]
        angle = calculate_angle(p1, p2, p3)
        if angle < min_angle_rad:
            return False
    return True

def count_valid_triangulations(point_set, min_angle_degrees):
    min_angle_rad = math.radians(min_angle_degrees)
    points_list = list(point_set)
    valid_count = 0
    
    # Generate all possible triangles
    for triangle_comb in combinations(points_list, 3):
        triangle_fs = frozenset(triangle_comb)
        if is_valid_triangle(triangle_fs, min_angle_rad):
            valid_count += 1
    
    return valid_count

def recursive_mesh_validator(mesh_configs, min_angle, index=0):
    if index >= len(mesh_configs):
        return 0
    
    current_config = mesh_configs[index]
    valid_in_current = count_valid_triangulations(current_config, min_angle)
    
    # Recursive call for remaining configurations
    remaining_valid = recursive_mesh_validator(mesh_configs, min_angle, index + 1)
    
    # Apply weighting based on configuration size
    weight = len(current_config) if len(current_config) > 0 else 1
    return valid_in_current * weight + remaining_valid

# Initial mesh configurations
mesh_A = frozenset({(0, 0), (1, 0), (0, 1), (1, 1)})
mesh_B = frozenset({(2, 2), (3, 2), (2, 3), (3, 3), (2.5, 2.5)})
mesh_C = frozenset({(0, 2), (1, 3), (0, 4)})

all_meshes = [mesh_A, mesh_B, mesh_C]
minimum_angle = 30  # degrees

valid_triangulations_count = recursive_mesh_validator(all_meshes, minimum_angle)
print(f"Result: {valid_triangulations_count}")