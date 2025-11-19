import heapq
import itertools
from math import sqrt

def calculate_triangle_area(a, b, c):
    # Using Heron's formula
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_side_lengths(vertices):
    pairs = list(itertools.combinations(vertices, 2))
    return [distance(p[0], p[1]) for p in pairs]

# Triangular plot vertices (x, y coordinates)
plots = [
    [(0, 0), (4, 0), (2, 3)],
    [(1, 1), (5, 1), (3, 4)],
    [(0, 2), (3, 5), (6, 2)]
]

quality_scores = []

for plot in plots:
    sides = get_side_lengths(plot)
    area = calculate_triangle_area(*sides)
    perimeter = sum(sides)
    # Score calculation combines area, perimeter, and coordinate sums
    coord_sum = sum(x + y for x, y in plot)
    score = area * 0.5 + perimeter * 0.3 + coord_sum * 0.2
    heapq.heappush(quality_scores, -score)  # Max heap using negative values

# Extract top 2 scores
first = -heapq.heappop(quality_scores)
second = -heapq.heappop(quality_scores)

# Final score is weighted combination
final_score = first * 0.7 + second * 0.3

print(f"Result: {round(final_score, 2)}")