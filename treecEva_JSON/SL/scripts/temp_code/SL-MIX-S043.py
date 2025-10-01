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

def nested_operation(matrix):
    flattened = [item for sublist in matrix for item in sublist]
    processed = []
    for x in flattened:
        if x > 0:
            processed.append(math.sin(x))
        else:
            processed.append(math.cos(x))
    return sum(processed)

data_structure = {
    'layer1': [
        {'values': [2, -4, 8, -16]},
        {'values': [32, -64, 128]}
    ],
    'layer2': [
        [[1, -2], [3, -4]],
        [[5, -6], [7, -8]]
    ]
}

# Phase 1: Process layer1
layer1_results = []
for item in data_structure['layer1']:
    transformed = complex_transform(item['values'])
    layer1_results.extend(transformed)

# Phase 2: Process layer2
layer2_result = nested_operation(data_structure['layer2'])

# Phase 3: Combine results
combined = []
for i in range(min(len(layer1_results), 10)):  # Limit to first 10 elements
    if i < len(layer1_results):
        combined.append(layer1_results[i] * layer2_result)

# Phase 4: Statistical analysis
mean_val = sum(combined) / len(combined) if combined else 0
variance = sum((x - mean_val) ** 2 for x in combined) / len(combined) if combined else 0

# Phase 5: Final computation
weighted_sum = 0
for i, val in enumerate(combined):
    weight = math.exp(-i/len(combined)) if combined else 0
    weighted_sum += val * weight

# Phase 6: Apply final transformation
if weighted_sum > 0:
    result = int(math.floor(weighted_sum ** (1/3)))
else:
    result = int(math.ceil(abs(weighted_sum) ** (1/3))) * -1

print(f"Result: {result}")