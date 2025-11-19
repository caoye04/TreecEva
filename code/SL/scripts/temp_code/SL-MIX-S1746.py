import math
from functools import reduce

class SurveyPoint:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

points = [
    SurveyPoint(0, 0, 2),
    SurveyPoint(3, 4, 3),
    SurveyPoint(1, 1, 5),
    SurveyPoint(2, 2, 7),
    SurveyPoint(5, 0, 11)
]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Calculate pairwise distances between consecutive points
distances = []
for i in range(len(points) - 1):
    dx = points[i+1].x - points[i].x
    dy = points[i+1].y - points[i].y
    dist = math.sqrt(dx*dx + dy*dy)
    distances.append(dist)

# Find prime identifiers that are also Fibonacci numbers
fib_set = {1, 2, 3, 5, 8, 13, 21, 34, 55}
prime_ids = {p.id for p in points}
fib_prime_intersection = frozenset(fib_set & prime_ids)

# Compute least common multiple of intersection sizes
lcm_accum = 1
for d in distances:
    size = len(fib_prime_intersection)
    if size > 0:
        lcm_accum = lcm(lcm_accum, size)

# Apply greedy selection of points with minimum coordinate sum
sorted_points = sorted(points, key=lambda p: p.x + p.y)
greedy_sum = 0
selected_points = set()
for p in sorted_points:
    if p.id in fib_prime_intersection and p.id not in selected_points:
        greedy_sum += p.x + p.y
        selected_points.add(p.id)

# Final checksum combines all computations
checksum = int(sum(distances) * lcm_accum + greedy_sum)
print(f"Result: {checksum}")