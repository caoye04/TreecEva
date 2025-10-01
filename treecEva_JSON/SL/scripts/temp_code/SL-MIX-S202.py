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

def aggregate_values(items):
    product = 1
    sum_val = 0
    for item in items:
        if item > 0:
            product *= item
        sum_val += item
    return product + sum_val

data_matrix = [
    [2, -4, 8, -16, 32],
    [-3, 9, -27, 81],
    [5, -10, 15, -20, 25, -30]
]

processed_layers = []
for layer in data_matrix:
    processed_layer = complex_transform(layer)
    processed_layers.append(processed_layer)

aggregated_values = []
for processed_layer in processed_layers:
    value = aggregate_values(processed_layer)
    aggregated_values.append(value)

bitwise_accum = 0
for i, val in enumerate(aggregated_values):
    if i % 2 == 0:
        bitwise_accum ^= int(val * 100)
    else:
        bitwise_accum |= int(val * 100)

# Apply final transformation
final_result = (bitwise_accum & 0xFF) + (bitwise_accum >> 8)
print(f"Result: {final_result}")