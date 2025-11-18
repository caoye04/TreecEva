from functools import reduce

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(depth, leaves):
    if depth == 0:
        val = leaves.pop() if leaves else 0
        return TreeNode(val)
    left = build_tree(depth - 1, leaves)
    right = build_tree(depth - 1, leaves)
    node = TreeNode(0, left, right)
    node.val = (left.val + right.val) % 1000
    return node

def traverse_with_pruning(root):
    if not root:
        return 0
    stack = [root]
    total = 0
    while stack:
        node = stack.pop()
        if node.val > 500:  # Pruning condition
            continue
        total += node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return total

# Initial growth factors
initial_factors = [2, 3, 5, 8] * 2  # Extend to match required nodes

# Build the binary tree with depth 3 (requires 8 leaves)
root = build_tree(3, initial_factors[::-1])

# Traverse with pruning to calculate orchid score
orchid_score = traverse_with_pruning(root)
print(f"Result: {orchid_score}")