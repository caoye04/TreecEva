import math

def complex_transform(data):
    transformed = []
    for key, values in data.items():
        if isinstance(values, list):
            processed = []
            for v in values:
                if isinstance(v, (int, float)):
                    processed.append(math.log(abs(v) + 1))
                elif isinstance(v, str):
                    processed.append(len(v) ** 2)
            transformed.append((key, sum(processed)))
    return dict(transformed)

def aggregate_stats(mapping):
    stats = {
        'sum': sum(mapping.values()),
        'mean': sum(mapping.values()) / len(mapping),
        'max': max(mapping.values()),
        'min': min(mapping.values())
    }
    return stats

data_structure = {
    'group_a': [10, -20, 'hello', 3.5],
    'group_b': ['world', 100, -5.2, 'test'],
    'group_c': [2.718, 'a' * 10, -100]
}

transformed_data = complex_transform(data_structure)
stats = aggregate_stats(transformed_data)

# Perform bitwise operations on the integer parts of stats
bitwise_operations = [
    int(stats['sum']) & int(stats['mean']),
    int(stats['max']) | int(stats['min']),
    int(stats['sum']) ^ int(stats['max'])
]

# Apply a complex formula using the bitwise results
final_result = (bitwise_operations[0] * 3 + bitwise_operations[1] - bitwise_operations[2]) // 2

print(f'Result: {final_result}')