import math

def process_data(arr):
    transformed = []
    for i, val in enumerate(arr):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

data = [4, -9, 16, -25, 36]
processed = process_data(data)

# Nested dictionary with lambda transformations
transformations = {
    'level1': {
        'a': lambda x: x * 2,
        'b': lambda x: x + 5
    },
    'level2': {
        'c': lambda x: x // 3,
        'd': lambda x: x % 7
    }
}

mapped_values = []
for idx, val in enumerate(processed):
    if idx < 2:
        mapped_values.append(transformations['level1']['a'](val))
    else:
        mapped_values.append(transformations['level2']['c'](val))

# Bitwise operations on selected elements
bitwise_result = (int(mapped_values[0]) & int(mapped_values[1])) ^ int(mapped_values[2])

# String manipulation based on conditions
condition_str = ''.join([str(int(x)) for x in mapped_values if x > 10])
char_sum = sum(ord(c) for c in condition_str)

# Final calculation combining all previous results
final_result = (bitwise_result * len(condition_str)) + (char_sum % 100)

print(f'Result: {final_result}')