from math import sqrt
from functools import reduce

class MovementNode:
    def __init__(self, x, y, next_node=None):
        self.x = x
        self.y = y
        self.next = next_node

class EnergyTracker:
    def __init__(self):
        self.total_energy = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def consume(self, amount):
        self.total_energy += amount

# Build linked list: (3,4) -> (-1,2) -> (0,5) -> (2,-3) -> (1,1)
head = MovementNode(1, 1)
node4 = MovementNode(2, -3, head)
node3 = MovementNode(0, 5, node4)
node2 = MovementNode(-1, 2, node3)
node1 = MovementNode(3, 4, node2)

scaling_factor = 2.0
accumulated_distance = 0.0

with EnergyTracker() as tracker:
    current = node1
    positions = []
    while current:
        positions.append((current.x, current.y))
        current = current.next
    
    # Filter out moves with negative coordinates
    valid_moves = list(filter(lambda pos: pos[0] >= 0 and pos[1] >= 0, positions))
    
    # Scale valid moves
    scaled_moves = list(map(lambda pos: (pos[0] * scaling_factor, pos[1] * scaling_factor), valid_moves))
    
    # Calculate cumulative distance
    if scaled_moves:
        prev_x, prev_y = 0.0, 0.0
        for x, y in scaled_moves:
            delta = sqrt((x - prev_x)**2 + (y - prev_y)**2)
            accumulated_distance += delta
            prev_x, prev_y = x, y

print(f"Result: {round(accumulated_distance, 2)}")