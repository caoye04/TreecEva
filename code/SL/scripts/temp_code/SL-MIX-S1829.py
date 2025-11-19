import math
from collections import deque

# Robot navigation simulation with waypoint processing
waypoints = [(0, 0), (3, 4), (7, 1), (2, 6)]
movement_queue = deque()
orientation_scores = []

for i in range(len(waypoints) - 1):
    x1, y1 = waypoints[i]
    x2, y2 = waypoints[i + 1]
    
    # Calculate Euclidean distance between waypoints
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Determine movement priority based on distance and position
    priority = distance > 5 and x2 > y2
    
    if priority:
        movement_queue.appendleft((x2, y2))
    else:
        movement_queue.append((x2, y2))
    
    # Calculate orientation score using trigonometry
    angle_radians = math.atan2(y2 - y1, x2 - x1)
    orientation_score = round(math.cos(angle_radians) * 100)
    orientation_scores.append(orientation_score)

# Process movement queue to calculate final orientation adjustment
final_orientation_score = 0
while movement_queue:
    x, y = movement_queue.pop()
    adjustment = (x ^ y) & 0xF  # Bitwise XOR and mask
    final_orientation_score += adjustment

# Apply final logical condition
if len(orientation_scores) > 3 or sum(orientation_scores) < 0:
    final_orientation_score *= -1
else:
    final_orientation_score += 10

print(f"Result: {final_orientation_score}")