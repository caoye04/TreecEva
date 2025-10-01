import math

def transform_data(data):
    transformed = []
    for item in data:
        if isinstance(item, int):
            transformed.append(math.factorial(item % 7))
        elif isinstance(item, str):
            transformed.append(len(item) ** 2)
        else:
            transformed.append(0)
    return transformed

def process_nested(nested_dict):
    results = {}
    for key, value in nested_dict.items():
        if isinstance(value, list):
            results[key] = sum(transform_data(value))
        elif isinstance(value, dict):
            sub_results = process_nested(value)
            results[key] = sum(sub_results.values())
        else:
            results[key] = value * 3
    return results

data_structure = {
    'a': [3, 'hello', 5],
    'b': {
        'c': [2, 'world', 4],
        'd': 7
    },
    'e': ['test', 6, {'f': [1, 'x', 3]}]
}

intermediate = process_nested(data_structure)
flattened_values = []
for v in intermediate.values():
    if isinstance(v, dict):
        flattened_values.extend(v.values())
    else:
        flattened_values.append(v)

weighted_sum = sum(val * idx for idx, val in enumerate(flattened_values, 1))
final_result = weighted_sum % 1000 + int(math.sqrt(max(flattened_values)))
print(f'Result: {final_result}')