from collections import deque
import math

def calculate_segment_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def backtrack_optimize(path_deque, accumulated=0):
    if len(path_deque) <= 1:
        return accumulated
    current = path_deque.popleft()
    next_point = path_deque[0]
    distance = calculate_segment_distance(current, next_point)
    return backtrack_optimize(path_deque, accumulated + distance)

# Drone waypoints in 2D space
waypoints = deque([(0, 0), (3, 4), (7, 4), (7, 0)])
optimized_distance = backtrack_optimize(waypoints)
print(f'Result: {round(optimized_distance)}')