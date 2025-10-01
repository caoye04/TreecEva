import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_values(matrix):
    result = 0
    for row in matrix:
        for val in row:
            if val > 0:
                result += val
            else:
                result -= val
    return result

data_structure = {
    'layer1': [
        {'a': 3, 'b': -4},
        {'c': 5, 'd': -6, 'nested': [2, -8, 3]}
    ],
    'layer2': {
        'x': [10, -20, 30],
        'y': [
            [1, -2, 3],
            [-4, 5, -6]
        ]
    }
}

# Process layer1
layer1_sum = 0
for item in data_structure['layer1']:
    for key, value in item.items():
        if isinstance(value, list):
            processed = complex_transform(value)
            layer1_sum += sum(processed)
        else:
            layer1_sum += value if value > 0 else -value

# Process layer2
layer2_aggregate = aggregate_values(data_structure['layer2']['y'])
layer2_x_transform = complex_transform(data_structure['layer2']['x'])
layer2_x_sum = sum(layer2_x_transform)

# Combine results with bitwise operations
intermediate_a = int(layer1_sum) & 0xFF
intermediate_b = int(layer2_aggregate) | 0xF0
intermediate_c = int(layer2_x_sum) ^ 0xAA

# Final calculation
final_result = ((intermediate_a << 2) + intermediate_b) * intermediate_c - (intermediate_a | intermediate_b)
print(f"Result: {final_result}")