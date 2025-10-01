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
        if n > 0:
            product *= n
    return product

data_structure = {
    'layer1': [
        {'a': 3, 'b': -4},
        {'c': 5, 'd': -6, 'nested': [2, -8, 3]}
    ],
    'layer2': {
        'x': [10, -20, 30],
        'y': {
            'deep': [
                {'p': 7, 'q': -9},
                {'r': 11, 's': -13}
            ]
        }
    }
}

# Step 1: Extract all numeric values
numbers = []

# From layer1
for item in data_structure['layer1']:
    for v in item.values():
        if isinstance(v, list):
            numbers.extend(v)
        else:
            numbers.append(v)

# From layer2
for v in data_structure['layer2']['x']:
    numbers.append(v)

for item in data_structure['layer2']['y']['deep']:
    for val in item.values():
        numbers.append(val)

# Step 2: Transform the numbers
transformed_numbers = complex_transform(numbers)

# Step 3: Perform bitwise operations on the first 5 transformed numbers
bitwise_result = int(transformed_numbers[0])
for i in range(1, min(5, len(transformed_numbers))):
    if i % 2 == 1:
        bitwise_result = bitwise_result & int(transformed_numbers[i])
    else:
        bitwise_result = bitwise_result | int(transformed_numbers[i])

# Step 4: Aggregate the rest
product_of_rest = aggregate_stats(transformed_numbers[5:])

# Step 5: Final calculation
final_result = (bitwise_result + product_of_rest) % 1000
print(f"Result: {final_result}")