import math

def transform_data(data_dict):
    transformed = {}
    for key, value in data_dict.items():
        if isinstance(value, list):
            transformed[key] = [math.log(x) if x > 0 else 0 for x in value]
        elif isinstance(value, dict):
            transformed[key] = {k: v**2 for k, v in value.items()}
        else:
            transformed[key] = value
    return transformed

def aggregate_values(data):
    total = 0
    for item in data:
        if isinstance(item, dict):
            for v in item.values():
                total += v if isinstance(v, (int, float)) else 0
        elif isinstance(item, (int, float)):
            total += item
    return total

# Initialize complex nested data structure
complex_data = {
    'group1': [math.e, math.e**2, -1, 0],
    'group2': {'a': 3, 'b': 4, 'c': 5},
    'group3': [
        {'x': 2, 'y': 3},
        {'x': 4, 'y': 5}
    ],
    'group4': 42
}

# Transform the data
processed_data = transform_data(complex_data)

# Perform aggregation on nested structures
agg_value1 = aggregate_values(processed_data['group1'])
agg_value2 = aggregate_values(processed_data['group3'])

# Bitwise and mathematical operations
bitwise_result = (int(agg_value1) & int(agg_value2)) ^ processed_data['group2']['c']

# Final calculation step
result = (bitwise_result * 2) + len(processed_data['group1']) - round(math.sqrt(processed_data['group4']))

print(f'Result: {result}')