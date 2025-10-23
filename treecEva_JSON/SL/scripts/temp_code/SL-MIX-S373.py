from collections import deque
from math import sqrt
from functools import reduce
from dataclasses import dataclass

def harmonic_mean(values):
    if not values or 0 in values:
        return 0
    n = len(values)
    reciprocal_sum = sum(1.0 / v for v in values)
    return n / reciprocal_sum

@dataclass
class Position:
    x: float
    y: float
    depth: float

# Underwater drone trajectory
positions = [
    Position(0.0, 0.0, 10.0),
    Position(3.0, 4.0, 12.0),
    Position(7.0, 8.0, 9.0),
    Position(10.0, 12.0, 15.0)
]

depth_changes = []
cumulative_displacement = 0.0
position_stack = deque()

for i in range(1, len(positions)):
    prev_pos = positions[i-1]
    curr_pos = positions[i]
    
    delta_x = curr_pos.x - prev_pos.x
    delta_y = curr_pos.y - prev_pos.y
    delta_z = curr_pos.depth - prev_pos.depth
    
    segment_distance = sqrt(delta_x**2 + delta_y**2 + delta_z**2)
    cumulative_displacement += segment_distance
    
    if delta_z != 0:
        depth_changes.append(abs(delta_z))
    
    position_stack.appendleft((delta_x, delta_y, delta_z))

if depth_changes:
    smoothing_factor = harmonic_mean(depth_changes) / max(depth_changes)
else:
    smoothing_factor = 1.0

smoothed_trajectory_length = cumulative_displacement * smoothing_factor

print(f"Result: {smoothed_trajectory_length}")