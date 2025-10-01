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

def aggregate_stats(nums):
    product = 1
    sum_vals = 0
    count = 0
    for n in nums:
        if n > 0:
            product *= n
            sum_vals += n
            count += 1
    avg = sum_vals / count if count else 0
    return product, avg, count

data_structure = {
    'layer1': [
        {'a': [2, -8, 3], 'b': [4, -2, 16]},
        {'c': [1, 9, -5], 'd': [7, -3, 25]}
    ],
    'layer2': {
        'groupA': (10, -4, 6, 2),
        'groupB': (3, -9, 12, -1)
    }
}

# Flatten and process layer1
flat_list1 = []
for item in data_structure['layer1']:
    for sublist in item.values():
        flat_list1.extend(sublist)

processed_layer1 = complex_transform(flat_list1)

# Process layer2
tuple_data = list(data_structure['layer2']['groupA']) + list(data_structure['layer2']['groupB'])
processed_layer2 = complex_transform(tuple_data)

# Combine processed data
combined_data = processed_layer1 + processed_layer2

# Apply bit manipulation to positive integers
bitwise_results = []
for x in combined_data:
    if x == int(x) and x > 0:
        int_x = int(x)
        bitwise_results.append((int_x << 1) ^ (int_x >> 1))

# Aggregate statistics
product, avg, count = aggregate_stats(bitwise_results)

# Final calculation
if count > 0:
    result = int((product ** (1/count)) + avg) & 0xFF
else:
    result = 0

print(f"Result: {result}")