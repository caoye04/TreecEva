from collections import deque

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(limit):
    fib = [0, 1]
    while len(fib) < limit:
        fib.append(fib[-1] + fib[-2])
    return fib

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_fibonacci_tree(depth):
    if depth <= 0:
        return None
    
    fib_nums = fibonacci_sequence(2**depth)
    root = TreeNode(fib_nums[0])
    queue = deque([root])
    index = 1
    
    for level in range(1, depth):
        for _ in range(len(queue)):
            node = queue.popleft()
            if index < len(fib_nums):
                node.left = TreeNode(fib_nums[index])
                queue.append(node.left)
                index += 1
            if index < len(fib_nums):
                node.right = TreeNode(fib_nums[index])
                queue.append(node.right)
                index += 1
    return root

def collect_leaves(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    leaves = []
    if root.left:
        leaves.extend(collect_leaves(root.left))
    if root.right:
        leaves.extend(collect_leaves(root.right))
    return leaves

# Build a binary tree with depth 4
botanical_tree = build_fibonacci_tree(4)

# Collect all leaf values
leaf_values = collect_leaves(botanical_tree)

# Filter for prime numbers using list comprehension
prime_leaves = [val for val in leaf_values if is_prime(val)]

# Calculate the sum of prime leaf values
prime_leaf_sum = sum(prime_leaves)

print(f"Result: {prime_leaf_sum}")