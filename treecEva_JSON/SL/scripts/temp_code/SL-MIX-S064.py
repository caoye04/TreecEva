import math

def transform_data(data):
    transformed = []
    for key, values in data.items():
        sub_result = []
        for val in values:
            if isinstance(val, int) and val > 0:
                sub_result.append(math.log(val) * 2)
            elif isinstance(val, str):
                sub_result.append(len(val) ** 2)
            else:
                sub_result.append(0)
        transformed.append((key, sum(sub_result)))
    return dict(transformed)

def process_nested(nested_dict):
    results = {}
    for outer_key, inner_dict in nested_dict.items():
        temp = []
        for inner_key, inner_values in inner_dict.items():
            transformed = transform_data({inner_key: inner_values})
            temp.append(transformed[inner_key] if inner_key in transformed else 0)
        results[outer_key] = sum(temp)
    return results

data_structure = {
    'group1': {
        'subsetA': [1, 4, 'hello', -3, 9],
        'subsetB': ['world', 2, 3, '', 5]
    },
    'group2': {
        'subsetC': [7, 'test', 0, 8],
        'subsetD': [10, -1, 'example']
    }
}

processed = process_nested(data_structure)
aggregated = [math.floor(val * 1.5) for val in processed.values() if val > 0]
bitwise_ops = [(x & 3) | (x >> 2) for x in aggregated]
final_result = sum(bitwise_ops) ^ 0xF  # XOR with hexadecimal 15

print(f'Result: {final_result}')