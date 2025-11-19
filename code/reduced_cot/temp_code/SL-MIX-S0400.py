import math
import heapq
from functools import reduce
from collections import defaultdict

def fibonacci_mod_log(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        c = (a + b) % mod
        if i % 3 == 0:
            log_factor = int(math.log(i) * 10) % mod
            c = (c - log_factor) % mod
        a, b = b, c
    return b

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

# Generate sequence
mod = 100
sequence = [fibonacci_mod_log(i, mod) for i in range(7)]

# Build binary tree
root = None
root = insert_level_order(sequence, root, 0, len(sequence))

# Inorder traversal to get node values in list
node_values = []
inorder_traversal(root, node_values)

# Metadata dictionary comprehension with merging
metadata_base = {i: f"phase_{i}" for i in range(len(node_values))}
metadata_extra = {i: {"value": val, "hash": hash(f"phase_{i}") % 1000} for i, val in enumerate(node_values)}
merged_metadata = {k: {"name": metadata_base[k], **metadata_extra[k]} for k in metadata_base}

# Cumulative sum of transformed string hashes
hashes = [abs(hash(v["name"]) ^ v["hash"]) for v in merged_metadata.values()]
cumulative_hash_sum = reduce(lambda x, y: (x + y) % mod, hashes, 0)

print(f"Result: {cumulative_hash_sum}")