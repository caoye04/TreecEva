from functools import wraps
from collections import defaultdict
import math

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

@performance_monitor
def calculate_euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

@performance_monitor
def dp_route_optimizer(points):
    n = len(points)
    # Memoization table for dynamic programming
    memo = {}
    
    def dp(current, visited_mask):
        if visited_mask == (1 << n) - 1:
            return calculate_euclidean(points[current], points[0])
        
        if (current, visited_mask) in memo:
            return memo[(current, visited_mask)]
        
        min_dist = float('inf')
        for i in range(n):
            if not (visited_mask & (1 << i)):
                dist = calculate_euclidean(points[current], points[i]) + dp(i, visited_mask | (1 << i))
                min_dist = min(min_dist, dist)
        
        memo[(current, visited_mask)] = min_dist
        return min_dist
    
    return dp(0, 1)

# Delivery coordinates in a city grid
warehouse_locations = [
    (0, 0),     # Distribution center
    (3, 4),     # Retail store Alpha
    (-2, 5),    # Office complex Beta
    (1, -3),    # Commercial plaza Gamma
    (-4, -1)    # Industrial zone Delta
]

# Optimization process
optimized_distance = dp_route_optimizer(warehouse_locations)
print(f'Result: {round(optimized_distance)}')