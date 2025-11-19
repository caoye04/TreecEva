from dataclasses import dataclass
from typing import Dict, Tuple
import math

class RobotState:
    IDLE = 'IDLE'
    MOVING = 'MOVING'
    OBSTACLE = 'OBSTACLE'

@dataclass
class Position:
    x: int
    y: int
    
def manhattan_distance(pos: Position) -> int:
    return abs(pos.x) + abs(pos.y)

# Initial robot configuration
robot_position = Position(0, 0)
current_state = RobotState.IDLE

# Movement vectors for N, E, S, W
movements = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

# Obstacles in the warehouse (x, y) -> penalty
obstacles_map = {(2, 2): 1, (3, 1): 2, (0, 1): 1}

# Command sequence with state transitions
command_sequence = [
    ('MOVE', 'N', 3),
    ('CHECK', (0, 1)),
    ('MOVE', 'E', 2),
    ('CHECK', (2, 2)),
    ('MOVE', 'S', 1),
    ('CHECK', (3, 1))
]

for cmd in command_sequence:
    if cmd[0] == 'MOVE' and current_state != RobotState.OBSTACLE:
        direction, steps = cmd[1], cmd[2]
        dx, dy = movements[direction]
        robot_position.x += dx * steps
        robot_position.y += dy * steps
        current_state = RobotState.MOVING
    elif cmd[0] == 'CHECK':
        check_pos = cmd[1]
        if check_pos in obstacles_map:
            # Apply penalty and transition to obstacle state
            penalty = obstacles_map[check_pos]
            robot_position.x -= penalty
            robot_position.y -= penalty
            current_state = RobotState.OBSTACLE
            break  # Stop execution on obstacle
        else:
            current_state = RobotState.IDLE

final_distance = manhattan_distance(robot_position)
print(f'Result: {final_distance}')