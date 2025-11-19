import heapq
from collections import defaultdict

class DistrictNode:
    def __init__(self, pollution, left=None, right=None):
        self.pollution = pollution
        self.left = left
        self.right = right

# Construct a binary tree representing city districts
# Level 0
root = DistrictNode(15)
# Level 1
root.left = DistrictNode(10)
root.right = DistrictNode(20)
# Level 2
root.left.left = DistrictNode(8)
root.left.right = DistrictNode(12)
root.right.left = DistrictNode(18)
root.right.right = DistrictNode(25)
# Level 3
root.left.left.left = DistrictNode(5)
root.left.left.right = DistrictNode(9)
root.left.right.left = DistrictNode(11)
root.right.right.right = DistrictNode(30)

def calculate_min_path_sum(node):
    if not node:
        return float('inf')
    if not node.left and not node.right:  # Leaf node
        return node.pollution
    left_sum = calculate_min_path_sum(node.left)
    right_sum = calculate_min_path_sum(node.right)
    return node.pollution + min(left_sum, right_sum)

min_pollution_score = calculate_min_path_sum(root)
print(f"Result: {min_pollution_score}")