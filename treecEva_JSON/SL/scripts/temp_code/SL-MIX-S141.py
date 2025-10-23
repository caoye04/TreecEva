import math
from functools import reduce
from itertools import combinations

def triangle_area(vertices):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

def triangle_perimeter(vertices):
    (x1, y1), (x2, y2), (x3, y3) = vertices
    side1 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    side2 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
    side3 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
    return side1 + side2 + side3

# Triangle vertex coordinates in a mesh
mesh_triangles = [
    [(0, 0), (4, 0), (2, 3)],
    [(4, 0), (6, 2), (2, 3)],
    [(2, 3), (6, 2), (3, 5)],
    [(0, 0), (2, 3), (-1, 2)]
]

# Calculate quality scores for each triangle
triangle_scores = {}
for i, vertices in enumerate(mesh_triangles):
    area = triangle_area(vertices)
    perimeter = triangle_perimeter(vertices)
    # Quality score combines logarithmic area with exponential perimeter weighting
    score = math.log(area + 1) * math.exp(perimeter / 10) if area > 0 else 0
    triangle_scores[f'T{i+1}'] = score

# Generate combinatorial connections between triangles
triangle_ids = list(triangle_scores.keys())
connections = list(combinations(triangle_ids, 2))

# Connection strength based on score similarity
connection_weights = {
    (t1, t2): math.exp(-abs(triangle_scores[t1] - triangle_scores[t2]))
    for t1, t2 in connections
}

# Mesh stability index calculation
score_sum = sum(triangle_scores.values())
weight_product = reduce(lambda x, y: x * y, connection_weights.values(), 1)
combined_factor = math.log(score_sum + 1) if score_sum > 0 else 0

mesh_stability_index = round((combined_factor * weight_product) ** (1/3), 6)

print(f"Result: {mesh_stability_index}")