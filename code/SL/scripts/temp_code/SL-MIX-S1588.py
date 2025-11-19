from collections import namedtuple

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def transform_leaves(leaf_str):
    # Apply string transformation: reverse and duplicate each digit
    transformed = ''.join([char * 2 for char in leaf_str[::-1]])
    return int(transformed) if transformed.isdigit() else 0

def calculate_leaf_count(node):
    if not node:
        return 0
    
    # Convert node value to string and apply transformation
    leaf_str = str(node.value)
    transformed_value = transform_leaves(leaf_str)
    
    # Recursively calculate for children and sum
    left_count = calculate_leaf_count(node.left)
    right_count = calculate_leaf_count(node.right)
    
    return transformed_value + left_count + right_count

def build_sample_tree():
    # Build a simple binary tree
    #       12
    #      /  \
    #     3    45
    root = TreeNode(12)
    root.left = TreeNode(3)
    root.right = TreeNode(45)
    return root

# Execution point Y
tree_root = build_sample_tree()
final_leaf_count = calculate_leaf_count(tree_root)
print(f"Result: {final_leaf_count}")