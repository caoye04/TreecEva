import math
from itertools import combinations

class VertexNode:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.next = None

class TriangularMeshProcessor:
    def __init__(self):
        self.head = None
    
    def add_vertex(self, x, y, z):
        new_node = VertexNode(x, y, z)
        new_node.next = self.head
        self.head = new_node
    
    def get_vertices_as_list(self):
        vertices = []
        current = self.head
        while current:
            vertices.append((current.x, current.y, current.z))
            current = current.next
        return vertices

class TempStorage:
    def __enter__(self):
        self.storage = set()
        return self.storage
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.storage.clear()

def calculate_triangle_area(a, b, c):
    # Using Heron's formula
    side_a = math.sqrt(sum((b[i] - c[i])**2 for i in range(3)))
    side_b = math.sqrt(sum((a[i] - c[i])**2 for i in range(3)))
    side_c = math.sqrt(sum((a[i] - b[i])**2 for i in range(3)))
    s = (side_a + side_b + side_c) / 2
    return math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

def transform_coordinates(vertices, transformation_matrix):
    transformed = []
    for vertex in vertices:
        # Apply 3x3 transformation matrix to 3D point
        x, y, z = vertex
        new_x = transformation_matrix[0][0]*x + transformation_matrix[0][1]*y + transformation_matrix[0][2]*z
        new_y = transformation_matrix[1][0]*x + transformation_matrix[1][1]*y + transformation_matrix[1][2]*z
        new_z = transformation_matrix[2][0]*x + transformation_matrix[2][1]*y + transformation_matrix[2][2]*z
        transformed.append((new_x, new_y, new_z))
    return transformed

def optimize_mesh_area(triangles, depth=0):
    if depth > 3:  # Limit recursion depth
        return sum(calculate_triangle_area(*triangle) for triangle in triangles)
    
    # Try removing one triangle and see if total area decreases
    min_area = sum(calculate_triangle_area(*triangle) for triangle in triangles)
    best_triangles = triangles[:]
    
    for i in range(len(triangles)): 
        test_triangles = triangles[:i] + triangles[i+1:]
        test_area = optimize_mesh_area(test_triangles, depth+1)
        if test_area < min_area:
            min_area = test_area
            best_triangles = test_triangles
    
    return min_area

# Initialize mesh processor
mesh_processor = TriangularMeshProcessor()

# Add vertices for a tetrahedron
mesh_processor.add_vertex(0, 0, 0)      # Vertex A
mesh_processor.add_vertex(1, 0, 0)      # Vertex B
mesh_processor.add_vertex(0.5, 1, 0)    # Vertex C
mesh_processor.add_vertex(0.5, 0.5, 1)  # Vertex D

# Get vertices as list
vertex_list = mesh_processor.get_vertices_as_list()

# Define transformation matrix (scaling by 2 in all dimensions)
transformation_matrix = [
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
]

# Transform coordinates
transformed_vertices = transform_coordinates(vertex_list, transformation_matrix)

# Generate all possible triangles from 4 vertices (combinations of 3)
triangles = list(combinations(transformed_vertices, 3))

# Calculate initial surface area
initial_surface_area = sum(calculate_triangle_area(*triangle) for triangle in triangles)

# Optimize mesh using recursive backtracking
with TempStorage() as temp_storage:
    temp_storage.add(initial_surface_area)
    optimized_surface_area = optimize_mesh_area(triangles)
    temp_storage.add(optimized_surface_area)

print(f"Result: {round(optimized_surface_area, 2)}")