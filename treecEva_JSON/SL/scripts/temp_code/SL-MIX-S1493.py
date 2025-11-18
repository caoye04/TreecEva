from functools import reduce
from math import comb

class TreeNode:
    def __init__(self, growth_rate=0):
        self.growth_rate = growth_rate
        self.left = None
        self.right = None

def calculate_branch_factor(node):
    if not node:
        return 0
    left_factor = calculate_branch_factor(node.left)
    right_factor = calculate_branch_factor(node.right)
    combinations = comb(max(1, left_factor + right_factor), min(2, left_factor, right_factor))
    return node.growth_rate + combinations

tree_root = TreeNode(3)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(4)
tree_root.left.left = TreeNode(1)
tree_root.left.right = TreeNode(3)

growth_factors = {}
with open('growth_data.txt', 'w') as f:
    f.write('initial')

with open('growth_data.txt', 'r+') as f:
    content = f.read()
    if content == 'initial':
        factor_a = calculate_branch_factor(tree_root)
        factor_b = reduce(lambda x, y: x * y, [n.growth_rate for n in [tree_root, tree_root.left, tree_root.right]], 1)
        growth_factors['alpha'] = factor_a + factor_b
        f.seek(0)
        f.write(str(growth_factors['alpha']))
        f.truncate()

with open('growth_data.txt', 'r') as f:
    stored_value = int(f.read())
    adjusted_factor = (stored_value ** 2) // (tree_root.growth_rate + 1)
    normalized_score = adjusted_factor - sum([tree_root.left.left.growth_rate, tree_root.left.right.growth_rate])
    final_growth_score = normalized_score >> 1  # Right shift by 1 is equivalent to integer division by 2

print(f'Result: {final_growth_score}')