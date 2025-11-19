import math

def calculate_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# Vertex coordinates for a triangular mesh
vertex_coordinates = [
    (0, 0, 0),
    (3, 0, 0),
    (0, 4, 0),
    (0, 0, 5)
]

# Calculate all pairwise distances between vertices
pairwise_distances = [
    calculate_distance(vertex_coordinates[i], vertex_coordinates[j])
    for i in range(len(vertex_coordinates))
    for j in range(i + 1, len(vertex_coordinates))
]

# Find the maximum distance
max_edge_length = max(pairwise_distances)

# Compute a stability metric using set operations on distance thresholds
threshold_set = {d for d in pairwise_distances if d > 2.5}
stability_base = len(threshold_set) * sum(threshold_set)

# Apply geometric adjustment factor
geometric_factor = math.ceil(max_edge_length) if max_edge_length > 5 else math.floor(max_edge_length)

# Final stability index calculation
mesh_stability_index = stability_base // geometric_factor if geometric_factor != 0 else 0

print(f"Result: {mesh_stability_index}")