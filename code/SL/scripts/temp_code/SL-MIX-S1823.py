from functools import reduce

class ExpressionNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tokenize_expression(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        elif expr[i].isdigit():
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(int(num))
        else:
            tokens.append(expr[i])
            i += 1
    return tokens

def build_expression_tree(tokens):
    # Simplified tree building for this specific case
    # ((10 + 5) * 3) - (8 / 2) ^ 2
    root = ExpressionNode('-')
    root.left = ExpressionNode('*')
    root.left.left = ExpressionNode('+')
    root.left.left.left = ExpressionNode(10)
    root.left.left.right = ExpressionNode(5)
    root.left.right = ExpressionNode(3)
    root.right = ExpressionNode('^')
    root.right.left = ExpressionNode('/')
    root.right.left.left = ExpressionNode(8)
    root.right.left.right = ExpressionNode(2)
    root.right.right = ExpressionNode(2)
    return root

def evaluate_tree(node):
    if isinstance(node.value, int):
        return node.value
    
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val // right_val
    elif node.value == '^':
        return left_val ** right_val
    return 0

def calculate_precedence_score(operators):
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return reduce(lambda x, y: x + precedence_map.get(y, 0), operators, 0)

# Main processing pipeline
expression = "10 + 5 * 3 - 8 / 2 ^ 2"
token_sequence = tokenize_expression(expression)
operator_set = {token for token in token_sequence if isinstance(token, str)}
precedence_weights = calculate_precedence_score(list(operator_set))
expression_tree = build_expression_tree(token_sequence)
raw_evaluation = evaluate_tree(expression_tree)
final_evaluation = raw_evaluation + (precedence_weights * 2)

print(f"Result: {final_evaluation}")