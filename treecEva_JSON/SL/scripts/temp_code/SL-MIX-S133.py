def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

tokens = ['sin', '(', 'x', ')', '+', 'cos', '(', 'y', ')']
fib_cache = {}
char_positions = set()
unique_chars = frozenset(''.join(tokens))

with open('temp_tokens.txt', 'w') as f:
    for i, token in enumerate(tokens):
        f.write(f'{token}\n')
        for ch in token:
            char_positions.add(ord(ch) * fibonacci(i+1))

checksum = 0
if char_positions and unique_chars:
    weighted_sum = sum(char_positions)
    unique_count = len(unique_chars)
    checksum = (weighted_sum % unique_count) if unique_count else 0
else:
    checksum = -1

print(f'Result: {checksum}')