from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        current = queue.popleft()
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def calculate_vitality_sum(root):
    if not root:
        return 0
    
    total_vitality = 0
    queue = deque([(root, 0)])  # (node, depth)
    
    while queue:
        node, depth = queue.popleft()
        leaves_in_subtree = count_leaves(node)
        vitality_score = depth * leaves_in_subtree
        total_vitality += vitality_score
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return total_vitality

tree_structure = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], [7, None, None]]]
flattened_structure = [1, 2, 3, 4, 5, 6, 7]
root = build_tree(flattened_structure)
vitality_sum_result = calculate_vitality_sum(root)
print(f"Result: {vitality_sum_result}")