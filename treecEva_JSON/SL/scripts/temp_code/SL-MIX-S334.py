import math

def process_nested_data(data):
    result = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, int):
                temp.append(val ** 2)
            elif isinstance(val, str):
                temp.append(len(val))
            else:
                temp.append(int(val))
        result.append(sum(temp) + i * 10)
    return result

def transform_values(values):
    transformed = []
    for val in values:
        if val % 2 == 0:
            transformed.append(math.sqrt(val))
        else:
            transformed.append(val ** 3)
    return transformed

data_structure = [
    [1, 'hello', 3.0, 4],
    ['world', 2, 5, 6.0],
    [7, 8, 'test', 9]
]

processed_data = process_nested_data(data_structure)
transformed_data = transform_values(processed_data)

# Perform bit-wise operations
bitwise_result = 0
for i, val in enumerate(transformed_data):
    if i % 2 == 0:
        bitwise_result |= int(val)
    else:
        bitwise_result &= int(val)

# Final calculation
final_result = (bitwise_result ^ 0xFF) + sum([x for x in transformed_data if x > 10])

print(f'Result: {final_result}')