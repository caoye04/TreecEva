import math

def complex_transform(data):
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(math.sqrt(abs(val)))
    return transformed

def aggregate_stats(nums):
    if not nums:
        return 0
    total = sum(nums)
    avg = total / len(nums)
    variance = sum((x - avg) ** 2 for x in nums) / len(nums)
    return math.sqrt(variance)  # Standard deviation

data_structure = {
    'layer1': [
        {'a': 3, 'b': [1, 4, 9, 16]},
        {'a': -2, 'b': [25, 36, 49, 64]}
    ],
    'layer2': [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
}

# Process layer1
processed_values = []
for item in data_structure['layer1']:
    a_val = item['a']
    b_list = item['b']
    
    if a_val > 0:
        processed_b = [x * a_val for x in b_list]
    else:
        processed_b = [x + a_val for x in b_list]
    
    transformed_b = complex_transform(processed_b)
    processed_values.extend(transformed_b)

# Process layer2
layer2_flattened = [num for sublist in data_structure['layer2'] for num in sublist]
stats_deviation = aggregate_stats(layer2_flattened)

# Combine results
weighted_sum = 0
for i, val in enumerate(processed_values):
    weight = 1 + (i % 3) * 0.5
    weighted_sum += val * weight

# Final calculation
final_result = int(weighted_sum * stats_deviation) % 1000
print(f'Result: {final_result}')