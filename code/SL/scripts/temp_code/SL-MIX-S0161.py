import math

class TriangleNode:
    def __init__(self, area=0, left=None, right=None):
        self.area = area
        self.left = left
        self.right = right

def calculate_leaf_areas(node):
    if not node:
        return []
    if not node.left and not node.right:
        return [node.area]
    return calculate_leaf_areas(node.left) + calculate_leaf_areas(node.right)

def combinatorial_aggregation(areas):
    if len(areas) < 2:
        return sum(areas)
    combinations_set = set()
    for i in range(len(areas)):
        for j in range(i+1, len(areas)):
            combinations_set.add(areas[i] + areas[j])
    return sum(combinations_set)

# Constructing the binary tree
#       10
#      /  \
#     5    15
#    / \   / \
#   3   7 12  20
root = TriangleNode(10)
root.left = TriangleNode(5)
root.right = TriangleNode(15)
root.left.left = TriangleNode(3)
root.left.right = TriangleNode(7)
root.right.left = TriangleNode(12)
root.right.right = TriangleNode(20)

# Extract leaf areas
leaf_areas = calculate_leaf_areas(root)

# Apply combinatorial aggregation using a lambda for transformation
transformed_areas = list(map(lambda x: round(math.sqrt(x), 2), leaf_areas))

# Calculate final aggregated surface area
aggregated_surface_area = combinatorial_aggregation(transformed_areas)

print(f"Result: {aggregated_surface_area}")