tokens = ['3', '+', '4', '*', '2', '-', '1']
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
precedence_stack = []

for token in tokens:
    if token in precedence:
        while (precedence_stack and 
               precedence.get(precedence_stack[-1], 0) >= precedence[token]):
            precedence_stack.pop()
        precedence_stack.append(token)
    else:
        # Token is a number; no action needed for this simulation
        pass

precedence_stack_size = len(precedence_stack)
print(f'Result: {precedence_stack_size}')