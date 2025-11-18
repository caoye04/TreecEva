import itertools
import math

def calculate_triangle_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

vertices_set = [
    [(0, 0), (4, 0), (2, 3)],
    [(1, 1), (5, 1), (3, 4)],
    [(0, 2), (3, 5), (1, 6)]
]

area_threshold = 3.0
valid_triangles = [tri for tri in vertices_set if calculate_triangle_area(*tri) >= area_threshold]

# Compute stability metrics using permutations of vertex coordinates
stability_scores = []
for triangle in valid_triangles:
    coord_perms = list(itertools.permutations(triangle))
    score = sum(math.sqrt(sum(abs(a-b) for a, b in zip(perm[0], perm[1]))) for perm in coord_perms)
    stability_scores.append(score)

# Apply sorting and binary search-like filtering
stability_scores.sort()
filtered_scores = [s for s in stability_scores if s > sum(stability_scores)/len(stability_scores) or s < min(stability_scores)*2]

# Logical chain with short-circuit evaluation
delta_check = max(filtered_scores) - min(filtered_scores)
final_stability_index = 0
if delta_check > 10 and len(filtered_scores) >= 2:
    final_stability_index = round(delta_check * 1.73)
elif delta_check <= 10 or not filtered_scores:
    final_stability_index = round(sum(filtered_scores))
else:
    final_stability_index = 42

print(f"Result: {final_stability_index}")