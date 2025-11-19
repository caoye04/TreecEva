from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_single_child_nodes(root):
    if not root:
        return 0
    
    queue = deque([root])
    single_child_count = 0
    
    while queue:
        node = queue.popleft()
        
        # Check if node has exactly one child
        if (node.left and not node.right) or (not node.left and node.right):
            single_child_count += 1
            
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return single_child_count

# Create the binary tree
#       1
#      / \
#     2   3
#    /   / \
#   4   5   6
#  /
# 7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)

single_child_count = count_single_child_nodes(root)
print(f"Result: {single_child_count}")