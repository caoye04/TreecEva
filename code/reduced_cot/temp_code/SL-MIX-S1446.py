from collections import defaultdict

token_stream = ['(', '(', ')', '(', '(', ')', ')', ')']

def parse(tokens, index=0, current_depth=0):
    max_depth = current_depth
    while index < len(tokens):
        if tokens[index] == '(':
            index, deeper_max = parse(tokens, index + 1, current_depth + 1)
            max_depth = max(max_depth, deeper_max)
        elif tokens[index] == ')':
            return index + 1, max_depth
        else:
            index += 1
    return index, max_depth

depth_tracker = lambda d: d * 2 - 1 if d > 0 else 0
max_depth_dict = defaultdict(int)

index, max_depth = parse(token_stream)
max_depth_dict['final'] = depth_tracker(max_depth)

# Adjust for root level visibility
adjusted_max_depth = max_depth_dict['final'] + 1 if max_depth > 0 else 0
print(f"Result: {adjusted_max_depth}")