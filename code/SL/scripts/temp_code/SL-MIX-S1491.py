import itertools
import math

def base36_decode(s):
    return int(s, 36)

def is_valid_rectangle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return x1 < x2 and y1 < y2

def count_lattice_points_inside(x1, y1, x2, y2):
    return (x2 - x1 - 1) * (y2 - y1 - 1)

encoded_cells = ['1A3', 'Z2B', '5K9', 'X8M', '2R4']
decoded_coords = [divmod(base36_decode(cell), 100) for cell in encoded_cells]

rectangles = []
for p1, p2 in itertools.combinations(decoded_coords, 2):
    if is_valid_rectangle(p1, p2):
        rectangles.append((p1, p2))

selected_rectangles = []
rectangles.sort(key=lambda r: count_lattice_points_inside(r[0][0], r[0][1], r[1][0], r[1][1]), reverse=True)

used_points = set()
total_regions = 0

for rect in rectangles:
    p1, p2 = rect
    x1, y1 = p1
    x2, y2 = p2
    corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
    
    if not (corners & used_points):
        used_points.update(corners)
        total_regions += 1

print(f"Result: {total_regions}")