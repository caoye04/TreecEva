from functools import reduce
from itertools import combinations

def calculate_triangle_quality(vertices):
    # Calculate area using cross product formula
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
    perimeter = sum(((vertices[i][0]-vertices[(i+1)%3][0])**2 + (vertices[i][1]-vertices[(i+1)%3][1])**2)**0.5 for i in range(3))
    return area/perimeter if perimeter > 0 else 0

def greedy_vertex_adjustment(triangle_vertices):
    base_quality = calculate_triangle_quality(triangle_vertices)
    adjustments = [(0,0), (0.1,0), (-0.1,0), (0,0.1), (0,-0.1)]
    best_quality = base_quality
    for i in range(3):
        for dx, dy in adjustments:
            new_vertices = [list(v) for v in triangle_vertices]
            new_vertices[i][0] += dx
            new_vertices[i][1] += dy
            new_quality = calculate_triangle_quality(new_vertices)
            if new_quality > best_quality:
                best_quality = new_quality
    return best_quality

def process_triangles_dc(triangles_list):
    if len(triangles_list) <= 1:
        return [greedy_vertex_adjustment(t) for t in triangles_list]
    mid = len(triangles_list) // 2
    left_results = process_triangles_dc(triangles_list[:mid])
    right_results = process_triangles_dc(triangles_list[mid:])
    return left_results + right_results

def find_optimal_reconfiguration(triangle_qualities):
    n = len(triangle_qualities)
    if n < 3:
        return sum(triangle_qualities)
    max_sum = 0
    for combo in combinations(range(n), 3):
        subset = [triangle_qualities[i] for i in combo]
        current_sum = sum(subset)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Simulation data
triangular_meshes = [
    [[0, 0], [1, 0], [0, 1]],
    [[2, 2], [3, 2], [2, 3]],
    [[4, 1], [5, 1], [4.5, 2]],
    [[1, 4], [2, 3], [3, 4]],
    [[6, 6], [7, 5], [8, 6]]
]

# Process triangles with divide and conquer
processed_qualities = process_triangles_dc(triangular_meshes)

# Apply combinatorial optimization to find best triplet
optimized_score = find_optimal_reconfiguration(processed_qualities)

print(f"Result: {optimized_score}")