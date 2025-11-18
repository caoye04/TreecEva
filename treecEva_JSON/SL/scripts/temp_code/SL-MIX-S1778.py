def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def encode_char(c, pos):
    base_shift = fibonacci(pos + 1)
    return chr((ord(c) - ord('A') + base_shift) % 26 + ord('A'))

message = 'CRYPTO'
encoded_chars = []
for idx, char in enumerate(message):
    encoded_chars.append(encode_char(char, idx))

# Divide and conquer checksum calculation
values = [ord(c) for c in encoded_chars]

reduce_func = lambda x, y: (x + y) % 97

def divide_and_conquer_reduce(lst):
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    left = divide_and_conquer_reduce(lst[:mid])
    right = divide_and_conquer_reduce(lst[mid:])
    return reduce_func(left, right)

verification_checksum = divide_and_conquer_reduce(values)
print(f'Result: {verification_checksum}')