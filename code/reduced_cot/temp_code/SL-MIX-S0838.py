from collections import deque
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def harmonic_mean(values):
    n = len(values)
    if n == 0:
        return 0
    return n / sum(1/x for x in values)

class FungalNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_fibonacci_tree(levels):
    fib = [1, 1]
    for i in range(2, levels + 5):  # Extra to ensure sufficient values
        fib.append(fib[-1] + fib[-2])
    
    root = FungalNode(fib[0])
    queue = deque([root])
    fib_index = 1
    
    for level in range(levels - 1):
        for _ in range(len(queue)):
            node = queue.popleft()
            if fib_index < len(fib):
                node.left = FungalNode(fib[fib_index])
                fib_index += 1
                queue.append(node.left)
            if fib_index < len(fib):
                node.right = FungalNode(fib[fib_index])
                fib_index += 1
                queue.append(node.right)
    return root

def collect_leaves(node):
    if not node:
        return []
    if not node.left and not node.right:
        return [node.value]
    return collect_leaves(node.left) + collect_leaves(node.right)

tree_root = build_fibonacci_tree(7)
leaf_values = collect_leaves(tree_root)

lcm_of_leaves = leaf_values[0]
for val in leaf_values[1:]:
    lcm_of_leaves = lcm(lcm_of_leaves, val)

nutrient_queue = deque()
for i in range(1, 11):
    nutrient_concentration = lcm_of_leaves // i
    nutrient_queue.append(nutrient_concentration)

concentrations = list(nutrient_queue)[:5]
final_harmonic_mean = harmonic_mean(concentrations)
print(f"Result: {final_harmonic_mean}")