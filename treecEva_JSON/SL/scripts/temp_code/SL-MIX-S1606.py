import heapq
import re

def tokenize(expr):
    return re.findall(r'\d+|[+\-*/()]', expr)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_expression_tree(tokens):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    ops_heap = []  # Min-heap of (precedence, operator)
    vals_stack = []
    
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.isdigit():
            vals_stack.append(TreeNode(int(t)))
        elif t in prec:
            heapq.heappush(ops_heap, (prec[t], t))
        i += 1
    
    # Simplified tree building: use heap to determine operation order
    while ops_heap:
        _, op = heapq.heappop(ops_heap)
        if len(vals_stack) >= 2:
            right = vals_stack.pop()
            left = vals_stack.pop()
            node = TreeNode(op, left, right)
            vals_stack.append(node)
    
    return vals_stack[0] if vals_stack else None

def evaluate_tree(node):
    if not node:
        return 0
    if isinstance(node.val, int):
        return node.val
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    match node.val:
        case '+': return left_val + right_val
        case '-': return left_val - right_val
        case '*': return left_val * right_val
        case '/': return left_val // right_val if right_val != 0 else 0
        case _: return 0

expression = "3*4+2-5"
tokens = tokenize(expression)
root = build_expression_tree(tokens)
root_value = evaluate_tree(root) if root else 0
print(f"Result: {root_value}")