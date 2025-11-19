from functools import reduce

class SensorNode:
    def __init__(self, identifier, left=None, right=None):
        self.id = identifier
        self.left = left
        self.right = right

def compute_route_efficiency(route):
    # Route is a list of node identifiers
    if not route:
        return 0
    product = reduce(lambda x, y: x * y, route, 1)
    return product if product % 2 == 0 else -product

def traverse_and_score(node, current_path=[]):
    if not node:
        return []
    new_path = current_path + [node.id]
    if not node.left and not node.right:
        return [compute_route_efficiency(new_path)]
    left_scores = traverse_and_score(node.left, new_path)
    right_scores = traverse_and_score(node.right, new_path)
    return left_scores + right_scores

# Constructing the sensor network tree
#                 3
#               /   \
#              5     2
#             / \   / \
#            7   1 4   6
root = SensorNode(3)
root.left = SensorNode(5)
root.right = SensorNode(2)
root.left.left = SensorNode(7)
root.left.right = SensorNode(1)
root.right.left = SensorNode(4)
root.right.right = SensorNode(6)

all_scores = traverse_and_score(root)
optimal_score = max(all_scores) if all_scores else 0

print(f"Result: {optimal_score}")