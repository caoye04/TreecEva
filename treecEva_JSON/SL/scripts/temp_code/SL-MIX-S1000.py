from collections import deque

token_stream = deque(['BEGIN', 'VAR', 'BEGIN', 'IF', 'THEN', 'ELSE', 'END', 'ASSIGN', 'BEGIN', 'WHILE', 'DO', 'END', 'END'])
block_stack = []
nesting_depth = 0
aggregated_signature = 0

while token_stream:
    token = token_stream.popleft()
    if token == 'BEGIN':
        nesting_depth += 1
        block_stack.append({'start_depth': nesting_depth, 'content_sum': 0})
    elif token == 'END' and block_stack:
        block_info = block_stack.pop()
        depth_contribution = block_info['start_depth']
        content_contribution = block_info['content_sum']
        block_signature = depth_contribution + content_contribution
        aggregated_signature += block_signature
        if block_stack:
            block_stack[-1]['content_sum'] += ord('E') + ord('N') + ord('D')
    else:
        ascii_sum = sum(ord(char) for char in token)
        if block_stack:
            block_stack[-1]['content_sum'] += ascii_sum

print(f"Result: {aggregated_signature}")