from functools import reduce

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_tokens(tokens):
    stack = []
    for tok in tokens:
        if tok.isdigit():
            stack.append(TreeNode(int(tok)))
        else:
            right_child = stack.pop()
            left_child = stack.pop()
            node = TreeNode(0, left_child, right_child)
            stack.append(node)
    return stack[0] if stack else None

def evaluate_tree(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return node.val
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    # Encoding rule: if operator is '+', use XOR; if '-', use AND; else OR
    node.val = left_val ^ right_val if node.val == 0 else (left_val & right_val if node.val == 1 else left_val | right_val)
    return node.val

# Encoded token stream: postfix notation with operands and operators represented as 0('+'), 1('-'), 2('*')
token_stream = ['3', '5', '0', '7', '2', '1', '0']  # Represents ((3 XOR 5) OR (7 AND 2))
tree_root = build_tree_from_tokens(token_stream)
evaluated_result = evaluate_tree(tree_root)
print(f"Result: {evaluated_result}")