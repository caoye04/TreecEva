import re
from collections import deque

def tokenize(expression):
    return re.findall(r'\d+|[+\-*/^()]', expression)

def parse_expression(tokens):
    # Simple precedence: ^ (right assoc), *, /, +, - (left assoc)
    def apply_op(ops, values):
        op = ops.pop()
        right = values.pop()
        left = values.pop()
        if op == '+': values.append(left + right)
        elif op == '-': values.append(left - right)
        elif op == '*': values.append(left * right)
        elif op == '/': values.append(left // right)
        elif op == '^': values.append(left ** right)
    
    values = []
    ops = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        else:
            while (ops and ops[-1] != '(' and 
                   precedence.get(ops[-1], 0) >= precedence.get(token, 0) and
                   not (token == '^' and ops[-1] == '^')):
                apply_op(ops, values)
            ops.append(token)
    
    while ops:
        apply_op(ops, values)
    
    return values[0]

token_sequence = ['3', '*', '4', '+', '2', '^', '3']
evaluated_result = parse_expression(token_sequence)
print(f'Result: {evaluated_result}')