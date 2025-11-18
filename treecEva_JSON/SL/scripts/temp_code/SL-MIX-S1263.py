from collections import deque
import math

def calculate_euclidean_distance(x, y):
    return math.sqrt(x**2 + y**2)

# Movement commands: (direction, distance)
# Directions: 'N' (North/y+), 'S' (South/y-), 'E' (East/x+), 'W' (West/x-)
command_queue = deque([('E', 5), ('N', 3), ('W', 2), ('N', 4), ('E', 1)])

# Robot starts at origin
robot_x, robot_y = 0, 0

# Execute all movement commands
while command_queue:
    direction, distance = command_queue.popleft()
    if direction == 'N':
        robot_y += distance
    elif direction == 'S':
        robot_y -= distance
    elif direction == 'E':
        robot_x += distance
    elif direction == 'W':
        robot_x -= distance

# Calculate final Euclidean distance from origin
final_distance = calculate_euclidean_distance(robot_x, robot_y)
print(f'Result: {final_distance}')