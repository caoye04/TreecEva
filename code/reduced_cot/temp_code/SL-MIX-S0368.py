import heapq
from collections import defaultdict

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        else:
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(int(num))
    return tokens

def hash_token(token):
    if isinstance(token, int):
        return hash(str(token)) % 1000
    else:
        return hash(token) % 1000

# Priority queue for operators
operator_queue = []
# Stack for operands
operand_stack = []
# Accumulator for expression value
expression_value = 0

# Transformation function
transform = lambda x: x * 2 if isinstance(x, int) else ord(x[0])

# Input expression
input_expression = "3 + 5 * ( 2 + 8 )"
tokens = tokenize(input_expression)

precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

for token in tokens:
    token_hash = hash_token(token)
    transformed_token = transform(token)
    
    if isinstance(token, int):
        operand_stack.append(transformed_token)
    elif token == '(':
        heapq.heappush(operator_queue, (0, token))
    elif token == ')':
        while operator_queue and operator_queue[0][1] != '(':
            op = heapq.heappop(operator_queue)[1]
            if len(operand_stack) >= 2:
                b = operand_stack.pop()
                a = operand_stack.pop()
                if op == '+':
                    operand_stack.append(a + b)
                elif op == '-':
                    operand_stack.append(a - b)
                elif op == '*':
                    operand_stack.append(a * b)
                elif op == '/':
                    operand_stack.append(a // b)
        if operator_queue:
            heapq.heappop(operator_queue)  # Remove the '('
    elif token in precedence:
        while (operator_queue and 
               operator_queue[0][1] != '(' and
               precedence.get(operator_queue[0][1], 0) >= precedence[token]):
            op = heapq.heappop(operator_queue)[1]
            if len(operand_stack) >= 2:
                b = operand_stack.pop()
                a = operand_stack.pop()
                if op == '+':
                    operand_stack.append(a + b)
                elif op == '-':
                    operand_stack.append(a - b)
                elif op == '*':
                    operand_stack.append(a * b)
                elif op == '/':
                    operand_stack.append(a // b)
        heapq.heappush(operator_queue, (precedence[token], token))

while operator_queue:
    op = heapq.heappop(operator_queue)[1]
    if len(operand_stack) >= 2:
        b = operand_stack.pop()
        a = operand_stack.pop()
        if op == '+':
            operand_stack.append(a + b)
        elif op == '-':
            operand_stack.append(a - b)
        elif op == '*':
            operand_stack.append(a * b)
        elif op == '/':
            operand_stack.append(a // b)

if operand_stack:
    expression_value = operand_stack[0]

print(f"Result: {expression_value}")