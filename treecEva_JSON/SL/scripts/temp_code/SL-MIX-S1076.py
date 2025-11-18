from functools import reduce

class DeliveryNode:
    def __init__(self, time, left=None, right=None):
        self.time = time
        self.left = left
        self.right = right
        self.subtree_times = []

def collect_subtree_times(node):
    if not node:
        return []
    left_times = collect_subtree_times(node.left)
    right_times = collect_subtree_times(node.right)
    node.subtree_times = [node.time] + left_times + right_times
    return node.subtree_times

def calculate_min_time_for_valid_subtrees(node):
    if not node:
        return float('inf')
    
    min_time = float('inf')
    if len(node.subtree_times) >= 3:
        min_time = min(min_time, sum(sorted(node.subtree_times)[:3]))
    
    if node.left:
        min_time = min(min_time, calculate_min_time_for_valid_subtrees(node.left))
    if node.right:
        min_time = min(min_time, calculate_min_time_for_valid_subtrees(node.right))
    
    return min_time

# Build delivery tree
#       10
#      /  \
#     5    15
#    / \   / \
#   3   7 12  20
#  /
# 1
root = DeliveryNode(10)
root.left = DeliveryNode(5)
root.right = DeliveryNode(15)
root.left.left = DeliveryNode(3)
root.left.right = DeliveryNode(7)
root.right.left = DeliveryNode(12)
root.right.right = DeliveryNode(20)
root.left.left.left = DeliveryNode(1)

# Collect all subtree times
collect_subtree_times(root)

# Calculate minimum delivery time for subtrees with at least 3 nodes
min_delivery_time = calculate_min_time_for_valid_subtrees(root)

print(f"Result: {min_delivery_time}")