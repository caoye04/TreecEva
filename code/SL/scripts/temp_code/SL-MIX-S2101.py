from collections import deque

token_stream = ['TAG_A', 5, 'TAG_B', 3, 'TAG_C', 2, 7, 4]
tag_stack_map = {}
current_tag = None
stack = deque()

i = 0
while i < len(token_stream):
    token = token_stream[i]
    if isinstance(token, str) and token.startswith('TAG'):
        current_tag = token
        tag_stack_map[current_tag] = deque()
    elif isinstance(token, int):
        if current_tag:
            tag_stack_map[current_tag].append(token)
            stack.append(token)
        else:
            if stack:
                top_val = stack.pop()
                new_val = top_val ^ token
                stack.append(new_val)
    i += 1

final_stack_sum = sum(stack)
print(f"Result: {final_stack_sum}")