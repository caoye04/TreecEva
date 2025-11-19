class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def encode(value):
    return value * 3 + 7

def decode(encoded_value):
    return (encoded_value - 7) // 3

def build_tree():
    # Building a simple binary tree:
    #       4
    #      / \
    #     2   6
    #    /|   |\
    #   1 3   5 8
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(8)
    return root

def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [encode(node.val)] + inorder_traversal(node.right)

# Build the tree and get encoded in-order traversal
root = build_tree()
encoded_values = inorder_traversal(root)

# Decode the values and compute their sum
node_values_sum = sum(decode(val) for val in encoded_values)

print(f"Result: {node_values_sum}")