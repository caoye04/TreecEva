from collections import deque

class StorageNode:
    def __init__(self, capacity, occupancy, left=None, right=None):
        self.capacity = capacity
        self.occupancy = occupancy
        self.left = left
        self.right = right
    
    def is_violating(self):
        return (self.occupancy / self.capacity) > 0.8

def audit_warehouse(root):
    if not root:
        return 0
    
    violation_count = 0
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node.is_violating():
            violation_count += 1
            # Short-circuit: only check children if current node is violating
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # If not violating, do not add children to queue (short-circuit)
    
    return violation_count

# Constructing the warehouse tree
#       Root(100, 90)
#      /             \
#  Left(50, 45)    Right(200, 170)
#   /      \          /         \
# LL(30,25) LR(40,35) RL(100,90) RR(150,130)

root = StorageNode(100, 90)
root.left = StorageNode(50, 45)
root.right = StorageNode(200, 170)
root.left.left = StorageNode(30, 25)
root.left.right = StorageNode(40, 35)
root.right.left = StorageNode(100, 90)
root.right.right = StorageNode(150, 130)

violation_count = audit_warehouse(root)
print(f"Result: {violation_count}")