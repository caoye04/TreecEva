from functools import reduce

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse(node):
    if not node:
        return []
    return [node.value] + traverse(node.left) + traverse(node.right)

# Tree structure:
#       5
#      / \
#     3   8
#    /   / \
#   2   7   9
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Extract all node values
node_values = traverse(root)

# Compute total growth using lambda and reduce
total_growth = reduce(lambda x, y: x + y, node_values)

print(f"Result: {total_growth}")