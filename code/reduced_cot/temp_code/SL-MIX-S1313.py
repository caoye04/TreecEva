from collections import deque

class JointNode:
    def __init__(self, angle=0):
        self.angle = angle
        self.next = None

# Initialize mechanical components
rotational_stack = []  # Stack for angular adjustments
positional_queue = deque()  # Queue for linear corrections
base_joint = JointNode(45)
base_joint.next = JointNode(90)
base_joint.next.next = JointNode(135)

# Batch calculate modular adjustments using list comprehension
angular_modifications = [((x * 17) % 360) for x in range(5, 15)]

# Process adjustments through stack operations
for mod in angular_modifications[::2]:
    rotational_stack.append(mod)

# Apply positional corrections through queue
position_deltas = {10, 20, 30, 40, 50}
sensor_readings = {15, 25, 30, 45, 50}
valid_corrections = position_deltas & sensor_readings  # Set intersection

for correction in sorted(list(valid_corrections)):
    positional_queue.append(correction)

# Execute linked list traversal with accumulated modifications
current_node = base_joint
accumulated_torque = 0

while current_node:
    if rotational_stack:
        angular_adj = rotational_stack.pop()
    else:
        angular_adj = 0
        
    if positional_queue:
        position_adj = positional_queue.popleft()
    else:
        position_adj = 0
    
    # Calculate combined mechanical effect
    node_contribution = (current_node.angle + angular_adj - position_adj) % 180
    accumulated_torque = (accumulated_torque * 2 + node_contribution) % 1000
    current_node = current_node.next

# Final adjustment calculation
final_torque = (accumulated_torque * sum(angular_modifications[-3:]) - len(valid_corrections)) % 500
print(f"Result: {final_torque}")