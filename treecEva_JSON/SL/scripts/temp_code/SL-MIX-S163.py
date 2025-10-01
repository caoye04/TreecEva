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
    product = 1
    for n in nums:
        product *= n if n != 0 else 1
    avg = sum(nums) / len(nums) if nums else 0
    return product, avg

data_structure = {
    'layer1': [
        {'values': [3, -4, 5, -6]},
        {'values': [7, -8, 9, -10]}
    ],
    'layer2': {
        'subA': [2, 4, 8],
        'subB': [1, 3, 5, 7]
    }
}

# Process layer1 data
processed_layer1 = []
for item in data_structure['layer1']:
    transformed = complex_transform(item['values'])
    processed_layer1.extend(transformed)

# Process layer2 data
layer2_combined = data_structure['layer2']['subA'] + data_structure['layer2']['subB']
layer2_squared = [x**2 for x in layer2_combined]

# Combine all processed data
all_data = processed_layer1 + layer2_squared

# Apply filtering and transformation
filtered_data = [x for x in all_data if x > 10]
transformed_data = [math.log(x) for x in filtered_data if x > 0]

# Perform aggregation
product, average = aggregate_stats(transformed_data)

# Final calculation step
result = int((product + average) * 1000) % 997

print(f'Result: {result}')