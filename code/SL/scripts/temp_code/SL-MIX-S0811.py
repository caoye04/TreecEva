from collections import deque
from itertools import permutations
import functools

def encode_shift(value, positions):
    return (value + positions) % 10

cipher_stack = deque([1, 2, 3, 4, 5])  # Stack initialization
perm_gen = permutations([1, 2, 3], 2)
transform_lambda = lambda x, y: x * 2 + y

for i in range(3):
    a, b = next(perm_gen)
    top_element = cipher_stack.pop()
    transformed = transform_lambda(top_element, a ^ b)
    cipher_stack.append(transformed)

final_value = cipher_stack[-1]
cipher_result = encode_shift(final_value, sum(cipher_stack))
print(f"Target result: {cipher_result}")