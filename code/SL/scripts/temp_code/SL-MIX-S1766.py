from math import factorial
from itertools import permutations

def compute_vertex_hash(coords):
    # Sort coordinates and apply XOR chain
    sorted_coords = sorted(coords)
    hash_value = 0
    for coord in sorted_coords:
        hash_value ^= int(coord * 1000)  # Scale to integer for XOR
    return hash_value

# Vertex coordinates for a triangular mesh
vertex_data = [
    [0.123, 0.456, 0.789],
    [0.234, 0.567, 0.891],
    [0.345, 0.678, 0.912]
]

# Process each vertex through hash function
vertex_hashes = [compute_vertex_hash(vertex) for vertex in vertex_data]

# Apply combinatorial transformation: sum of all pairwise XOR products
comb_transform = 0
for i in range(len(vertex_hashes)):
    for j in range(i+1, len(vertex_hashes)):
        comb_transform += vertex_hashes[i] ^ vertex_hashes[j]

# Calculate geometric factor based on coordinate permutations
geom_factor = 0
for vertex in vertex_data:
    perms = list(permutations(vertex))
    geom_factor += len(perms) * sum(int(c*1000) for c in vertex)

# Final mesh signature combines combinatorial and geometric components
mesh_signature = (comb_transform & 0xFFFF) + (geom_factor >> 4)
print(f"Result: {mesh_signature}")