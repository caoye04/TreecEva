import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_values(values):
    total = 0
    for i, v in enumerate(values):
        if i < len(values) // 2:
            total += v
        else:
            total -= v
    return total

data_structure = {
    'layer1': [
        {'a': 3, 'b': [2, 4, 6]},
        {'a': -5, 'b': [1, 3, 5]}
    ],
    'layer2': [
        {'x': 2.5, 'y': [7, 14, 21]},
        {'x': -1.5, 'y': [8, 16, 32]}
    ]
}

# Process layer1
processed_layer1 = []
for item in data_structure['layer1']:
    temp = item['a'] * sum(item['b'])
    processed_layer1.append(temp)

# Process layer2
processed_layer2 = []
for item in data_structure['layer2']:
    temp = item['x'] * max(item['y'])
    processed_layer2.append(temp)

# Combine processed layers
combined = processed_layer1 + processed_layer2

# Transform the combined list
transformed_combined = complex_transform(combined)

# Aggregate values
aggregated_value = aggregate_values(transformed_combined)

# Final calculation
result = int(abs(aggregated_value) * 10) % 1000

print(f"Result: {result}")