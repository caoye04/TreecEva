import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_stats(numbers):
    total = sum(numbers)
    mean = total / len(numbers) if numbers else 0
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers) if numbers else 0
    return {
        'sum': total,
        'mean': mean,
        'variance': variance,
        'count': len(numbers)
    }

data_structure = {
    'layer1': [
        {
            'name': 'group_a',
            'values': [1, -4, 9, -16, 25]
        },
        {
            'name': 'group_b',
            'values': [3, -8, 15, -24, 35]
        }
    ],
    'layer2': {
        'matrix': [
            [2, 3, 5],
            [7, 11, 13],
            [17, 19, 23]
        ],
        'metadata': {
            'dimensions': (3, 3),
            'prime_sum': 0
        }
    }
}

# Process layer1 data
processed_values = []
for group in data_structure['layer1']:
    transformed = complex_transform(group['values'])
    stats = aggregate_stats(transformed)
    processed_values.extend(transformed)
    group['stats'] = stats

# Process layer2 data
matrix = data_structure['layer2']['matrix']
prime_sum = 0
for row in matrix:
    for element in row:
        prime_sum += element

data_structure['layer2']['metadata']['prime_sum'] = prime_sum

# Complex calculation using processed data
weighted_sum = 0
for i, val in enumerate(processed_values):
    weight = (i % 3) + 1
    weighted_sum += val * weight

# Final computation
normalization_factor = math.log(abs(weighted_sum)) if weighted_sum != 0 else 1
denominator = data_structure['layer2']['metadata']['prime_sum']

if denominator != 0:
    result = int((weighted_sum / denominator) * normalization_factor)
else:
    result = 0

# Adjust result based on special conditions
if result < 0:
    result = abs(result) ^ 0xFF
elif result > 1000:
    result = result >> 2

print(f"Result: {result}")