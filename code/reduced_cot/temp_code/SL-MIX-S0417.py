import math
from collections import deque

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def cross_product(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def convex_hull(points):
    points = sorted(set(points), key=lambda p: (p.x, p.y))
    if len(points) <= 1:
        return points
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def polygon_area(points):
    if len(points) < 3:
        return 0.0
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i].x * points[j].y
        area -= points[j].x * points[i].y
    return abs(area) / 2.0

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Trajectory data: list of lists of (x,y) tuples
trajectories = [
    [(0,0), (1,1), (2,0), (1,-1)],
    [(0,0), (0,2), (2,2), (2,0)],
    [(1,1), (3,1), (3,3), (1,3)]
]

stability_scores = []

for traj in trajectories:
    points = [Point(x, y) for x, y in traj]
    
    # Compute convex hull
    hull = convex_hull(points)
    hull_area = polygon_area(hull)
    
    # Compute bounding rectangle area
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    rect_area = (max(xs) - min(xs)) * (max(ys) - min(ys))
    
    # Compute distances and their standard deviation
    distances = [distance(points[i], points[i+1]) for i in range(len(points)-1)]
    if len(distances) == 0:
        std_dev = 0
    else:
        mean_dist = sum(distances) / len(distances)
        variance = sum((d - mean_dist) ** 2 for d in distances) / len(distances)
        std_dev = math.sqrt(variance)
    
    # Compute stability score
    if rect_area == 0 or std_dev == 0:
        score = 0
    else:
        score = (hull_area / rect_area) * (1 / std_dev)
    stability_scores.append(score)

# Dynamic programming to find maximum sum of stability scores with constraint
# Constraint: no two selected trajectories can be adjacent in the original list
n = len(stability_scores)
if n == 0:
    final_stability_score = 0
elif n == 1:
    final_stability_score = stability_scores[0]
else:
    dp = [0] * n
    dp[0] = stability_scores[0]
    dp[1] = max(stability_scores[0], stability_scores[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + stability_scores[i])
    final_stability_score = dp[n-1]

print(f"Result: {round(final_stability_score, 6)}")