from collections import deque
from functools import reduce

def transform_layer(data, op):
    return list(map(op, data))

def filter_valid(chars):
    return list(filter(lambda x: x.isalnum(), chars))

cipher_sequence = ['*', 'a', '1', '&', 'b', '2', '#', 'c', '3']
processing_stack = deque()

for char in cipher_sequence:
    if char.isalpha():
        processing_stack.append(char.upper())
    elif char.isdigit():
        processing_stack.append(int(char) * 2)
    else:
        if processing_stack:
            processing_stack.pop()

transformed_values = transform_layer(list(processing_stack), lambda x: x if isinstance(x, int) else ord(x))
valid_elements = filter_valid([str(elem) for elem in transformed_values])
numeric_values = [int(x) for x in valid_elements if x.isdigit()]
alphanumeric_codes = [ord(c) for c in valid_elements if c.isalpha()]
combined_list = numeric_values + alphanumeric_codes

decoded_sum = reduce(lambda acc, val: acc ^ val, combined_list, 0) if combined_list else 0
print(f"Result: {decoded_sum}")