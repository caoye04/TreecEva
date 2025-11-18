import math
from functools import reduce

class WaypointNode:
    def __init__(self, x, y, next_node=None):
        self.x = x
        self.y = y
        self.next = next_node

def decode_coordinate(encoded_str):
    parts = encoded_str.split(',')
    return float(parts[0]), float(parts[1])

def encode_coordinate(x, y):
    return f"{x:.1f},{y:.1f}"

# Create linked list of waypoints from encoded strings
encoded_waypoints = ["1.0,2.0", "4.0,6.0", "8.0,3.0", "10.0,7.0"]
head = None
for coord_str in reversed(encoded_waypoints):
    x, y = decode_coordinate(coord_str)
    head = WaypointNode(x, y, head)

# Efficiency calculation lambda with closure over base_weight
base_weight = 1.5
efficiency_calculator = lambda node: base_weight * math.sqrt(node.x**2 + node.y**2) + math.atan2(node.y, node.x)

# Process waypoints using functional programming
waypoint_nodes = []
current = head
while current:
    waypoint_nodes.append(current)
    current = current.next

# Apply transformation and filtering
filtered_scores = list(map(efficiency_calculator, filter(lambda n: n.x > 2.0, waypoint_nodes)))

# Calculate cumulative efficiency with geometric adjustment
geometric_factor = reduce(lambda acc, score: acc + math.log(abs(score)+1), filtered_scores, 0)
cumulative_efficiency = round(geometric_factor * 1000)

print(f"Result: {cumulative_efficiency}")