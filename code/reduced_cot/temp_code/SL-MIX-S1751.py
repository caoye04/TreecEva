from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_tokens(tokens):
    stack = []
    root = None
    current = None
    
    for token in tokens:
        if token == 1:  # Opening tag
            node = TreeNode(1)
            if not root:
                root = node
                current = root
            else:
                if current:
                    if not current.left:
                        current.left = node
                    elif not current.right:
                        current.right = node
                    stack.append(current)
                current = node
        elif token == -1 and current:  # Closing tag
            if stack:
                current = stack.pop()
    return root

def calculate_max_depth(node):
    if not node:
        return 0
    left_depth = calculate_max_depth(node.left)
    right_depth = calculate_max_depth(node.right)
    return max(left_depth, right_depth) + 1

token_stream = [1, 1, -1, 1, 1, -1, -1, -1]

# Parse tokens into tree structure
syntax_tree_root = build_tree_from_tokens(token_stream)

# Calculate maximum nesting depth
max_depth = calculate_max_depth(syntax_tree_root) if syntax_tree_root else 0

print(f"Result: {max_depth}")