class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum_leaf_to_leaf(root):
    if not root:
        return 0
    
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_gain = helper(node.left)
        right_gain = helper(node.right)
        
        # Only include paths with positive contributions
        current_max = node.val + max(0, left_gain) + max(0, right_gain)
        max_sum = max(max_sum, current_max)
        
        # Return the max gain if continuing the path from parent
        return node.val + max(0, left_gain, right_gain)
    
    max_sum = float('-inf')
    helper(root)
    return max_sum

def build_risk_tree():
    # Risk factors for investment nodes
    root = TreeNode(-3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(-2)
    root.right.right = TreeNode(5)
    return root

# Main processing pipeline
risk_tree_root = build_risk_tree()
portfolio_stability_index = max_path_sum_leaf_to_leaf(risk_tree_root)
print(f"Result: {portfolio_stability_index}")