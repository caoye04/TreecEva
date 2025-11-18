from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

def build_tree():
    # Build a ternary tree with 3 levels
    # Leaves (level 3)
    leaves = [TreeNode(val=i%2) for i in range(1, 10)]  # Values: [1,0,1,0,1,0,1,0,1]
    
    # Level 2 nodes
    n2_1 = TreeNode(val=0, left=leaves[0], middle=leaves[1], right=leaves[2])
    n2_2 = TreeNode(val=0, left=leaves[3], middle=leaves[4], right=leaves[5])
    n2_3 = TreeNode(val=0, left=leaves[6], middle=leaves[7], right=leaves[8])
    
    # Root node (level 1)
    root = TreeNode(val=0, left=n2_1, middle=n2_2, right=n2_3)
    return root

def simulate_circuit(node):
    if not node:
        return 0
    if not node.left and not node.middle and not node.right:  # Leaf node
        return node.val
    
    # Recursively get child outputs
    left_out = simulate_circuit(node.left)
    middle_out = simulate_circuit(node.middle)
    right_out = simulate_circuit(node.right)
    
    # Count active signals
    active_count = sum([left_out, middle_out, right_out])
    
    # State machine for gate logic
    match active_count:
        case 1:
            return left_out ^ middle_out ^ right_out
        case 2:
            return left_out & middle_out & right_out
        case 3:
            return left_out | middle_out | right_out
        case _:
            return 0

tree_root = build_tree()
root_output = simulate_circuit(tree_root)
print(f"Result: {root_output}")