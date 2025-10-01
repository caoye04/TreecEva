import math

def complex_transform(data):
    result = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(math.sqrt(abs(val)))
    return result

def nested_operation(x, y, z):
    a = x * y + z
    b = (a & 0xFF) | (z << 2)
    c = math.log(b + 1) if b > 0 else 0
    return int(c) ^ (x % 10)

data_structure = {
    'layer1': [
        {'values': [3, -4, 5]},
        {'values': [7, -2, 9, 16]}
    ],
    'layer2': {
        'sub_a': (12, 8, 5),
        'sub_b': [1, 3, 5, 7, 9]
    }
}

# Process layer1
processed_values = []
for item in data_structure['layer1']:
    transformed = complex_transform(item['values'])
    processed_values.extend(transformed)

# Process layer2
tuple_sum = sum(data_structure['layer2']['sub_a'])
list_product = 1
for num in data_structure['layer2']['sub_b']:
    list_product *= num

# Combine results
intermediate_value = nested_operation(tuple_sum, len(processed_values), list_product)

# Final calculation
bit_shifted = intermediate_value << 3
masked_value = bit_shifted & 0x1FF
final_result = masked_value - (processed_values[0] + processed_values[-1])

print(f"Result: {final_result}")