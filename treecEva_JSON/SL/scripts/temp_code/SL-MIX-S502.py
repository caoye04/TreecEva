import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            transformed.append(val ** 2)
        elif i % 3 == 1:
            transformed.append(math.sqrt(abs(val)))
        else:
            transformed.append(math.log(abs(val) + 1))
    return transformed

def aggregate_metrics(matrix):
    results = []
    for row in matrix:
        product = 1
        for elem in row:
            product *= elem if elem != 0 else 1
        results.append(product)
    return sum(results) / len(results) if len(results) > 0 else 0

data_structure = {
    'layer1': [
        {'values': [2, -4, 8, -16, 32], 'weights': [0.5, 0.25, 0.75]},
        {'values': [-3, 9, -27, 81], 'weights': [0.3, 0.6, 0.9]}
    ],
    'layer2': [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    'metadata': {
        'version': '1.2.3',
        'processed': False,
        'tags': ['math', 'transform', 'aggregate']
    }
}

# Process layer1 transformations
weighted_sum = 0
for item in data_structure['layer1']:
    transformed_values = complex_transform(item['values'])
    for i, tv in enumerate(transformed_values):
        weight_idx = i % len(item['weights'])
        weighted_sum += tv * item['weights'][weight_idx]

# Process layer2 aggregations
aggregation_result = aggregate_metrics(data_structure['layer2'])

# Apply mathematical transformation to combine results
intermediate_value = math.sin(weighted_sum) * math.cos(aggregation_result)

# Apply bit manipulation to create a mask
bit_mask = (int(intermediate_value * 1000) & 0xFF) ^ 0xAA

# Final calculation combining all components
final_result = (bit_mask << 2) + int(math.ceil(abs(intermediate_value) * 100))

print(f"Result: {final_result}")