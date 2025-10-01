import math

def process_nested_data(data):
    result = 0
    for i, sublist in enumerate(data):
        temp = 0
        for j, val in enumerate(sublist):
            if isinstance(val, str):
                temp += len(val) * (i + 1)
            elif isinstance(val, int):
                temp += val ^ (j + 1)
            elif isinstance(val, float):
                temp += int(math.log(abs(val) + 1))
        result += temp << (i + 1)
    return result

def transform_values(mapping, keys):
    transformed = []
    for key in keys:
        if key in mapping:
            value = mapping[key]
            if isinstance(value, list):
                transformed.append(process_nested_data([value]))
            else:
                transformed.append(value * 2)
        else:
            transformed.append(-1)
    return transformed

data_structure = [
    ["hello", 42, 3.14],
    ["world", 10, -2.718, "test"],
    [100, "example", 1.414, 7, "end"]
]

mapping_dict = {
    'a': ["alpha", 5, 2.71],
    'b': 12,
    'c': ["beta", 20, -1.41, "gamma"],
    'd': 8
}

keys_list = ['a', 'b', 'c', 'd', 'e']

processed_data = process_nested_data(data_structure)
transformed_values = transform_values(mapping_dict, keys_list)

# Perform complex calculation
final_result = processed_data
for i, val in enumerate(transformed_values):
    if i % 2 == 0:
        final_result += val * (i + 1)
    else:
        final_result -= val >> (i - 1) if i > 0 else val

# Apply final transformation
final_result = (final_result & 0xFFFF) ^ ((final_result >> 16) & 0xFFFF)
print(f"Result: {final_result}")