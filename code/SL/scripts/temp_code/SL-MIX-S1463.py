import heapq

class JointNode:
    def __init__(self, adjustment, next_node=None):
        self.adjustment = adjustment
        self.next = next_node

def build_command_sequence(adjustments):
    head = None
    for adj in reversed(adjustments):
        head = JointNode(adj, head)
    return head

def process_joint_chain(head):
    total = 0
    current = head
    while current and total >= 0:  # Short-circuit: stop if total goes negative
        total += current.adjustment
        current = current.next
    return total

# Priority queue of commands: (priority, joint_adjustments_list)
command_heap = []
commands = [
    (3, [15, -7, 12]),      # Priority 3
    (1, [20, -5, 3]),       # Priority 1
    (4, [-10, 8, 2]),       # Priority 4 (highest)
    (2, [5, 5, -4])         # Priority 2
]

for priority, adjustments in commands:
    chain = build_command_sequence(adjustments)
    heapq.heappush(command_heap, (-priority, id(chain), chain))  # Max-heap using negated priority

joint_omega_cumulative = 0
processed_count = 0
max_commands = 3

while command_heap and processed_count < max_commands:
    _, _, command_chain = heapq.heappop(command_heap)
    local_adjustment = process_joint_chain(command_chain)
    # Apply adjustment only if it's positive and total won't exceed 100
    if local_adjustment > 0 and (joint_omega_cumulative + local_adjustment) <= 100:
        joint_omega_cumulative += local_adjustment
    processed_count += 1

print(f"Result: {joint_omega_cumulative}")