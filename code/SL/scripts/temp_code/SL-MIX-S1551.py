import hashlib

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hash_string(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16) % 10000

def build_fractal_tree(depth, path=''):
    if depth == 0:
        return None
    node_val = hash_string(path)
    node = TreeNode(node_val)
    node.left = build_fractal_tree(depth-1, path+'L')
    node.right = build_fractal_tree(depth-1, path+'R')
    return node

def collect_leaves(node, leaves_list):
    if not node:
        return
    if not node.left and not node.right:
        leaves_list.append(node.val)
    collect_leaves(node.left, leaves_list)
    collect_leaves(node.right, leaves_list)

def prune_subtree(node, target_path, current_path=''):
    if not node or current_path == target_path:
        return None
    node.left = prune_subtree(node.left, target_path, current_path+'L')
    node.right = prune_subtree(node.right, target_path, current_path+'R')
    return node

tree_root = build_fractal_tree(4)
leaves_before_pruning = []
collect_leaves(tree_root, leaves_before_pruning)
prune_subtree(tree_root, 'LL')
leaves_after_pruning = []
collect_leaves(tree_root, leaves_after_pruning)
pruned_leaves_sum = sum(leaves_before_pruning) - sum(leaves_after_pruning)
print(f"Result: {pruned_leaves_sum}")