import itertools

token_stream = ['+', '*', '(', ')', '-', '/', '^', 'sin', 'cos', 'log']
precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sin': 4, 'cos': 4, 'log': 4}
parenthesis_stack = []
aggregated_precedence = 0

for token in token_stream:
    if token in precedence_map:
        current_score = precedence_map[token]
        if parenthesis_stack:
            # Inside parentheses, boost precedence by 1 but cap at 5
            boosted = min(current_score + 1, 5)
            aggregated_precedence += boosted
        else:
            aggregated_precedence += current_score
    elif token == '(':
        parenthesis_stack.append(token)
    elif token == ')' and parenthesis_stack:
        parenthesis_stack.pop()
        # Apply a closure bonus only if stack is now empty
        if not parenthesis_stack:
            aggregated_precedence += sum(filter(lambda x: x > 2, precedence_map.values()))

print(f"Result: {aggregated_precedence}")