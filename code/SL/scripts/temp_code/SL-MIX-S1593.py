from functools import lru_cache
from itertools import combinations

class GeoPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

def tokenize_coordinates(coord_string):
    tokens = coord_string.strip().split(';')
    points = []
    for token in tokens:
        x, y = map(int, token.split(','))
        points.append(GeoPoint(x, y))
    return points

@lru_cache(maxsize=None)
def min_enclosing_rect(vertices_tuple):
    if len(vertices_tuple) <= 1:
        return 0
    
    xs = [p.x for p in vertices_tuple]
    ys = [p.y for p in vertices_tuple]
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    return 2 * (width + height)

def process_polygon_pipeline(raw_data):
    # Step 1: Parse coordinates
    vertex_points = tokenize_coordinates(raw_data)
    
    # Step 2: Generate all possible quadrilateral subsets
    quad_candidates = list(combinations(vertex_points, 4))
    
    # Step 3: Apply transformation filters
    valid_quads = [
        q for q in quad_candidates 
        if sum(p.x % 2 for p in q) == 2 and sum(p.y % 3 for p in q) <= 3
    ]
    
    # Step 4: Calculate optimized perimeters using DP
    perimeters = [
        min_enclosing_rect(tuple(sorted(quad, key=lambda p: (p.x, p.y))))
        for quad in valid_quads
    ]
    
    # Step 5: Find minimum perimeter with constraint
    if not perimeters:
        return 0
    
    # Additional filtering based on geometric properties
    filtered_perimeters = [
        p for p in perimeters 
        if p > 0 and p % 5 == 0
    ]
    
    return min(filtered_perimeters) if filtered_perimeters else 0

# Execution
polygon_data = "1,2;4,6;7,3;2,8;9,1;5,5;3,7;8,4"
transformed_data = ''.join(chr(ord(c) + 1) for c in polygon_data)[::-1]
restored_data = ''.join(chr(ord(c) - 1) for c in transformed_data)[::-1]

optimized_perimeter = process_polygon_pipeline(restored_data)
print(f"Result: {optimized_perimeter}")