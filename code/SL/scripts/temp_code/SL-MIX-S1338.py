from collections import deque
from functools import reduce

tokens = ['3', '5', '+', '2', '*', '4', '-']
operand_stack = []
operator_queue = deque()

# Process tokens
for token in tokens:
    if token.isdigit():
        operand_stack.append(int(token))
    else:
        operator_queue.append(token)

# Apply operations using lambda functions
operations = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y
}

while operator_queue:
    op = operator_queue.popleft()
    if len(operand_stack) >= 2:
        b = operand_stack.pop()
        a = operand_stack.pop()
        result = operations[op](a, b)
        operand_stack.append(result)

# Build binary tree from remaining operands
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = build_tree(values[:mid])
    root.right = build_tree(values[mid+1:])
    return root

tree_root = build_tree(operand_stack)

# Evaluate tree with different lambdas per level
def evaluate_tree(node, level=0):
    if not node:
        return 0
    if not node.left and not node.right:
        return node.val
    
    left_val = evaluate_tree(node.left, level + 1)
    right_val = evaluate_tree(node.right, level + 1)
    
    # Switch-like logic using dictionary
    level_ops = {
        0: lambda x, y: x + y,
        1: lambda x, y: x * y,
        2: lambda x, y: x - y
    }
    
    operation = level_ops.get(level % 3, lambda x, y: x + y)
    return operation(left_val, right_val)

final_evaluation = evaluate_tree(tree_root)
print(f'Result: {final_evaluation}')