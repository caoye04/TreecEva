import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        sub_result = 1
        for j, val in enumerate(sublist):
            if isinstance(val, int) and val > 0:
                sub_result *= val
            elif isinstance(val, str):
                sub_result *= len(val)
        result += sub_result if i % 2 == 0 else -sub_result
    return result

def transform_string(s):
    parts = s.split('_')
    transformed = []
    for part in parts:
        if len(part) % 2 == 0:
            transformed.append(part.upper())
        else:
            transformed.append(part.lower())
    return ''.join(transformed)

data_structure = [
    [2, 'hello', 3],
    ['world', 4, 'test'],
    [5, 'a', 'bc', 7],
    ['even', 'odd', 2]
]

string_input = 'this_is_a_complex_test_string'

# Process the nested data
processed_value = process_nested_data(data_structure)

# Transform the string
transformed_string = transform_string(string_input)

# Perform mathematical operations
log_value = math.log(processed_value + 100)
exp_value = math.exp(2)
sqrt_value = math.sqrt(len(transformed_string))

# Combine results with bitwise operations
bitwise_result = (int(log_value) & int(exp_value)) | int(sqrt_value)

# Final calculation
final_result = (bitwise_result ^ len(data_structure)) + sum([len(s) for s in transformed_string.split('_')])

print(f'Result: {final_result}')