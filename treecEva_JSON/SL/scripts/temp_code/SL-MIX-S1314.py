from functools import reduce

def calculate_rectangle_area(rect):
    x1, y1, x2, y2 = rect
    return abs((x2 - x1) * (y2 - y1))

def calculate_overlap_area(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    overlap_width = max(0, min(x2, x4) - max(x1, x3))
    overlap_height = max(0, min(y2, y4) - max(y1, y3))
    return overlap_width * overlap_height

rectangles = [
    (0, 0, 4, 4),
    (2, 2, 6, 6),
    (1, 1, 5, 5)
]

# Calculate individual areas
individual_areas = [calculate_rectangle_area(r) for r in rectangles]

# Calculate pairwise overlaps
pairwise_overlaps = [
    calculate_overlap_area(rectangles[i], rectangles[j])
    for i in range(len(rectangles))
    for j in range(i+1, len(rectangles))
]

# Calculate triple overlap using lambda and reduce
triple_overlap = reduce(
    lambda acc, idx: acc + calculate_overlap_area(rectangles[idx[0]], rectangles[idx[1]]),
    [(0, 1), (1, 2)],
    0
) if len(rectangles) >= 3 else 0

with open('temp_calc.txt', 'w') as f:
    f.write(f"Individual: {individual_areas}\n")
    f.write(f"Pairwise: {pairwise_overlaps}\n")
    f.write(f"Triple: {triple_overlap}\n")

# Apply inclusion-exclusion principle
sum_individual = sum(individual_areas)
sum_pairwise = sum(pairwise_overlaps)
total_overlap_area = sum_individual - sum_pairwise + triple_overlap

print(f"Result: {total_overlap_area}")