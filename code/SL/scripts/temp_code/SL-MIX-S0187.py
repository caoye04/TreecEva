from functools import reduce

def token_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += len(args[0]) if args else 0
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@token_counter
def process_tokens(tokens):
    return tokens

token_stream = [3, 5, '+', 2, '*']
processed = process_tokens(token_stream)

# Evaluate expression: 3 + 5 * 2
stack = []
for item in processed:
    if isinstance(item, int):
        stack.append(item)
    elif item == '+':
        b, a = stack.pop(), stack.pop()
        stack.append(a + b)
    elif item == '*':
        b, a = stack.pop(), stack.pop()
        stack.append(a * b)

final_result = stack[0] if stack else 0
print(f'Result: {final_result}')