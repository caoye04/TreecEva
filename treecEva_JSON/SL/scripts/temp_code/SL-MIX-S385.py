import math

def transform_data(data):
    transformed = []
    for i, item in enumerate(data):
        if isinstance(item, int):
            transformed.append(math.factorial(item % 7))
        elif isinstance(item, str):
            transformed.append(len(item) ** 2)
        else:
            transformed.append(sum(x ** 2 for x in item))
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
    'alpha': [3, 'hello', [1, 2, 3]],
    'beta': {
        'gamma': [4, 'world', [2, 3]],
        'delta': 5
    },
    'epsilon': [6, 'test', [1, 1, 1, 2]]
}

intermediate = process_nested(data_structure)
aggregated = sum(intermediate.values())
weighted_sum = aggregated * len(intermediate)
modulus_operation = weighted_sum % 997
log_value = int(math.log(modulus_operation + 1) * 100)
final_result = log_value ^ 0xFF
print(f'Result: {final_result}')