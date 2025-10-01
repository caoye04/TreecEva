import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def nested_operation(matrix):
    flattened = [item for sublist in matrix for item in sublist]
    processed = []
    for x in flattened:
        if x > 0:
            processed.append(math.log(x + 1))
        else:
            processed.append(-math.log(abs(x) + 1))
    return sum(processed)

data_structure = {
    'layer1': [
        {'a': 3, 'b': [2, -4, 6]},
        {'a': -2, 'b': [1, 3, -5]}
    ],
    'layer2': [
        [7, -3],
        [2, 4, -1]
    ]
}

# Begin processing
layer1_data = data_structure['layer1']
layer2_data = data_structure['layer2']

# Process layer1
intermediate_values = []
for item in layer1_data:
    a_val = item['a']
    b_vals = item['b']
    transformed_b = complex_transform(b_vals)
    aggregated = sum(transformed_b) * a_val
    intermediate_values.append(aggregated)

# Process layer2
layer2_sum = nested_operation(layer2_data)

# Combine results
combined = intermediate_values + [layer2_sum]
weighted_sum = sum(val * (i + 1) for i, val in enumerate(combined))

# Bitwise operations
bitwise_result = 0
for val in combined:
    int_val = int(abs(val))
    bitwise_result ^= (int_val << 1) & 0xFF

# Final calculation step
result = (weighted_sum + bitwise_result) % 1000

print(f'Result: {int(result)}')