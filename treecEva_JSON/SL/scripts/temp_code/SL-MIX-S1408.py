from collections import deque, defaultdict
from functools import reduce

token_stream = ['IF', 'LPAREN', 'IDENT', 'GT', 'NUM', 'RPAREN', 'LBRACE', 'IDENT', 'EQ', 'NUM', 'SEMICOLON', 'RBRACE']
token_stack = []
token_queue = deque(token_stream)
token_counts = defaultdict(int)
scope_depth = 0
max_scope = 0

while token_queue:
    token = token_queue.popleft()
    token_counts[token] += 1
    
    if token == 'LBRACE':
        token_stack.append(token)
        scope_depth += 1
        max_scope = max(max_scope, scope_depth)
    elif token == 'RBRACE' and token_stack and token_stack[-1] == 'LBRACE':
        token_stack.pop()
        scope_depth -= 1
    elif token == 'LPAREN':
        token_stack.append(token)
    elif token == 'RPAREN' and token_stack and token_stack[-1] == 'LPAREN':
        token_stack.pop()
    
    # Short-circuit evaluation: if we have more than 2 IF tokens and less than 2 SEMICOLON tokens
    if token_counts['IF'] > 2 and token_counts['SEMICOLON'] < 2:
        scope_depth += 1
    
    # Complex condition using reduce to check if any brace-like token count exceeds threshold
    brace_tokens = [token_counts['LBRACE'], token_counts['RBRACE'], token_counts['LPAREN'], token_counts['RPAREN']]
    if reduce(lambda x, y: x + y, filter(lambda z: z > 1, brace_tokens), 0) > 2:
        if scope_depth > 0:
            scope_depth -= 1

# Final adjustment based on token balance
if len(token_stack) > 0:
    scope_depth = max(0, scope_depth - len(token_stack))

print(f"Result: {scope_depth}")