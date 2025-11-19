import math
from collections import deque
from dataclasses import dataclass
from functools import reduce

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree():
    # Build a binary tree with specific values
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)
    return root

def compute_security_key(root):
    if not root:
        return 0
    
    queue = deque([root])
    xor_accumulator = 0
    log_sum = 0.0
    
    while queue:
        node = queue.popleft()
        # Apply bitwise XOR with shifted value
        shifted_val = node.val << 2
        xor_accumulator ^= shifted_val
        
        # Apply logarithmic transformation
        if node.val > 0:
            log_sum += math.log2(node.val)
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    # Final security key computation
    exponent_part = int(math.pow(2, log_sum % 3))
    security_key = xor_accumulator & exponent_part
    return security_key

tree_root = build_tree()
security_key = compute_security_key(tree_root)
print(f"Result: {security_key}")